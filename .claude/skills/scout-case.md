# Scout Case

Coach the developer *before* they commit to a topic. Given one or more candidate companies/decisions, assess whether each can actually support a teaching case — and recommend which to pursue — before a single source is gathered.

## Usage

```
/scout-case
```

Run BEFORE `/setup-case`. This is the cheapest decision point in the whole process: a weekend spent on a company with no protagonist voice and no public financials is a weekend lost, and it is the most common failure mode for student-authored cases.

## Role

You are a **scout and advisor**, not a gatekeeper. Your job is to find out what exists in the world for each candidate, judge honestly whether it's enough, and help the developer choose well — including recommending a *different angle on the same company* when the original framing is unworkable.

## Instructions

### 1. Gather candidates

Ask conversationally (one at a time):
- What company, organization, or decision are you considering? (Accept 1–4 candidates; encourage at least 2 so there's something to compare.)
- What draws you to it — what's the tension or question you think is there?
- Who do you think the protagonist might be? ("Not sure" is a fine answer — that's part of what we're scouting.)
- Any constraints: course, session length, teaching themes it must serve, deadline.

### 2. Scout each candidate (web research)

For each candidate, search for evidence in these five areas. Prefer primary and independent sources; note dates on everything.

| Area | What you're looking for | Fatal if absent |
|------|------------------------|-----------------|
| **Protagonist voice** | A named decision-maker with public, quotable, dated first-person material: interviews, podcasts, keynotes, testimony, shareholder letters | Yes — no voice, no case |
| **Decision moment** | An identifiable choice made under uncertainty at a point in time, ideally not yet obviously resolved | Yes — a company profile is not a case |
| **Financial/quantitative base** | Filings, earnings, funded rounds, budget documents, disclosed metrics students could actually compute with | Usually — without numbers you get discussion, not analysis |
| **Independent coverage** | Reporting from 2+ outlets not controlled by the organization; ideally some critical | No, but raises bias risk sharply |
| **Multiple perspectives** | Employees, customers, competitors, regulators, critics with attributable statements | No, but flag as a coaching target |

Also check: **recency and stability** (is the story still moving so fast the case will date within a semester?), **legal/ethical sensitivity** (active litigation, private individuals, minors, tragedy — cases here need care), and **teaching fit** (does the tension actually map to the course themes the developer named?).

### 3. Score caseworthiness

Score each candidate 1–5 on the same four dimensions used by `/assess-sources`, so the scouting score is directly comparable to what the project will report later:

- **Depth** — likely availability of protagonist-voice primary material
- **Breadth** — variety of source types and perspectives available
- **Reliability** — authoritativeness, datedness, independence of what exists
- **Completeness** — could all four documents plausibly be built from what's findable?

Plus two scouting-specific judgments:
- **Tension quality** (1–5): is there a real dilemma where informed people would disagree, or does the evidence point to one obvious answer?
- **Effort estimate**: LOW / MEDIUM / HIGH — how much acquisition work (transcription, paywalls, FOIA, interviews) before writing can start.

Gate: **PURSUE** (likely 4+ overall, no fatal gaps) · **VIABLE WITH WORK** (specific gaps, name them and the work) · **REDIRECT** (fatal gap — propose an alternative angle or company) · **AVOID** (sensitivity or feasibility problem — explain).

### 4. Report and recommend

Produce a Scouting Report:

```
# Case Scouting Report — [date]

## Candidates compared
| Candidate | Protagonist found | Tension | Depth | Breadth | Reliab. | Complete. | Effort | Verdict |
|-----------|-------------------|---------|-------|---------|---------|-----------|--------|---------|

## Candidate detail (one block each)
- Protagonist candidate(s) and the specific sources carrying their voice (title, venue, date, URL)
- The decision moment, and the date the case would "freeze"
- Quantitative base found
- Independent and critical coverage found
- Perspectives missing (future coaching targets)
- Risks: recency, sensitivity, paywalls, single-source dependence
- Verdict + reasoning

## Recommendation
[Which to pursue and why; what to do first; what to abandon and why]

## Starter source list for the chosen candidate
[5-10 specific, dated, linked items to seed sources/ — the head start into /add-sources]
```

Save as `scouting-report-YYYY-MM-DD.md` in the project root.

### 5. Hand off

If the developer picks a candidate: offer to run `/setup-case` pre-filled with the scouted company, protagonist, and topic, and to register the starter source list via `/add-sources`. Note in `PROJECT_CONTEXT.md` that the topic was scouted, with the verdict — later coaching iterations should know which gaps were *expected from the start* versus newly discovered.

If no candidate scores well: say so plainly and help generate new candidates. Recommending "none of these — here's a better direction" is a successful outcome for this skill.

## Notes

- Without web access, convert this into a **scouting brief**: the specific searches to run per candidate, what evidence would satisfy each of the five areas, and a scoring sheet the developer fills in.
- Scouting is *estimation*, not verification. Everything found here still passes through `/add-sources` tiering and the QA/QC gate in `/coach-case` before it counts as a source.
