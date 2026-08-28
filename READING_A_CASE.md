# Reading a Case Critically

*For students. Use this on a case you were handed, and on the case you built yourself —
your own is the harder one, and the more useful.*

---

## This is the actual assignment

Building the case teaches you how AI drafts. Checking it teaches you something you will
use for the rest of your career: **how to be accountable for work you did not write.**

You will spend that career receiving AI-assisted material — analyses, memos, models,
summaries — and signing your name to decisions based on it. The skill is not "spot the
robot." Modern AI writing is fluent, well-organized, and confident, and it is confident
in exactly the same voice whether it is right or wrong. **Fluency carries no
information about accuracy.** The skill is knowing where to look, and having the habit
of looking.

A case study is an unusually good training ground for this. The sources are finite and
in front of you, the errors are findable in an afternoon, and nobody loses money when
you miss one.

---

## What actually goes wrong

Every failure below is real. Each was found in a case built with this kit, and each is
recorded in `evals/test-log.md` and `lessons_learned.md` with the run it came from. They
are not hypotheticals and they are not rare.

### 1. The quotation that is almost right

The most common defect, and nearly invisible on a read-through. Words go missing from
the middle of a quote. A comparison reverses — the source says *"more Roman Empire
decline than dinosaur extinction"* and the case says *"decline, not extinction."* The
sentence's framing gets pulled inside the quotation marks, so words the author wrote
appear as words the speaker said. Sometimes an illustration the author invented sits in
quotes with a real person's name attached.

**In one package, five of these survived a verification pass that reported quotes
clean.** They were found later, by tracing every quoted span to its source file one at a
time.

### 2. Assent converted into assertion

An interviewer states a figure. The subject says *"yeah, it's correct."* The case then
reports the figure as the subject's own claim.

This happened with a headline number — *30,000 AI assistants* — that appeared exactly
once in the transcript, **spoken by the podcast host.** The executive's entire
contribution was five words of agreement. One document in the package disclosed this
properly. The other three carried it as established fact, and it was in the case title.

Ask of any striking number: **who said it first, and was the other person just being
polite?**

### 3. The rich source base that is one voice

A case rested on 33 sources. Roughly 82% of them were the subject describing himself —
his company's pages, his own essays, friendly interviews. The source list looked
impressive. The assessment even said so in prose, and then let the case proceed.

**Count voices, not sources.** Five interviews with the same executive in five
publications is one perspective, not five. Ask who is missing: an employee, a customer,
a regulator, a competitor, anyone who would lose something if the story were true.

### 4. The edited transcript quoted as speech

Many published interviews carry a line like *"this conversation has been edited for
clarity and length."* That means the words on the page are the editor's arrangement of
what was said. They are excellent evidence of what someone thinks. They are **not** that
person's exact words, and quoting them as verbatim speech is a small fabrication.

The same applies to machine transcripts — auto-generated captions garble names and
technical terms, and "cleaning them up" inside quotation marks invents speech.

### 5. The check that passed without looking

A verification run reported quotes as passing. It had reasoned about *categories* of
source — "the essay quotations are quotable as written," "the transcripts use the
bracket convention" — and never examined a single individual quotation.

**A conclusion is not a result.** When any check tells you it passed, ask what it
examined and how much. "Quotes: PASS" tells you nothing. "Traced 340 quoted spans; 12
could not be matched to a source" tells you a great deal.

### 6. The correction that made things worse

Twice, in separate runs, fixing about 25 verification findings **introduced 11 or 12 new
ones** — stale numbers copied from a draft, a footer contradicting the header in its own
file, a quotation breaking a rule the same round had just added.

And in one of those rounds the AI reported *"Fixed. All 15 converted"* when **eight were
still sitting in the documents.** It was not being evasive. It had lost track across a
long round of edits, exactly as a person does.

**Repair is editing, and editing introduces errors. "I fixed everything" is a claim to
check, not a result to accept.**

---

## The thirty-minute check

You cannot verify everything, and you do not need to. Do this instead. It is deliberately
short enough that you will actually do it.

**1 · Trace five quotations, character by character.** Pick the five that carry the most
weight — the ones the argument would collapse without. Open the source file and find the
exact words. Not the gist. The words. Most defects live here.

**2 · Ask who is speaking, and whether they volunteered it.** For each quotation and each
striking number: who said it first? If a striking figure came from the interviewer, the
case cannot present it as the subject's claim.

**3 · Count the voices.** List every person quoted. Mark each as independent, interested,
or company. If more than half your substance comes from people with a stake in how the
story reads, the case has a structural problem no amount of good writing fixes.

**4 · Take one number and follow it.** Any number. Find where it first appears, check the
arithmetic if it was derived, and check whether every document in the package uses the
same value. Packages disagree with themselves surprisingly often.

**5 · Read what the documents claim about themselves.** If a case says "all quotations
are verbatim," check whether that is true. **A false claim about the work's own rigor is
worse than the defect it conceals**, because it tells the reader not to look.

**6 · Ask each check what it examined.** Not whether it passed. How many things it
looked at, and what it could not reach. A check that could not run — no network, no
access — is not a check that passed.

---

## Three exercises

**A · Find the planted defects.** `evals/fixtures/jpm-llm-suite/defect-set.yaml` holds 19
deliberately seeded errors drawn from real misses. Have someone inject a few into a copy
of a finished case and hand it to you cold. Score yourself on how many you find, and — the
more interesting number — how many you were confident about but wrong on.

**B · Verify a classmate's case, then have them verify yours.** This is the highest-value
half hour in the exercise. **You are the worst available reader of your own work**: you
know what you meant, so you read your intention rather than the words on the page. In
testing, independent readers routinely found defects the author had looked straight past —
including a word the author had invented inside quotation marks and never noticed.

**C · Break your own case on purpose.** Take a finished document, plant three defects of
different kinds, and give it to someone else. You learn more about where errors hide from
designing them than from finding them.

---

## What to write down

The reflection is not a formality; it is where most of the learning actually lands. After
each round, record:

- **One thing the AI did well that would have taken you hours.** Be specific and honest.
  The point is not to conclude that AI is unreliable — it is to know *where* it is
  reliable.
- **One thing it got wrong that read perfectly.** Quote it. Note what tipped you off, or
  note that nothing did and you found it only by checking mechanically.
- **One thing you accepted without checking, and why.** This is the most useful entry and
  the most uncomfortable one. Everyone has some. Naming the reason — it looked plausible,
  you were tired, it agreed with what you expected — is how you learn your own failure
  pattern.
- **Where you overruled the tool and were right.** These matter. Your judgment about
  whether a source is credible or a framing is fair is not something the tool has.

---

## The habit worth keeping

**"The AI generated it" is not a defense**, and it will not be accepted by a colleague, an
instructor, a client, or a board. Anything you hand over becomes yours the moment you
hand it over.

That is not a reason to avoid these tools. It is the reason to work like a manager who
delegates: give the work to a capable assistant, expect competent output, and check it
before it goes out — because your name is on it and theirs is not.

---

*The failures cited here are drawn from this project's own records. The maintainers
found every one of them the hard way, usually after publishing something that turned out
to be wrong. `lessons_learned.md` has 76 entries and most of them are mistakes.*
