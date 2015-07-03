#!/usr/bin/env sh

# Sometimes I need older FontForge to compare bugs.
# This Docker command will only work on GNU+Linux
docker run -it --rm -u fontdev \
  -e DISPLAY=unix$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v $HOME/src/github.com/BoonUni/boonjot/:/home/fontdev/boonjot \
  sungsit/fontforge:2012
