#!/bin/bash
picom &
protonvpn-cli connect -f -p tcp &
nm-applet &
python3 ~/.config/qtile/config/get_clrs.py &
xfce4-terminal &