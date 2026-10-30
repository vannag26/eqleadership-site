# Image sources: redesign preview (aria/2026-10-30-eq-redesign)

All photographs come from Vanna's Library (`/workspace/vanna/library/Images/`), re-encoded by `tools/eq_images.py` to AVIF, WebP and JPG with width and height set. None is the Orbisolo hero video frame set (orbisolo-exec-05/11/12/14) or a VibeAPI image.

| File | Use | Source | Crop |
|---|---|---|---|
| img/v2/hero-{768,1280,1774}.* | Hero (preloaded, fetchpriority high) | Images/Healthcare AI/hc-ai-boardroom-skyline.png | full 2:1 |
| img/v2/conversation-{640,1080}.* | Why EQ | Images/Orbisolo Executive/orbisolo-exec-08.png | 3:2 centre |
| img/v2/team-{640,1080}.* | Programs | Images/Orbisolo Executive/orbisolo-exec-10.png (also used inside orbisolo.com, not as its hero) | 3:2 centre |
| img/v2/clinical-team-{640,1080}.* | Who it's for | Images/Orbisolo Executive/orbisolo-exec-01.png | 3:2, 45% |
| img/v2/eq-badge-{64,80,88,128,160,176}.{avif,webp,png} | Header (80, 64 on mobile), footer (88), 404 | img/eq-badge-176.png (approved badge from f5fe3ff) | - |
| favicons, img/og-image.jpg | Unchanged from f5fe3ff | - | - |
| media/eq-commercial.mp4 + poster-960 | Existing approved short film (unchanged) | Earlier Canva footage (see img/CREDITS.md) | - |

Skipped after viewing: orbisolo-exec-02/03/04/05/06/07/13/14 and hc-ai-innovation/patient-care/solutions banners (baked-in text, icon overlays or claims), 09 (no people), 11/12 (Orbisolo hero frames; 11 also has a slogan on screen).
The self-check photo was replaced by a "four areas" panel and the final CTA photo by CSS art, so no extra images were needed.
