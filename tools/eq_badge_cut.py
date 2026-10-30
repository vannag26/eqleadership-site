# Badge cut from the 600-dpi render of the PDF master (1890px). Same method as the approved f5fe3ff cut (/workspace/eqlogo/cut.py), coordinates x2.
from PIL import Image, ImageDraw, ImageFilter; import numpy as np, math
K=2
src=Image.open('r600.png').convert('RGB'); a=np.asarray(src).astype(float); d=765-a.sum(2)
cx,cy=469*K,471*K; pts=[]
for i in range(2880):
    t=2*math.pi*i/2880
    for r10 in range(4600*K,3900*K,-1):
        r=r10/10; x=cx+r*math.cos(t); y=cy+r*math.sin(t); xi,yi=int(x),int(y); fx,fy=x-xi,y-yi
        v=(d[yi,xi]*(1-fx)*(1-fy)+d[yi,xi+1]*fx*(1-fy)+d[yi+1,xi]*(1-fx)*fy+d[yi+1,xi+1]*fx*fy)
        if v>150: pts.append((x,y)); break
P=np.array(pts); x,y=P[:,0],P[:,1]
_,_,V=np.linalg.svd(np.stack([x*x,x*y,y*y,x,y,np.ones_like(x)],1)); A,B,C,Dd,E,F=V[-1]
ell=lambda xx,yy: A*xx*xx+B*xx*yy+C*yy*yy+Dd*xx+E*yy+F
c=np.linalg.solve(np.array([[2*A,B],[B,2*C]]),[-Dd,-E]); rs=np.hypot(x-c[0],y-c[1]); print('center',c,'r',rs.min(),rs.max())
H,W=d.shape; yy,xx=np.mgrid[0:H,0:W].astype(float)
g=ell(xx,yy); gx=2*A*xx+B*yy+Dd; gy=B*xx+2*C*yy+E; sd=g/np.hypot(gx,gy)
nx=gx/np.hypot(gx,gy); ny=gy/np.hypot(gx,gy)
if ell(c[0],c[1])>0: sd=-sd; nx,ny=-nx,-ny
alpha=np.clip(0.5-(sd+0.8*K)/K,0,1)   # same edge position, 2x finer ramp
band=sd>-1.8*K; out=a.copy()
ix=np.clip(np.round(xx-nx*3.5*K).astype(int),0,W-1); iy=np.clip(np.round(yy-ny*3.5*K).astype(int),0,H-1)
lighter=(a.sum(2)>a[iy,ix].sum(2)+30)&band; out[lighter]=a[iy[lighter],ix[lighter]]
im=Image.fromarray(np.dstack([out,alpha*255]).clip(0,255).astype(np.uint8),'RGBA'); im=im.crop(im.getbbox())
s=max(im.size); sq=Image.new('RGBA',(s,s),(0,0,0,0)); sq.paste(im,((s-im.size[0])//2,(s-im.size[1])//2)); sq.save('badge-master.png'); print('badge',sq.size)
# E/Q mark for favicons (as mark.py, x2)
mcx,mcy,R=471*K,450*K,212*K; S=4
m=Image.new('L',(W*S,H*S),0); dr=ImageDraw.Draw(m)
dr.ellipse(((mcx-R)*S,(mcy-R)*S,(mcx+R)*S,(mcy+R)*S),fill=255)
dr.polygon([(px*K*S,py*K*S) for px,py in [(540,560),(728,600),(728,642),(540,668)]],fill=255)
m=m.resize((W,H),Image.LANCZOS).filter(ImageFilter.GaussianBlur(6*K))
mm=np.asarray(m)[...,None]/255; comp=a*mm+np.array([38,12,40.])*(1-mm)
side=540*K; x0=mcx-side//2+18*K; y0=mcy-side//2+8*K
Image.fromarray(comp.astype(np.uint8)).crop((x0,y0,x0+side,y0+side)).save('mark-master.png'); print('mark',side)
