#!/bin/sh

clear
echo -e "\033[94m#################################################\033[0m"
echo -e "\033[94m########## \033[1mInstall Woof's Qtile Config\033[0m\033[94m ##########\033[0m"
echo -e "\033[94m#################################################\033[0m"

config() {
	echo -e "\033[94m#################################################\033[0m"
	echo -e "\033[95m\033[1mStarting...\033[0m"
	sleep 3
	clear
	echo -e "\033[95m\033[1mDeleting Files...\033[0m"
	rm -rf ~/.config/qtile/*
	sleep 1
	clear
	echo -e "\033[95m\033[1mCopying Files...\033[0m"
	cp -r ./* ~/.config/qtile/
	sleep 1
	clear
	echo -e "\033[94mDone copying, going to install fonts.\033[0m"
	mkdir ~/.fonts
	cp ./fonts/* ~/.fonts
	sleep 1
	clear
	echo -e "\033[96m"
	read -p "Do you want set qtile as the default desktop in xinitrc (yes/no): " yn
	case $yn in
	    [Yy]* ) echo "exec qtile start" > ~/.xinitrc;;
	    [Nn]* ) clear; exit;;
	esac

}

echo -e "\033[41mAll contents of ~/.config/qtile will be deleted\033[0m"
echo -e "\033[96m"
echo -e "All contents of ~/.config/qtile will be deleted"
read -p "Are you sure you want to install Woof's config? (yes/no): " yn
case $yn in
    [Yy]* ) config;;
    [Nn]* ) clear; exit;;
esac

