import PySimpleGUI as sg
import subprocess
import wget
import sys
import os

errorvar = 0

def tryhard():
    try:
        os.remove('LAN.ico')
    except Exception:
        pass
    try:
        os.rename(r".LANTMP.ico", "LAN.ico")
    except Exception:
        pass
    try:
        os.remove(r'LanLauncher.exe')
    except Exception:
        pass
    try:
        os.rename(r'.LanLauncherTMP.exe', 'LanLauncher.exe')
    except Exception:
        pass
    subprocess.Popen('LanLauncher.exe', shell=True)
    sys.exit()

def error_message():
    sg.set_options(font=('Cambria', 10))
    sg.theme('DarkAmber')
    errorlay = [[sg.Text('Could not update LanLauncher.')],
                [sg.Button('Close')]]
    errorwin = sg.Window('', errorlay)

    error = 0
    while error == 0:
        event, values = errorwin.read()
        if event == 'Close' or event == sg.WIN_CLOSED:
            error += 1
            errorwin.close()
            sys.exit()
try:
    wget.download(r'https://github.com/JugAndDoubleTap/LanLauncher/raw/main/bin/LanLauncher.exe', '.LanLauncherTMP.exe')
    wget.download(r'https://raw.githubusercontent.com/JugAndDoubleTap/LanLauncher/main/bin/LAN.ico', ".LANTMP.ico")
except Exception:
    errorvar = 1
    error_message()
if errorvar == 0:
    tryhard()
