# Changelog

All notable changes to this template will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [4.5.0] - 2026-08-28

*The kit now collects its own field evidence. Previously that meant chasing users after
the fact for things they had already forgotten; now the assistant that just did the work
offers to write it down while it still remembers.*

### Added
- **`/report-experience` — an end-of-run field report, drafted by the agent and submitted
  by the user.** Offered once when a package is finished, declined without argument. **The
  agent drafts it from its own memory of the run, not by interviewing the user**, because
  the most valuable material is what the agent knows and the author never saw: which
  instruction was ambiguous enough to need interpreting, which step took three times
  longer than it should have, which file the kit referenced that does not exist.
  - **The form's most important field is "what did you work around?"** Workarounds are
    where a design is wrong and nobody files a complaint — a step skipped, a config field
    left blank because the course does not use it, a file edited by hand that was supposed
    to be automatic. The skill tells the agent it will have done at least one of these and
    thought nothing of it at the time, and to go back and look
  - Reports are classified **DEFECT / GAP / FRICTION / MISFIT / WORKED WELL** — the same
    taxonomy the field-test intake method already uses, so triage arrives pre-done rather
    than needing a second pass

- **`.github/ISSUE_TEMPLATE/field-report.yml`** — a structured issue form: version, tool
  path, role, workflow stage, classification, what happened, what was worked around, what
  would have helped. Structured rather than free-text so reports across many runs can be
  compared instead of read one at a time

### Changed
- **Submission is a pre-filled link, never a command.** The agent assembles a
  `issues/new?template=field-report.yml&...` URL rather than calling `gh` — which would
  need a CLI and an authenticated account that most people using this kit do not have.
  The link works from every tool path including Cowork and chat, and **it puts the submit
  button in the user's hand**: the agent drafts, shows the full text in the conversation
  first, and never posts on anyone's behalf or describes a report as sent
- **Privacy is enforced at drafting time, not left to the user to catch.** A report
  describes the kit's behaviour and never the case's content — no source material, no
  quotations, no student work, no local paths. The skill carries the rewrite explicitly:
  not *"it let us cite one executive fourteen times"* but *"the assessment cleared a base
  where one executive carried most of the substantive claims"*
- Offered from all four tool paths — `AGENTS.md` behaviour, the `/verify-all`
  pre-publication checklist, the README workflow table, and `STARTER_PROMPT.md` for chat

### Notes
- This replaces a planned one-time survey of the ~30 students and 3 faculty who have
  already used the kit. **A harvest decays; a habit compounds.** The survey is still worth
  doing once for the cohort already past, but every run from here reports itself
- The kit has spent months generating evidence with seeded defects and blind agent probes
  while real users' experience went uncollected. This is the cheap instrument that should
  have existed first

## [4.4.0] - 2026-08-27

*The kit has always made the author careful. It has never taught the reader to check.
This adds the missing half — and corrects the project's own record, which understated its
classroom use badly enough to distort the roadmap.*

### Added
- **`READING_A_CASE.md` — a student-facing guide to checking a case critically.** Every
  verification tool in this kit points at the person writing the case; the student
  receives a verified artifact and is implicitly invited to trust it, which is the
  opposite of the outcome the exercise exists to produce. The guide inverts that. It
  covers six failure patterns — **each one a real defect from this project's own logs,
  cited with the run it came from** — a thirty-minute checking procedure short enough
  that students will actually run it, three exercises including verifying a classmate's
  case, and a reflection prompt whose most useful entry is *"one thing you accepted
  without checking, and why."*
  - The material is deliberately drawn from the maintainers' failures rather than
    invented examples: a verification pass that reported clean over five real quote
    defects; a headline figure spoken by an interviewer and carried as the subject's
    claim in three of four documents; a 33-source base that was 82% the subject
    describing himself; a correction round that introduced eleven new defects while
    fixing twenty-five; and an AI reporting *"Fixed. All 15 converted"* with eight still
    live. **A record of being confidently wrong teaches this better than any invented
    example, and the project has an unusually complete one**
  - Wired into the README's file table and teaching section, and into `AGENTS.md` so
    agents offer it when a draft is finished rather than at the end of the project

### Changed
- **`PROJECT_CONTEXT.md` now records the kit's actual classroom use.** Roughly **30 MBA
  students and 3 faculty** have built cases with it, students in both roles the kit
  supports — authoring and critiquing their own work — and faculty have **taught with the
  output of at least two case developments.** The testing history listed three individual
  tests and none of this, so the repository's own record implied the pedagogical premise
  was unproven when it has been demonstrated at cohort scale
  - The correction comes with the distinction that matters: that adoption ran on
    **v3.1.x-era releases**, before source integrity, the independence cap, the freeze
    protocol, and the halved lengths. **The method is classroom-proven; the current
    verification pipeline is not.** Those are two different claims and the record now
    keeps them apart

### Notes
- The understatement had a cost worth naming: a status review written the same day marked
  classroom teaching **untested** and ranked the roadmap accordingly. That conclusion was
  drawn from what the repository's logs contained rather than from what its maintainer
  knew — **an absence of records read as an absence of evidence**, which is the same
  failure this project has documented in its own tooling more than ten times

## [4.3.1] - 2026-08-27

*Five defects found by running a full authoring pass against the fixture — the first run
that tested shipped instructions rather than shipping new ones. Scorecard in
`evals/test-log.md`.*

### Fixed
- **`add-disclaimers` handed authors an overclaim to paste into finished cases.** Its
  publication-ready boilerplate asserted *"All factual claims, quotes, and data points
  have been verified against primary source documents"* — unconditional, in text the kit
  tells you to put in a document, and **the exact sentence v4.1.0 tells authors to hunt
  down and delete**. Replaced with wording that says what was actually done: quotations
  traced to dated sources, checks recorded in the quality report, remaining unverified
  claims disclosed there. The skill now opens by stating that a disclaimer describes what
  happened and must be edited when a check did not run — **a disclaimer asserting
  verification that did not occur converts a gap into a false statement over the author's
  name**

- **The same file hardcoded "v3.0" into that pasted text**, and had done for fourteen
  releases, so every case using it told readers something false about which methodology
  produced it. Now `[template_version]`, read from `TEMPLATE_VERSION`

- **`examples/` advertised pre-v4.2.0 lengths as the standard** — a ~5,800-word Main Case
  against a 2,500-word target. The excerpts are kept at original size because they record
  a real run, with a note saying so: **read them for what a finished document looks like,
  not for a length to hit**

- **Zero verification debt is unreachable offline and nothing admitted it.** A claim
  needing a reference work, a filing, or a paywalled article cannot be settled without a
  network, and the publication bar is zero open debt. In testing a package sat with five
  such passages against that bar. `/verify-all` now explains that *acknowledged* is a real
  option — the author names what would settle the item, why it cannot be settled now, and
  labels the claim as a claim. It also draws the line that matters: **a check that could
  not run is still `NOT RUN` and still blocks**, which is a different thing from evidence
  that cannot currently be obtained

- **The length rule did not distinguish prose from evidence, and following it broke a
  chain of custody.** v4.2.1 said to cut by deleting the weakest material. Applied to the
  Additional Sources document — which is not prose but the evidence file every quotation
  is traced through — an agent hit the target exactly as instructed and **severed
  traceability for four quotations the Main Case went on to use**. It refused to repeat
  the cut and overran the target instead, which was correct. `write-document` now exempts
  the evidence file: let it run long, take the reduction out of the prose documents, and
  treat a very long evidence file as a signal to narrow the case rather than to delete
  rows. `case-config.yaml` marks `additional_sources` a guide rather than a ceiling

### Notes
- The run confirmed three of four claims under test — the freeze protocol, the
  post-correction re-verification pass, and the independence rule — and returned a partial
  on word budgeting: package overshoot fell from +41% to +27%, with the Main Case landing
  inside tolerance at +9% for the first time
- All five defects above were found by an agent following the kit's own instructions and
  reporting where they contradicted themselves. **Four of them had been read past
  repeatedly by maintainers**

## [4.3.0] - 2026-08-27

*Verification gains a freeze protocol and a mandatory second pass after corrections. Both
come from watching a full authoring run verify itself, then fixing what it found, then
discovering what the fixing had done.*

### Added
- **`/verify-all` step 0: freeze the tree.** A verification report describes the package
  at one moment, and the workflow never said so. In testing, a `/verify-all` log was
  written at 10:51, the documents it described were edited at 11:05, and by the time a
  second pass read that log **four of its statements were false about the files on disk**.
  The log was not wrong when written — it was wrong when read, which is worse, because
  nothing in it said so. The skill now records every document's **word count** in the
  report header before checking (a fingerprint that needs no terminal, so the Cowork path
  can do it), tells the author the tree is frozen, forbids the verifier from repairing as
  it goes, and re-reads the counts at the end. **If anything moved, the report is void and
  says so in those words** rather than being quietly patched to match

- **`/verify-all`: a required re-verification pass after corrections.** The workflow used
  to end at "fix the findings", and that is where the defects were hiding. Measured in the
  same run: fixing 25 findings **introduced 11 new ones** — stale counts copied from an
  interim draft, a footer contradicting the header in its own file, speaker miscounts, a
  quotation breaking a convention the same round had just added. Roughly two new problems
  for every five fixed. The new section requires freezing again, re-verifying with someone
  who did not make the fixes, and checking **both** that each fix landed and that the round
  introduced nothing new

- **"All fixed" is now explicitly a claim to be checked.** In the same test the authoring
  agent reported *"Fixed. All 15 converted to indirect speech or unquoted"* when **eight
  were still live** across all four documents. Not evasion — it had lost track. The skills
  now say to verify each reported fix against the source rather than against whoever
  reports it, and `AGENTS.md` carries the rule where every agent reads it

- **The two surprises are stated for authors in the README**, in the teaching section:
  fixing problems creates problems, and "I fixed everything" is frequently wrong in
  complete good faith. For a kit whose purpose includes showing where AI fails, these are
  among the most useful things it can hand someone in advance — they are currently learned
  by accident, late, and usually after publication

### Changed
- **`VERIFICATION_PLEDGE.md`** gains two header checkboxes — whether the last clean run was
  against a frozen package, and whether corrections since were re-verified by someone who
  did not make them — plus an eighth affirmation that corrections were confirmed against
  sources rather than assumed
- **`STARTER_PROMPT.md`** carries both rules in the author's own voice, so the chat path
  is not the one that quietly omits them

### Notes
- The honest status line this release adds: until a pass comes back clean **against a tree
  nobody edited during it**, nobody has read the package end to end without also changing
  it. That was true of the test package and went unnoticed until a second verifier said so

## [4.2.1] - 2026-08-27

*Three defects found by running the workflow with no slash-commands, as a Cowork user
would. Two were introduced in v4.0.0; the third has probably always been there.*

### Fixed
- **`documents.required` had no handling for a config that lacks it.** v4.0.0 told agents
  in bold to read that key before assuming four documents, and never said what to do when
  it is absent — which is the case for every project created before v4.0.0. An agent hit
  exactly that and had to guess. Both `AGENTS.md` and `write-document.md` now say: fall
  back to all four, mention once that the setting exists, continue. **A missing key is a
  default, not an error**

- **The Cowork path claimed no terminal was needed, and that was not true.** v4.0.0 said
  Cowork "does not require a terminal, an editor, or any developer setup" while the
  README's own Step 2 opens with `git clone`, `/export-pdf` hands over a Pandoc command,
  and `/git-update` is entirely git. The README now names all three and gives the
  non-terminal alternative for each — GitHub's Download ZIP button, opening the finished
  markdown in Word or Docs to make a PDF, and keeping the folder in a synced drive if you
  are not using git. **Nothing in the authoring, sourcing or verification workflow needs a
  terminal**; those three conveniences do, and saying so is better than a claim an author
  discovers is wrong at step two

- **Word-count targets were stated but never enforced, and agents overshoot badly.** In
  testing, an agent following `write-document` exceeded every target it was given —
  Main Case +37%, Supplement +49%, Teaching Note +23%, Additional Sources +55%, **+41% on
  the package**. Halving the targets in v4.2.0 achieves nothing if drafts land 41% over
  them. The skill now requires budgeting the target across planned sections *before*
  writing, checking the count when each document is finished, cutting when more than 10%
  over **before** showing the author, cutting by deleting the weakest material rather than
  compressing prose, and reporting the final count against target. A per-section length
  check is added to the inline verification, because over-length is far cheaper to correct
  a section at a time than in one pass at the end

### Notes
- All three were found by having an agent run the full workflow from `AGENTS.md` with no
  slash-command surface — the condition a Cowork user is in. That test also confirmed the
  v4.0.0 premise holds: the agent located every procedure through `AGENTS.md`, ran eight
  of them, and produced a complete four-document package without a single slash-command
- It does **not** substitute for running actual Cowork, and the README's "not yet
  field-tested" callout stands

## [4.2.0] - 2026-08-27

*Document lengths cut to roughly half, and `/setup-case` now recommends rather than
assumes. Prompted by a teaching colleague's observation that the kit's targets overwhelm
both the student writing the case and the professor revising it.*

### Changed
- **Target lengths halved.** The Main Case drops from 4,000-6,000 words to **2,000-3,000
  (about 8-12 pages at 250 words per page)**, and the other three scale to match. A
  complete package now lands near **7,500 words rather than 15,000** — exactly half a
  published teaching case. The reasoning is practical rather than stylistic: the author
  is usually writing alongside a full-time job, and the reviewer is a professor working
  through a stack of these. **A case nobody finishes reading teaches nothing, and a case
  too long to revise does not get revised**

- **`/setup-case` now asks about length — as a recommendation, not a specification.** It
  states one suggested size in plain terms ("about 2,500 words, roughly 10 pages… does
  that work, or would you like it longer or shorter?") and takes agreement as the answer.
  It does not present a menu, does not ask the author to name a word count, and does not
  ask them to size each document separately. Longer and shorter map to defined tiers;
  full published length exists but is never offered unprompted. The skill is explicitly
  told not to argue the author up or down from their answer

### Fixed
- **Three locations disagreed about document length, all introduced in v4.0.0.**
  `case-config.yaml` carried the lightened values, while the README table still
  advertised the original 4,000-6,000 word Main Case and — worse — **`setup-case.md`
  still wrote the heavy values into every newly generated config**, so running
  `/setup-case` silently overwrote the lighter defaults. The kit's own guidance was
  inconsistent with the kit's own behaviour. All four surfaces now agree, and the
  skill's config template reads the answered values instead of hardcoding any
- **`templates/PROMPTS.md` and `templates/FOLDER_TEMPLATE.md` restated word counts
  inline**, which is how the previous drift started. They now point at
  `documents.target_word_counts` rather than repeating a number that will age

## [4.1.0] - 2026-08-27

*The kit was overclaiming what its own checks establish — in a repository whose whole
subject is AI overclaiming. This release corrects the claims and makes the human's
accountability explicit everywhere an agent or an author will read it.*

### Changed
- **"Why You Can Trust What This Produces" is gone.** That heading promised something no
  workflow can deliver, and the section under it kept the promise up: *"every claim is
  tracked, tiered, and traced"*, *"you always know exactly what is sourced and what is
  not"*, *"`/verify-all` traces every quote to a dated source"*, and *"you can defend
  every sentence in your case."* **This project's own field testing falsified the third
  one** — a `/verify-all` run reported quotes passing on a package a later line-by-line
  trace showed carried five real quote defects. The section is now *"Built for
  Verification — and for Your Judgment"*, it says the kit surfaces issues rather than
  certifies output, and it cites that failure by name with a pointer to
  `evals/test-log.md`. A kit that asks authors not to overstate what their sources
  support should not overstate what its checks establish

- **The organizing metaphor is now explicit: the author is a manager delegating to a
  capable assistant.** The AI does real work and the author remains accountable for what
  ships under their name. The README carries a table splitting what the AI is good at
  from what only the author can decide, and states plainly that *"the AI generated it"*
  is not a defense a colleague, chair, or student should accept

- **`AGENTS.md` gains "Who Is Responsible"** — the behavioural half of the same idea,
  which matters more than the marketing half because every agent reads it. Never imply
  work is verified because a check passed; hand judgment calls back rather than settling
  them by picking whatever lets the work proceed; volunteer doubts at the time rather
  than burying them in a log; expect to be overruled by someone who knows their field.
  Plus a reporting rule: *"Traced 340 quoted spans; 12 could not be matched"* is useful
  to someone exercising judgment, *"Quotes: PASS"* is not

- **`VERIFICATION_PLEDGE.md` now claims work done rather than outcomes achieved.** It
  read as a certificate — *"Every quotation is traced"* — which is a claim about the
  package. Each item is now a claim about what the author personally did and judged, it
  opens with an explicit statement of accountability, and it closes by naming what the
  pledge does **not** claim: that every sentence was independently confirmed, that the
  checks caught everything, or that no error remains. It claims a named person looked
  and is accountable

- **The teaching purpose is stated as a purpose.** The kit is a tool for learning where
  current AI genuinely helps and where it fails — the fluent paragraph resting on a
  quotation that does not exist, the abundant source base that turns out to be the
  subject talking about themselves, the check that returned green without looking.
  Authors are told to notice those moments and write them down, and agents are told to
  name their own failures as material worth recording rather than smoothing over

- **Propagated to every author-facing surface** — README, `AGENTS.md`,
  `VERIFICATION_PLEDGE.md`, `STARTER_PROMPT.md`, `.github/copilot-instructions.md` — so
  the framing reaches all three tool paths rather than only the front page

### Notes
- No logic changed. Every check does exactly what it did in v4.0.0; what changed is what
  the kit says those checks mean
- The Cowork path added in v4.0.0 is still not field-tested, and its README callout
  stands

## [4.0.0] - 2026-08-26

*Repositioning release. Two defaults change: the recommended tool path, and how much
writing the kit asks of an author. Both come from a teaching colleague who forked v3.1.2,
rebuilt the onboarding around non-technical students, and reported back what worked. No
skill logic changed — the kit does the same things, and asks less of the person starting
out.*

### Changed
- **Claude Cowork is now the recommended path.** The kit previously offered three tools
  as a flat comparison table and asked a new author to choose between them before doing
  anything. That is a poor first question for someone who has never used a terminal.
  Cowork works on the project folder directly, needs no install, no editor and no command
  line, and reads `AGENTS.md` like every other agent. Step 3 now recommends it with a
  full inline quickstart, and the other three tools follow as *alternate paths, if you
  prefer one*, with the comparison table moved below the recommendation rather than in
  front of it

- **The slash-command fallback is now stated as the normal case rather than a
  degradation.** `/slash-commands` are Claude Code's format. `AGENTS.md` has always told
  other agents to read the skill file and follow its procedure, but buried it in a
  sentence; an agent could reasonably have told a Cowork user that a capability was
  unavailable. It now says explicitly: **the skill file is the specification and the
  slash-command is only a shortcut to it**, and never report a capability as unavailable
  for want of a command

- **Document scope is configurable, and the defaults are lighter.** `case-config.yaml`
  gains `documents.required` — the list of documents a course expects, in order — and
  `/write-document`, `/verify-all` and `/verify-cross-document` now read it instead of
  assuming four. **A document a course does not require is not a missing document**, and
  reporting it as one teaches authors to ignore the check. Word-count targets drop to a
  range sized for someone writing alongside a full-time job (Main Case 3,000 rather than
  5,000; Supplement 1,200 rather than 3,000), with the full-length figures kept in the
  file as a documented alternative
  - **The Teaching Note is unaffected as an artifact.** The skill that writes it is
    unchanged and it remains in `documents.required` by default. Removing it from that
    list is how a course expresses "the instructor writes this, not the student" —
    the capability does not go away

- **`STARTER_PROMPT.md` now opens by pointing chat users at Cowork.** The chat path
  exists for tools that cannot read local files, which means copying content back and
  forth. Anyone who can avoid that should

### Notes
- **The Cowork path has not been field-tested and the README says so in a status
  callout.** This is uncomfortable and deliberate. The kit's own evidence says the
  least-technical path is the one whose users are least able to notice a missing
  guardrail, and this release promotes an untested path to the front door. The callout
  states it plainly and asks for issues. **Running one case end-to-end through Cowork is
  the first thing the next release should do**
- Designed from the colleague's stated principles rather than from a diff of his fork,
  which was not available. Two claims in the third-hand summary of his changes were
  checked against this repository and found wrong — verification debt is gated at "zero
  **or acknowledged**", not at zero; and the kit's MIT relicensing at v3.2.0 left
  produced cases defaulting to CC BY-NC, so educational-content protection was never
  lost. Neither error changed the design, but both would have if taken on trust
- Major version because two defaults change, not because anything broke. Existing clones
  are unaffected; adopters who pull will find a different recommendation and lighter
  targets, both overridable in `case-config.yaml`

## [3.10.0] - 2026-08-26

*Instruction release. Three gaps that the field test and the compliance probes exposed
in the guidance itself rather than in any skill's logic. No behaviour changes to
tooling; `AGENTS.md` grows three sections and the writer's path gains a gate.*

### Added
- **`AGENTS.md` — "Who Verifies".** The kit had no rule about who runs verification.
  The agent that wrote a document is the worst available reader of it: it knows what it
  meant, so it reads intent rather than text; it has already judged each quotation once;
  and it has a stake in the work being finished. The rule is to prefer a verifier that
  did not author the documents, and — when that is not practical — to **say so in the
  report**, because an undisclosed self-review is indistinguishable from an independent
  one. A clean self-review is now explicitly a draft check rather than the publication
  gate. Wired into `verify-all.md` as a `Verifier:` header field with an explicit
  `SAME SESSION AS AUTHOR` value and a pre-flight step that labels the run without
  blocking it. **The evidence for this is uncomfortable**: the single verification run
  in this project's history performed by an independent agent recorded the condition in
  its own log — *"fresh eyes; did not author the documents"* — and found a spliced
  composite quote the authoring session had missed. The condition was met, noted, and
  never written down as a requirement, so every run since has been free to skip it

- **`AGENTS.md` — "A Check That Cannot Run Must Say So".** A check has three outcomes,
  not two: it passed, it found something, or it could not run. The third is never
  reported as either of the other two. This is the most recurrent bug in the project's
  history and it had been fixed six times without once being stated as a rule: a release
  workflow that silently did nothing for six versions; a preflight check that went green
  because it could not list a remote; a lint script that aborted on an old shell and was
  reported as lint violations against a clean tree; a quote tracer that extracted zero
  spans from wrapped quotations and called the document clean; an eval harness that
  handed its agents an empty source directory; and a link check that examined no URLs and
  was recorded as warnings. Each fix was local; the principle never reached the file the
  next author would read. The section carries the diagnostic that would have caught all
  six — *if this check were completely broken right now, what would it print?*

- **`write-document.md` — a quoting gate at drafting time (step 3b).** `AGENTS.md` has
  carried good quoting rules since v3.2.0, and the writer never saw them: the skill's
  only quote guidance was whether a quote had a named speaker and a dated source. So the
  rules lived entirely in the verification path and the writer kept creating exactly what
  the verifier then caught — unmarked smoothing has been counted in the dozens on three
  separate occasions. The new step **references the canonical rules rather than
  duplicating them** (two copies drift) and adds what belongs at drafting time: check a
  source's processing status *before* quoting it, **paste and trim rather than retype**,
  never quote from a summary or dossier, keep your own framing outside the marks, and do
  not smooth disfluencies inside quotation marks

### Changed
- **`/verify-all`'s inline quote check now asks about fidelity, not only attribution.**
  It previously asked whether every quote had a named speaker and a dated source. A
  correctly attributed quotation can still be misquoted, and the check was testing one
  of the two questions
- **`STARTER_PROMPT.md`** — the chat path carries the independence rule in plain
  language with a concrete instruction (*start a new chat for verification*). This path
  serves the least technical users, who are least able to notice a missing guardrail
- **`.github/copilot-instructions.md`** — its summary of what `AGENTS.md` covers was
  incomplete and now names the quoting rules, the verification-independence rule, and
  the check-integrity rule

### Notes
- All three changes are guidance, not logic. They are cheap, they are correct
  independently of the open question below, and none of them required new tooling
- **The field incident that prompted v3.9.0 is still unexplained.** The independence
  rule is the leading hypothesis for it and shipping the rule is not the same as
  confirming the diagnosis. See the v3.9.0 and v3.9.1 entries in `evals/test-log.md` for
  the three hypotheses already tested and falsified

## [3.9.1] - 2026-08-26

*A correction. v3.9.0 claimed two quote fixes worked; controlled testing shows one of
them did and one did not. No behaviour changes — the code stands, the claim does not.*

### Fixed
- **v3.9.0's claim about `/verify-quotes` was not supported by evidence, and is
  withdrawn.** The release said the skill "was reported as passed without being
  performed at the granularity it specifies" and rewrote its prose to force span-level
  enumeration. That rewrite has since been tested against the v3.8.0 text in a
  controlled comparison — two blind agents, identical corrupted documents, identical
  source corpus, the skill file the only difference — and **the v3.8.0 text scored
  identically: 5/5, including on a defect class named by neither skill text.** When
  `/verify-quotes` is run as an agent's whole task, the old wording was already
  sufficient. The rewrite is retained because it documents the failure classes more
  clearly, but it should not be described as having fixed anything

### Changed
- **The `/verify-all` change is the one that carries the release.** Re-tested under the
  condition the original failure actually occurred in — the quote check running as one
  of eight sub-checks rather than as the whole job — the two versions separate clearly.
  The v3.8.0 pipeline adjudicated 96 "distinct quotations" and missed one planted
  defect; the v3.9.0 pipeline enumerated 355 individual spans, verdicted all 355, and
  caught it. The missed defect — the author's framing pulled inside a quotation — is
  exactly what disappears when spans are grouped before checking. Separately, with no
  network access, the v3.8.0 pipeline recorded the link check as six warnings and did
  not block on it; the v3.9.0 pipeline reported `0 of 4 URLs requested`, declared the
  check **NOT RUN**, and blocked publication. **A check that examined nothing is not a
  check that passed**, and only the newer pipeline says so

### Notes
- **The incident that motivated v3.9.0 is still not explained.** Three hypotheses have
  now been tested and none reproduces it: the skill text was not inadequate, and
  orchestration alone does not induce a PASS — the v3.8.0 pipeline reported a quote
  failure and blocked distribution. What differed about the original run remains
  unknown; the untested candidates are a long preceding authoring session, a verifier
  checking documents it had itself written, and a real case with no planted defects to
  find. **A real weakness has been fixed without the incident having been explained,
  and those are not the same accomplishment**
- **Validating a fix by executing its procedure yourself measures the specification,
  not the behaviour.** v3.9.0's own validation ran the mandated procedure as a script
  and scored 6/6, which was reported at the time as evidence the change worked. It was
  evidence the change was *sufficient if followed*. Whether it would be followed took
  four blind agent runs to answer, and the answer was different for the two halves of
  the release
- Both probe runs, including the falsified prediction, are recorded in
  `evals/test-log.md`

## [3.9.0] - 2026-08-26

*First release driven by field evidence rather than by the author's roadmap. Two
complete four-document case packages were built against v3.8.0 by an operator other
than the author, on cases the author did not choose, against sources the author did
not curate. The intake method was fixed in writing before the material was read.*

### Fixed
- **The verification pipeline reported verdicts it had not earned.** `/verify-all`
  returned PASS on quotes for a document set in which a later span-by-span file trace
  found five substantive defects: two misquotes, a comparison reversed, framing pulled
  inside the quotation marks, dropped words, and constructed illustrations sitting in
  quotes attributed to named sources. The quote check had reasoned about *source
  categories* — "the essay quotations are quotable as written", "the ASR quotations use
  the bracket convention" — and never enumerated individual quoted spans. `/verify-quotes`
  already specified span-level tracing, requiring a source file and line number for a
  VERIFIED verdict and carrying a five-way MODIFIED taxonomy that names four of the five
  defects found. **The skill was not deficient; it was reported as passed without being
  performed at the granularity it specifies, and nothing in the output could tell the
  two apart.** `/verify-quotes` now requires mechanical enumeration of every quoted span
  of four or more words as a numbered list before any verification, states that a fact
  about a class of sources is not a verdict on any span, and requires spans-extracted
  and spans-verdicted to be equal or the check reports INCOMPLETE

- **`/verify-all` could launder a shallow sub-check into a pass.** Every sub-check must
  now report the number of units it examined — spans traced, figures recomputed, links
  requested, voices counted — in a new column of the summary table. **A check that
  cannot state its unit count is reported as `NOT RUN`, which blocks publication exactly
  as a failure does.** A verdict is earned by an amount of work and the report must show
  the amount; "PASS" with no unit count is an opinion, not a result

- **`scripts/lint.sh` aborted on macOS and preflight called it a lint failure.** The
  script used `mapfile`, a bash 4+ builtin, while macOS ships bash 3.2 as `/bin/bash`.
  It crashed at the file-collection line, and because preflight discarded stderr the
  crash was reported as "lint violations" against a tree whose markdown was clean — a
  substantive verdict the check never reached. Replaced with a `while read` loop;
  verified under bash 3.2 (53 tracked files, 0 violations). CI never caught this because
  GitHub runners have bash 5

- **Preflight checks 2 and 3 could not distinguish a crash from a finding.** Both were
  `if ./script >/dev/null 2>&1`, collapsing three outcomes into two. They now share a
  `run_gate` helper with an explicit convention — 0 clean, 1 a real finding, anything
  else means the check broke and its verdict means nothing — and a broken check reports
  `COULD NOT RUN` with the captured stderr. Verified by sabotage in all three
  directions: crash, real violations, and clean

### Changed
- **`/assess-sources` now computes an independence ratio and applies it as a cap on the
  overall gate**, rather than testing only for the presence of one independent source.
  A base of 33 sources that was ~82% the subject's own material scored YELLOW and
  proceeded, because the gate averages four dimensions of which two — Depth and
  Completeness — reward volume: a prolific self-publisher scores 5 and 4 there and pulls
  the average up past a RED reliability score, while independence entered only as a
  floor of one source. **The report named the imbalance accurately and then let it
  through; describing a problem is not gating it.** `independent_share` below 20% now
  caps the gate at RED, and between 20% and one third at YELLOW with the outcome layer
  blocked. Replayed against the four gate decisions in field testing, the cap changes
  exactly the one that was wrong and leaves the three that were right untouched.
  The skill now also distinguishes the two failure modes explicitly — a *thin* base
  fails for scarcity and is obvious, a *one-sided* base fails for concentration and
  looks like progress — and separates claims about what a subject thinks (where self
  sources are legitimate evidence) from claims about outcomes and firm scale (where
  they are not)

- **`/add-sources` now requires the raw capture of anything read live to be saved as a
  source file before registration.** Research delegated to subagents or read through a
  browser returns a dossier, and the dossier paraphrases; the verbatim wording stays in
  the session and dies with it, so quotations drawn from it trace to nothing. The chain
  of custody for a quotation runs page → committed file → document, and a hop that
  exists only in a session breaks it

- **Gate logs are no longer discarded by default.** `*.log` was added to `.gitignore`
  specifically to exclude verification-skill output; field testing showed that to be
  backwards, since the assessment and verification logs are the evidence that the gates
  ran and what they concluded. Of two cases built the same week, one kept its gate logs
  only because the operator noticed and forced the add, and the other kept none.
  `assess-*`, `verify-*`, `coach-*` and `scout-*` logs are now negated back in; stray
  logs stay ignored

### Added
- **Seeded defect set v3 — D17, D18, D19**, written before any of the above fixes, per
  the standing rule that bugs are test cases wearing disguises. D17 corrupts four
  quotations four different ways against untouched sources; D18 builds a deep base that
  is 80% company/self while still satisfying the floor-of-one independence test; D19
  registers a source whose only artifact is a summarizing dossier and quotes it. **This
  is the first defect set drawn from cases the author did not choose** — the most
  externally valid one in the project

### Notes
- **All four findings are the same shape**, and it is a shape this project has already
  fixed twice in its release tooling: a workflow that silently did nothing for six
  versions, and a preflight check that went green because it could not reach the remote
  it was meant to compare against. Both were caught and hardened. The same sweep was
  never run over the verification pipeline, which is the part users actually depend on
- **Sized deliberately as a minor version.** Every fix makes the existing architecture
  do what it already says — enumerate the spans, compute the ratio, keep the logs. No
  new stage, no new document, no change to the workflow map. The counter-argument is
  recorded rather than buried: if the two gates *are* the architecture, then "they
  narrate rather than gate" is structural and v4.0 would be defensible
- **What this field test did not cover**: both runs used the Claude Code path, so the
  Copilot and chat paths still have no field evidence — and the chat path serves the
  users least equipped to notice a missing guardrail. Neither case reached a classroom,
  so teaching readiness remains unmeasured. Two cases, one operator, one week

## [3.8.1] - 2026-07-31

### Added
- **Release preflight check 11: no local machine paths in tracked files.** This is a public template — absolute home directories, machine names, and session paths leak how a maintainer's computer is organized and are useless to anyone who clones the kit. The check greps tracked files for `/Users/...`, `/home/...`, `C:\Users\`, and application-support and session directories, and fails the release if any appear. A username segment must start with an alphanumeric and be followed by another segment, so prose describing the *shape* of a path is not mistaken for a real one — the first version of the check flagged its own changelog entry. Verified in both directions: clean tree passes, planted paths fail

- **Preflight check 10 now reports remotes it could not reach** instead of quietly skipping them. A remote that fails to respond is not a remote that agrees with you, and a check that passes because it failed to look is the same failure class that let `release.yml` no-op for six versions — found immediately, when an unauthenticated environment made the private remote unlistable and the check still went green

### Changed
- Preflight is now 11 checks, one of which can warn. `RELEASING.md` updated

### Notes
- Field testing of the kit against independent case examples is underway outside this repository. Findings will land in a subsequent release; the intake method is fixed in advance so that evidence drives the roadmap rather than confirming it

## [3.8.0] - 2026-07-28

### Fixed
- **Release automation had been silently doing nothing since v3.5.1.** `release.yml` triggered on a change to `TEMPLATE_VERSION`, then skipped if tag `v{version}` already existed. Because releases are pushed as `git push main --tags`, the tag always arrived with the commit — so the check always found it and the workflow always stood down. Six versions were tagged with no GitHub Release created, and nothing surfaced the gap because a workflow that skips looks identical to one that had nothing to do

### Changed
- **`release.yml` now triggers on pushing a `v*` tag.** Publishing a version and publishing its release notes become the same action, so neither can be forgotten without the other. The tag-exists check — the actual bug — is deleted, since the tag's presence is now the precondition rather than a conflict. The workflow never creates tags, so tags remain authored locally: one authority, and `release-preflight.sh` check 10 stays meaningful
- **The workflow fails loudly on a missing CHANGELOG section** rather than falling back to "see CHANGELOG for details." An empty release looks fine and tells a reader nothing; a red Actions run is visible and fixable. Preflight check 4 blocks this earlier — the workflow failure is the backstop
- **`/release-kit` step 8 and `RELEASING.md`** rewritten accordingly: confirm the release published rather than remember to publish it, with the `gh release create` path retained as documented fallback

## [3.7.0] - 2026-07-28

### Changed
- **`STARTER_PROMPT.md` brought current — the chat-tool path was four releases behind.** It carried v3.0-era methodology with no mention of scouting, coaching, source independence, processing status, verification debt, quote verdicts, or the go/no-go gate. The least technical users, least able to notice a missing guardrail, were running the weakest version of the workflow. Now included, in conversational form: pre-commitment scouting; the three separate source questions (tier = access, independence = whose thumb is on the scale, processing = can it support a quotation); a coaching step that names gaps, offers research, checks new material before it counts, and reports honestly whether an addition helped or hurt; voice-based rather than outlet-based perspective counting; verification-debt tracking during drafting; the full quoting rules; VERIFIED/MODIFIED/LIKELY/DISPUTED/APOCRYPHAL verdicts; and a pre-share checklist
- **Workflow map now points chat-tool users somewhere.** The map is written in slash commands, which Option C users cannot run. A note under it explains the path is identical and sends them to `STARTER_PROMPT.md`, which now cross-links back

## [3.6.0] - 2026-07-27

### Added
- **Workflow map in the README** — a Mermaid diagram near the top showing the whole path from cloning the template to teaching the case: scout, configure, gather and register sources, the go/no-go assessment gate, the coaching loop when sources are thin, writing the four documents, the publication gate, and publishing. Renders natively on GitHub and stays diffable like everything else here. Three things it makes visible that six sections of prose buried: the **two gates** that carry the design (`/assess-sources` blocks writing on thin sources; `/verify-all` blocks publishing unverified claims), the **three loops** that are normal rather than failure, and the verified case body as the destination
- **`docs/workflow-map.svg`** — the same map as a standalone image for slides, handouts, and printing. The README's Mermaid version is authoritative

## [3.5.4] - 2026-07-27

### Added
- **`release-preflight.sh` check 10 — published tags are immutable.** Compares every local tag against both remotes' tag *objects* and fails with the remedy. Written because a tag recreated locally (pointing at the same commit, but a new annotated-tag object) got a push rejected part-way through, after other refs had already landed. Verified by sabotage: recreated a published tag, confirmed the check fires and names the drift, confirmed it clears on restore

### Changed
- **`/release-kit` and `RELEASING.md`** — a non-negotiable rule stated up front: never amend a pushed commit, never recreate a pushed tag, and ask "has this been pushed?" before either. If a tag genuinely must move, delete it on the remote deliberately so the change is visible rather than force-pushed over. Push commands now use `;` instead of `&&`, since the two remotes are independent and a rejected ref on one should not silently skip the other

## [3.5.3] - 2026-07-27

### Changed
- **Remaining placeholder names genericized** — v3.5.2 fixed the two company-name examples; this completes the sweep. Eight further instances used real executives or names alluding to them, including one that fused two real people ("Teresa Carlson Waldron") paired with an invented title ("Chief Availability Officer"). Replaced across `case-config.yaml` (header example block and inline comments), the indirect-speech examples in `AGENTS.md`, `/verify-quotes`, and `QA_WORKFLOW`, and the source-filename examples in `SOURCE_ACQUISITION`. Placeholders now read `CompanyXYZ`, `Jane Doe`, `Doe`. A kit built on attribution discipline should not model a fabricated composite of real executives as an example. **Deliberately preserved**: real names in the testing history, `assess-bias` provenance, `defect-set.yaml`, `evals/`, and `examples/` — those record real runs against real sources, and genericizing them would destroy the evidence trail

## [3.5.2] - 2026-07-27

### Changed
- **Generic placeholders in setup examples** — the repository-naming example in the README and the company-naming example in `/setup-case` used a real pharmaceutical company. Replaced with `CompanyXYZ`, so nobody reads a placeholder as a suggestion. (References to that company in the testing history, bias-skill provenance, and defect-set remain: those are factual records of real runs, not examples.)

### Added
- **README note on maintainer files** — the template ships the tooling used to develop the kit itself (`scripts/`, `evals/`, `RELEASING.md`, `.gitignore-private`, and the `release-kit` and `run-eval` skills). Case authors can delete all of it; nothing in the case workflow depends on it

## [3.5.1] - 2026-07-27

### Changed
- **README Perplexity guidance** — rewritten: cut from ~700 words to ~260 and reframed around what Perplexity does well for this work (scouting a topic, finding and vetting sources, Computer's recurring tasks for keeping a source base current between semesters, Projects for working a corpus and sharing it with students). The handoff point — Perplexity works in its own environment, so bring sources into the repo and switch tools for authoring and verification — is stated once instead of repeated as a series of caveats

## [3.5.0] - 2026-07-27

Maintainer tooling and Perplexity guidance. This kit argues that important work needs checklists, verification gates, and logged provenance — while its own release process ran on memory. Three consecutive releases each failed at a manual step. This release makes the release process as disciplined as the case process.

### Added
- **`scripts/bump-version.sh`** — propagates a version to all seven files that restate it, then verifies; `--check` audits consistency without changing anything. Rejects non-semver input and detects drift in any single file
- **`scripts/lint.sh`** — lints *tracked* markdown exactly as CI does. Linting the working directory locally reported 78 violations where CI saw 10; the 68 phantoms came from gitignored eval content and hid the real ones
- **`scripts/release-preflight.sh`** — nine checks, each corresponding to something that previously went wrong. The critical one refuses to proceed if copyrighted eval corpus or golden baselines are staged for publication — the single error that cannot be undone once pushed to a public repository
- **`scripts/release-notes.sh`** — extracts a CHANGELOG section for `gh release create --notes-file`
- **`/release-kit` skill** — the judgment layer above those scripts: decide the semver bump, write the changelog, run preflight, commit, tag, push dev-then-public, verify what shipped
- **`/run-eval` skill** — orchestrates a regression run against a frozen fixture, including the separation of writer, verifier, and judge roles (an agent that checks its own work does not find the errors it just made) and honest interpretation of results
- **README — guidance for Perplexity users.** Many faculty have campus Enterprise Pro or Education licenses. Perplexity is well suited to scouting and sourcing, and cannot run the authoring workflow: Comet's agent is blocked from local files, Computer's filesystem is an isolated cloud sandbox, and only the Mac-only Personal Computer can touch a local folder — without documented git or shell support. Windows and Linux users have no Perplexity local-file agent at all. Also notes that inline citations make sources easy to find but do not confirm that a source supports the claim attached to it

### Changed
- **`RELEASING.md`** — pre-publish checklist replaced with the executable preflight; added a script reference table and the reasoning behind automating these steps
- **`AGENTS.md`, `README.md`, `CLAUDE.md`** — maintainer skills separated from authoring skills, so a professor writing a case is never offered `/release-kit`

## [3.4.0] - 2026-07-27

Adoption release. The kit was good and invisible: a prospective adopter landing on the repository had to imagine the output before deciding whether to invest a weekend. This release shows the work.

### Added
- **`examples/`** — excerpts from a real generated case package (JPMorgan LLM Suite, ITEC-617), so a prospective adopter can judge the output before investing time: main case opening, teaching note learning objectives and 80-minute session plan, source registry showing tier/independence/processing side by side, the `/verify-all` report including the two defects it caught, and the verification-debt ledger. Each excerpt is annotated with what to notice and why, and the folder README states the package's weaknesses (thin, executive-heavy source base) as plainly as its strengths. Linked prominently from the main README

### Changed
- **Terminology** — "HBR-style" replaced with "business school" throughout (README, AGENTS.md, STARTER_PROMPT, add-disclaimers, PROJECT_CONTEXT, CITATION.cff, PROMPTS). The kit teaches general case method, not one publisher's house style, and the previous wording invoked a trademark the project has no relationship to
- **`.markdownlint.json`** — MD029 disabled: step numbers in procedural skill files are semantic, and renumbering them to satisfy the linter would degrade them for human readers

### Fixed
- **Markdown lint CI** — ten violations resolved, six of which predated v3.1.0 and had left the build red long enough to stop being read. Two were structural defects introduced in the v3.3.0 release commit: a duplicate `### Added` heading in the changelog, and a horizontal rule placed directly after a paragraph, which markdown parses as a setext heading

## [3.3.0] - 2026-07-27

Source integrity release. Every change traces to a defect found by running the kit against real source material — the JPMorgan corpus baseline run and the 2026-07-27 coaching probes. The theme: tier measures *access*, but nothing measured *interest* or *quotability*, and documents were asserting rigor they couldn't support.

### Changed
- **`sources/Source_Registry.md`** — new **Independence** column (INDEPENDENT / INTERESTED / COMPANY / UNKNOWN, with the specific interest named) and **Processing Status** definitions (VERBATIM / EDITED / ASR / EXTRACTED). A full-text vendor-sponsored transcript is T1 *and* compromised; both facts now get recorded
- **`.claude/skills/add-sources.md`** — captures independence and processing status at registration, reading the document itself for sponsor reads, editorial notes, and ASR artifacts; warns the user immediately when a source cannot support verbatim quotation
- **`.claude/skills/assess-sources.md`** — new source-integrity step ahead of the go/no-go gates; downgrades Reliability when quoted T1 sources are edited or machine-transcribed; treats "no independent source" as blocking regardless of source count
- **`.claude/skills/verify-quotes.md`** — new **MODIFIED** verdict covering the five failure classes that look verbatim but aren't (spliced, silently corrected, smoothed, edited-source, assent-converted-to-assertion); establishes processing status before assigning any verdict; checks whether the documents' own integrity claims are true
- **`.claude/skills/assess-bias.md`** — counts by **voice** (who is speaking) rather than outlet (who published), since five interviews with one executive across five outlets is one perspective; flags interested non-company voices
- **`.claude/skills/add-disclaimers.md`** — audits integrity claims already in the drafts and replaces overstated ones with precise, supportable statements
- **`AGENTS.md`** — new canonical **Quoting Rules**: quote only from VERBATIM sources, never verbatim from an edited source, bracket convention for ASR, no splicing, attribute to the speaker rather than the venue, and never assert more integrity than the evidence supports
- **`evals/fixtures/jpm-llm-suite/defect-set.yaml`** — v2, 16 defects; six new classes all drawn from real production failures
- **`evals/fixtures/jpm-llm-suite/scripts/grounding_check.py`** — v2 fixes a quote-parity bug where one unpaired quotation mark caused the checker to compare narrative prose against the corpus (measured 54.8% → 78.7% on identical input)

### Added
- **`evals/fixtures/jpm-llm-suite/probe-set.yaml`** — repeatable coaching-skill probes with recorded pass criteria: coach gap-detection recall, scout calibration against actual post-sourcing assessment, scout discrimination
- **`/scout-case` skill** — pre-commitment coaching: scouts 1–4 candidate topics for whether they can support a case at all (protagonist voice and decision moment are fatal-if-absent; quantitative base, independent coverage, and perspective range grade quality), scores each on the same four dimensions `/assess-sources` uses later, and returns PURSUE / VIABLE WITH WORK / REDIRECT / AVOID with a starter source list. Prevents the most expensive failure in case development — discovering three weekends in that the company can't support a case
- **`learning-context.yaml`** — optional classroom-context config (audience program and per-domain fluency, session length/size/modality/format, prep expectations, teaching themes and target skill, which front-ends to generate, persona behavior, accessibility, and machine-readable guardrails). Front-end generators read it so one verified case body renders differently for different audiences — the mechanism behind mass customization
- **`RELEASING.md`** — two-remote workflow (private dev repo for daily work, public template for curated releases) with pre-publish checklist and guidance on eval assets vs. copyright
- **`/coach-case` skill** — the kit now acts as a coach and advisor, not just a pipeline: diagnoses gaps across five lenses (source-type coverage, voice-based perspective coverage, foundational confidence of load-bearing claims, biographical grounding for every named person/organization, rubric-facing weaknesses), offers targeted research help with proposed queries, runs a QA/QC gate (provenance/independence/corroboration/tier/risk) on everything gathered before it counts, measures before/after assessment deltas so additions that hurt are caught honestly, and logs every iteration to `coaching/coaching-log.md` with a git checkpoint
- **`templates/COACHING_LOG.md`** — iteration log template: gap map, QA/QC verdicts, teachable discrepancies, score deltas, helped/neutral/hurt judgment
- **`evals/`** baseline results: v3.2.0 baseline run vs frozen JPM corpus (10/10 seeded-defect recall, 31/35 judged; golden blessed after surgical fixes)

### Regression results (`evals/test-log.md`)
5/5 detection on the new defect classes, plus additional true positives. On the same documents, v3.2.0's verification reported ~225 verified quotes; v3.3.0 reports ~33 of ~195, because three of five sources cannot support verbatim quotation at all. The standard became accurate, not stricter for its own sake. Coaching-skill probes: `/coach-case` 6/6 gap-detection recall with eight verified novel findings; `/scout-case` calibration MAE 0.5 with zero signed bias.

## [3.2.0] - 2026-07-07

Trust and standards release: relicense to MIT, lead with the verification story, and adopt the AGENTS.md cross-tool standard so the kit works consistently across Claude Code, Copilot, Codex, Cursor, Gemini CLI, and other agentic harnesses.

### Changed
- **LICENSE** — Relicensed the kit from CC BY-NC 4.0 to **MIT** (loosening restrictions; sole-copyright-holder change). The kit's license now explicitly covers only the kit itself; case studies produced with it remain the author's work under the author's chosen license (`case-config.yaml` still suggests CC BY-NC 4.0 as a sensible default for educational materials)
- **CLAUDE.md** — Now imports canonical guidance from `AGENTS.md` (`@AGENTS.md`) and keeps only Claude Code-specific content (slash commands, between-document gates)
- **.github/copilot-instructions.md** — Slimmed to a pointer at `AGENTS.md` plus the Copilot skill-equivalents table (removes duplicated guidance that could drift)
- **.claude/skills/verify-quotes.md** — Added confidence verdicts (VERIFIED / LIKELY / DISPUTED / APOCRYPHAL) with required evidence per verdict, a publication rule (only VERIFIED ships in quotation marks), and an explicit trace-to-primary-source requirement (quote-aggregator sites are not verification)
- **README.md** — New "Built for Verification" section explaining verification debt, source tiers/gates, and the seven-check pipeline; new License section; updated badges to v3.2.0/MIT
- **templates/SOURCE_ACQUISITION.md** — Expanded legal guidance: keep case repos private during development, prefer links + excerpts for T2 sources, educational fair use is a balancing test not a blanket exemption

### Added
- **AGENTS.md** — Canonical, tool-neutral agent guidance following the Linux Foundation-stewarded AGENTS.md convention (read natively by OpenAI Codex, Cursor, Copilot coding agent, Windsurf, Zed, and others; Gemini CLI via one-line settings entry)
- **VERIFICATION_PLEDGE.md** — Author sign-off checklist converting the verification workflow into a shareable statement for colleagues, chairs, and editors
- **CITATION.cff** — Makes the kit citable (GitHub renders a "Cite this repository" button)
- **CONTRIBUTING.md** — Contribution path for other professors and practitioners, including the verified-body invariant for generator skills

## [3.1.0] - 2026-02-23

Add VS Code + GitHub Copilot as a second agentic AI path alongside Claude Code. Students with GitHub Education get Copilot Pro free, making this an accessible alternative with Agent Mode (file read/write, terminal commands, custom instructions).

### Added
- `.github/copilot-instructions.md` — Custom instructions for VS Code + GitHub Copilot Agent Mode, with skill equivalents table mapping all 16 `/slash-commands` to natural-language requests

### Changed
- **README.md** — Rewrote Step 3 with three tool options: Claude Code (Option A), VS Code + Copilot (Option B), Chat Tools (Option C). Added comparison table, "Getting Tech Help" subsection, Copilot references in Step 4, Skills Reference, file listing, and Troubleshooting
- **WORKFLOW.md** — Added VS Code + Copilot parallel instructions to each phase (Configure, Register Sources, Assess, Write, Verify). Updated Quick Reference section title and notes
- **STARTER_PROMPT.md** — Updated header to list VS Code + Copilot as another agentic tool that doesn't need this file
- **CLAUDE.md** — Added Copilot Compatibility section noting `.github/copilot-instructions.md`
- **templates/FOLDER_TEMPLATE.md** — Added `.github/copilot-instructions.md` to directory tree

## [3.0.0] - 2026-02-23

Major upgrade to conversation-first, skill-driven experience. Students interact through `/slash-commands` that handle all file creation/editing. Verification built into every phase.

Motivated by two rounds of testing:
- **Rob Silverman** (beginner): Exposed chat-tool breakage, code block confusion, decision overload, missing git checkpoints
- **Leif's Moderna case** (power-user, 17 steps): Exposed source friction, verification debt, financial errors, bias discovered late

### Added

#### New Skills (11)
- `/setup-case` — Conversational project setup (replaces `/setup-project`). Asks questions one-at-a-time, writes `case-config.yaml`, `PROJECT_CONTEXT.md`, and `verification-debt.yaml` programmatically
- `/add-sources` — Detects new files in `sources/`, asks metadata, classifies into quality tiers (T1/T2/T3), updates Source Registry
- `/write-document` — Interactive document writing with prerequisites checking, section-by-section writing, inline verification, and research loop support
- `/check-status` — Project dashboard with phase progress, verification debt summary, source tier breakdown, recommended next action (replaces `/guide-next-step`)
- `/validate-financials` — Extracts financial figures, checks arithmetic, cross-references against sources
- `/assess-bias` — Analyzes source composition for perspective balance: selection bias, survivorship bias, framing bias, authority bias, recency bias
- `/verify-cross-document` — Structural alignment between documents: Teaching Note references case content, Supplement frameworks used in analysis, timeline consistency
- `/add-disclaimers` — Standardized AI-generated content disclaimers (classroom/draft/publication contexts) and AI methodology notes
- `/export-pdf` — Formats documents for PDF export with heading hierarchy, page breaks, and conversion instructions

#### New Files
- `verification-debt.yaml` — Tracks unverified AI-generated claims with statuses (unverified/verified/removed/flagged)
- `sources/Source_Registry.md` — Source catalog with quality tiers (T1 primary, T2 partial, T3 referenced), replacing `Source_Links.md`

#### New Concepts
- **Source Tiers**: T1 (full-text in repo), T2 (partial/paywalled), T3 (referenced only)
- **Verification Debt**: Automatic tracking of unsourced AI claims during writing
- **Research Loops**: Named concept for iterative source-gathering during writing
- **Go/No-Go Gates**: GREEN/YELLOW/RED assessment for source readiness
- **Verification Gates**: Lightweight checks between documents

### Changed

#### Skills Enhanced
- `/assess-sources` — Added source tier breakdown, go/no-go gates (GREEN/YELLOW/RED), minimum viable source check, early bias detection
- `/verify-all` — Added `/validate-financials`, `/assess-bias`, `/verify-cross-document` to sequence; added verification debt summary and pre-publication checklist
- `/verify-consistency` — Added integration with `verification-debt.yaml`
- `/git-update` — Updated Co-Authored-By to Opus 4.6

#### Entry Points Rewritten
- **README.md** — One default path (not "choose"), separate code blocks per platform (Mac/Windows), troubleshooting section, agentic vs chat tool distinction, git checkpoints in workflow
- **STARTER_PROMPT.md** — Rewritten for chat tools only. Clear header distinguishing chat vs agentic tools. File upload workflow. No local file path references. Self-contained prompt
- **CLAUDE.md** — Removed overlap with STARTER_PROMPT. Added conversation-first behavioral instructions, iterative process model, verification debt tracking, source tier definitions, updated skill table (16 skills)
- **WORKFLOW.md** — Replaced linear 6-step with iterative model showing research loops. Added verification gates between documents. Added skill-driven workflow. Added "Targeted Edits" phase

#### Templates Updated
- **PROMPTS.md** — Added Phase 2.5 (Source Tier Classification), Phase 7.5 (Financial Verification), Phase 7.6 (Bias Assessment), Phase 8 (Disclaimers and Final Preparation)
- **QA_WORKFLOW.md** — Added `/validate-financials`, `/assess-bias`, `/verify-cross-document` to check schedule; added verification debt section; updated pre-publication checklist
- **SOURCE_ACQUISITION.md** — Added Source Tier Classification section, "Working with AI Web Access Limitations" section, expanded research workflow with iterative loops
- **FOLDER_TEMPLATE.md** — Updated directory structure with `verification-debt.yaml` and `Source_Registry.md`; updated skill list (16 skills); updated post-clone setup to reference `/setup-case`

#### Configuration
- `case-config.yaml` — Added `case.case_type` field ("business" or "public_policy"); added auto-generated header comment; updated template version to 3.0.0

#### Infrastructure
- `validate-template.yml` — Updated required files list for all new skills and files; added verification-debt.yaml validation

### Removed
- `.claude/skills/setup-project.md` — Replaced by `/setup-case`
- `.claude/skills/guide-next-step.md` — Replaced by `/check-status`

## [2.0.0] - 2026-02-21

Major simplification. Refocused the starter kit around an AI-guided workflow with a clear entry point, removing premature community infrastructure.

### Added
- `STARTER_PROMPT.md` — The centerpiece entry point. Students copy this prompt into any AI tool (Claude Code, ChatGPT, Gemini, Perplexity) to get guided through the entire case study development process
- `/assess-sources` skill — Evaluates source materials across four dimensions (depth, breadth, reliability, completeness) and produces a Source Assessment Report
- `/guide-next-step` skill — Checks project state and recommends the specific next action to take

### Changed
- **README.md** — Rewritten from 823 lines to ~140 lines. Now a student-focused quick start guide instead of a full methodology reference (detailed prompts remain in `templates/PROMPTS.md`)
- **CLAUDE.md** — Rewritten with "Your Role" and "How to Behave" sections that define Claude as an interactive case study development guide
- **WORKFLOW.md** — Simplified from 352 lines to ~120 lines. Six clear steps: Gather, Configure, Prompt, Develop, Verify, Publish
- **case-config.yaml** — Added prominent header with concrete example (Tesla factory automation) to make the first-edit experience more approachable
- **validate-template.yml** — Updated required files list (removed deleted files, added new ones)
- **FOLDER_TEMPLATE.md** — Removed reference to deleted `SKILLS_SETUP.md`
- **PULL_REQUEST_TEMPLATE.md** — Removed reference to deleted `CONTRIBUTING.md`

### Removed
- `CONTRIBUTING.md` — Premature community infrastructure
- `HALL_OF_FAME.md` — Premature community infrastructure
- `COMMUNITY_REGISTRY.md` — Premature community infrastructure
- `docs/ECOSYSTEM.md` — Premature community infrastructure
- `docs/GITHUB_PAGES.md` — Premature community infrastructure
- `docs/patterns/` — Entire pattern library directory (premature)
- `_config.yml`, `Gemfile`, `index.md` — Jekyll/GitHub Pages files
- `.github/workflows/update-registry.yml` — Community workflow
- `.github/workflows/stale.yml` — Community workflow
- `.github/workflows/issue-labeler.yml` — Community workflow
- `.github/workflows/pages.yml` — GitHub Pages workflow
- `.github/ISSUE_TEMPLATE/register-project.yml` — Community issue template
- `.github/ISSUE_TEMPLATE/submit-innovation.yml` — Community issue template
- `templates/SKILLS_SETUP.md` — Redundant (skills already exist in `.claude/skills/`)
- `templates/workflows/` — Downstream project workflow (premature)

## [1.1.0] - 2026-02-20

### Added

#### GitHub Pages Website (Disabled)
- **Just the Docs theme** - Professional documentation site configuration
- `_config.yml` - Jekyll configuration with remote theme
- `index.md` - Attractive landing page with methodology overview
- `Gemfile` - Ruby dependencies for Jekyll
- `.github/workflows/pages.yml` - Auto-deployment workflow (currently disabled)
- Front matter added to README.md, WORKFLOW.md, docs/ECOSYSTEM.md for navigation
- `docs/GITHUB_PAGES.md` - Documentation for enabling/disabling the feature

#### Ecosystem Hub Features
- **Community Registry** (`COMMUNITY_REGISTRY.md`) - Voluntary project registration system
- **Pattern Library** (`docs/patterns/`) - Curated collection of community-contributed patterns
- **Hall of Fame** (`HALL_OF_FAME.md`) - Recognition for contributors
- **Ecosystem Guide** (`docs/ECOSYSTEM.md`) - How to participate in the community

#### Issue Templates
- `register-project.yml` - Register case study projects to join community
- `submit-innovation.yml` - Submit prompts, skills, or workflow improvements

#### Automation Workflows
- `release.yml` - Auto-create GitHub releases when TEMPLATE_VERSION changes
- `update-registry.yml` - Auto-update community registry from registration issues
- `issue-labeler.yml` - Auto-label issues based on title and content
- `stale.yml` - Manage stale issues and PRs

#### Downstream Project Support
- `templates/workflows/check-template-updates.yml` - Workflow for case repos to check for template updates

### Changed
- Enhanced `templates/RETROSPECTIVE.md` with AI-Specific Innovations section

### Previous
- WORKFLOW.md with complete end-to-end workflow documentation

## [1.0.0] - 2026-01-12

### Added

- Initial template release
- 8-phase case study development methodology in README.md
- Template files:
  - `PROMPTS.md` - Copy-paste prompts for each development phase
  - `SKILLS_SETUP.md` - Claude Code verification skill templates
  - `QA_WORKFLOW.md` - Quality assurance procedures
  - `SOURCE_ACQUISITION.md` - Research and materials management guide
  - `FOLDER_TEMPLATE.md` - Project structure quick-start
  - `RETROSPECTIVE.md` - Post-case-study feedback capture
- Parameterized configuration via `case-config.yaml`
- Claude Code verification skills in `.claude/skills/`
- GitHub Actions CI/CD:
  - Markdown linting
  - Link validation
  - Template structure validation
- GitHub Issue templates for continuous improvement
- Contributing guidelines
