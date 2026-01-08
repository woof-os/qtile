#!/bin/sh

if [ "$ROFI_RETV" = "1" ] || [ "$ROFI_RETV" = "2" ]
then
	notify-send "Copied $@ to clipboard."
	echo "$@" | xsel -i -b
	exit 0
fi

cat $HOME/Basement/bookmarks.txt
