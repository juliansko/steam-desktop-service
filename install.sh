#!/bin/sh

pip install watchdog
mkdir -p ~/.local/bin
cp watch.py ~/.local/bin/
chmod +x ~/.local/bin/watch.py
mkdir -p ~/.config/systemd/user
cp steam-desktop.service ~/.config/systemd/user/
systemctl --user enable steam-desktop --now