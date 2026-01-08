#!/bin/sh

if [ "$ROFI_RETV" = "1" ] || [ "$ROFI_RETV" = "2" ]
then
	zen-browser "https://www.online-latin-dictionary.com/latin-english-dictionary.php?parola=$@" --new-tab
	exit 0
fi

echo "Enter the Latin term"
