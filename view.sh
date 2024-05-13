#!/bin/sh
rm -rf ~/.tmp/zathura/
mkdir -p ~/.tmp/zathura
touch ~/.tmp/zathura/current
wget $(echo $(xclip -o)) -O ~/.tmp/zathura/current && zathura ~/.tmp/zathura/current
