# EQ Leadership Institute redesign preview. Source = index.html at commit 4741669 (f5fe3ff + PR #1 fixes); copy kept verbatim except
# the edits listed in drafts/eq-copy-slots.md. Run inside eqleadership-site on aria/2026-10-30-eq-redesign.
import subprocess,re
src=subprocess.run(['git','show','4741669:index.html'],capture_output=True,text=True,check=True).stdout
s=src
MAIL='hello@eqleadershipinstitute.com'
CALL=f'mailto:{MAIL}?subject=Book%20a%20call&amp;body=Hello%2C%0A%0AI%27d%20like%20to%20book%20a%20call.%0A%0AName%3A%0ARole%3A%0AOrganization%3A%0AWhat%20I%27d%20like%20to%20discuss%3A%0AGood%20times%20for%20me%3A%0A'
def pic(n,ws,W,H,sizes,alt,extra=''):
    ss=lambda e: ', '.join(f'img/v2/{n}-{w}.{e} {w}w' for w in ws)
    return f'<picture><source type="image/avif" srcset="{ss("avif")}" sizes="{sizes}"><source type="image/webp" srcset="{ss("webp")}" sizes="{sizes}"><img src="img/v2/{n}-{ws[-1]}.jpg" srcset="{ss("jpg")}" sizes="{sizes}" width="{W}" height="{H}" alt="{alt}"{extra}></picture>'
def badge(px,lazy):
    lz=' loading="lazy" decoding="async"' if lazy else ''
    if px==80: srcs='<source media="(max-width:719px)" type="image/avif" srcset="img/v2/eq-badge-64.avif 1x, img/v2/eq-badge-128.avif 2x"><source media="(max-width:719px)" type="image/webp" srcset="img/v2/eq-badge-64.webp 1x, img/v2/eq-badge-128.webp 2x"><source type="image/avif" srcset="img/v2/eq-badge-80.avif 1x, img/v2/eq-badge-160.avif 2x"><source type="image/webp" srcset="img/v2/eq-badge-80.webp 1x, img/v2/eq-badge-160.webp 2x">'
    else: srcs='<source type="image/avif" srcset="img/v2/eq-badge-88.avif 1x, img/v2/eq-badge-176.avif 2x"><source type="image/webp" srcset="img/v2/eq-badge-88.webp 1x, img/v2/eq-badge-176.webp 2x">'
    return f'<picture>{srcs}<img class="mark" src="img/v2/eq-badge-{px*2}.png" width="{px}" height="{px}" alt=""{lz}></picture>'
def rep(a,b,count=1):
    global s
    assert s.count(a)>=1, a[:90]
    s=s.replace(a,b,count if count else -1) if count else s.replace(a,b)
# head
rep('<meta name="viewport" content="width=device-width,initial-scale=1">','<meta name="viewport" content="width=device-width,initial-scale=1">\n<meta name="robots" content="noindex, nofollow">')
rep('<link rel="preload" as="image" href="img/hero.webp" imagesrcset="img/hero-900.webp 900w, img/hero.webp 1680w" imagesizes="100vw">',
    '<link rel="preload" as="image" type="image/avif" imagesrcset="img/v2/hero-768.avif 768w, img/v2/hero-1280.avif 1280w, img/v2/hero-1774.avif 1774w" imagesizes="100vw" fetchpriority="high">')
rep('href="css/site.css"','href="css/eq.css"')
# header + footer badge
rep('<picture><source srcset="img/eq-badge-176.webp" type="image/webp"><img class="mark" src="img/eq-badge-176.png" width="80" height="80" alt=""></picture>',badge(80,False))
rep('<picture><source srcset="img/eq-badge-176.webp" type="image/webp"><img class="mark" src="img/eq-badge-176.png" width="88" height="88" alt="" loading="lazy" decoding="async"></picture>',badge(88,True))
# hero image
s=re.sub(r'(<section class="hero"[^>]*>\s*)<picture>.*?</picture>',lambda m:m.group(1)+'<div class="hero-media">'+pic('hero',(768,1280,1774),1774,887,'100vw','A leader standing to guide a boardroom discussion with executives and clinicians, city skyline at sunset',' fetchpriority="high"')+'</div>',s,count=1,flags=re.S)
# why: walk -> conversation
s=re.sub(r'<picture><source type="image/webp" srcset="img/walk-900.webp.*?</picture>',pic('conversation',(640,1080),1080,720,'(max-width:899px) 92vw, 540px','Four leaders, including a physician, in a warm conversation in a bright hospital lobby',' loading="lazy" decoding="async"'),s,flags=re.S)
# self-check: notebook photo -> four areas panel (names + notes are the approved self-check copy)
AREAS=[('Self-awareness','Noticing what you feel and how you come across.'),('Self-regulation','Choosing your response, especially under pressure.'),('Empathy','Understanding how others feel and what they need.'),('Connection','Communicating clearly and building trust.')]
panel='<div class="areas" aria-labelledby="areas-h"><p class="kicker">Self-check areas</p><h3 id="areas-h">Key areas</h3><ol>'+''.join(f'<li><span class="n" aria-hidden="true">0{i+1}</span><div><strong>{a}</strong><span>{b}</span></div></li>' for i,(a,b) in enumerate(AREAS))+'</ol></div>'
s=re.sub(r'<div class="photo">\s*<picture><source type="image/webp" srcset="img/notebook-900.webp.*?</picture>\s*</div>',panel,s,flags=re.S)
# programs: room -> team
s=re.sub(r'<picture><source type="image/webp" srcset="img/room-900.webp.*?</picture>',pic('team',(640,1080),1080,720,'(max-width:899px) 92vw, 540px','A leadership team of executives and a physician standing together in a boardroom',' loading="lazy" decoding="async"'),s,flags=re.S)
# who: workshop -> clinical team
s=re.sub(r'<picture><source type="image/webp" srcset="img/workshop-900.webp.*?</picture>',pic('clinical-team',(640,1080),1080,720,'(max-width:899px) 92vw, 540px','A clinical team gathered around a workstation, working through a decision together',' loading="lazy" decoding="async"'),s,flags=re.S)
# final CTA: photo background removed (CSS aubergine art)
s=re.sub(r'(<section class="section on-dark final"[^>]*>\s*)<picture>.*?</picture>\s*',r'\1',s,count=1,flags=re.S)
# no prices
rep('<p>A four-week live virtual cohort. $795 founding seat. <a href="#lab">Details</a></p>','<p>A four-week live virtual cohort. Contact us for pricing. <a href="#lab">Details</a></p>')
rep('<p class="kicker">Paid assessments · USD</p>','<p class="kicker">Paid assessments</p>')
rep(' All prices are in US dollars; scope and delivery details are agreed before purchase.',' Scope and delivery details are agreed before purchase.')
rep('<p><strong style="font-size:1.6em">$795</strong> per leader, one-time. Seats are limited to keep the group small. Next cohort dates announced soon.</p><div class="btn-row" style="margin-top:16px"><a class="btn btn-clay" href="https://buy.stripe.com/28E7sLfQw5bE11Ddae7Vm0u" rel="noopener" data-cta="lab-reserve">Reserve a founding seat</a></div>',
    f'<p><strong>Contact us for pricing.</strong> Seats are limited to keep the group small. Next cohort dates announced soon.</p><div class="btn-row" style="margin-top:16px"><a class="btn btn-clay" href="{CALL}" data-cta="lab-book-call">Book a call</a></div>')
assert '$' not in re.sub(r'<script>.*?</script>','',s,flags=re.S), 'price left'
# Contact us for pricing + Book a call band after the paid assessments
rep('<p class="disclaimer" style="margin-top:24px">These are EQ',f'<div class="cta-band"><p>Contact us for pricing.</p><a class="btn btn-clay" href="{CALL}" data-cta="assessments-book-call">Book a call</a></div>\n    <p class="disclaimer" style="margin-top:24px">These are EQ')
# final CTA: add Book a call
rep('data-cta="final-conversation">Request an Assessment</a>',f'data-cta="final-conversation">Request an Assessment</a>\n      <a class="btn btn-ghost" href="{CALL}" data-cta="final-book-call">Book a call</a>')
# footer: from Florida + visible hello@
rep('<span>&copy; 2026 EQ Leadership Institute</span>',f'<span>&copy; 2026 EQ Leadership Institute &middot; from Florida &middot; <a href="mailto:{MAIL}?subject=EQ%20Leadership%20Institute">{MAIL}</a></span>')
open('index.html','w').write(s); print('index',len(s))
nf=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex, nofollow">
<title>Page not found | EQ Leadership Institute</title><meta name="description" content="This page could not be found. Return to EQ Leadership Institute.">
<meta name="theme-color" content="#3A2242"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" type="image/png" sizes="32x32" href="/img/favicon-32.png"><link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="preload" href="/fonts/fraunces-latin.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/fonts/manrope-latin.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="/css/eq.css"></head>
<body class="nf-body"><main id="main" class="nf"><div class="wrap center">{badge(88,False).replace('src="img/','src="/img/').replace('srcset="img/','srcset="/img/').replace(', img/',', /img/')}
<p class="kicker">404</p><h1>Page not found</h1><p class="lead">The page you are looking for is misplaced.</p>
<div class="btn-row"><a class="btn btn-clay" href="/">Back to home</a><a class="btn btn-ghost" href="/#self-check">Take the free self-check</a></div></div></main></body></html>
'''
open('404.html','w').write(nf); print('404 ok')
