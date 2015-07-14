# บุญจด สุดหรรษา (BoonJot)

![BoonJot Screenshoot](images/boonjot-screenshot.png?raw=true)

BoonJot is left-handed comic sans family (I supposed). It’s machine-made family with unique stroke speed, pen shape & drawing direction especially Thai glyphs. I designed & drew each glyph as single stroke before expanded it to get proper weight with [FontForge](http://fontforge.github.io/en-US/) then worked in detail with [Inkscape](https://inkscape.org/en/). Glyph style is up-right italic but unlike many handwriting fonts, BoonJot doesn’t try to connect glyphs together. That maintains its casual look & still somewhat legible on screen at small size.

Specimen and test pages can be found here <https://fontuni.com/boonjot/> or in PDF format here <https://fontuni.com/boonjot/docs/boonjot-specimen.pdf>.

## Build Fonts

Binary fonts were already built & included in `fonts` dir but you can do it yourself anyway.

- Install FontForge (+Python extention)
- Compile ttfautohint from dev repo <http://repo.or.cz/w/ttfautohint.git> or `brew install ttfautohint --HEAD` for better Thai hinting.
- Compile Google's woff2 compressor <https://github.com/google/woff2>.
- Clone this repos & get inside it.
- Fontuni library for building OT features & RevealJS for HTML pages are required. Run `git submodule init && git submodule update`
- Then run `fontforge -script scripts/build.py` to build TTF, WOFF & WOFF2 fonts

## Build Pages (locally)

- I use [Pandoc (v1.15+)](http://pandoc.org/installing.html#installing-from-source), [RevealJS](https://github.com/hakimel/reveal.js/) & [Sass](http://sass-lang.com/install) to convert markdown to html. If you edit the file `sources/index.md`, just run `sh scripts/build-pages.sh` to rebuild it.
- The slides won't work properly with file uri scheme (for example `file:///fontuni/boonjot/index.html`) so you need whatever webserver which can serve static html. Many built-in webservers will work just fine, for example `python2 -m SimpleHTTPServer 4000` or `python3 -m http.server 4000` or `ruby -run -e httpd -- -p 4000 .` or `php -S localhost:4000`.
- Then open your browser & go to <http://localhost:4000/>

## CSS workarounds

- The `locl` feature only works for installed fonts (on your machine). For web fonts (`@font-face`), we need to precisely enable this feature like this one:

  ```
  body {
    -webkit-font-feature-settings:"locl"; 
    -moz-font-feature-settings:"locl"; 
    -ms-font-feature-settings:"locl"; 
    font-feature-settings:"locl";
  }
  ```

## Known issues & Wontfix

See [#12](https://github.com/fontuni/boonjot/issues/12)

