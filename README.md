# Steam Desktop Watcher

This is a python service that watches your flatpak steam directory and all the games in the menu are landing in your 
local applications folder automatically. 

**TLDR**:This puts your Steam games in your application menu when installing them

If you have already installed games you may want to re-add the application menu shortcut from steam

## Installation

Just do `sh install.sh` and you should be good to go. 

You are required to have pip and systemd installed and thats kind of it. If
you don't have them installed you can probably write a better script in 5 minutes and if you don't know
what those mean - don't worry, your good

## Shortcomings

I have no idea if this works on other desktops (it should tho), also this will not give you applications shortcuts on the
desktop. If someone wants to they are very welcome to contribute and extend the script to the Desktop folder as well. Also this
is very much done quick and dirty but if you want an elegant solution just ask valve to finally fix the flatpak and make it official
