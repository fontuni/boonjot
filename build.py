#!/usr/bin/env fontforge
#
# Copyright (c) 2015, Sungsit Sawaiwan (https://sungsit.com | gibbozer [at] gmail [dot] com).
#
# This Font Software is licensed under the SIL Open Font License, Version 1.1 (OFL).
# You should have received a copy of the OFL License along with this file.
# If not, see http://scripts.sil.org/OFL
#

# This script will only work with FontForge's Python extension.
import fontforge
import os

# Predifined vars
family = 'BoonJot'
version = '1.0-alpha1'
source = 'sources/BoonJot-400.ufo'
weights = [400]
copyright =  'Copyright (c) 2015, Sungsit Sawaiwan (https://sungsit.com | gibbozer [at] gmail [dot] com). This Font Software is licensed under the SIL Open Font License, Version 1.1 (http://scripts.sil.org/OFL).'
features = ['Thai-Basic', 'Latin-4']
feature_dir = 'libraries/f0ntuni/features/'
build_dir = 'fonts/'

def setFontInfo(source,family,weight):
  font = fontforge.open(source)
  font.familyname = family
  font.fontname = family + '-' + str(weight)
  font.fullname = family + ' ' + str(weight)
  font.weight = str(weight)
  font.os2_weight = weight
  font.version = version
  font.copyright = copyright

def printFontInfo(fontfile):
  font = fontforge.open(fontfile)
  print('\nFamily Name: ' + font.familyname)
  print('Font Name: ' + font.fontname)
  print('Full Name: ' + font.fullname)
  print('Font Weight: ' + font.weight)
  print('OS2 Weight: ' + str(font.os2_weight))
  print('Font Version: ' + font.version)
  print('Font Copyright: ' + font.copyright)
  font.close()

def buildFont(source,family,weight):
  font = fontforge.open(source)
  setFontInfo(source,family,weight)

  ttf = build_dir + font.fontname + '.ttf'
  otf = build_dir + font.fontname + '.otf'
  genflags  = ('opentype', 'PfEd-lookups', 'no-hints')

  for feature in features:
    font.mergeFeature(feature_dir + feature + '.fea')  

  font.generate(ttf, flags=genflags)
  printFontInfo(ttf)
  font.generate(otf, flags=genflags)
  printFontInfo(otf)
  font.close()

if not os.path.exists(build_dir):
  os.makedirs(build_dir)

for weight in weights:
  buildFont(source,family,weight)
