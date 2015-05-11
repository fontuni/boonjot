#!/usr/bin/env fontforge
##
# This script will only work with FontForge's Python extension.
# 
# Usage:
##

import os
import argparse
import fontforge

'''
Thai Font Build:

1. Base: Bare OTF without any features but it should work with HarfBuzz
2. Min: Minamal glyph set without positional Thai PUA, intensively use `mark` & `mkmk`. 
3. Full: This will be use in wide-range of applications, include Adobe's.
4. Pro: At least include Latin-1. Some pro features like `tnum`, `frac` ... may be added later.

Note: Glyph sets can be just encoding slots. For FontForge, encoding & namelist files can be imported to `~/.config/fontforge/` but I have no idea about other font editors. So let's stick with UnicodeFull to keep things simple.

'''

parser = argparse.ArgumentParser(description='This script will create new FontForge file and set some font properties which suitable for Thai font.')
parser.add_argument("family", type=str, help="Font family name")
args = parser.parse_args()

# Set global variables
encoding = "UnicodeFull"
template = "BoonThing-400.ufo" # Todo: Change to arg when we have more weights.
family = args.family.replace(" ","-")

builddir = "build/"
if not os.path.exists(builddir):
  os.makedirs(builddir)

def setFontProp(template,family,weight):
  font = fontforge.open(template)
  font.familyname = args.family
  font.os2_weight = int(weight)
  font.weight = str(weight)
  font.fontname = family + "-" + str(weight)
  font.fullname = family + " " + str(weight)
  font.copyright = "Built from BoonThing font template. Add your copyright here." # reset copyright for new font.
  font.save(builddir + font.fontname)
  font.close()

def buildThaiBase(source,ext):
  src = fontforge.open(source)
  src.generate(source + "." + ext)
  src.close()

# 1. Base
setFontProp(template,family,"400")
buildThaiBase(builddir + family + "-400","otf")
buildThaiBase(builddir + family + "-400","ufo")

# Clear tmp file
os.remove(builddir + family + "-400")


# 2. Minimal
# Todo: Find out how to select or clear glyphs from FontForge API
# http://dmtr.org/ff.php