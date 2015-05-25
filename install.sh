#!/bin/zsh

#Exits on error
set -e

#Output Every command
#set -x

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

if [ ! -d ~/.config/sublime-text-3/ ]; then
  mkdir ~/.config/sublime-text-3/
fi

if [ ! -d ~/.config/sublime-text-3/Packages/ ]; then
  mkdir ~/.config/sublime-text-3/Packages/
fi

if [ ! -d ~/.config/sublime-text-3/Packages/User ]; then
  mkdir ~/.config/sublime-text-3/Packages/User/
fi

echo -e "Installing Files"

cp -r $(pwd)/Buggy---Linux ~/.config/sublime-text-3/Packages/User/
cp -r $(pwd)/CF ~/.config/sublime-text-3/Packages/User/
