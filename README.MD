
# LanLauncher

## Overview

Ever wanted to play **Plutonium** without an internet connection? This project, **LanLauncher**, allows you to launch **Plutonium** without requiring an internet connection, ensuring a hassle-free experience. It works on **Windows**, and **Linux** systems (such as the **Steam Deck**). (wine is required for linux systems)

Just fill out the relevant information in the provided fields and click the launch button to start.

![Capture](https://github.com/JugAndDoubleTap/LanLauncher/assets/133887820/5e63b9fa-ba83-41af-8fef-3807dbc63bb8)

## Features

- Launch **Plutonium** offline without an active internet connection
- Launch a LAN server directly from the GUI
- Install mods and custom maps directly from the GUI (must have "standard" mod file structure, like WAW custom maps)
- Commandline arguments to launch with no gui, directly into a game
- Compatible with **Windows** and **Linux** (with wine)
- Simple user interface

## Installation

1. **Download** the latest release of LanLauncher from the [releases section.](https://github.com/JugAndDoubleTap/LanLauncher/releases)
2. **Run** the executable. No installation is required just extract the zip file, open the program and fill in the necessary paths, and launch **Plutonium** offline to your heart's content.

## Using with commandline

**LanLauncher** can be launched using the following commandline arguments
- **-nogui** required for all of the other arguments to work, launches with no gui using the specificed folders and gameid to launch a game, uses the settings set in the GUI if no replacements are provided (launching using -nogui -gameid "T6" -mode "ZM" and nothing else will launch Black ops 2 into zombies mode, provided you have set the path to Black ops 2 inside the GUI already)
- **-mode** sets the mode, there are only 2 valid options which are "ZM" or "MP" usage example : -mode "ZM"
- **-gameid** sets which game will be launched, valid options are "T4", "T5", "T6", "IW5" usage example : -gameid "T6"
- **-gamedir** sets the game directory that will be launched usage example : -gamedir "Z:\SteamLibrary\steamapps\common\Call of Duty World at War"
- **-plutoniumdir** sets the plutonium directory that will be used usage example : -plutoniumdir "C:\Users\User\AppData\Local\Plutonium"
- **-name** sets the name that will be used ingame, default is the one set in the GUI usage example : -name "JugAndDoubleTap"



This program uses the following libraries and external tools:

### Third-Party Libraries
- **PyInstaller**: Used to package the Python scripts into an executable.
- **FreeSimpleGUI**: Used for building the user interface.
- **wget (python)**: Used mainly in the updater to download a later release.
- **7-Zip**: Used for extracting mod archives. (zip, 7z, rar, exe)


## License Summary

### PyInstaller
- **License**: Dual-licensed under the GNU General Public License v2.0 (GPLv2) with an exception for bundling and the Apache License 2.0 for certain files.
- **Usage**: PyInstaller is used to package the Python scripts into an executable format.
- **Source**: [PyInstaller GitHub Repository](https://github.com/pyinstaller/pyinstaller)
- **License Text**: A copy of the PyInstaller license is included [here.](https://github.com/JugAndDoubleTap/LanLauncher/raw/main/ThirdParty-Licenses/pyinstaller-license.txt)

### 7-Zip
- **License**: GNU Lesser General Public License v2.1 (LGPLv2.1), with an "unRAR license restriction" and BSD 3-Clause License for specific parts.
- **Usage**: 7-Zip is used to extract mod archives.
- **Source**: [7-Zip Website](https://www.7-zip.org)
- **License Text**: A copy of the 7-Zip license is included [here.](https://github.com/JugAndDoubleTap/LanLauncher/raw/main/ThirdParty-Licenses/7zip-license.txt)

### Original Code License
This project, **LanLauncher**, is licensed under the **GNU Lesser General Public License v3.0 (LGPLv3)**. A copy of this license is provided [here.](https://github.com/JugAndDoubleTap/LanLauncher/raw/main/LICENSE)


### Additional Information

[Plutonium launcher website.](https://plutonium.pw/)

For more details about the licenses, see the `ThirdParty-Licenses` directory in this repository, where the full text of relevant third-party licenses is included.
