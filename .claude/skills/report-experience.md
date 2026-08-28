# Report Experience

Offer to send the kit's maintainers a short report on how this run actually went, as a
GitHub issue the user reviews and submits.

## Usage

```
/report-experience
```

Offer it **unprompted** when a case package is finished or when the user is wrapping up —
after `/verify-all`, after `/export-pdf`, or whenever they say they are done. Offer it
**once**. If they decline, do not raise it again.

## Why this exists

Almost everything this kit knows about its own failures came from watching real runs. The
maintainers cannot see those runs. **You can** — you have just spent an hour inside one,
and you know things the user cannot report:

- which instruction you had to interpret because it was ambiguous
- what you worked around silently
- which step took far longer than it should have
- what the kit asked for that did not exist
- where a check told you something that turned out to be wrong

A user asked "how did that go?" a month later remembers almost none of this. **You have it
now, and in an hour it is gone.**

## Instructions

### 1. Ask once, plainly

> "Before we finish — would you like me to send the kit's maintainers a short note on how
> this went? I'd draft it, you'd review it, and you'd click submit. It takes a minute and
> it's the main way this thing improves. Happy to skip it."

If they say no, stop. Do not ask again this session.

### 2. Draft it from what you actually saw

**Write the draft yourself, from your own memory of the run.** Do not interview the user
field by field — you were there for the parts that matter most and they were not watching
you work.

Pick the **single most useful thing** from this run. One good report beats five vague ones.
In order of value:

1. **Something you worked around.** Highest value by a distance. Anywhere you deviated from
   the kit's instructions because they did not fit — a step skipped, a file edited by hand
   that was meant to be automatic, an instruction you interpreted because it was ambiguous,
   a field you left blank because the course did not use it. **You will have done at least
   one of these and thought nothing of it at the time.** Go back and look.
2. **Something the kit said that was wrong** — a check that passed over a real problem, a
   file it referenced that does not exist, a claim contradicted by another file.
3. **Something that took much longer than it should have.**
4. **A place the kit assumed a kind of case that did not match this one** — the subject, the
   sources available, the course, the time the author had.
5. **Something that worked notably well**, if nothing above applies. Knowing what to protect
   is worth something.

Classify it: **DEFECT** (did something incorrect) · **GAP** (did nothing where it should
have) · **FRICTION** (right, but slow or confusing) · **MISFIT** (assumed a case shape that
did not hold) · **WORKED WELL**. A rough call is fine.

### 3. Keep the case out of it

**A report describes the kit's behaviour, never the case's content.** This is not optional
and you must apply it while drafting, not ask the user to catch it afterwards.

Never include: passages from the case, source material, quotations from sources, the
student's work, file paths from the user's machine, or names of people in the case where
the point can be made without them.

Write the behaviour instead:

- Not *"it let us cite Waldron 14 times without an independent source"*
- But *"the assessment cleared a base where one executive carried most of the substantive claims"*

Naming the company is usually fine and often useful — public companies and public sources.
Naming a student is not. When unsure, leave it out; the behaviour is what matters.

### 4. Build the link

Read the version from `TEMPLATE_VERSION`. Then URL-encode each value and assemble:

```
https://github.com/leifulstrup/Agentic-AI-Case-Study-Development-Starter-Kit/issues/new?template=field-report.yml&version=VERSION&what_happened=TEXT&workaround=TEXT&expected=TEXT
```

The form's own fields are `version`, `path`, `role`, `stage`, `kind`, `what_happened`,
`workaround`, `expected`, `context`. Prefill what you can; the dropdowns the user picks
themselves in a couple of clicks.

**Use the link, not a command line.** Do not run `gh issue create` — it needs a GitHub CLI
and an authenticated account, and most people using this kit have neither. A link works
from every tool path including Cowork and chat, needs no install, and — the real reason —
**puts the submit button in the user's hand.** You draft; they decide.

### 5. Show them the text before the link

Paste the drafted report in the conversation first, then the link. They should see exactly
what will be posted without opening a browser to find out.

> "Here's what I'd send — have a read and change anything. \[draft\] \
> If it looks right, this link opens it pre-filled on GitHub and you can submit it:
> \[link\]"

**Never post on their behalf**, and never describe it as sent. It is posted when they click
submit, and you will not know whether they did.

### 6. If they would rather not use GitHub

Offer to write the same text to `field-report.md` in the project folder so they can email it
or hand it to a colleague who will file it. A report that reaches the maintainers by any
route is worth more than one that never gets written.

## Notes

- **One report per run.** Do not batch several issues; pick the most useful thing.
- **Students should ask their instructor first** if the work is graded or the course has
  rules about sharing coursework. Say so when the user is a student.
- The maintainers re-classify everything on their end. A wrong `kind` costs nothing; a
  report not sent costs the whole signal.

## Output

No log file. The draft goes in the conversation, and the issue is the artifact — if the
user submits it.
