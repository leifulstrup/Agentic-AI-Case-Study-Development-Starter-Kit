# Example — `verification-debt.yaml` excerpt

*The kit's distinguishing mechanism: when AI writes something from its own knowledge rather than your sources, it is logged here with the source type needed to resolve it. Publication expects the count at zero.*

---

```yaml
last_updated: "2026-07-08"
items:
  - claim: "LLMs are neural networks built on the 'transformer' architecture,
      trained on very large text corpora to predict and generate language
      (definitional passage)"
    document: "Supplement (Section 1, 'Large language models')"
    source_needed: "Authoritative reference on transformer/LLM fundamentals"
    status: verified
    date_added: "2026-07-08"
    date_resolved: "2026-07-08"
    source: "Vaswani, A., et al., 'Attention Is All You Need,' Advances in Neural
      Information Processing Systems 30 (NeurIPS 2017), arXiv:1706.03762"
    note: "Citation confirmed by checking title/authors/venue/year against the
      primary record; inline citation added in Supplement §1 and listed as
      Referenced Work #6 (T3) in the bibliography."

  - claim: "Spliced composite quotation in Main Case Section VIII — six-domain
      list inserted mid-quotation from a different answer"
    document: "Main Case (Section VIII)"
    source_needed: "Restore verbatim wording from McKinsey transcript lines 133-138"
    status: verified
    date_added: "2026-07-08"
    date_resolved: "2026-07-08"
    note: "Flagged by the verification pass. Quote restored; domain list moved
      outside the quotation marks as paraphrase with its own citation."
```

*[Seven further items omitted. Final state: 9 of 9 verified, 0 open.]*

---

## What to notice in this excerpt

**The AI flags its own unsourced claims while drafting.** The transformer definition is *correct* — and it came from the model's general knowledge, not from any source in the repo. The kit's rule is that correct-but-unsourced still counts as debt. The author decides whether to cite it or cut it; what they cannot do is not know.

**Debt is resolved, not deleted.** Each item keeps its history: what was claimed, what source was needed, what resolved it, and when. The file is an audit trail, not a to-do list that gets tidied away.

**Verification findings become debt items too.** The spliced quote entered the ledger the moment the verifier found it, and stayed open until repaired. Nothing gets quietly fixed.

**Zero open items is the publication bar.** `VERIFICATION_PLEDGE.md` turns that into a statement the author signs and attaches when sharing the case.
