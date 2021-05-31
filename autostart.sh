#!/bin/bash
picom &
nm-applet &
python3 ~/.config/qtile/config/get_clrs.py &
wal -R &