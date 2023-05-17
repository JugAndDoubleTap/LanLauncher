import PySimpleGUI as sg
import os
import subprocess
import configparser

version_num = "V1.1.1"

exe_path = r".\bin\plutonium-bootstrapper-win32.exe"
name_arg = "+name"
lan_arg = "-lan"
t4_arg = "t4sp"
t5_arg = "t5sp"
t6_arg = "t6zm"
iw5_arg = "iw5mp"
usernamecache = r""
waw = r""
bo1 = r""
bo2 = r""
mw3 = r""
plutoniumfold = r""
winuser = os.getlogin()
cdir = r"C:/Users/"
plutoapp = r"/AppData/Local/Plutonium"
wawtest = r"C:/Program Files (x86)/Steam/steamapps/common/Call of Duty World at War"
bo1test = r"C:/Program Files (x86)/Steam/steamapps/common/Call of Duty Black Ops"
bo2test = r"C:/Program Files (x86)/Steam/steamapps/common/Call of Duty Black Ops II"
mw3test = r"C:/Program Files (x86)/Steam/steamapps/common/Call of Duty Modern Warfare 3"

config = configparser.ConfigParser()

if os.path.isfile('LanLauncher.ini'):
    config.read('LanLauncher.ini')
    usernamecache = config.get('LanLauncher', 'username')
    plutoniumfold = config.get('LanLauncher', 'plutonium folder')
    waw = config.get('LanLauncher', 'world at war folder')
    bo1 = config.get('LanLauncher', 'black ops 1 folder')
    bo2 = config.get('LanLauncher', 'black ops 2 folder')
    mw3 = config.get('LanLauncher', 'modernwarfare 3 folder')

else:
    if os.path.exists(wawtest):
        waw = wawtest

    if os.path.exists(bo1test):
        bo1 = bo1test

    if os.path.exists(bo2test):
        bo2 = bo2test

    if os.path.exists(mw3test):
        mw3 = mw3test
        
    if os.path.exists(cdir + winuser + plutoapp):
        plutoniumfold = cdir + winuser + plutoapp
        
    config['LanLauncher'] = {'username': usernamecache,
    'plutonium folder': plutoniumfold,
    'world at war folder': waw,
    'black ops 1 folder': bo1,
    'black ops 2 folder': bo2,
    'modernwarfare 3 folder': mw3}
    with open('LanLauncher.ini', 'w') as configfile:
        config.write(configfile)
        
sg.set_options(font=('Cambria', 10))
sg.theme('DarkAmber')
layout_main = [ 
            [sg.Text('Username', pad=((0, 1), (0, 0))), sg.InputText(usernamecache, key='usernamecache7', pad=((81, 5), (0, 0))), sg.Radio("Zombies", key='zombies', default=True, group_id='game_mode', pad=((56, 0), (0, 0)))],
            [sg.Text('Plutonium folder', pad=((0, 1), (0, 0))), sg.InputText(plutoniumfold, key='pluto7', pad=((42, 0), (0, 0))), sg.FolderBrowse(key='pluto7'), sg.Radio("Multiplayer", key='multiplayer', group_id='game_mode', pad=((0, 0), (0, 0)))],
            [sg.Text('World at War folder', pad=((0, 1), (0, 0))), sg.InputText(waw, key='waw7', pad=((26, 0), (0, 0))), sg.FolderBrowse(key='waw7'), sg.Button('Launch T4')],
            [sg.Text('Black ops folder  ', pad=((0, 1), (0, 0))), sg.InputText(bo1, key='bo17', pad=((40, 0), (0, 0))), sg.FolderBrowse(key='bo17'), sg.Button('Launch T5')],
            [sg.Text('Black ops II folder  ', pad=((0, 1), (0, 0))), sg.InputText(bo2, key='bo27', pad=((29, 0), (0, 0))), sg.FolderBrowse(key='bo27'), sg.Button('Launch T6')],
            [sg.Text('ModernWarfare 3 Folder', pad=((0, 1), (0, 0))), sg.InputText(mw3, key='mw37', pad=((0, 0), (0, 0))), sg.FolderBrowse(key='mw37'), sg.Button('Launch IW5')],
            [sg.Button('Close', pad=((0, 1), (0, 0))), sg.Button('Help'), sg.Text('Made By JugAndDoubleTap', pad=((54, 0), (0, 0))), sg.Text(version_num, pad=((270, 0), (0, 0)))] ]


def helpwin():
    layout_help = [ [sg.Text('The folder refers to the location at which your game is installed.\nFor example, if you have it installed to C:/games/pluto_t6_fullgame\nThen that is what you would either type or browse for.')],
    [sg.Button('Close')]]
    window_help = sg.Window('LanLauncher', layout_help, icon=('LAN.ico'))
    helpa = 0
    while (helpa == 0):
        event, values = window_help.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            helpa += 1
            window_help.close()

def error_pluto():
    layout_pluto = [ [sg.Text('The selection in field "Plutonium folder" does not contain valid\nPlutonium launcher data.')],
    [sg.Button('Close')]]
    window_pluto = sg.Window('LanLauncher', layout_pluto, icon=('LAN.ico'))
    error1 = 0
    while (error1 == 0):
        event, values = window_pluto.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            error1 += 1
            window_pluto.close()

def error_t4():
    layout_t4 = [ [sg.Text('The selection in field "World at war folder" does not contain valid\nWorld at War game data.')],
    [sg.Button('Close')]]
    window_t4 = sg.Window('LanLauncher', layout_t4, icon=('LAN.ico'))
    error2 = 0
    while (error2 == 0):
        event, values = window_t4.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            error2 += 1
            window_t4.close()

def error_t5():
    layout_t5 = [ [sg.Text('The selection in field "Black ops folder" does not contain valid\nBlack ops game data.')],
    [sg.Button('Close')]]
    window_t5 = sg.Window('LanLauncher', layout_t5, icon=('LAN.ico'))
    error3 = 0
    while (error3 == 0):
        event, values = window_t5.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            error3 += 1
            window_t5.close()

def error_t6():
    layout_t6 = [ [sg.Text('The selection in field "Black ops II folder" does not contain valid\nBlack ops II game data.')],
    [sg.Button('Close')]]
    window_t6 = sg.Window('LanLauncher', layout_t6, icon=('LAN.ico'))
    error4 = 0
    while (error4 == 0):
        event, values = window_t6.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            error4 += 1
            window_t6.close()

def error_iw5():
    layout_iw5 = [ [sg.Text('The selection in field "ModernWarfare 3 folder" does not contain valid\nModern Warfare 3 game data.')],
    [sg.Button('Close')]]
    window_iw5 = sg.Window('LanLauncher', layout_iw5, icon=('LAN.ico'))
    error5 = 0
    while (error5 == 0):
        event, values = window_iw5.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            error5 += 1
            window_iw5.close()

def error_name():
    layout_name = [ [sg.Text('The username you selected is invalid.')],
    [sg.Button('Close')]]
    window_name = sg.Window('LanLauncher', layout_name, icon=('LAN.ico'))
    error6 = 0
    while (error6 == 0):
        event, values = window_name.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            error6 += 1
            window_name.close()

window_main = sg.Window('LanLauncher', layout_main, icon=('LAN.ico'))
mainwindow = 0
while (mainwindow == 0):
    event, values = window_main.read()
    if event == sg.WIN_CLOSED or event == 'Close':
        mainwindow += 1
        window_main.close()
 
    if event == 'Launch T4':
        usernamecache = values['usernamecache7']
        plutoniumfold = values['pluto7']
        waw = values['waw7']
        bo1 = values['bo17']
        bo2 = values['bo27']
        mw3 = values['mw37']
        config.read('LanLauncher.ini')
        config.set('LanLauncher', 'username', usernamecache)
        config.set('LanLauncher', 'world at war folder', waw)
        config.set('LanLauncher', 'black ops 1 folder', bo1)
        config.set('LanLauncher', 'black ops 2 folder', bo2)
        config.set('LanLauncher', 'modernwarfare 3 folder', mw3)
        config.set('LanLauncher', 'plutonium folder', plutoniumfold)
        with open('LanLauncher.ini', 'w') as configfile2:
            config.write(configfile2)
        if usernamecache != "":
            
            if os.path.exists(plutoniumfold + "/bin/plutonium-bootstrapper-win32.exe"):
                
                if os.path.isfile(waw + "/main/iw_00.iwd"):
                    
                    if values['multiplayer'] == True:
                        t4_arg = "t4mp"
                    waw = f'"{waw}"'
                    usernamecache = f'"{usernamecache}"'
                    tmp_bat = plutoniumfold + "/tmp.bat"
                    if os.path.exists(tmp_bat):
                        os.remove(tmp_bat)
                    with open(tmp_bat, 'w') as f:
                        f.write("@echo off\n")
                        f.write(f"{exe_path} {t4_arg} {waw} {name_arg} {usernamecache} {lan_arg}")     
                    p = subprocess.Popen(tmp_bat, cwd=plutoniumfold)
                    stdout, stderr = p.communicate()
                else:
                    error_t4()
            else:
                error_pluto()
        else:
            error_name()
            
    elif event == 'Launch T5':
        usernamecache = values['usernamecache7']
        plutoniumfold = values['pluto7']
        waw = values['waw7']
        bo1 = values['bo17']
        bo2 = values['bo27']
        mw3 = values['mw37']
        config.read('LanLauncher.ini')
        config.set('LanLauncher', 'username', usernamecache)
        config.set('LanLauncher', 'world at war folder', waw)
        config.set('LanLauncher', 'black ops 1 folder', bo1)
        config.set('LanLauncher', 'black ops 2 folder', bo2)
        config.set('LanLauncher', 'modernwarfare 3 folder', mw3)
        config.set('LanLauncher', 'plutonium folder', plutoniumfold)
        with open('LanLauncher.ini', 'w') as configfile2:
            config.write(configfile2)
        if usernamecache != "":
            
            if os.path.exists(plutoniumfold + "/bin/plutonium-bootstrapper-win32.exe"):
                
                if os.path.isfile(bo1 + "/main/iw_00.iwd"):
                    
                    if values['multiplayer'] == True:
                        t5_arg = "t5mp"
                    bo1 = f'"{bo1}"'
                    usernamecache = f'"{usernamecache}"'
                    tmp_bat = plutoniumfold + "/tmp.bat"
                    if os.path.exists(tmp_bat):
                        os.remove(tmp_bat)
                    with open(tmp_bat, 'w') as f:
                        f.write("@echo off\n")
                        f.write(f"{exe_path} {t5_arg} {bo1} {name_arg} {usernamecache} {lan_arg}")                        
                    p = subprocess.Popen(tmp_bat, cwd=plutoniumfold)
                    stdout, stderr = p.communicate()
                else:
                    error_t5()
            else:
                error_pluto()
        else:
            error_name()
        
    elif event == 'Launch T6':
        usernamecache = values['usernamecache7']
        plutoniumfold = values['pluto7']
        waw = values['waw7']
        bo1 = values['bo17']
        bo2 = values['bo27']
        mw3 = values['mw37']
        config.read('LanLauncher.ini')
        config.set('LanLauncher', 'username', usernamecache)
        config.set('LanLauncher', 'world at war folder', waw)
        config.set('LanLauncher', 'black ops 1 folder', bo1)
        config.set('LanLauncher', 'black ops 2 folder', bo2)
        config.set('LanLauncher', 'modernwarfare 3 folder', mw3)
        config.set('LanLauncher', 'plutonium folder', plutoniumfold)
        with open('LanLauncher.ini', 'w') as configfile2:
            config.write(configfile2)
        if usernamecache != "":
            
            if os.path.exists(plutoniumfold + "/bin/plutonium-bootstrapper-win32.exe"):
                
                if os.path.isfile(bo2 + "/zone/all/base.ipak"):
                    
                    if values['multiplayer'] == True:
                        t6_arg = "t6mp"
                    bo2 = f'"{bo2}"'
                    usernamecache = f'"{usernamecache}"'
                    tmp_bat = plutoniumfold + "/tmp.bat"
                    if os.path.exists(tmp_bat):
                        os.remove(tmp_bat)
                    with open(tmp_bat, 'w') as f:
                        f.write("@echo off\n")
                        f.write(f"{exe_path} {t6_arg} {bo2} {name_arg} {usernamecache} {lan_arg}") 
                    p = subprocess.Popen(tmp_bat, cwd=plutoniumfold)
                    stdout, stderr = p.communicate()
                else:
                    error_t6()
            else:
                error_pluto()
        else:
            error_name()


    elif event == 'Launch IW5':
        usernamecache = values['usernamecache7']
        plutoniumfold = values['pluto7']
        waw = values['waw7']
        bo1 = values['bo17']
        bo2 = values['bo27']
        mw3 = values['mw37']
        config.read('LanLauncher.ini')
        config.set('LanLauncher', 'username', usernamecache)
        config.set('LanLauncher', 'world at war folder', waw)
        config.set('LanLauncher', 'black ops 1 folder', bo1)
        config.set('LanLauncher', 'black ops 2 folder', bo2)
        config.set('LanLauncher', 'modernwarfare 3 folder', mw3)
        config.set('LanLauncher', 'plutonium folder', plutoniumfold)
        with open('LanLauncher.ini', 'w') as configfile2:
            config.write(configfile2)
        if usernamecache != "":
            
            if os.path.exists(plutoniumfold + "/bin/plutonium-bootstrapper-win32.exe"):
                
                if os.path.isfile(mw3 + "/main/iw_00.iwd"):

                    
                    mw3 = f'"{mw3}"'
                    usernamecache = f'"{usernamecache}"'
                    tmp_bat = plutoniumfold + "/tmp.bat"
                    if os.path.exists(tmp_bat):
                        os.remove(tmp_bat)
                    with open(tmp_bat, 'w') as f:
                        f.write("@echo off\n")
                        f.write(f"{exe_path} {iw5_arg} {mw3} {name_arg} {usernamecache} {lan_arg}")
                    p = subprocess.Popen(tmp_bat, cwd=plutoniumfold)
                    stdout, stderr = p.communicate()
                else:
                    error_iw5()
            else:
                error_pluto()
        else:
            error_name()
            
    elif event == 'Help':
        helpwin()
