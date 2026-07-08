#!/usr/bin/env python3
"""Layer 1 grounding checker (helper, not referee).

Checks that quotes and salient numbers in generated case documents are
grounded in the frozen source corpus.

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

QUOTE_RE = re.compile(r'[“"]([^“”"]{15,400})[”"]')
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


def fuzzy_in(needle: str, haystack: str) -> bool:
    needle = needle.strip(" ,.;:—-\"'")
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
        quotes = [q for q in QUOTE_RE.findall(text)]
        numbers = set(NUMBER_RE.findall(text))

        missing_q = [q for q in quotes if not fuzzy_in(normalize(q), corpus)]
        missing_n = [n for n in numbers
                     if normalize_number(n) not in normalize_number(corpus)]

        total_q += len(quotes); found_q += len(quotes) - len(missing_q)
        total_n += len(numbers); found_n += len(numbers) - len(missing_n)

        print(f"\n=== {doc.name} ===")
        print(f"  quotes: {len(quotes) - len(missing_q)}/{len(quotes)} grounded")
        for q in missing_q:
            print(f"    UNGROUNDED QUOTE: \"{q[:90]}...\"" if len(q) > 90
                  else f"    UNGROUNDED QUOTE: \"{q}\"")
        print(f"  numbers: {len(numbers) - len(missing_n)}/{len(numbers)} grounded")
        for n in sorted(missing_n):
            print(f"    UNGROUNDED NUMBER: {n}")

    print("\n=== OVERALL ===")
    qr = 100.0 * found_q / total_q if total_q else 100.0
    nr = 100.0 * found_n / total_n if total_n else 100.0
    print(f"  Quote grounding rate:  {qr:.1f}% ({found_q}/{total_q})")
    print(f"  Number grounding rate: {nr:.1f}% ({found_n}/{total_n})")
    print("  Reminder: fuzzy matcher — review FAILs by hand, spot-check PASSes.")
    sys.exit(0 if (found_q == total_q and found_n == total_n) else 1)


if __name__ == "__main__":
    main()
