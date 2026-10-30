#!/usr/bin/env bash
set -e; R=/workspace/tmp/repos/eqleadership-site; D=/workspace/tmp/wr/eq-dist
rm -rf "$D"; mkdir -p "$D/css" "$D/img" "$D/media"; cd "$R"
cp index.html 404.html _headers robots.txt site.webmanifest favicon.svg favicon.png "$D/"; cp css/eq.css "$D/css/"; cp -r fonts "$D/"
cp -r img/v2 "$D/img/"; cp img/favicon-*.png img/apple-touch-icon.png img/og-image.jpg "$D/img/"
cp media/eq-commercial.mp4 media/eq-commercial-poster-960.jpg "$D/media/"
du -sh "$D"
