#!/usr/bin/env python3
"""Layer 1 grounding checker v2 (helper, not referee).

Checks that ATTRIBUTED quotes and salient numbers in generated case documents
are grounded in the frozen source corpus.

v2 fixes three defects found by measuring v1 against a known-good corpus:

1. QUOTE PARITY (the big one). v1 used a single character class for open and
   close marks, so one unpaired quote flipped pairing and every subsequent
   "quote" was the narrative prose BETWEEN quotations. Documents written with
   straight quotes only (306 of them in the test corpus) are especially
   vulnerable, since straight marks are open/close ambiguous. v2 matches curly
   and straight quotes separately and rejects captured prose by content
   (embedded source citations, em-dash openings, paragraph breaks, markdown).
2. ATTRIBUTION. Only quoted spans with a nearby attribution signal are checked;
   rhetorical quotes, scare quotes, defined terms, and Teaching Note role-play
   prompts are skipped and counted separately.
3. ELLIPSES AND BRACKETS. Legitimate quotes contain "…" for omissions and
   [bracketed] corrections, so the full string never appears contiguously in the
   source. v2 matches on the longest uninterrupted fragment.

Measured on the v3.2.0 baseline output: v1 reported 54.8% grounding, v2 reports
78.7%; full agent tracing of the same documents found ~97%. The residual gap is
PDF-extraction line-break artifacts and genuinely borderline compound phrases.
**This script remains a lead-generator, not a release gate** — treat FAILs as
items to check by hand, and never fail a version on its number alone.

Usage:
    python3 grounding_check.py <case-study-dir> <sources-dir>

Output: per-document and overall grounding rates, plus every ungrounded
item for human review. Fuzzy matching means borderline items still need
eyes — treat FAIL items as leads, and spot-check a sample of PASSes.

No dependencies beyond the standard library.
"""

import re
import sys
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

# Curly and straight quotes are matched SEPARATELY. A single character class
# containing “ ” and " cannot tell an opening mark from a closing one, so one
# unpaired quote anywhere in the document flips parity and every subsequent
# "match" is the narrative prose BETWEEN quotations. That bug — not rhetorical
# quoting — produced v1's ~45% false-flag rate.
CURLY_RE = re.compile(r'\u201C([^\u201C\u201D]{15,400})\u201D')
STRAIGHT_RE = re.compile(r'"([^"\u201C\u201D]{15,400})"')

# Prose that leaked in via the parity bug looks like narrative, not speech.
# Belt-and-braces guard: a quoted span containing a source citation or a
# markdown/structural marker is not a quotation.
# Straight quotes cannot be told apart (open vs. close), so with an odd number
# anywhere the pairing shifts and narrative prose gets captured. These patterns
# identify captured prose by CONTENT rather than relying on parity.
NOT_A_QUOTE_RE = re.compile(
    r'\([A-Za-z][A-Za-z.&\s]{2,45},\s*[A-Za-z][A-Za-z.]{1,9}\s*\d{0,2},?\s*20\d\d\)'  # (Source, Date) inside
    r'|^\s*[—\-–]\s'          # starts with an em-dash clause
    r'|^\s*\('                # starts with a parenthetical
    r'|\n\s*\n'              # spans a paragraph break
    r'|^\s*[-*|#>]'           # markdown structure
    r'|\*\*'                  # bold markers
    r'|\bExhibit \d'          # cross-references
)


def iter_quotes(text: str):
    """Yield (span_text, start, end) for genuine quoted spans."""
    for rx in (CURLY_RE, STRAIGHT_RE):
        for m in rx.finditer(text):
            span = m.group(1)
            if NOT_A_QUOTE_RE.search(span):
                continue
            yield span, m.start(), m.end()

# A quoted span counts as an attributed claim only if attribution appears nearby:
# a speech verb, a name+comma pattern, or a parenthetical source citation.
ATTRIB_RE = re.compile(
    r'\b(said|says|told|noted|added|explained|argued|put it|recalled|'
    r'according to|wrote|stated|described|asked|replied|observed|'
    r'continued|concluded|warned|acknowledged|conceded)\b'
    r'|\([A-Z][A-Za-z.&\s]{2,40},\s*(?:[A-Z][a-z]{2,8}\.?\s*)?\d{1,2}?,?\s*20\d\d\)'  # (Source, Date)
    r'|—\s*[A-Z][a-z]+\s+[A-Z][a-z]+',                                                        # — Speaker Name
    re.I)

# Contexts where quotation marks are not source claims.
SKIP_RE = re.compile(
    r'\b(imagine|suppose|pretend|you are|you\'re|role[- ]play|prompt|'
    r'ask students|cold call|hypothetical|so-called|what we call|'
    r'term|termed|called|labeled|known as)\b', re.I)

ATTRIB_WINDOW = 220   # chars either side of the quote to inspect
NUMBER_RE = re.compile(
    r'\$[\d,.]+\s*(?:billion|million|trillion|B|M|K)?'   # money
    r'|\b\d{1,3}(?:,\d{3})+\b'                            # 30,000 / 400,000
    r'|\b\d+(?:\.\d+)?%'                                  # percentages
)
FUZZY_THRESHOLD = 0.85


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.replace("’", "'").replace("‘", "'")
    text = text.replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", text).lower().strip()


def normalize_number(num: str) -> str:
    n = num.lower().replace(" ", "")
    n = n.replace("billion", "b").replace("million", "m").replace("trillion", "t")
    return n


def load_corpus(sources_dir: Path) -> str:
    texts = []
    for p in sorted(sources_dir.rglob("*")):
        if p.is_file() and p.suffix.lower() in {".md", ".txt", ".csv", ".html"}:
            try:
                texts.append(p.read_text(errors="ignore"))
            except OSError:
                pass
    if not texts:
        sys.exit(f"No readable text sources found under {sources_dir} "
                 "(PDFs need text extraction first — convert or export .txt copies).")
    return normalize(" ".join(texts))


def longest_fragment(quote: str) -> str:
    """Quotes legitimately contain ellipses (omissions) and [bracketed]
    corrections, so the full string never appears contiguously in the source.
    Match on the longest uninterrupted fragment instead."""
    parts = re.split(r'\u2026|\.\.\.|\[[^\]]*\]', quote)
    return max(parts, key=len) if parts else quote


def fuzzy_in(needle: str, haystack: str) -> bool:
    needle = longest_fragment(needle)
    needle = needle.strip(" ,.;:—-\"'")
    if len(needle) < 12:
        return True   # too short to test meaningfully; leave to human review
    if needle in haystack:
        return True
    # windowed fuzzy match: window same length as needle (+small slack),
    # fine-grained step so a true match isn't straddled by window edges
    n = len(needle)
    step = max(5, n // 10)
    for i in range(0, max(1, len(haystack) - n // 2), step):
        window = haystack[i:i + n + 8]
        if SequenceMatcher(None, needle, window).quick_ratio() >= FUZZY_THRESHOLD \
           and SequenceMatcher(None, needle, window).ratio() >= FUZZY_THRESHOLD:
            return True
    return False


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    case_dir, sources_dir = Path(sys.argv[1]), Path(sys.argv[2])
    corpus = load_corpus(sources_dir)

    total_q = found_q = total_n = found_n = 0
    for doc in sorted(case_dir.glob("*.md")):
        text = doc.read_text(errors="ignore")

        quotes, skipped = [], 0
        for span, start, end in iter_quotes(text):
            lo = max(0, start - ATTRIB_WINDOW)
            hi = min(len(text), end + ATTRIB_WINDOW)
            context = text[lo:hi]
            if SKIP_RE.search(context) and not ATTRIB_RE.search(context):
                skipped += 1
                continue
            if not ATTRIB_RE.search(context):
                skipped += 1          # unattributed quoted text — not a source claim
                continue
            quotes.append(span)

        numbers = set(NUMBER_RE.findall(text))

        missing_q = [q for q in quotes if not fuzzy_in(normalize(q), corpus)]
        missing_n = [n for n in numbers
                     if normalize_number(n) not in normalize_number(corpus)]

        total_q += len(quotes); found_q += len(quotes) - len(missing_q)
        total_n += len(numbers); found_n += len(numbers) - len(missing_n)

        print(f"\n=== {doc.name} ===")
        print(f"  attributed quotes: {len(quotes) - len(missing_q)}/{len(quotes)} grounded"
              f"   ({skipped} unattributed/rhetorical spans skipped)")
        for q in missing_q:
            print(f"    UNGROUNDED QUOTE: \"{q[:90]}...\"" if len(q) > 90
                  else f"    UNGROUNDED QUOTE: \"{q}\"")
        print(f"  numbers: {len(numbers) - len(missing_n)}/{len(numbers)} grounded")
        for n in sorted(missing_n):
            print(f"    UNGROUNDED NUMBER: {n}")

    print("\n=== OVERALL ===")
    qr = 100.0 * found_q / total_q if total_q else 100.0
    nr = 100.0 * found_n / total_n if total_n else 100.0
    print(f"  Attributed-quote grounding: {qr:.1f}% ({found_q}/{total_q})")
    print(f"  Number grounding rate: {nr:.1f}% ({found_n}/{total_n})")
    print("  Reminder: fuzzy matcher — review FAILs by hand, spot-check PASSes.")
    print("  v2 checks only attributed quotes; skipped spans are reported per document.")
    sys.exit(0 if (found_q == total_q and found_n == total_n) else 1)


if __name__ == "__main__":
    main()
