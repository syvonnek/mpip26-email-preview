import os, subprocess

SRC  = os.path.expanduser("~/Downloads/MPIP26-Emails/assets/drive-src/screens")
OUT  = os.path.expanduser("~/Downloads/MPIP26-Emails/assets")
HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# name -> (source, object-position, accent rgb for the corner tint)
PLATES = {
    "plate-day1":     (f"{SRC}/about/Style Groups Interior Scene.png",              "center",     "34,211,238"),
    "plate-day2":     (f"{SRC}/day2/02 AI as Your Assistant Editor.jpg",     "center", "139,92,246"),
    "plate-oneweek":  (f"{SRC}/day1/03 Lab 2 - Creative Grading.png",               "center",     "34,211,238"),
    "plate-lastcall": (f"{SRC}/day2/04 From Rough Audio to Finished Sound.jpg",     "center",     "227,79,203"),
    "plate-incart1":  (f"{SRC}/day2/01 Find the Story in the Footage.jpg",          "center",     "34,211,238"),
    "plate-incart2":  (f"{SRC}/day2/05 Visualize the Story with Firefly Boards.jpg","center",     "34,211,238"),
}

W, H = 1240, 580

TPL = """<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:#080b12}}
.h{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:#080b12}}
.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{pos};
     filter:brightness(.92) saturate(1.06) contrast(1.02)}}
.scrim{{position:absolute;inset:0;background:linear-gradient(97deg,
  rgba(8,11,18,.98) 0%, rgba(8,11,18,.955) 28%, rgba(8,11,18,.80) 46%,
  rgba(8,11,18,.44) 63%, rgba(8,11,18,.17) 81%, rgba(8,11,18,.05) 100%)}}
.vig{{position:absolute;inset:0;background:linear-gradient(180deg,
  rgba(8,11,18,.34) 0%, rgba(8,11,18,0) 22%, rgba(8,11,18,0) 72%, rgba(8,11,18,.42) 100%)}}
.tint{{position:absolute;inset:0;background:radial-gradient(780px 400px at 8% -20%, rgba({acc},.20), transparent 62%)}}
</style></head><body>
<div class="h"><img class="bg" src="file://{img}"><div class="scrim"></div><div class="vig"></div><div class="tint"></div></div>
</body></html>"""

for name, (img, pos, acc) in PLATES.items():
    if not os.path.exists(img):
        print("MISSING", img); continue
    html = os.path.join(HERE, name + ".html")
    open(html, "w").write(TPL.format(W=W, H=H, img=img, pos=pos, acc=acc))
    shot = os.path.join(HERE, name + ".png")
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                    f"--screenshot={shot}", f"--window-size={W},{H}",
                    f"file://{html}"], check=True, capture_output=True)
    final = os.path.join(OUT, name + "-620x290.jpg")
    subprocess.run(["magick", shot, "-resize", f"{W}x{H}", "-quality", "84",
                    "-strip", "-interlace", "Plane", final], check=True)
    print("built", os.path.basename(final), os.path.getsize(final)//1024, "KB")
