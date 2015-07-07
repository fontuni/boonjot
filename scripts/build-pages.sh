#!/usr/bin/env sh

# Covert scss to css
sass css/boonjot.scss libraries/reveal.js/css/theme/boonjot.css

# To-do add customized theme/css
pandoc --to=revealjs -V revealjs-url=libraries/reveal.js -V theme=boonjot --standalone sources/index.md -o index.html

# To print PDF file from Chrome, append `?print-pdf` to url then just print.
# /index.html?print-pdf#/
