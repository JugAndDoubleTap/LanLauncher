import PySimpleGUI as sg
import os
import subprocess
import configparser

version_num = "V1.1.7"

exe_path = r"\bin\plutonium-bootstrapper-win32.exe"
usernamecache = r""
waw = r""
bo1 = r""
bo2 = r""
iw5 = r""
plutoniumfold = r""

config = configparser.ConfigParser()

if os.path.isfile('LanLauncher.ini'):
    config.read('LanLauncher.ini')
    usernamecache = config.get('LanLauncher', 'username')
    plutoniumfold = config.get('LanLauncher', 'plutonium folder')
    waw = config.get('LanLauncher', 'world at war folder')
    bo1 = config.get('LanLauncher', 'black ops 1 folder')
    bo2 = config.get('LanLauncher', 'black ops 2 folder')
    iw5 = config.get('LanLauncher', 'modernwarfare 3 folder')

else:
    if os.path.exists("C:/Program Files (x86)/Steam/steamapps/common/Call of Duty World at War"):
        waw = r"C:/Program Files (x86)/Steam/steamapps/common/Call of Duty World at War"

    if os.path.exists("C:/Program Files (x86)/Steam/steamapps/common/Call of Duty Black Ops"):
        bo1 = r"C:/Program Files (x86)/Steam/steamapps/common/Call of Duty Black Ops"

    if os.path.exists("C:/Program Files (x86)/Steam/steamapps/common/Call of Duty Black Ops II"):
        bo2 = r"C:/Program Files (x86)/Steam/steamapps/common/Call of Duty Black Ops II"

    if os.path.exists("C:/Program Files (x86)/Steam/steamapps/common/Call of Duty Modern Warfare 3"):
        iw5 = r"C:/Program Files (x86)/Steam/steamapps/common/Call of Duty Modern Warfare 3"
        
    if os.path.exists("C:/Users/" + os.getlogin() + r"/AppData/Local/Plutonium"):
        plutoniumfold = r"C:/Users/" + os.getlogin() + r"/AppData/Local/Plutonium"
        
    config['LanLauncher'] = {'username': usernamecache,
    'plutonium folder': plutoniumfold,
    'world at war folder': waw,
    'black ops 1 folder': bo1,
    'black ops 2 folder': bo2,
    'modernwarfare 3 folder': iw5}
    with open('LanLauncher.ini', 'w') as configfile:
        config.write(configfile)
        
sg.set_options(font=('Cambria', 10))
sg.theme('DarkAmber')
layout_main = [ [sg.Text('Username', pad=((0, 0), (0, 0)))],
            [sg.InputText(usernamecache, key='usernamecache7', pad=((0, 0), (0, 0))), sg.Radio(r"SP/ZM", key='zombies', default=True, group_id='game_mode', pad=((61, 0), (0, 0)))],
            [sg.Text('Plutonium folder', pad=((0, 0), (0, 0)))],
            [sg.InputText(plutoniumfold, key='pluto7', pad=((0, 0), (0, 0))), sg.FolderBrowse(key='pluto7'), sg.Radio("MP", key='multiplayer', group_id='game_mode', pad=((0, 0), (0, 0)))],
            [sg.Text('World at War folder', pad=((0, 0), (0, 0)))],    
            [sg.InputText(waw, key='waw7', pad=((0, 0), (0, 0))), sg.FolderBrowse(key='waw7'), sg.Button('Launch T4')],
            [sg.Text('Black ops folder  ', pad=((0, 0), (0, 0)))],
            [sg.InputText(bo1, key='bo17', pad=((0, 0), (0, 0))), sg.FolderBrowse(key='bo17'), sg.Button('Launch T5')],
            [sg.Text('Black ops II folder  ', pad=((0, 0), (0, 0)))],
            [sg.InputText(bo2, key='bo27', pad=((0, 0), (0, 0))), sg.FolderBrowse(key='bo27'), sg.Button('Launch T6')],
            [sg.Text('ModernWarfare 3 Folder', pad=((0, 0), (0, 0)))],
            [sg.InputText(iw5, key='iw5', pad=((0, 0), (0, 0))), sg.FolderBrowse(key='mw37'), sg.Button('Launch IW5')],
            [sg.Button('Close', pad=((0, 0), (0, 0))), sg.Button('Help'), sg.Text('Made By JugAndDoubleTap', pad=((0, 0), (0, 0))), sg.Text(version_num, pad=((44, 0), (0, 0)))] ]

 
def write2config():
    usernamecache = values['usernamecache7']
    plutoniumfold = values['pluto7']
    waw = values['waw7']
    bo1 = values['bo17']
    bo2 = values['bo27']
    iw5 = values['iw5']
    config.read('LanLauncher.ini')
    config.set('LanLauncher', 'username', usernamecache)
    config.set('LanLauncher', 'world at war folder', waw)
    config.set('LanLauncher', 'black ops 1 folder', bo1)
    config.set('LanLauncher', 'black ops 2 folder', bo2)
    config.set('LanLauncher', 'modernwarfare 3 folder', iw5)
    config.set('LanLauncher', 'plutonium folder', plutoniumfold)
    with open('LanLauncher.ini', 'w') as configfile2:
        config.write(configfile2)
       
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
        write2config()
        if values['usernamecache7'] != "":
            
            if os.path.exists(values['pluto7'] + "/bin/plutonium-bootstrapper-win32.exe"):
                
                if os.path.isfile(values['waw7'] + "/main/iw_00.iwd"):
                    
                    if values['multiplayer'] == True:
                        t_arg = "t4mp"
                    if values['multiplayer'] == False:
                        t_arg = "t4sp"
                    waw = values['waw7']
                    usernamecache = values['usernamecache7']
                    launchwaw = fr'"{waw}"'
                    usernamecachelaunch = fr'"{usernamecache}"'
                    p = subprocess.Popen(rf"{plutoniumfold + exe_path} {t_arg} {launchwaw} +name {usernamecachelaunch} -lan", cwd=plutoniumfold)
                    stdout, stderr = p.communicate()
                else:
                    error_t4()
            else:
                error_pluto()
        else:
            error_name()
            
    elif event == 'Launch T5':
        write2config()
        if values['usernamecache7'] != "":
            
            if os.path.exists(values['pluto7'] + "/bin/plutonium-bootstrapper-win32.exe"):
                
                if os.path.isfile(values['bo17'] + "/main/iw_00.iwd"):
                    
                    if values['multiplayer'] == True:
                        t_arg = "t5mp"
                    if values['multiplayer'] == False:
                        t_arg = "t5sp"
                    bo1 = values['bo17']
                    usernamecache = values['usernamecache7']
                    launchbo1 = fr'"{bo1}"'
                    usernamecachelaunch = fr'"{usernamecache}"'
                    p = subprocess.Popen(rf"{plutoniumfold + exe_path} {t_arg} {launchbo1} +name {usernamecachelaunch} -lan", cwd=plutoniumfold)
                    stdout, stderr = p.communicate()
                else:
                    error_t5()
            else:
                error_pluto()
        else:
            error_name()
        
    elif event == 'Launch T6':
        write2config()
        if values['usernamecache7'] != "":
            
            if os.path.exists(values['pluto7'] + "/bin/plutonium-bootstrapper-win32.exe"):
                
                if os.path.isfile(values['bo27'] + "/zone/all/base.ipak"):
                    
                    if values['multiplayer'] == True:
                        t_arg = "t6mp"
                    if values['multiplayer'] == False:
                        t_arg = "t6zm"
                    bo2 = values['bo27']
                    usernamecache = values['usernamecache7']
                    launchbo2 = fr'"{bo2}"'
                    usernamecachelaunch = fr'"{usernamecache}"'
                    p = subprocess.Popen(rf"{plutoniumfold + exe_path} {t_arg} {launchbo2} +name {usernamecachelaunch} -lan", cwd=plutoniumfold)
                    stdout, stderr = p.communicate()
                else:
                    error_t6()
            else:
                error_pluto()
        else:
            error_name()


    elif event == 'Launch IW5':
        write2config()
        if values['usernamecache7'] != "":
            
            if os.path.exists(values['pluto7'] + "/bin/plutonium-bootstrapper-win32.exe"):
                
                if os.path.isfile(values['iw5'] + "/main/iw_00.iwd"):
                    t_arg = "iw5mp"
                  #  if values['multiplayer'] == True:
                  #      t_arg = "iw5mp"
                  #  if values['multiplayer'] == False:
                  #      t_arg = "iw5sp"
                    iw5 = values['iw5']
                    usernamecache = values['usernamecache7']
                    launchiw5 = fr'"{iw5}"'
                    usernamecachelaunch = fr'"{usernamecache}"'
                    p = subprocess.Popen(rf"{plutoniumfold + exe_path} {t_arg} {launchiw5} +name {usernamecachelaunch} -lan", cwd=plutoniumfold)
                    stdout, stderr = p.communicate()
                else:
                    error_iw5()
            else:
                error_pluto()
        else:
            error_name()
            
    elif event == 'Help':
        helpwin()
