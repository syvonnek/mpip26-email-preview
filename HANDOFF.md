# MPIP26 Email Campaign — Handoff (2026-08-22, v2)

**End goal:** 7 individual HTML files, delivered to Tyree, each HubSpot-ready and rendering correctly across real email clients (Outlook, Gmail, Apple Mail) and devices. Not just "looks good in a browser preview."

## Where everything lives
- **Local working folder:** `~/Downloads/MPIP26-Emails/` (git repo, remote = `syvonnek/mpip26-email-preview` on GitHub)
- **Published preview (GitHub Pages, live):** https://syvonnek.github.io/mpip26-email-preview/
  - `index.html` — list view, one link per email
  - `all-emails.html` — all 7 stacked on one page
- **Deploy workflow:** edit → `git add -A && git commit -m "..." && git push origin main` → GitHub Pages rebuilds in ~30-60s at the same URL. Always verify the push actually landed (curl the file, grep for your change) before telling her it's live — Pages has a short propagation delay.
- **Campaign copy source:** `~/Downloads/MPIP26-Campaign-Plan.html` (Tyree's plan — first draft, not gospel; verify facts against the live site)
- **Live event site (source of truth for facts):** https://postinpremiere.com — always re-verify facts here fresh, don't trust anything cached from earlier in a conversation without rechecking if it's consequential (pricing, registration URLs, speaker assignments).
- **Curated brand asset library (Google Drive, syvonnek@fmctraining.com):** "Modern Post in Premiere - Social Assets" — logos, instructor portraits, hero photography, Color Mode screenshots. Local mirror at `assets/drive-src/` (gitignored, not pushed — too large).

## The 7 files
1. `MPIP26-Email-01-Launch-Announcement.html` — most polished, the flagship (custom hero, redesigned Day 1/Day 2 cards, Event Details card)
2. `MPIP26-Email-02-ColorMode-DeepDive.html` — Day 1 session-by-session grid
3. `MPIP26-Email-03-AITrack-DeepDive.html` — Day 2 session-by-session grid
4. `MPIP26-Email-04-OneWeekOut.html` — countdown, time zones, group quote
5. `MPIP26-Email-05-LastCall.html` — final reminder
6. `MPIP26-InCart-01.html` / `MPIP26-InCart-02.html` — abandoner recovery

## Design system
- Colors: bg `#030611`, spectrum gradient cyan `#22D3EE` → blue `#4F7CFF` → violet `#8B5CF6` → magenta `#E34FCB`
- Font: Source Sans 3 (Google Font) + Arial/Helvetica fallback
- Logo ratio (verified via `getBoundingClientRect()` on the live site — don't re-derive from CSS, measure it): FMC height 34 : Adobe height 48 — **Adobe renders noticeably bigger/taller than FMC**, not equal. Current email asset sizing: FMC 58×30, Adobe 78×42. Assets: `fmc-logo-nav.png`/`fmc-logo-footer.png`, `adobe-logo-nav.png`/`adobe-logo-footer.png` (same files reused for both nav and footer contexts now).
- UTM scheme: `utm_campaign=MPIP-2026&utm_source=hs_email&utm_medium=email&utm_content=<page>_<location>`

## 🔴 CRITICAL — link routing decision made this session, not yet fully applied
Syvonne was asked directly and confirmed via the question tool:
- **Register Now / Finish Registering buttons** → must point to the **live Zoom Events URL**, verified fresh this session:
  `https://events.zoom.us/ev/AnqUWF2mloHzYgsaptQx0wsb4wWZ83seXLO9Zsdmx0UuPdyxNy3i~AjXUpViZrU7gePZJuMcrI7aF8idMW1htM7Rnn6eJ-UMfTNFM9zMaFJPKWA`
  Append UTM params as a query string on this URL (e.g. `?utm_campaign=MPIP-2026&utm_source=hs_email&utm_medium=email&utm_content=<location>`). **This is a change from earlier in the session** where these buttons pointed to `www.postinpremiere.com/?...#pricing` — that's now wrong, replace it everywhere.
  ⚠️ Before using this URL, re-verify it's still current by checking the live site's Register button href fresh — Zoom Events links can be regenerated.
- **All other links** (View Program → `#agenda`, footer brand logo link, "event site" links, contact links) → must consistently use **`https://www.postinpremiere.com`** (with `www.` — check for and fix any bare `postinpremiere.com` without www).
- **Status: NOT YET APPLIED to any file.** This was confirmed right as the session ran out of context. Do this first in the new thread — it's the single most consequential fix outstanding (wrong link = broken registration flow).

## 🔴 Megan Belka's photo — resolved, now approved for use
Earlier in this session I found (and saved to memory as `adobe-color-flagged-assets`) that Megan's photo on the live site was flagged as carrying a branded arrow/chevron treatment from a different site's template, and told Syvonne not to use it. **Syvonne has now explicitly overridden this and confirmed: use it, styled like the live site does.**
- Source downloaded and cropped: `assets/megan-belka-64.jpg` (128×128, 2x for retina, centered face crop from the original 676×740 source — already verified visually, crop is clean)
- **Live site's actual styling** (measured via computed styles, use this exactly):
  - Photo: 88×88 (display), `border-radius:50%`, `object-fit:cover`, no border on the image itself
  - Wrapper (`.contact-photo-ring`): 90×90, `border-radius:50%`, `padding:1px`, `background: rgba(255,255,255,.18)` — creates a thin 1px light ring around the photo
- **Status: NOT YET APPLIED.** Need to: add this photo to the "Questions about the event?" contact card in all 7 emails, positioned **left** of the text (currently the cards are text-only, centered, no photo). Also:
  - **Left-justify the text** in that card (currently centered) — applies to all 7 emails
  - **Give the card border a nicer/varied outline color** — Syvonne said it "looks boring" with the flat cyan `rgba(34,211,238,.22)` used identically in every email. Intent: match each email's own accent color instead of uniform cyan. I was in the middle of pulling each email's subhead accent color when the session ended (my grep pattern didn't match — read each file's subhead `<div>` directly instead, don't rely on regex against the CSS block). Reasonable mapping to use: Email1/2/4/6/7 = cyan `#22D3EE`, Email3 = violet `#8B5CF6`, Email5 = magenta `#E34FCB`/`#F49BE0` (verify against each file's actual subhead color before applying, don't assume).

## Email 2 — outstanding fixes (none applied yet)
1. Increase the size of the session thumbnail images in the grid/list (currently 64×64px, `session-s1-96.jpg` etc.) — make them bigger.
2. Improve text wrapping on the session description lines (the "benefit" copy added under each Speaker line) — add `text-wrap:pretty` or similar, consider widening the text column.
3. Instructor title in the "Day 1 Instructors" card should read as **two lines**: "Co-Program Manager," / "Adobe Expert" (currently one line: "Co-Program Manager · Adobe Expert" with a middot separator — replace with a line break after the comma).
4. Move the **"View Full Program" button** so it's centered directly underneath the session grid/list (not down in the later combined CTA row with Register Now).
5. Restructure the pricing area into an **Event-Details-style bordered box** (matching Email 1's card treatment) containing **only the Register Now button, centered** — remove View Full Program from that box since it moved per #4.

## Email 3 — outstanding fixes (none applied yet)
1. **Subhead copy change:** replace "AI that supports your judgment, not replaces it." with two lines: **"AI is not the workflow.<br>You are."**
2. Same button restructuring as Email 2 (#4 and #5 above): View Full Program centered under the session grid, Event-Details-style box with only Register Now centered inside.
3. Possible copy tweak to the "Take one day or both" section incorporating the phrase "attend one day or both" — **this one is ambiguous**, she said it fast and it wasn't fully clarified. Don't strip the existing accurate pricing/day-structure copy to fit a short dictated phrase — ask her directly what she wants there before changing it, or make a minimal, sensible edit and flag it for her review rather than guessing big.

## Email 4 — outstanding, needs collaborative copy work
She dictated draft copy that she flagged herself as rough: *"Your calendar only needs two days. Your access lasts 180. Join the sessions live, or build the two days around your own schedule."* She said **"needs work"** — meaning don't just drop this in verbatim, help refine it. Likely intended to replace the current intro paragraph or the "Day 1 moves from... Day 2 covers..." program-value sentence — ask her which, or propose a polished version and confirm before applying.

## Email 5 — outstanding bug
**"Double horizontal line under first reg button, remove one."** There's a rendering bug — two divider lines are stacking under the first Register button where there should be one. Find the duplicate `<div style="height:1px; background:rgba(255,255,255,.12)...">` divider row near that button and delete the extra one. Haven't located the exact line yet — check the DIVIDER rows in that file.

## What's fully done and verified (from before, still holds)
- All 7 emails built, real HTML text throughout (no baked-text-into-image treatments — that was tried and explicitly rejected as looking soft/uninspectable)
- Content accuracy pass complete: correct instructor titles (Co-Program Manager · Adobe Expert, not "Adobe Master Trainer"), no "lead both days" overclaim, ticket-tier-qualified recording access language, no unsupported Q&A claims — verified via QA grep, zero remaining instances of the banned phrases
- "Produced by FMC in partnership with Adobe" line removed everywhere
- Register button arrow now `vertical-align:middle` (was misaligned before)
- Questions Contact card fonts sized: label 16.5px, name 18px, meta 13.4px
- Eyebrow labels (Learn from Adobe Experts, Event Details, Why this day matters, etc.) standardized to 14px / 14px margin-bottom site-wide
- Email 1 hero image is a file Syvonne supplied directly (not agent-generated) — if it ever needs to change again, ask her for a new source image

## What has NOT been started at all
- **Real cross-client testing.** Nothing has been pasted into actual HubSpot. Nothing has been checked in real Outlook (desktop especially — the worst offender for CSS support), Gmail (web + app), or Apple Mail. Everything so far is verified only in a Chromium browser preview. The templates carry standard bulletproof armor (VML buttons for Outlook, `color-scheme:dark` only, table-based layout, no CSS backgrounds behind text) but this is unverified in practice. **Do not tell her this is "HubSpot-ready" until it's actually been tested in HubSpot's own preview/send-test tooling at minimum.**
- Social media assets (separate Canva-based track, prompt already handed to her for a fresh thread on that — not this one)
- Porting Email 1's full polish level to Emails 4, 5, and both In-Cart emails (2 and 3 are now getting their own pass per the items above)
- Email 1's Subject B A/B test variant ("Color grading, reimagined. Live with Adobe") is documented in the campaign plan but not wired into anything — she'll need to set it up manually in HubSpot's subject A/B field
- Email 4's group-quote CTA — plan originally called for a third full button; current build has it as an inline text link. Never explicitly resolved.

## House rules (don't relitigate these)
- Never touch postinpremiere.com itself — read-only, local files only
- Local-first, publish only on go-ahead — but she has repeatedly and explicitly authorized pushing to the `mpip26-email-preview` GitHub Pages repo specifically, that standing authorization holds
- No baked-text-in-image treatments for body content — real HTML/live text only (exception: the Email 1 hero banner, which is a supplied image, not built by the agent)
- When a fact is consequential (registration URLs, pricing, who's flagged/approved), re-verify against the live site fresh rather than trusting something from earlier in a long conversation

## Immediate next steps for the new thread, in priority order
1. Fix the registration link routing (Zoom URL for Register buttons, www.postinpremiere.com for everything else) — all 7 files
2. Add Megan's photo + left-justify text + accent-colored border in the Questions Contact card — all 7 files
3. Email 2 fixes (bigger thumbnails, text wrap, instructor title, button restructuring)
4. Email 3 fixes (subhead copy, same button restructuring, clarify the "attend one day or both" ask with her)
5. Email 5's double-divider bug (quick, isolated fix)
6. Email 4 copy collaboration (needs her input, don't just paste her draft in)
7. Once all 7 are visually confirmed, move to actual HubSpot import + cross-client testing — this is the real finish line, not a "nice to have"
