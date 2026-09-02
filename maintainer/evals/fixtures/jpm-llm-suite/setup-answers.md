# Scripted Setup Answers — jpm-llm-suite

*When running the eval pipeline, answer the skills' questions from this script verbatim. If a skill asks something not covered here, choose the option closest to these intents, note the question and your answer in the run log, and propose an addition to this file after the run.*

## /setup-case (skip if case-config.yaml copied directly; answer if re-run)

| Question topic | Answer |
|----------------|--------|
| Company | JPMorgan Chase & Co. (short: JPMorgan) |
| Topic (one sentence) | How JPMorgan built and deployed LLM Suite, an internal generative AI platform, and now navigates the tension between bottom-up employee innovation and top-down process transformation |
| Protagonist | Derek Waldron, Chief Analytics Officer |
| Course | ITEC-617, Kogod School of Business, Spring 2026 |
| Case type | Business |
| Session length | 80 minutes |

## /add-sources (metadata for the frozen corpus)

| Source | Type | Expected tier |
|--------|------|---------------|
| VentureBeat "Beyond the Pilot" interview (Dec 2025) | Primary interview / transcript | T1 |
| McKinsey interview with Derek Waldron (Oct 2025) | Primary interview | T1 |
| Bloomberg TV interview with Jamie Dimon (Oct 2025) | Executive interview (notes/transcript) | T1 or T2 per file completeness |
| CNBC exclusive on JPMorgan AI strategy (Sept 2025) | News article | T1 or T2 per file completeness |
| JPMorgan Q3 2025 earnings materials | Financial | T1 |

Answer date/origin questions from the file contents; do not invent metadata.

## /assess-sources

No user decisions expected. Record the go/no-go result and dimension scores in the run log. Expected outcome for the full corpus: GREEN or YELLOW (breadth is the weakest dimension — few critic/regulator voices). If RED, that itself is a regression signal to investigate.

## /write-document

| Decision point | Answer |
|----------------|--------|
| Additional Sources outline approval | Accept the proposed outline unchanged |
| Main Case opening scene | Choose the option centered on Waldron facing the bottom-up vs. top-down decision; if not offered, pick option 1 |
| Central tension confirmation | Bottom-up innovation (30,000+ employee-created assistants) vs. top-down process transformation ("makers to checkers") |
| Supplement concepts | Accept suggestions; ensure platform-vs-point-solutions and enterprise AI architecture are included |
| Teaching Note learning objectives | Accept suggestions; ensure one objective covers innovation management and one covers workforce transformation |
| Section-by-section feedback | "Continue" at every pause (no edits — we're testing default output quality) |

## /verify-all

No user decisions. Save the full report; it is the primary Layer 1/Layer 2 artifact.
