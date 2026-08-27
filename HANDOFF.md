# MPIP26 Email Campaign — Handoff (2026-08-27, v3)

**Preview link (send to anyone, always current):**
https://syvonnek.github.io/mpip26-email-preview/all-emails.html

Repo: `~/Downloads/MPIP26-Emails/` (git, remote `syvonnek/mpip26-email-preview`, GitHub Pages).
Deploy: `git add -A && git commit -m "..." && git push origin main` -> live in ~30-60s at the same URL. Always verify with curl before telling anyone it's live -- Pages has propagation delay.

## Status: NOT in HubSpot yet. NOT final. Actively gathering comments (team + Jordan) before handoff to Tyree.

---

## The 6 files (Email 1 already sent -- DO NOT TOUCH)
1. `MPIP26-Email-01-Launch-Announcement.html` -- **SENT. Off limits.**
2. `MPIP26-Email-02-ColorMode-DeepDive.html` -- Day 1 deep dive
3. `MPIP26-Email-03-AITrack-DeepDive.html` -- Day 2 deep dive
4. `MPIP26-Email-04-OneWeekOut.html` -- one week out, time zones
5. `MPIP26-Email-05-LastCall.html` -- final reminder
6. `MPIP26-InCart-01.html` / `MPIP26-InCart-02.html` -- abandoned-registration recovery (behavior-triggered, NOT fixed-date)

Preview pages `index.html` and `all-emails.html` already split into "Main Campaign" vs "In-Cart Follow-Up - behavior-triggered."

---

## CRITICAL -- HubSpot passport (already in every file, verify on any new file)
Must be the literal first thing before `<!doctype html>`:
```
<!--
  templateType: "email"
  isAvailableForNewContent: true
-->
<!--
isEnabledForEmailV3Rendering: true
-->
```
Right after `<body>` opens, the editable preview-text field (already present in all 6):
```
<div id="preview_text" style="display:none!important; max-height:0; overflow:hidden; mso-hide:all; opacity:0; color:transparent;">
  {% text "preview_text"
    label="Preview Text <span class=help-text>This will be used as the preview text that displays in some email clients</span>",
    value="<default preview line>",
    no_wrapper=True
  %}
</div>
```
Import into HubSpot: "Create email" -> paste whole file as-is. **Never run through HubSpot AI.**

## Pre-flight status: ALL 6 FILES PASS
Verified: templateType + V3 flag present, preview_text token present, CAN-SPAM tokens present (`{{ unsubscribe_link }}`, `{{ subscription_preferences_url }}`, `{{ site_settings.company_* }}`), zero non-ASCII characters, no `<script>`/`<form>` tags, no `position:absolute`, MSO conditionals balanced, all images on live CDNs (no local/relative paths), file sizes 30-47KB (well under Gmail's 102KB clip threshold).

## PRE-SEND TASK: image hosting
All plate/session/icon images currently live on `syvonnek.github.io` (personal GitHub Pages) -- fine for team review, but before a real send these should move to HubSpot's Files (where the FMC/Adobe logos already live: `4023639.fs1.hubspotusercontent-na1.net`). Reasoning: emails outlive the event site; if postinpremiere.com ever changes/archives, email images break silently for years. ~30 files to upload, then a URL find-replace in one pass. **Cannot do the HubSpot upload from this session -- connector not authorized.** Social icons already re-hosted off the IPH domain onto this repo (no more cross-brand dependency).

## PRE-SEND TASK: Day 2 speakers -- REMIND TYREE
Email 3 (AI Track Deep Dive)'s session grid currently shows **NO speaker names** -- deliberately removed because 4 of 6 sessions were "To be announced" and it read as unfinished/broken. **Confirmed on the live site:** Luisa Winters -> "Find the Story in the Footage" (Session 1), Eran Stern -> "When the Edit Is Missing Something" (Session 3). The other 4 sessions are still TBA as of this writing.

**Action: before Email 3 is scheduled, re-add speaker lines to the Day 2 grid once the full roster is confirmed.** Don't send it speaker-less if names are available by send time. Tell Tyree directly, don't rely only on this file.

## Contact links (fixed 2026-08-27)
Elise/Megan links now use hash anchors, verified live on the deployed site (curled and confirmed both IDs exist):
- `https://www.postinpremiere.com/?utm_campaign=MPIP-2026&utm_source=hs_email&utm_medium=email&utm_content=<tag>_group_quote#contact-elise`
- `https://www.postinpremiere.com/?utm_campaign=MPIP-2026&utm_source=hs_email&utm_medium=email&utm_content=<tag>_contact_megan#contact-megan`

A `#hash` never reaches the server so no redirect can strip it (previous `?contact=` param was being dropped on the www redirect -- now legacy/fallback only, still works but doesn't differentiate). Site-side fix applied directly to the live repo; the working copy in `adobe-color-roadshow/samples` does NOT have it yet -- sync before next production edit there.

---

## Design system (locked as of this session, unless flagged "IN PROGRESS")

**Colors:** page bg `#191c23` (must stay lighter than the card so the card reads as ONE surface, not three stacked backgrounds -- this was a real bug, fixed 2026-08-27; currently reviewing further options, see Open Items). Card `#000000`. Spectrum gradient: cyan `#22D3EE` -> blue `#4F7CFF` -> violet `#8B5CF6` -> magenta `#E34FCB`. Day 1 accent blue `#6FA8FF`, Day 2 accent pink `#F06ECF`. On-air/live blue `#5B8DEF`. Price bullet violet `#B98BFF`.

**Fonts:** Source Sans 3 (Google Font) + Arial/Helvetica fallback.

**Card frame:** single rounded card, `border:1px solid rgba(255,255,255,0.28)`, `border-radius:18px`, subtle `box-shadow:0 24px 70px rgba(0,0,0,.55)`. One card only -- page bg must contrast against it (see color note).

### The branded plate (top of every email except Email 1)
Background: `plate-bg-620x360.jpg` (desert aerial, brightened/desaturated for legibility -- do not re-darken, was fixed per explicit "I need to see more of it" feedback).
Structure top to bottom:
- Kicker: `FMC x Adobe Present` -- 14.5px
- `Modern Post in Premiere` -- **52px / font-weight:700 / line-height:.94** (reduced from 900 to 700 per latest instruction; mobile scales to 33px)
- Gradient subtitle `Color Mode + AI-Assisted Post-Production` -- 19px, `background-clip:text` gradient, **falls back to solid periwinkle in Outlook** (acceptable, still legible)
- Thin gradient rule
- Globe icon + **WORLDWIDE TRAINING EVENT** -- gradient text, replaces old cyan pill
- Date `September 29-30, 2026` -- 21px white
- Metadata row: clock icon + `9 AM-5:30 PM ET`  (18px gap, NO vertical divider -- removed per instruction)  on-air icon + `Live Online` -- clock icon `icon-clock-44.png` (cyan), on-air icon `icon-onair-44.png` (blue, just re-fixed to match clock's visual size -- was rendering smaller due to asset trim margins)
- Price line: `$99 one day` **violet bullet (15px, #B98BFF)** `$149 both days` -- white, 13.6px/800, margin-top:10px for breathing room
- Right side: Premiere interface image, Pr badge baked into the JPG's top-left corner (not a separate overlay)

**Per-email plate interface images** (own file each, Pr badge baked in, full frame -- NEVER crop, several past crops were reverted after complaints):
- E2 (Color Mode): `plate-ui-u-e2.jpg` -- Adobe's 1544x974 Color Mode hero, 135px display height
- E3 (AI Track): `plate-ui-u-e3.jpg` -- AI media search panel, full frame, 109px display height -- **swapped 3+ times per complaints, current version confirmed full-frame/uncropped, double-check it still reads clearly before final send**
- E4 (One Week Out): `plate-ui-u-e5.jpg` (Film Color grading) -- filename says e5, content is what was originally e5
- E5 (Last Call): `plate-ui-u-e4.jpg` (Essential Sound) -- filenames intentionally swapped between E4/E5, don't "fix" this
- IC1: `plate-ui-u-ic1.jpg` (adjustment panels)
- IC2: `plate-ui-u-ic2.jpg` (Style Groups scene)

### Worldwide access banner (below the plate, above content)
One-line sentence, spectrum-tinted bar, globe icon: **"Join live from anywhere with real-time captions. Replays dubbed in seven languages."** Must not wrap to 2 lines -- max ~86 chars at this width.

### "Created for editors worldwide" access strip (mid-email)
Left-aligned eyebrow (13px) + 3 cells (icons 32px): Real-time captions (CC speech-bubble icon matching the live site, `icon-cc-44.png`, CC text centered in bubble body) / Dubbed recordings / 180-day replay. Below: gradient-filled pill bar, globe icon, "LANGUAGES" label + all 7 named (English, Spanish, French, German, Japanese, Portuguese, Italian) -- spelling out all 7 is the strongest answer to Adobe's international-emphasis ask (Michelle Gallina's original question).

### Event Details card
Gradient border at 50% opacity (softened to match the Megan contact card below -- full opacity read too loud). Background: `evd-bg-580x450.jpg`, desert texture, brightened per feedback (veil 42%->26%, brightness->72%, darkened center band only where text sits). Contents: eyebrow "EVENT DETAILS" -> date -> time (16px, dimmed) -> camcorder icon + **"Live on Zoom"** (reverted from "Live Online" -- ED names the platform, plate names the delivery style, deliberate division) -> hairline gradient divider -> prices (white, weight-differentiated not color -- gradient price text was tried and reverted as "too flamboyant") -> ticket-choice line "Choose Day 1, Day 2, or both. Recordings included for the day or days you select." -> Register button -> View Full Program (white, underlined, NOT blue -- was competing with Elise's link color) -> group quote line, **13px** font size.

**Container width:** all boxed sections normalized to **30px side padding** (Megan card and E2 instructors card were at 36px, now matched).

### Day cards (Color Mode / AI-Assisted, side by side)
Used in IC1, IC2, One Week Out only (NOT deep dives -- would dilute single-day focus; NOT Last Call -- kept short/urgent). Icons baked as PNGs matching the live site: rainbow ring (`icon-day1-ring.png`), sparkle burst (`icon-day2-spark.png`).
**IN PROGRESS as of context cutoff:** background glow needs to be bigger/more premium (current radial glow too small/subtle per latest feedback), and deciding whether cards need a banner/header treatment instead of floating day labels -- 3 options (A/B/C) built at `day-cards-options.html`, not yet picked. Also just built `page-bg-options.html` (5 page-background color choices) because current `#191c23` was disliked in the latest message -- reason not yet given, options awaiting review.

### Session grids (E2, E3 only)
4:3 thumbnails (128x96 display, 512x384 source, `table-layout:fixed` to prevent mobile overflow -- this was a real bug, session titles ran off the right edge on phones, fixed). Day labels above grid: colored square + "DAY 1 - COLOR MODE" (cyan) / "DAY 2 - AI-ASSISTED POST-PRODUCTION" (violet) -- added because readers couldn't tell which day a grid belonged to. Alexis Van Hurkman's photo re-cropped wider so he doesn't look distorted ("dinosaur" complaint) -- 512x384, face doesn't fill frame edge-to-edge like other thumbs, intentional per latest feedback.

### Buttons
Register Now / Continue Registration: gradient pill, arrow icon untouched, label text `top:2px` (was top:1px). "View Full Program ->" replaces "View Program" everywhere, moved from directly-under-grid to after "Why this day matters" (E2) / "Take one day or both" renamed **"Day 2, on its own or paired with Day 1"** (E3).

### In-Cart specific
Headlines rewritten to not open on a negative ("You don't need another webinar" removed). IC1: "Still deciding? Here's what you get." IC2: "Register once. / Learn for 180 days." IC2 section labels renamed: "Learn on your schedule" / "Why join live" / "Choose your access". Both have a facts-card section (vertical accent wash + centered text, 16px body -- was 14px) -- this is the section the glow/banner redesign question above applies to as well.

---

## Open items, in priority order
1. **Day cards glow/banner redesign** -- 3 options built, awaiting pick (`day-cards-options.html`)
2. **Page background color** -- 5 options just built (`page-bg-options.html`), awaiting pick -- current `#191c23` disliked in latest message
3. **On-air icon size** -- just re-fixed (was rendering smaller than the clock icon at the same nominal size due to asset trim margins), verify it looks right after next deploy
4. **Jordan's copy pass + team comments** -- sent via Slack, awaiting response, requested with a same-day deadline
5. **Speaker roster for Day 2** -- see critical note above
6. **Image CDN migration to HubSpot** -- pre-send task, needs manual upload
7. **The real finish line: HubSpot import + cross-client test send** (Outlook desktop especially -- CSS background stripping is the biggest risk given how much of this design relies on background images with solid-color fallbacks). Nothing has been tested outside a Chromium preview yet.

## House rules, don't relitigate
- Never touch postinpremiere.com directly (site work happens in a separate thread/repo: `adobe-color-roadshow/samples`, dev server on `localhost:8830` or `8831`)
- Never edit Email 1 -- already sent
- Real HTML/live text only, no baked-text-into-images for body content (hero banners/interface screenshots are the exception, always with Pr badge baked in when relevant)
- Push to `mpip26-email-preview` repo is standing-authorized, no need to ask each time
- Always verify a deploy actually landed (curl + grep, or byte-size match on images) before saying "it's live" -- Pages has propagation lag and browsers cache aggressively
- When editing multiple files with the same find/replace, always verify tag balance (`<tr>`/`</tr>`, `<td>`/`</td>`, `<table>`/`</table>` counts must match) before pushing -- several past edits broke card structure silently until caught by screenshot review
