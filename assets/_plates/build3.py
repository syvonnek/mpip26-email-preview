import os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
W, H = 1240, 580

HEAD = """<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:%dpx;height:%dpx;overflow:hidden;background:#080b12}
.h{position:relative;width:%dpx;height:%dpx;overflow:hidden;background:#06080f}
</style></head><body>""" % (W,H,W,H)

# A — pure gradient field, spectrum sweep bottom-right
A = HEAD + """
<div class="h">
 <div style="position:absolute;inset:0;background:
   radial-gradient(900px 520px at 4% -18%, rgba(227,79,203,.30), transparent 62%),
   radial-gradient(760px 460px at 96% 116%, rgba(139,92,246,.28), transparent 60%),
   radial-gradient(600px 380px at 78% 8%, rgba(79,124,255,.16), transparent 62%)"></div>
 <div style="position:absolute;right:-90px;top:50%;transform:translateY(-50%);
   width:560px;height:560px;border-radius:50%;
   background:conic-gradient(from 200deg,#22D3EE,#4F7CFF,#8B5CF6,#E34FCB,#22D3EE);
   filter:blur(58px);opacity:.30"></div>
 <div style="position:absolute;inset:0;background:linear-gradient(97deg,
   rgba(6,8,15,.97) 0%, rgba(6,8,15,.90) 34%, rgba(6,8,15,.55) 56%, rgba(6,8,15,.10) 82%, rgba(6,8,15,0) 100%)"></div>
</div></body></html>"""

# B — gradient + concentric colour-wheel rings (nods to Color Mode dials)
B = HEAD + """
<div class="h">
 <div style="position:absolute;inset:0;background:
   radial-gradient(880px 500px at 6% -16%, rgba(227,79,203,.26), transparent 62%),
   radial-gradient(700px 440px at 98% 112%, rgba(79,124,255,.22), transparent 60%)"></div>
 <div style="position:absolute;right:56px;top:50%;transform:translateY(-50%);width:330px;height:330px;">
  <div style="position:absolute;inset:0;border-radius:50%;
    background:conic-gradient(from 0deg,#E34FCB,#8B5CF6,#4F7CFF,#22D3EE,#4F7CFF,#8B5CF6,#E34FCB);
    opacity:.62;-webkit-mask:radial-gradient(circle, transparent 56%, #000 58%, #000 70%, transparent 72%);
    mask:radial-gradient(circle, transparent 56%, #000 58%, #000 70%, transparent 72%)"></div>
  <div style="position:absolute;inset:38px;border-radius:50%;
    background:conic-gradient(from 90deg,#22D3EE,#8B5CF6,#E34FCB,#22D3EE);
    opacity:.42;-webkit-mask:radial-gradient(circle, transparent 62%, #000 64%, #000 78%, transparent 80%);
    mask:radial-gradient(circle, transparent 62%, #000 64%, #000 78%, transparent 80%)"></div>
  <div style="position:absolute;inset:104px;border-radius:50%;
    background:radial-gradient(circle,rgba(227,79,203,.55),transparent 70%);filter:blur(16px)"></div>
 </div>
 <div style="position:absolute;inset:0;background:linear-gradient(97deg,
   rgba(6,8,15,.98) 0%, rgba(6,8,15,.93) 32%, rgba(6,8,15,.60) 55%, rgba(6,8,15,.12) 84%, rgba(6,8,15,0) 100%)"></div>
</div></body></html>"""

# C — gradient + waveform/scope bars
C = HEAD + """
<div class="h">
 <div style="position:absolute;inset:0;background:
   radial-gradient(900px 520px at 5% -18%, rgba(227,79,203,.28), transparent 62%),
   radial-gradient(740px 450px at 97% 114%, rgba(139,92,246,.24), transparent 60%)"></div>
 <div style="position:absolute;right:0;bottom:0;top:0;width:64%;display:flex;align-items:flex-end;gap:9px;padding:0 40px 54px 0;opacity:.55">
""" + "".join(
  f'<div style="flex:1;height:{h}%;border-radius:4px 4px 0 0;background:linear-gradient(180deg,{c} 0%,rgba(6,8,15,0) 100%)"></div>'
  for h,c in zip([26,44,68,38,84,54,72,30,60,46,90,36,64,50,78,32],
                 ["#22D3EE","#4F7CFF","#8B5CF6","#E34FCB"]*4)
) + """
 </div>
 <div style="position:absolute;inset:0;background:linear-gradient(97deg,
   rgba(6,8,15,.98) 0%, rgba(6,8,15,.94) 33%, rgba(6,8,15,.62) 56%, rgba(6,8,15,.14) 84%, rgba(6,8,15,0) 100%)"></div>
</div></body></html>"""

for tag, doc in [("A",A),("B",B),("C",C)]:
    p = os.path.join(HERE, f"lc-{tag}.html"); open(p,"w").write(doc)
    shot = os.path.join(HERE, f"lc-{tag}.png")
    subprocess.run([CHROME,"--headless","--disable-gpu","--hide-scrollbars",
                    f"--screenshot={shot}",f"--window-size={W},{H}",f"file://{p}"],
                   check=True,capture_output=True)
    out = os.path.join(HERE, f"lc-{tag}.jpg")
    subprocess.run(["magick",shot,"-quality","86","-strip",out],check=True)
    print("built",tag, os.path.getsize(out)//1024,"KB")
