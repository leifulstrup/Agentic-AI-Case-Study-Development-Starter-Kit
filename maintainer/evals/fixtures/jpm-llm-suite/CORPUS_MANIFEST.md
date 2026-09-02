# Corpus Manifest — jpm-llm-suite

*Proves every eval run uses the identical frozen corpus. Regenerate with the command below after copying sources in; any hash mismatch at run time means STOP — the corpus has drifted.*

```bash
cd maintainer/evals/fixtures/jpm-llm-suite
find sources -type f ! -name .gitkeep -exec shasum -a 256 {} \; | sort -k2
```

**Corpus version**: v1
**Frozen date**: 2026-07-08
**Populated by**: Leif Ulstrup (copied from the private ITEC-617 JPM case repo)

## Frozen files

| Path | Description | SHA-256 |
|------|-------------|---------|
| `sources/Source_Links.md` | Source links/registry from original case project | `73520a72c2715109d2518911f8d11709e2e3d93c8af162a762b656868ab58d72` |
| `sources/financial/JPMorgan_Q3_2025_Earnings.pdf` | JPMorgan Q3 2025 earnings materials | `d2a35730caad8fbe9d5256a5dc39b088b5735a24a327d35c3c7f4f10edb225a8` |
| `sources/news/CNBC_JPMorgan_AI_Blueprint.pdf` | CNBC exclusive on JPMorgan AI strategy, Sept 2025 | `d997ffa9541abd3d42b790c3f95aa3cc35377b0e16247bef7280902b7ea179b0` |
| `sources/transcripts/Bloomberg_Dimon_Interview.txt` | Bloomberg TV interview with Jamie Dimon, Oct 2025 | `0b1f994fbf8b44dd62b1dcaf54c4a51947b34356f5f450bda88dc773d5e0d312` |
| `sources/transcripts/McKinsey_Waldron_Interview.pdf` | McKinsey interview with Derek Waldron, Oct 2025 | `11b7d6c1f4761960f999eac4f8d5a4638bac1b00f4260ba0628775573da5c182` |
| `sources/transcripts/VentureBeat_Interview_Transcript.txt` | VentureBeat "Beyond the Pilot" interview with Derek Waldron, Dec 2025 | `237ee564ebfa606b75e5ea541033a20b423084214514b8917b68d4ae1355a4c9` |

Note: two sources are PDFs. For `grounding_check.py` (text formats only), export text copies at run time (e.g., `pdftotext file.pdf file.txt`) into the run directory — do NOT add them to this frozen corpus.

## Change history

| Corpus version | Date | Change |
|----------------|------|--------|
| v1 | 2026-07-08 | Initial freeze: 6 files, 3 transcripts + 1 news + 1 financial + source links |
