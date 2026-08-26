import os, subprocess
SRC  = os.path.expanduser("~/Downloads/MPIP26-Emails/assets/drive-src/screens")
OUT  = os.path.expanduser("~/Downloads/MPIP26-Emails/assets")
HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
W, H = 1240, 580

# name -> (source, crop box or None, accent)
UI = {
 "plate-day2":     (f"{SRC}/day2/02 AI as Your Assistant Editor.jpg",      (0,0,470,552),   "139,92,246"),
 "plate-oneweek":  (f"{SRC}/day1/02 Lab 1 - Primary Correction.png",       (0,455,968,726), "34,211,238"),
 "plate-lastcall": (f"{SRC}/day2/04 From Rough Audio to Finished Sound.jpg",(0,0,560,552),  "227,79,203"),
 "plate-incart2":  (f"{SRC}/day1/01 Welcome - Color Mode Foundations.png", (0,470,968,726), "34,211,238"),
}

TPL = """<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:#080b12}}
.h{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:#080b12}}
.tintA{{position:absolute;inset:0;background:radial-gradient(820px 460px at 6% -12%, rgba({acc},.20), transparent 62%)}}
.tintB{{position:absolute;inset:0;background:radial-gradient(680px 420px at 100% 118%, rgba({acc},.13), transparent 60%)}}
.uiwrap{{position:absolute;top:50%;right:-2%;transform:translateY(-50%);
  width:{uw}%;display:flex;align-items:center;justify-content:flex-end;
  -webkit-mask-image:linear-gradient(94deg, transparent 0%, rgba(0,0,0,.35) 12%, #000 34%, #000 100%);
          mask-image:linear-gradient(94deg, transparent 0%, rgba(0,0,0,.35) 12%, #000 34%, #000 100%)}}
.uiwrap img{{width:100%;height:auto;display:block;
  filter:brightness(.94) saturate(1.04) contrast(1.02);
  border-radius:10px}}
.scrim{{position:absolute;inset:0;background:linear-gradient(97deg,
  rgba(8,11,18,.99) 0%, rgba(8,11,18,.97) 30%, rgba(8,11,18,.72) 48%,
  rgba(8,11,18,.26) 66%, rgba(8,11,18,.05) 84%, rgba(8,11,18,0) 100%)}}
.vig{{position:absolute;inset:0;background:linear-gradient(180deg,
  rgba(8,11,18,.30) 0%, rgba(8,11,18,0) 24%, rgba(8,11,18,0) 74%, rgba(8,11,18,.40) 100%)}}
</style></head><body>
<div class="h">
  <div class="tintA"></div><div class="tintB"></div>
  <div class="uiwrap"><img src="file://{img}"></div>
  <div class="scrim"></div><div class="vig"></div>
</div></body></html>"""

for name,(src,box,acc) in UI.items():
    tmp = os.path.join(HERE, name + "-crop.png")
    if box:
        subprocess.run(["magick", src, "-crop",
                        f"{box[2]-box[0]}x{box[3]-box[1]}+{box[0]}+{box[1]}",
                        "+repage", tmp], check=True)
    else:
        subprocess.run(["magick", src, tmp], check=True)
    # wide short crops need to sit larger; tall crops smaller
    import struct
    w,h = [int(x) for x in subprocess.run(["magick","identify","-format","%w %h",tmp],
            capture_output=True,text=True,check=True).stdout.split()]
    uw = 66 if (w/h) < 1.6 else 78
    html = os.path.join(HERE, name + "2.html")
    open(html,"w").write(TPL.format(W=W,H=H,img=tmp,acc=acc,uw=uw))
    shot = os.path.join(HERE, name + "2.png")
    subprocess.run([CHROME,"--headless","--disable-gpu","--hide-scrollbars",
                    f"--screenshot={shot}",f"--window-size={W},{H}",f"file://{html}"],
                   check=True,capture_output=True)
    final = os.path.join(OUT, name + "-620x290.jpg")
    subprocess.run(["magick",shot,"-resize",f"{W}x{H}","-quality","84","-strip",
                    "-interlace","Plane",final],check=True)
    print("rebuilt",os.path.basename(final), os.path.getsize(final)//1024,"KB")
