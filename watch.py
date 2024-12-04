#!/usr/bin/env python3
import re
import subprocess
from watchdog.observers import Observer
import shutil

from watchdog.events import FileSystemEventHandler, DirCreatedEvent, FileCreatedEvent
from pathlib import Path

# Gets Home Directory Path
HOME = str(Path.home())

class MenuHandler(FileSystemEventHandler):
    def __init__(self, flatpak, local):
        self.flatpak = flatpak
        self.local = local

    # Function that is executed when a file is created
    def on_created(self, event: DirCreatedEvent | FileCreatedEvent) -> None:
        # Ends if the new file is a directory or not a game
        if event.is_directory:
            return
        filename = event.src_path.split("/")[-1]
        if (not filename.endswith(".desktop")) or filename.startswith("Steam") or filename.startswith("Proton"):
            return

        flatpak_path = event.src_path

        try:
            # Copies desktop file to local share
            shutil.copy2(flatpak_path, self.local)
            local_path = f"{self.local}/{filename}"

            with open(local_path, "r") as f:
                content = f.read()
            # Replaces the steam command with flatpak
            content = re.sub(r"Exec=steam", "Exec=flatpak run com.valvesoftware.Steam", content)
            # Copies the entire steam icon folder into local (yes I know this is a horrible practice and will probably cause overhead if your local library gets bigger but I just want to have my desktop entries. You are free to write a commit with an ignore function that ignores existing files (Find documentation in shutil docs))
            shutil.copytree(self.flatpak + icons_path, self.local + icons_path, dirs_exist_ok=True )

            try:
                # Updates icon cache on gnome
                subprocess.run(["gtk-update-icon-cache", self.local + icons_path, "-t"])
            except subprocess.CalledProcessError as e:
                pass

            with open(local_path, "w") as f:
                f.write(content)

        except Exception as e:
            print(e)

flatpak = HOME + "/.var/app/com.valvesoftware.Steam/.local/share/applications"
local = HOME + "/.local/share/applications"
icons_path = "/../icons/hicolor"

observer = Observer()
observer.schedule(MenuHandler(flatpak, local), path=flatpak, recursive=False)
observer.start()
try:
    while observer.is_alive():
        observer.join(1)

finally:
    observer.stop()
    observer.join()
