# EQ redesign: Library images -> img/v2/<name>-<w>.{avif,webp,jpg}
from PIL import Image
L='/workspace/vanna/library/Images/'
JOBS=[('hero','Healthcare AI/hc-ai-boardroom-skyline.png',None,(768,1280,1774)),
      ('conversation','Orbisolo Executive/orbisolo-exec-08.png',(3/2,.50),(640,1080)),
      ('team','Orbisolo Executive/orbisolo-exec-10.png',(3/2,.50),(640,1080)),
      ('clinical-team','Orbisolo Executive/orbisolo-exec-01.png',(3/2,.45),(640,1080))]
for name,src,crop,ws in JOBS:
    im=Image.open(L+src).convert('RGB'); W,H=im.size
    if crop:
        r,cx=crop; nw=round(H*r); x0=max(0,min(W-nw,round(W*cx-nw/2))); im=im.crop((x0,0,x0+nw,H))
    for w in ws:
        h=round(im.height*w/im.width); r=im.resize((w,h),Image.LANCZOS)
        r.save(f'img/v2/{name}-{w}.jpg',quality=80,optimize=True,progressive=True); r.save(f'img/v2/{name}-{w}.webp',quality=78,method=6); r.save(f'img/v2/{name}-{w}.avif',quality=58)
        print(name,w,h)
