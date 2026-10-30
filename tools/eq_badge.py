# Render badge sizes, favicons and OG from the cut master (run tools/eq_badge_cut.py first, in a work dir holding r600.png = pdftocairo -png -r 600 -transp -singlefile <master.pdf> r600).
from PIL import Image, ImageDraw; import base64, io, os
R='/workspace/tmp/repos/eqleadership-site'
badge=Image.open('badge-master.png'); mark=Image.open('mark-master.png').convert('RGB'); BG=(38,12,40)
for px in (64,128,192,80,160,240,88,176,264):
    r=badge.resize((px,px),Image.LANCZOS); b=f'{R}/img/v2/eq-badge-{px}'
    r.save(b+'.png',optimize=True); r.save(b+'.webp',quality=90,method=6); r.save(b+'.avif',quality=80)
def rounded(size,rad=0.2):
    im=mark.resize((size*4,size*4),Image.LANCZOS); m=Image.new('L',im.size,0)
    ImageDraw.Draw(m).rounded_rectangle((0,0,im.size[0]-1,im.size[1]-1),int(size*4*rad),fill=255)
    o=im.convert('RGBA'); o.putalpha(m); return o.resize((size,size),Image.LANCZOS)
rounded(32).save(f'{R}/img/favicon-32.png',optimize=True); rounded(48).save(f'{R}/favicon.png',optimize=True)
mark.resize((180,180),Image.LANCZOS).save(f'{R}/img/apple-touch-icon.png',optimize=True)
mark.resize((192,192),Image.LANCZOS).save(f'{R}/img/favicon-192.png',optimize=True)
mark.resize((512,512),Image.LANCZOS).save(f'{R}/img/favicon-512.png',optimize=True)
mk=Image.new('RGB',(512,512),BG); mk.paste(mark.resize((400,400),Image.LANCZOS),(56,56)); mk.save(f'{R}/img/favicon-maskable-512.png',optimize=True)
buf=io.BytesIO(); mark.resize((128,128),Image.LANCZOS).save(buf,'PNG',optimize=True); b64=base64.b64encode(buf.getvalue()).decode()
open(f'{R}/favicon.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 96 96" width="96" height="96"><defs><clipPath id="r"><rect width="96" height="96" rx="19" ry="19"/></clipPath></defs><image clip-path="url(#r)" width="96" height="96" href="data:image/png;base64,{b64}" xlink:href="data:image/png;base64,{b64}"/></svg>')
og=Image.open('/workspace/eqlogo/og-orig.jpg').convert('RGBA'); D=96
og.alpha_composite(badge.resize((D,D),Image.LANCZOS),(116-D//2,94-D//2)); og.convert('RGB').save(f'{R}/img/og-image.jpg',quality=88,optimize=True,progressive=True)
print('ok')
