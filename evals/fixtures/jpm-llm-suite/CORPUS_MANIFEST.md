# Corpus Manifest — jpm-llm-suite

*Proves every eval run uses the identical frozen corpus. Regenerate with the command below after copying sources in; any hash mismatch at run time means STOP — the corpus has drifted.*

```bash
cd evals/fixtures/jpm-llm-suite
find sources -type f ! -name .gitkeep -exec shasum -a 256 {} \; | sort -k2
```

**Corpus version**: v1 (UNPOPULATED — hashes pending first copy-in from the private JPM case repo)
**Frozen date**: TBD
**Populated by**: TBD

## Expected files (from the private ITEC-617 JPM case repo)

| Path | Description | SHA-256 |
|------|-------------|---------|
| `sources/transcripts/` — VentureBeat "Beyond the Pilot" interview, Dec 2025 | Primary interview with Derek Waldron | `PENDING` |
| `sources/transcripts/` — McKinsey interview with Derek Waldron, Oct 2025 | Primary interview | `PENDING` |
| `sources/transcripts/` — Bloomberg TV interview with Jamie Dimon, Oct 2025 | Executive interview | `PENDING` |
| `sources/news/` — CNBC exclusive on JPMorgan AI strategy, Sept 2025 | News coverage | `PENDING` |
| `sources/financial/` — JPMorgan Q3 2025 earnings materials | Financial source | `PENDING` |

*Adjust exact filenames to match the private repo when populating; the table above is the expected shape, not a contract on names.*

## Change history

| Corpus version | Date | Change |
|----------------|------|--------|
| v1 | TBD | Initial freeze |
