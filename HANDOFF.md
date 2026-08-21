# MPIP26 Email Campaign — Handoff (2026-08-22)

## Where everything lives
- **Local working folder:** `~/Downloads/MPIP26-Emails/` (git repo, remote = `syvonnek/mpip26-email-preview` on GitHub)
- **Published preview (GitHub Pages, live):** https://syvonnek.github.io/mpip26-email-preview/
  - `index.html` — list view, one link per email
  - `all-emails.html` — all 7 stacked on one page (built for the ChatGPT audit round, still useful)
- **Campaign copy source:** `~/Downloads/MPIP26-Campaign-Plan.html` (Tyree's plan — treat as a first draft, not gospel)
- **Live event site (source of truth for facts):** https://postinpremiere.com
- **Curated brand asset library (Google Drive, syvonnek@fmctraining.com):** "Modern Post in Premiere - Social Assets" — logos, instructor portraits, hero photography, Color Mode screenshots for both days. Local mirror at `assets/drive-src/`.
- **Deploy workflow:** edit → `git add -A && git commit && git push origin main` → GitHub Pages rebuilds in ~30-60s at the same URL.

## What's built
All 7 emails exist and are live in the preview:
1. `MPIP26-Email-01-Launch-Announcement.html` — **most polished, the flagship** (see below)
2. `MPIP26-Email-02-ColorMode-DeepDive.html` — Day 1 session-by-session
3. `MPIP26-Email-03-AITrack-DeepDive.html` — Day 2 session-by-session
4. `MPIP26-Email-04-OneWeekOut.html` — countdown, time zones, group quote
5. `MPIP26-Email-05-LastCall.html` — final reminder
6. `MPIP26-InCart-01.html` / `MPIP26-InCart-02.html` — abandoner recovery

**Important asymmetry:** Email 1 received many rounds of visual iteration (hero image, Day 1/Day 2 card redesign, Event Details card) that the other 6 did **not** get ported to. Only the *global/mechanical* fixes (logo sizing, eyebrow typography, Questions-Contact card fonts, arrow alignment, contact links) were applied everywhere via sed/Python across all 7 files. If Syvonne wants the Email 1 treatments (Event Details card, Day-card style) mirrored elsewhere, that's still open.

## Design system
- Colors: bg `#030611`, spectrum gradient cyan `#22D3EE` → blue `#4F7CFF` → violet `#8B5CF6` → magenta `#E34FCB`
- Font: Source Sans 3 (Google Font, loads fine in email) + Arial/Helvetica fallback
- Logo lockup ratio (verified via `getBoundingClientRect()` on the **live site**, not assumed): FMC height 34 : Adobe height 48 — **Adobe is significantly taller/bigger than FMC**, not equal. Current email sizing: FMC 58×30, Adobe 78×42 (assets: `fmc-logo-nav.png`/`fmc-logo-footer.png` and `adobe-logo-nav.png`/`adobe-logo-footer.png`, both regenerated from Drive source files at this ratio).
- UTM scheme on every link: `utm_campaign=MPIP-2026&utm_source=hs_email&utm_medium=email&utm_content=<page>_<location>`
- Register/CTA links point to `postinpremiere.com/?...#pricing` (⚠️ **not** `#register` — that anchor doesn't exist on the live site)
- Contact links go to the site's contact modal, not mailto: `?contact=megan#contact` (event inquiries) or `?contact=elise#contact` (group registration), each with its own UTM tag
- No photo for Megan Belka's contact card — text only

## Known flagged assets — never use
Documented in memory (`adobe-color-flagged-assets`): Megan Belka's photo and an older Alexis Van Hurkman crop on postinpremiere.com carry a branded arrow/chevron treatment traced to a different site's template. The curated Drive folder deliberately excludes them. Always pull instructor portraits from `02 Instructor Portraits/` in the Drive folder, never scrape them fresh from the live site.

## Content accuracy — verified against the live site + ChatGPT audit this session
Applied and confirmed via QA grep (zero remaining instances):
- Eran Stern / Luisa Winters titled "Co-Program Manager · Adobe Expert" everywhere (not "Adobe Master Trainer")
- No claim that they "lead both days" — Day 2 currently only confirms Luisa (Session 1) and Eran (Session 3); the rest are Speaker TBD and are named as such (session only, no fabricated speaker)
- Recording access language is ticket-tier-qualified throughout ($99 = that day's recording, $149 = both days')
- No "questions gathered from attendees" claim (unsupported); no "even joining for one lab" guarantee
- Email 2's "unveiled at NAB Show in April... keynoted at Post Production World Europe in May" line is **intentionally kept** — confirmed accurate by Elise O'Brien directly, don't second-guess it again

## What is NOT done yet — flag these explicitly in the new thread
1. **No real cross-client testing has happened.** Everything so far has been verified only in a Chromium-based browser preview (headless Chrome / the Claude Browser tool). Nothing has been pasted into actual HubSpot, and nothing has been checked in real Outlook (desktop, the worst offender), Gmail (web + app), Apple Mail, or a Litmus/Email on Acid style multi-client render test. The templates carry the standard bulletproof armor (VML buttons for Outlook, `color-scheme:dark` only, table-based layout, no CSS backgrounds behind text) but this has **not been empirically confirmed** in real clients. This is explicitly called out as still outstanding — do not tell Syvonne this is "done" until it's actually been tested in HubSpot's own preview/send-test tooling at minimum.
2. **Social media assets — not started.** Was scoped very early in this session (20-post campaign plan exists in the Campaign Plan doc) but all actual work this session went into the 7 emails. Zero social graphics have been built.
3. **Email 1's polish level not ported to Emails 2–5/InCart 1–2.** Their "pricing statement" sections are still the plain original lines, not the Event Details card treatment. Decide with Syvonne whether to mirror it.
4. **HubSpot subject-line A/B test for Email 1** — the campaign plan specifies a 10/10/80 split test (Subject A "New: Modern Post in Premiere, Sept 29–30" vs Subject B "Color grading, reimagined. Live with Adobe"). Subject B is documented in the campaign plan but not recorded anywhere in the actual HTML file — Syvonne needs to set this up manually in HubSpot's A/B subject field when she imports.
5. Group-quote CTA in Email 4 was originally spec'd by the campaign plan as a *third full button* in the CTA row; current build has it as an inline text link inside the group-quote card instead. Flagged to Syvonne once, never explicitly resolved either way.

## House rules reinforced hard this session (don't relitigate)
- Never touch postinpremiere.com itself — local files only, this whole project is Tyree's marketing campaign, not the live site
- Local-first, publish only on explicit go-ahead — but GitHub Pages publish has been explicitly authorized repeatedly this session for this specific repo
- No Canva integration turned out useful here (tried once, user rejected the candidates — abandoned)
- Baked-text-into-image treatments were tried and explicitly rejected as "not working" (soft/low-res, not inspectable) — **all Day 1/Day 2 and hero content must be real, live HTML text**, never flattened into a JPG with type baked in, except the header hero image itself which Syvonne is now supplying pre-made (see below)
- The current Email 1 hero image (`assets/hero-launch-620x320.jpg`) is a file Syvonne supplied directly (`MODERN POST IN PREMIERE.png` in Downloads) — not agent-generated. If it needs to change again, ask her for a new source image rather than trying to generate one from scratch.

## Immediate next message to send in the new thread
Paste this file's contents (or just link to it: `~/Downloads/MPIP26-Emails/HANDOFF.md`) and state clearly what she wants worked on next — most likely candidates: (a) real HubSpot import + cross-client testing, (b) porting Email 1's polish to the other 6, (c) starting social media assets.
