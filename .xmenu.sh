#!/bin/sh

xmenu <<EOF | sh &
Applications
	IMG:./icons/web.png	Web Browser	firefox
	IMG:./icons/gimp.png	Image editor	gimp
Terminal		kitty
Change Wallpaper	change-wall
Shutdown		poweroff
Reboot			reboot
EOF
