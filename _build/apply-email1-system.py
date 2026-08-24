#!/usr/bin/env python3
"""
Apply the Email 1 design system + Tyree's V2 content to the remaining 6 MPIP26 emails.

Strategy: surgical transform, not regeneration.
  - Swap in Email 1's exact <style> block (all mobile/tablet fixes)
  - Replace the top chrome with: Adobe masthead -> light Adobe header block
    (Tyree's eyebrow/headline/standfirst) -> spectrum bar -> hero -> intro -> CTA -> divider
  - PRESERVE each email's unique body content (session grids, time zones, instructors, fact lists)
  - Replace the tail with Email 1's Event Details card (buttons + group quote INSIDE it)
    followed by Megan's muted-border contact card
  - Normalize image srcs to public URLs, British -> US spelling, drop FMC Team signoff
"""
import re
import pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
CDN = "https://syvonnek.github.io/mpip26-email-preview/assets"
HS = "https://4023639.fs1.hubspotusercontent-na1.net/hub/4023639/hubfs"
SITE = "https://postinpremiere.com/?utm_campaign=MPIP-2026&utm_source=hs_email&utm_medium=email&utm_content="

SOURCE = BASE / "MPIP26-Email-01-Launch-Announcement.html"
src = SOURCE.read_text()

# ---- lift the canonical style block from Email 1 -------------------------------
STYLE = re.search(r"<style>.*?</style>", src, re.S).group(0)


def masthead(slug):
    return f'''      <!-- ADOBE MASTHEAD: white logo bar (FMC left / Adobe right) -->
      <tr><td class="px" bgcolor="#FFFFFF" style="background:#FFFFFF; padding:22px 36px;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
          <td valign="middle" align="left"><a href="https://www.fmctraining.com/?utm_campaign=MPIP-2026&utm_source=hs_email&utm_medium=email&utm_content={slug}_masthead_fmc" target="_blank"><img src="{HS}/fmc_logo_horizontal_dark.png" width="128" height="23" alt="FMC" style="display:block; border:0; vertical-align:middle;"></a></td>
          <td valign="middle" align="right"><a href="https://www.adobe.com/?utm_campaign=MPIP-2026&utm_source=hs_email&utm_medium=email&utm_content={slug}_masthead_adobe" target="_blank"><img src="{HS}/Adobe%20Wordmark%20Logo.png" width="91" height="30" alt="Adobe" style="display:block; border:0; vertical-align:middle;"></a></td>
        </tr></table>
      </td></tr>
'''


def header_block(eyebrow, h1, standfirst):
    return f'''
      <!-- ADOBE HEADER BLOCK: light ground, eyebrow, display headline, standfirst -->
      <tr><td class="advH" bgcolor="#F5F5F5" style="background:#F5F5F5; padding:44px 44px 46px;">
        <div class="advEyebrow" style="font-family:'Source Sans 3',Arial,sans-serif; font-size:11px; font-weight:700; letter-spacing:.20em; text-transform:uppercase; color:#5A5A5A; margin-bottom:20px;">{eyebrow}</div>
        <h1 class="advHero" style="margin:0 0 20px; font-family:'Source Sans 3',Arial,sans-serif; font-size:46px; font-weight:700; line-height:1.06; letter-spacing:-.032em; color:#101010; text-wrap:balance;">{h1}</h1>
        <div class="advSub" style="font-family:'Source Sans 3',Arial,sans-serif; font-size:17.5px; font-weight:350; line-height:1.52; color:#4A4A4A; max-width:480px; text-wrap:pretty;">{standfirst}</div>
        <table role="presentation" cellpadding="0" cellspacing="0" class="advPill" style="margin-top:24px;"><tr><td class="advPillPad" bgcolor="#FFFFFF" style="background:#FFFFFF; border:1.5px solid #22D3EE; border-radius:100px; padding:8px 20px 8px 14px;">
          <table role="presentation" cellpadding="0" cellspacing="0"><tr>
            <td valign="middle" class="advPillIcon" style="padding-right:11px;"><img class="advPillImg" src="{CDN}/pr-app-icon.png" width="29" height="29" alt="" style="display:block; border-radius:6px; border:0;"></td>
            <td valign="middle" class="advPillTxt" style="font-family:'Source Sans 3',Arial,sans-serif; font-size:16px; font-weight:700; letter-spacing:.12em; text-transform:uppercase; color:#101010; white-space:nowrap;">Live Online Training</td>
            <td valign="middle" class="advPillDot" style="padding:0 10px; color:#8B5CF6; font-size:14px; line-height:1;">&bull;</td>
            <td valign="middle" class="advPillDate" style="font-family:'Source Sans 3',Arial,sans-serif; font-size:16px; font-weight:700; letter-spacing:.04em; color:#0F8A9E; white-space:nowrap;">SEPT 29&ndash;30<span class="advPillYear">, 2026</span></td>
          </tr></table>
        </td></tr></table>
      </td></tr>

      <!-- ADOBE SPECTRUM BAR -->
      <tr><td bgcolor="#F5F5F5" style="background:#F5F5F5; font-size:0; line-height:0;">
        <img src="{HS}/Adobe%20Color%20Bar.png" width="620" height="52" alt="" style="display:block; width:100%; max-width:100%; height:auto; border:0;">
      </td></tr>
'''


def hero(img, w, h, alt):
    return f'''
      <!-- HERO VISUAL -->
      <tr><td bgcolor="#030611" align="center" style="background:#030611; font-size:0; line-height:0; border-bottom:1px solid rgba(255,255,255,0.09);">
        <img src="{CDN}/{img}" width="{w}" height="{h}" alt="{alt}" style="display:block; width:100%; max-width:100%; height:auto; border:0;">
      </td></tr>
'''


def intro_and_cta(slug, intro, cta_label, anchor):
    arrow = '<span style="vertical-align:middle; padding-left:7px;">&rarr;</span>'
    return f'''
      <!-- INTRO -->
      <tr><td class="px" align="center" bgcolor="#000000" style="background:#000000; padding:30px 36px 0;">
        <p style="margin:0 auto 0; max-width:492px; font-family:'Source Sans 3',Arial,sans-serif; font-weight:600; font-size:17px; line-height:1.5; color:#F5F7FA; text-align:center; text-wrap:balance;">{intro}</p>
      </td></tr>

      <!-- CTA -->
      <tr><td class="px" align="center" bgcolor="#000000" style="background:#000000; padding:24px 36px 0;">
<!--[if mso]>
        <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="{SITE}{slug}_register_top{anchor}" style="height:40px;v-text-anchor:middle;width:180px;" arcsize="50%" stroke="f" fillcolor="#4F7CFF">
          <center style="color:#FFFFFF;font-family:'Source Sans 3',Arial,sans-serif;font-size:13.5px;font-weight:700;">{cta_label} &rarr;</center>
        </v:roundrect>
        <![endif]-->
        <!--[if !mso]><!-->
        <table role="presentation" cellpadding="0" cellspacing="0" align="center"><tr><td bgcolor="#4F7CFF" style="background:linear-gradient(100deg,#22D3EE 0%,#4F7CFF 34%,#8B5CF6 67%,#E34FCB 100%); border-radius:100px;"><a class="vcta" href="{SITE}{slug}_register_top{anchor}" target="_blank" style="display:inline-block; mso-line-height-rule:exactly; line-height:16px; padding:10px 20px 13px 24px; white-space:nowrap; font-family:'Source Sans 3',Arial,sans-serif; font-size:13.5px; font-weight:700; color:#FFFFFF; letter-spacing:.01em;"><span style="position:relative; top:1px;">{cta_label}</span>{arrow}</a></td></tr></table>
        <!--<![endif]-->
      </td></tr>

      <!-- DIVIDER -->
      <tr><td class="px" bgcolor="#000000" style="background:#000000; padding:30px 36px 0;">
        <div style="height:1px; background:rgba(255,255,255,.12); font-size:0; line-height:0;">&nbsp;</div>
      </td></tr>
'''


def event_details_and_contact(slug, cta_label):
    arrow = '<span style="vertical-align:middle; padding-left:7px;">&rarr;</span>'
    return f'''      <!-- EVENT DETAILS (cyan border; CTAs + group quote live inside this card) -->
      <tr><td class="px" bgcolor="#000000" style="background:#000000; padding:46px 30px 0;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" bgcolor="#080b12" style="background:#080b12; border:1px solid rgba(34,211,238,.22); border-radius:16px;">
          <tr><td align="center" style="padding:28px 26px;">
            <div style="font-family:'Source Sans 3',Arial,sans-serif; font-weight:700; font-size:14px; letter-spacing:.18em; text-transform:uppercase; color:#8b90a5; margin-bottom:14px;">Event Details</div>
            <div style="font-family:'Source Sans 3',Arial,sans-serif; font-weight:700; font-size:22px; line-height:1.5; color:#F8FAFC;">September 29&ndash;30, 2026</div>
            <div style="font-family:'Source Sans 3',Arial,sans-serif; font-weight:250; font-size:19px; line-height:1.5; color:#F8FAFC;">9:00 AM to 5:30 PM ET</div>
            <div style="font-family:'Source Sans 3',Arial,sans-serif; font-weight:700; font-size:19px; line-height:1.5; color:#22D3EE;">Live on Zoom</div>
            <p style="margin:18px auto 0; max-width:380px; font-family:'Source Sans 3',Arial,sans-serif; font-weight:350; font-size:15.5px; line-height:1.45; color:#AAB2C0; text-align:center; text-wrap:pretty;">Every ticket includes real-time captions, professionally dubbed recordings on request, and 180 days of access to the sessions included with your registration.</p>
            <div style="height:1px; background:rgba(255,255,255,.10); margin:22px auto; max-width:200px;"></div>
            <div style="text-align:center;">
              <span class="priceCell" style="font-family:'Source Sans 3',Arial,sans-serif; font-weight:400; font-size:20px; line-height:1.4; color:#ffffff; white-space:nowrap;">Single day: $99</span>
              <span class="priceDiv" style="display:inline-block; width:1px; height:22px; background:rgba(255,255,255,.22); margin:0 16px; vertical-align:middle; border-radius:1px;"></span><br class="priceBr">
              <span class="priceCell" style="font-family:'Source Sans 3',Arial,sans-serif; font-weight:700; font-size:20px; line-height:1.4; color:#ffffff; white-space:nowrap;">Both days: $149</span>
            </div>

            <!-- CTA ROW: VIEW PROGRAM + REGISTER (identical sizing) -->
            <table role="presentation" cellpadding="0" cellspacing="0" class="ctaTbl" style="margin-top:26px;"><tr>
              <td class="ctaCell" valign="middle">
                <!--[if mso]>
                <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="{SITE}{slug}_view_program#agenda" style="height:40px;v-text-anchor:middle;width:150px;" arcsize="50%" strokecolor="#5b5570" fillcolor="#000000">
                  <center style="color:#E6EAF0;font-family:'Source Sans 3',Arial,sans-serif;font-size:13.5px;font-weight:700;">View Program</center>
                </v:roundrect>
                <![endif]-->
                <!--[if !mso]><!--><a class="btn" href="{SITE}{slug}_view_program#agenda" target="_blank" style="display:inline-block; white-space:nowrap; mso-line-height-rule:exactly; line-height:16px; padding:10px 20px 13px 24px; border:1px solid rgba(255,255,255,0.32); border-radius:100px; font-family:'Source Sans 3',Arial,sans-serif; font-size:13.5px; font-weight:700; color:#E6EAF0;"><span style="position:relative; top:1px;">View Program</span></a><!--<![endif]--></td>
              <td class="ctaGap" style="width:18px; font-size:1px; line-height:1px;">&nbsp;</td>
              <td class="ctaCell" valign="middle">
                <!--[if mso]>
                <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="{SITE}{slug}_register_bottom#pricing" style="height:40px;v-text-anchor:middle;width:180px;" arcsize="50%" stroke="f" fillcolor="#4F7CFF">
                  <center style="color:#FFFFFF;font-family:'Source Sans 3',Arial,sans-serif;font-size:13.5px;font-weight:700;">{cta_label} &rarr;</center>
                </v:roundrect>
                <![endif]-->
                <!--[if !mso]><!--><table role="presentation" cellpadding="0" cellspacing="0" width="100%"><tr><td bgcolor="#4F7CFF" style="background:linear-gradient(100deg,#22D3EE 0%,#4F7CFF 34%,#8B5CF6 67%,#E34FCB 100%); border-radius:100px;"><a class="btn" href="{SITE}{slug}_register_bottom#pricing" target="_blank" style="display:inline-block; white-space:nowrap; mso-line-height-rule:exactly; line-height:16px; padding:10px 20px 13px 24px; font-family:'Source Sans 3',Arial,sans-serif; font-size:13.5px; font-weight:700; color:#FFFFFF; letter-spacing:.01em;"><span style="position:relative; top:1px;">{cta_label}</span>{arrow}</a></td></tr></table><!--<![endif]--></td>
            </tr></table>

            <!-- GROUP QUOTE -->
            <div style="font-family:'Source Sans 3',Arial,sans-serif; font-weight:350; font-size:14px; line-height:1.6; color:#AAB2C0; text-align:center; margin-top:22px;">Registering five or more?<br class="groupQuoteBr"> <a href="{SITE}{slug}_group_quote&contact=elise#contact" target="_blank" style="color:#8FE3F5; font-weight:600; text-decoration:none;">Contact Elise O&rsquo;Brien</a> for a group quote.</div>
          </td></tr>
        </table>
      </td></tr>

      <!-- QUESTIONS CONTACT (muted border, text only, no photo) -->
      <tr><td class="px" align="center" bgcolor="#000000" style="background:#000000; padding:26px 36px 28px;">
        <table role="presentation" cellpadding="0" cellspacing="0" bgcolor="#080b12" style="background:#080b12; border:1px solid rgba(255,255,255,.10); border-radius:16px; width:100%;"><tr>
          <td align="center" style="padding:22px 30px;">
            <div style="font-family:'Source Sans 3',Arial,sans-serif; font-weight:350; font-size:16.5px; color:#AAB2C0; margin-bottom:5px;">Questions about the event?</div>
            <div style="font-family:'Source Sans 3',Arial,sans-serif; font-size:18px; font-weight:700; color:#F5F7FA;">Megan Belka</div>
            <div style="font-family:'Source Sans 3',Arial,sans-serif; font-weight:350; font-size:13.4px; color:#AAB2C0; margin-top:4px;">Event Manager, FMC Training</div>
            <div style="margin-top:6px;"><a href="{SITE}{slug}_contact_megan&contact=megan#contact" target="_blank" style="font-family:'Source Sans 3',Arial,sans-serif; font-weight:600; font-size:13.4px; color:#8FE3F5; text-decoration:none;">Contact Megan</a></div>
          </td>
        </tr></table>
      </td></tr>

'''


EMAILS = [
    dict(
        file="MPIP26-Email-02-ColorMode-DeepDive.html",
        slug="day1_deep_dive",
        title="Inside Day 1: Color Mode, session by session",
        preview="Foundations, correction, creative grading, grade management, and a live Adobe Q&amp;A.",
        eyebrow="Day 1 &middot; September 29",
        h1="One day. A completely new way to think about color.",
        standfirst="Adobe built Color Mode from the ground up for video editors. Day 1 is your opportunity to get inside it.",
        hero=("hero-colormode-620x264.jpg", 620, 264, "Adobe Color Mode in Premiere Pro"),
        intro="Foundations, primary correction, secondaries, creative grading, grade management, and a live Adobe Q&amp;A.",
        cta="Register Now", anchor="#pricing",
        body_start="<!-- SESSION LIST",
        tail_start="<!-- PRICING STATEMENT -->",
    ),
    dict(
        file="MPIP26-Email-03-AITrack-DeepDive.html",
        slug="day2_deep_dive",
        title="Day 2: where AI actually fits in your edit",
        preview="A practical day of AI-assisted workflows built around real editorial tasks.",
        eyebrow="Day 2 &middot; September 30",
        h1="AI is not the workflow. You are.",
        standfirst="Day 2 focuses on where AI can remove friction and give editors more room to make creative decisions.",
        hero=("hero-aitrack-620x264.jpg", 620, 264, "AI-assisted post-production in Premiere Pro"),
        intro="Search footage, compare takes, repair picture and sound, and plan with Firefly Boards.",
        cta="Register Now", anchor="#pricing",
        body_start="<!-- SESSION LIST -->",
        tail_start="<!-- CTA ROW -->",
    ),
    dict(
        file="MPIP26-Email-04-OneWeekOut.html",
        slug="one_week_out",
        title="Only one week until Modern Post in Premiere",
        preview="Live online training, global access, and 180 days to revisit what you learn.",
        eyebrow="One week to go",
        h1="Your calendar only needs two days. Your access lasts 180.",
        standfirst="Join live on September 29&ndash;30, or build the experience around your own schedule.",
        hero=("hero-launch-620x320.jpg", 620, 320, "Modern Post in Premiere. Live online training, Sept 29-30, 2026."),
        intro="One week out. Here is how to join from anywhere.",
        cta="Register Now", anchor="#pricing",
        body_start="<!-- TIME ZONES -->",
        tail_start="<!-- GROUP QUOTE -->",
    ),
    dict(
        file="MPIP26-Email-05-LastCall.html",
        slug="last_call",
        title="Last call: Modern Post starts tomorrow",
        preview="Color Mode begins at 9 AM ET tomorrow. Registration is still open.",
        eyebrow="Starts tomorrow",
        h1="Tomorrow, the edit changes color.",
        standfirst="Modern Post in Premiere begins at 9 AM ET with Color Mode Foundations, and builds into two full days of modern post-production workflows.",
        hero=("hero-launch-620x320.jpg", 620, 320, "Modern Post in Premiere. Live online training, Sept 29-30, 2026."),
        intro="Day 1: Color Mode. Day 2: AI-assisted post-production.",
        cta="Register Now", anchor="#pricing",
        body_start="<!-- DIVIDER -->",
        tail_start="<!-- PRICING -->",
    ),
    dict(
        file="MPIP26-InCart-01.html",
        slug="in_cart_push_1",
        title="Still deciding on Modern Post in Premiere?",
        preview="Here is what two days of modern post-production training actually gives you.",
        eyebrow="Your seat is still here",
        h1="You don&rsquo;t need another webinar.",
        standfirst="You need workflows you can actually use on the next project. One day on Color Mode, one day on AI-assisted post, both taught live.",
        hero=("hero-launch-620x320.jpg", 620, 320, "Modern Post in Premiere. Live online training, Sept 29-30, 2026."),
        intro="Two days. Two major shifts in post.",
        cta="Finish Registering", anchor="#pricing",
        body_start="<!-- THREE FACTS -->",
        tail_start="<!-- CTA: FINISH REGISTERING -->",
    ),
    dict(
        file="MPIP26-InCart-02.html",
        slug="in_cart_push_2",
        title="Can&rsquo;t attend live? Register anyway.",
        preview="The sessions happen September 29-30. Your access lasts 180 days.",
        eyebrow="Flexible access",
        h1="The live event is two days. The learning window is six months.",
        standfirst="You do not need to clear your calendar to get the full value of Modern Post in Premiere.",
        hero=("hero-launch-620x320.jpg", 620, 320, "Modern Post in Premiere. Live online training, Sept 29-30, 2026."),
        intro="Attend what you can. Replay everything else.",
        cta="Finish Registering", anchor="#pricing",
        body_start="<!-- THREE FACTS -->",
        tail_start="<!-- CTA: FINISH REGISTERING -->",
    ),
]

CONTAINER_RE = re.compile(r'(<table role="presentation" class="container".*?>\n)', re.S)
BRAND_RE = re.compile(r"[ \t]*<!-- BRAND -->")


def transform(cfg):
    path = BASE / cfg["file"]
    html = path.read_text()
    report = []

    # 1. canonical style block (brings every mobile/tablet fix)
    html, n = re.subn(r"<style>.*?</style>", lambda m: STYLE, html, count=1, flags=re.S)
    assert n == 1, f"{cfg['file']}: style block not found"

    # 2. title + preview text
    html = re.sub(r"<title>.*?</title>", f"<title>{cfg['title']}</title>", html, count=1, flags=re.S)
    html = re.sub(r'(value=")[^"]*(",\s*\n\s*no_wrapper=True)',
                  lambda m: m.group(1) + cfg["preview"] + m.group(2), html, count=1)

    # 3. top chrome: everything between container open and the body content marker
    cm = CONTAINER_RE.search(html)
    assert cm, f"{cfg['file']}: container not found"
    body_idx = html.find(cfg["body_start"], cm.end())
    assert body_idx != -1, f"{cfg['file']}: body marker {cfg['body_start']!r} not found"
    line_start = html.rfind("\n", 0, body_idx) + 1

    img, w, h, alt = cfg["hero"]
    top = (masthead(cfg["slug"])
           + header_block(cfg["eyebrow"], cfg["h1"], cfg["standfirst"])
           + hero(img, w, h, alt)
           + intro_and_cta(cfg["slug"], cfg["intro"], cfg["cta"], cfg["anchor"])
           + "\n")
    html = html[:cm.end()] + top + html[line_start:]
    report.append("top chrome replaced")

    # 4. tail: from the pricing/CTA marker through to BRAND.
    #    Search from the body content onward so the divider we just inserted in the
    #    top chrome cannot shadow an identically-named marker further down.
    search_from = html.find(cfg["body_start"])
    tail_idx = html.find(cfg["tail_start"], search_from + len(cfg["body_start"]))
    assert tail_idx != -1, f"{cfg['file']}: tail marker {cfg['tail_start']!r} not found"
    tail_line = html.rfind("\n", 0, tail_idx) + 1
    bm = BRAND_RE.search(html, tail_idx)
    assert bm, f"{cfg['file']}: BRAND marker not found after tail"
    html = html[:tail_line] + event_details_and_contact(cfg["slug"], cfg["cta"]) + html[bm.start():]
    report.append("tail (event details + contact) replaced")

    # 5. footer logo sizing + cyan site link (match Email 1 exactly)
    html = re.sub(r'<img src="[^"]*fmc-logo-footer\.png" width="\d+" height="\d+" alt="FMC" style="[^"]*"',
                  f'<img src="{CDN}/fmc-logo-footer.png" width="58" height="30" alt="FMC" style="display:block; border:0; vertical-align:middle;"', html)
    html = re.sub(r'<img src="[^"]*adobe-logo-footer\.png" width="\d+" height="\d+" alt="Adobe" style="[^"]*"',
                  f'<img src="{CDN}/adobe-logo-footer.png" width="75" height="41" alt="Adobe" style="display:block; border:0; vertical-align:middle; margin-top:-3px;"', html)
    html = re.sub(r'style="color:#B79CF7; text-decoration:none;">postinpremiere\.com</a>',
                  'style="color:#22D3EE; text-decoration:none;">postinpremiere.com</a>', html)

    # 6. all remaining local asset paths -> public CDN
    html = html.replace('src="assets/', f'src="{CDN}/')

    # 7. www subdomain does not resolve
    html = html.replace("https://www.postinpremiere.com", "https://postinpremiere.com")

    # 8. Tyree writes British; FMC is US
    for a, b in [("colour", "color"), ("Colour", "Color")]:
        html = html.replace(a, b)

    # 9. strip any leftover FMC Team signoff block
    html = re.sub(r"[ \t]*<!-- SIGNOFF -->.*?</td></tr>\n", "", html, flags=re.S)

    # 10. drop a divider left orphaned directly above the Event Details card
    html = re.sub(
        r"[ \t]*<!-- DIVIDER -->\n(?:(?![ \t]*<!--).*\n)*?(?=[ \t]*<!-- EVENT DETAILS)",
        "", html)

    path.write_text(html)
    return report


if __name__ == "__main__":
    for cfg in EMAILS:
        try:
            notes = transform(cfg)
            print(f"OK   {cfg['file']}: {', '.join(notes)}")
        except AssertionError as e:
            print(f"FAIL {e}")
