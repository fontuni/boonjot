# บุญจด สุดหรรษา (BoonJot)

BoonJot is left-handed comic sans family (I supposed). It’s machine-made family with unique stroke speed, pen shape & drawing direction especially Thai glyphs. I designed & drew each glyph as single stroke before expanded it to get proper weight with [FontForge](http://fontforge.github.io/en-US/) then worked in detail with [Inkscape](https://inkscape.org/en/). Glyph style is up-right italic but unlike handwriting fonts, BoonJot doesn’t try to connect glyphs together. That makes it casual & still somewhat legible on screen at small size.

**The font features are still in the early stage of development** but you can give it a try to see what it looks like here <https://boonuni.com/boonjot/>.

## Build Fonts

Binary fonts were already built & included in `fonts` dir but you can do it yourself anyway.

- Install FontForge (+Python extention)
- Clone this repos & get inside it.
- Run `git submodule init && git submodule update`
- Run `fontforge -script build.py`

## Serve Test Pages (locally)

I'm just too lazy to write HTML by hand, Markdown is pretty much easier (but Jekyll has a lot of dependencies nowadays, Pandoc may be better alternative to convert md -> html -> pdf).

- Install Ruby (recommended way: [rbenv](https://github.com/sstephenson/rbenv) + [ruby-build](https://github.com/sstephenson/ruby-build))
- Install Gem 'github-pages'
- (Jekyll also requires NodeJS or another JavaScript runtime, [nvm](https://github.com/creationix/nvm) is recommended if you want NodeJS.)
- Run `jekyll serve`
- Open your browser & go to `http://localhost:4000/`

