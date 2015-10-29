#!/usr/bin/env sh

# Covert scss to css
sass css/boonjot.scss css/boonjot.css

# Convert markdown to reveal.js slides
#pandoc -t revealjs --template=sources/pandoc-revealjs.tpl --standalone \
#  -V revealjs-url=libraries/reveal.js \
#  -V center=false --no-highlight \
#  sources/slideshow.md -o slideshow.html

# To print PDF file from Chrome, append `?print-pdf` to url then just print.
# /index.html?print-pdf#/
