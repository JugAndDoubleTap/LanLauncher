import subprocess
import wget
import sys
import os

def download_update(url):
    #wget function to download the updated EXE
    wget.download(url)


os.remove('LanLauncher.exe')
os.remove('LAN.ico')
download_update(r'https://github.com/JugAndDoubleTap/LanLauncher/raw/main/bin/LanLauncher.exe')
download_update(r'https://raw.githubusercontent.com/JugAndDoubleTap/LanLauncher/main/bin/LAN.ico')
subprocess.Popen('LanLauncher.exe', shell=True)
sys.exit()

    
