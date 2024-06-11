#!/bin/sh
notify-send "Loading zathura..."
URL=$(echo $(xclip -o))
FILE=${URL##*/}
ROOT="$HOME/Basement/PDF/"
mkdir -p $ROOT
ls $ROOT
wget "$URL" -O "$ROOT$FILE" && zathura "$ROOT$FILE"
notify-send "Zathura closed."
