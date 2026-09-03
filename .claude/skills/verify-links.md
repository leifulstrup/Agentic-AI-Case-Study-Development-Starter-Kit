# Verify Links

Validate all external URLs in case study documents.

## Usage

```
/verify-links [filename]
```

If no filename provided, verify links in all .md files.

## Instructions

1. **Extract all URLs** from the specified document(s):
   - Markdown links: `[text](url)`
   - Raw URLs: `https://...`
   - Reference-style links

2. **For each URL found**:
   - Record the URL and context
   - Use WebFetch to check accessibility
   - Verify page contains expected content

3. **Generate a report** with:
   - Total links checked
   - Working links (with expected content)
   - Working links (content mismatch)
   - Broken links (404, timeout)
   - Redirected links

   **Sort the failures — they are not the same finding.** A URL that answered is not a URL
   that is gone, and reporting them together tells the author nothing about what to do.

   | What happened | Verdict | What it means |
   |---|---|---|
   | 200, content matches the citation | **OK** | Nothing to do |
   | **403 / 429 / login wall / bot check** | **BLOCKED — not verified, not broken** | The host answered and refused. The source may be perfectly fine; you could not check it from here |
   | 404, 410, DNS failure | **DEAD** | A real defect. The citation points at nothing |
   | No network at all | **NOT RUN** | You did not look. Blocks publication |

   **BLOCKED is the common case and the kit previously had no word for it.** In a real run,
   `cnbc.com` returned 403 and `youtu.be` returned 429 — both live, both refusing automated
   requests. Reporting those as "broken" would send an author hunting for a replacement
   source that is not actually missing; reporting them as "checked" would claim a
   verification that did not happen.

   For each BLOCKED link: say the host answered, give the status code, and tell the author
   this one needs a human with a browser. That is a thirty-second task they can do and you
   cannot. **Do not retry in a loop and do not work around a bot check** — that is what the
   403 is for.

   A run where every link is BLOCKED is **not** a clean link check. Report the check as
   NOT RUN with the blocked count, so the pre-publication checklist stays honest.

### Tell the author what to do about it

**Never leave a blocked link as a silent gap.** The author cannot exercise judgment over a
check they do not know failed. List the specific URLs, say what happened to each, and lay
out the options — then let them choose. Do not choose for them, and do not push them
toward installing anything.

Present it roughly like this, adapted to what actually blocked:

> I could not verify 3 links. Two returned 403 (the site refused an automated request) and
> one returned 429 (rate limit). The pages are probably fine — I just could not reach them
> from here. Options, easiest first:
>
> **Open them yourself.** Click each one, check the page says what the citation claims,
> and tell me. About 30 seconds per link, and it is the most reliable answer available —
> a human with a browser is exactly what these sites are checking for.
>
> **If you are in Claude Cowork**, its built-in browser can often open pages that a plain
> fetch cannot, since it behaves like a real browser session. Worth trying before anything
> else.
>
> **For paywalled scholarly sources**, your university library proxy will usually get you
> in with credentials you already have and no new software.
>
> **There are third-party fetch and scraping services** that handle this class of blocking.
> They work, and they are a bigger step than the others: you would be installing software
> or connecting a service that gets access to what it fetches, usually with an API key to
> manage. If you go that way, prefer something you or your institution already use and
> have vetted. I am not recommending a specific one.
>
> Whatever you choose — **including doing nothing** — these three stay marked unverified in
> the package until someone confirms them. That is an honest state to publish in, as long
> as it is disclosed.

Rules for you, the agent, in that conversation:

- **Do not try to get around a bot check.** No retry loops, no alternate user agents, no
  cache or mirror services standing in for the source. The 403 is the site's decision and
  working around it is not verification — it is a different page that might say something
  else.
- **Never suggest anything involving the author's credentials** — no logging in on their
  behalf, no tool that wants their passwords or session cookies.
- **Do not rank third-party tools or name a favourite.** Say the category exists, say
  plainly what adopting one costs in access and trust, and stop. The author knows their
  institution's rules and you do not.
- **An unverified link stays unverified in the report** no matter which route they take.
  The goal is an accurate record, not a clean-looking one.

4. **For each problem**, provide:
   - Document and line where link appears
   - Expected content vs. found
   - Suggested fix

## Output

Create a log file:
- Filename: `verify-links-YYYY-MM-DD.log`
