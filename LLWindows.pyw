import os, wget, subprocess, sys, configparser, shutil, socket
import FreeSimpleGUI as sg
from zipfile import ZipFile
import LanLauncher as LL
import LLGameStarter as LLG
import LLConfigMaker as LLC

def MainWindow(GENERAL, settings):
    configList = ['']
    modList = ['']

    sg.theme(settings[GENERAL["THEME"]])
    sg.set_options(font=('Cambria', 10))
    serverTab = [
    [sg.Text('Select game to host server for', size=(23, 1)), sg.Text('', size=(7, 1)), sg.Button('Refresh config list'), sg.Button('Deselect config')],
    [
        sg.InputCombo(['World at War', 'Black ops II', 'Modern Warfare 3'], key='gameselectserver', enable_events=True, readonly=True),
        sg.Text('', size=(9, 1)),
        sg.Text(f'Available configs for {settings[GENERAL["GAMEID"]]}', key='configtitle')
    ],
    [
        sg.Column(
            [   
                [sg.Radio("ZM", key='serverzombies', default=True, group_id='gamemodeserver')],
                [sg.Radio("MP", key='servermultiplayer', group_id='gamemodeserver')],
                [sg.Text("Port number")],
                [sg.InputText('5000', key="port", size=(10, 2)), sg.Text('', size=(18,1))],
                [sg.Text("Your local IP address")],
                [sg.Text(socket.gethostbyname(socket.gethostname()), font=("Cambria", 10, "bold"))],
            ],
            vertical_alignment='top',
            pad=(0, 0)
        ),
        sg.Listbox(configList, size=(30, 10), key='configlist'),
    ],
    [sg.Text("")],
    [sg.Text('', size=(48, 1)), sg.Button('Launch server')],
    [sg.Text('', size=(35, 1)), sg.Button('Delete config '), sg.Button('Make a config')],
]
    settingsTab = [[sg.Text('Theme Selection')],
                               [sg.InputCombo(['DarkAmber', 
                                               'DarkPurple2', 
                                               'DarkBlack', 
                                               'DarkTeal10', 
                                               'LightBrown9', 
                                               'SandyBeach', 
                                               'DarkTanBlue'], key='themeselect', enable_events=True, readonly=True)]]
                              


    modsTab = [[sg.Text('Select game to see mods for', size=(22,1)), sg.Text('', size=(10,1)),sg.Button('Refresh mod list'), sg.Button('Deselect mod ')],
                            [sg.InputCombo(['World at War', 'Black ops', 'Black ops II', 'Modern Warfare 3'], key='gameselectmod', enable_events=True, readonly=True),sg.Text('', size=(9,1)),   sg.Text(f'Available mods for {settings[GENERAL["GAMEID"]]}', key='modtitle')               ],
                            [sg.Text('', size=(30,1)), sg.Listbox(modList, size=(30, 10), key='modlist'), sg.Text('')],
                            [sg.Text('', size=(30,1)), sg.Text('Install mods here')],
                            [sg.Text('', size=(30,1)), sg.InputText('Mod in Zip, Rar, 7z, or exe', size=(21,1), key='modtoinstall'), sg.FileBrowse('Browse', key='modtoinstall', file_types=(("Zip Files", "*.zip"), ("Rar Files", "*.rar"), ("7z Files", "*.7z"), ("Executable Files", "*.exe")))],
                            [sg.Text('', size=(38,1)),sg.Button('Delete mod '), sg.Button('Install mod')]
               ]
    
    mainTab = [[sg.Text('Username', pad=((0, 0), (0, 0)))],
                [sg.InputText(settings[GENERAL["USERNAME"]], key='username', pad=((0, 0), (0, 0))), sg.Radio(r"SP/ZM", key='zombies', default=True, group_id='gamemode', pad=((61, 0), (0, 0)))],
                [sg.Text('Plutonium folder (AppData)', pad=((0, 0), (0, 0)))],
                [sg.InputText(settings[GENERAL["PLUTONIUMINSTANCE"]], key='plutoniuminstance', pad=((0, 0), (0, 0))), sg.FolderBrowse(key='plutoniumfolder'), sg.Radio("MP", key='multiplayer', group_id='gamemode', pad=((0, 0), (0, 0)))],
                [sg.Text('World at War folder', pad=((0, 0), (0, 0)))],    
                [sg.InputText(settings[GENERAL["WAW"]], key='waw', pad=((0, 0), (0, 0))), sg.FolderBrowse(key='waw'), sg.Button('Launch T4')],
                [sg.Text('Black ops folder  ', pad=((0, 0), (0, 0)))],
                [sg.InputText(settings[GENERAL["BO1"]], key='bo1', pad=((0, 0), (0, 0))), sg.FolderBrowse(key='bo1'), sg.Button('Launch T5')],
                [sg.Text('Black ops II folder  ', pad=((0, 0), (0, 0)))],
                [sg.InputText(settings[GENERAL["BO2"]], key='bo2', pad=((0, 0), (0, 0))), sg.FolderBrowse(key='bo2'), sg.Button('Launch T6')],
                [sg.Text('ModernWarfare 3 folder', pad=((0, 0), (0, 0)))],
                [sg.InputText(settings[GENERAL["MW3"]], key='mw3', pad=((0, 0), (0, 0))), sg.FolderBrowse(key='mw3'), sg.Button('Launch IW5')],
               ]

    mainLayout = [[sg.TabGroup([[sg.Tab('Main', mainTab), sg.Tab('Mods', modsTab), sg.Tab('Lan Server', serverTab), sg.Tab('Misc', settingsTab)]])],
                [sg.Button('Close'), sg.Button('Save Settings'), sg.Button('Update'), sg.Button('Help'), sg.Text('Made By JugAndDoubleTap', pad=((0, 0), (0, 0))), sg.Text('V' + settings[GENERAL["VERSIONNUM"]], pad=((20, 0), (0, 0)))] 
                ]
    mainWindow = sg.Window(r'LanLauncher (for Plutonium)', mainLayout, icon=('LAN.ico'))
    windowLoop = True
    # loop so that the window stays running for button presses and other GUI features
    while (windowLoop == True):
        event, values = mainWindow.read()
        # switch statement for GUI button actions
        match event:
            case sg.WIN_CLOSED:
                windowLoop = False
                mainWindow.close()
            case "Close":
                LL.SaveToINI(GENERAL, settings, values)
                windowLoop = False
                mainWindow.close()
            case "Save Settings":
                LL.SaveToINI(GENERAL, settings, values)

            case "themeselect":
                if values['themeselect'] != '':
                    settings[GENERAL["THEME"]] = values['themeselect']
                    LL.SaveToINI(GENERAL, settings, values)
                    LL.LoadFromINI(GENERAL, settings)
                    windowLoop = False
                    mainWindow.close()
                    MainWindow(GENERAL, settings)
            case "Help":
                ErrorWindow(GENERAL, settings, "help")
            case "Update":
                UpdateWindow(GENERAL, settings, values)
            case "Launch T4":
                if values["multiplayer"] == True:
                    settings[GENERAL["MODEID"]] = 't4mp'
                else:
                    settings[GENERAL["MODEID"]] = 't4sp'

                settings[GENERAL["GAMEID"]] = 'World at War'
                LL.SaveToINI(GENERAL, settings, values)
                LL.LoadFromINI(GENERAL, settings)
                if values["modlist"] != []:
                    LLG.Launch(GENERAL, settings, values["modlist"][0])
                else:
                    LLG.Launch(GENERAL, settings, '')

            case "Launch T5":
                if values["multiplayer"] == True:
                    settings[GENERAL["MODEID"]] = 't5mp'
                else:
                    settings[GENERAL["MODEID"]] = 't5sp'

                settings[GENERAL["GAMEID"]] = 'Black ops'
                LL.SaveToINI(GENERAL, settings, values)
                LL.LoadFromINI(GENERAL, settings)
                if values["modlist"] != []:
                    LLG.Launch(GENERAL, settings, values["modlist"][0])
                else:
                    LLG.Launch(GENERAL, settings, '')

            case "Launch T6":
                if values["multiplayer"] == True:
                    settings[GENERAL["MODEID"]] = 't6mp'
                else:
                    settings[GENERAL["MODEID"]] = 't6zm'

                settings[GENERAL["GAMEID"]] = 'Black ops II'
                LL.SaveToINI(GENERAL, settings, values)
                LL.LoadFromINI(GENERAL, settings)
                if values["modlist"] != []:
                    LLG.Launch(GENERAL, settings, values["modlist"][0])
                else:
                    LLG.Launch(GENERAL, settings, '')

            case "Launch IW5":
                if values["multiplayer"] == True:
                    settings[GENERAL["MODEID"]] = 'iw5mp'
                else:
                    settings[GENERAL["MODEID"]] = 'iw5mp'

                settings[GENERAL["GAMEID"]] = 'Modern Warfare 3'
                LL.SaveToINI(GENERAL, settings, values)
                LL.LoadFromINI(GENERAL, settings)
                if values["modlist"] != []:
                    LLG.Launch(GENERAL, settings, values["modlist"][0])
                else:
                    LLG.Launch(GENERAL, settings, '')

            case "gameselectmod":
                match values['gameselectmod']:
                    case 'World at War':
                        path = values["plutoniuminstance"] + fr'\storage\t4\mods'
                        settings[GENERAL["MODID"]] = 'World at War'
                        mainWindow['modtitle'].update(f'Available mods for {settings[GENERAL["MODID"]]}')

                    
                
                    case 'Black ops':
                        path = values["plutoniuminstance"] + fr'\storage\t5\mods'
                        settings[GENERAL["MODID"]] = 'Black ops'
                        mainWindow['modtitle'].update(f'Available mods for {settings[GENERAL["MODID"]]}')

                    
                
                    case 'Black ops II':
                        path = values["plutoniuminstance"] + fr'\storage\t6\mods'
                        settings[GENERAL["MODID"]] = 'Black ops II'
                        mainWindow['modtitle'].update(f'Available mods for {settings[GENERAL["MODID"]]}')

                    
                
                    case 'Modern Warfare 3':
                        path = values["plutoniuminstance"] + fr'\storage\iw5\mods'
                        settings[GENERAL["MODID"]] = 'Modern Warfare 3'
                        mainWindow['modtitle'].update(f'Available mods for {settings[GENERAL["MODID"]]}')

                
                modList = []
                mainWindow['modlist'].update(values=modList)
                if os.path.exists(path):
                    modList = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
                    mainWindow['modlist'].update(values=modList)

                if not os.path.exists(path):
                    os.mkdir(path)

            case "Deselect mod " | "Refresh mod list":
                match settings[GENERAL["MODID"]]:
                    case 'World at War':
                        path = values["plutoniuminstance"] + fr'/storage/t4/mods'
                    case 'Black ops':
                        path = values["plutoniuminstance"] + fr'/storage/t5/mods'
                    case 'Black ops II':
                        path = values["plutoniuminstance"] + fr'/storage/t6/mods'
                    case 'Modern Warfare 3':
                        path = values["plutoniuminstance"] + fr'/storage/iw5/mods'

                modList = []
                mainWindow['modlist'].update(values=[])
                if os.path.exists(path):
                    modList = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
                    mainWindow['modlist'].update(values=modList)

            case "Install mod":
                abort = False
                if os.path.isdir(os.getcwd() + "/7z"):
                    match settings[GENERAL["MODID"]]:
                        case "World at War":
                            path = values["plutoniuminstance"] + fr'/storage/t4/mods'
                        case "Black ops":
                            path = values["plutoniuminstance"] + fr'/storage/t5/mods'
                        case "Black ops II":
                            path = values["plutoniuminstance"] + fr'/storage/t6/mods'
                        case "Modern Warfare 3":
                            path = values["plutoniuminstance"] + fr'/storage/iw5/mods'
                        case _:
                            abort = True


                else:
                    abort = True
                    ErrorWindow(GENERAL, settings, '7z')
                if abort == False: 
                    result = LL.ExtractArchive(path, values['modtoinstall'])
                    match result:
                        case "standard mod format":
                            if os.path.exists(path):
                                modList = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
                                mainWindow['modlist'].update(values=modList)
                        case "not standard mod format":
                            ErrorWindow(GENERAL, settings, result)
                        case "not supported extension":
                            ErrorWindow(GENERAL, settings, result)
                        case "failed to install mod":
                            ErrorWindow(GENERAL, settings, result)


            case "Delete mod ":
                abort = False
                match settings[GENERAL["MODID"]]:
                    case "World at War":
                        path = values["plutoniuminstance"] + fr'/storage/t4/mods'
                    case "Black ops":
                        path = values["plutoniuminstance"] + fr'/storage/t5/mods'
                    case "Black ops II":
                        path = values["plutoniuminstance"] + fr'/storage/t6/mods'
                    case "Modern Warfare 3":
                        path = values["plutoniuminstance"] + fr'/storage/iw5/mods'
                    case _:
                        abort = True
                if abort != True:
                    modToDelete = ''
                    try:
                        modToDelete = values['modlist'][0]
                    except Exception as e:
                        print(e)
                    if modToDelete != '':
                        try:
                            shutil.rmtree(path + "/" + modToDelete)
                        except Exception as e:
                            print(e)
                    
                        mainWindow['modlist'].update(values=[])
                        if os.path.exists(path):
                            modList = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
                            mainWindow['modlist'].update(values=modList)
                    else:
                        ErrorWindow(GENERAL, settings, 'noMod')

            case "gameselectserver":
                match values['gameselectserver']:
                    case "World at War":
                        path = values["plutoniuminstance"] + fr'\storage\t4\main'
                        settings[GENERAL["SERVERID"]] = 'World at War'
                        mainWindow['configtitle'].update(f'Available configs for {settings[GENERAL["SERVERID"]]}')


                
                    case "Black ops":
                        path = values["plutoniuminstance"] + fr'\storage\t5\main'
                        settings[GENERAL["SERVERID"]] = 'Black ops'
                        mainWindow['configtitle'].update(f'Available configs for {settings[GENERAL["SERVERID"]]}')


                        
                    case "Black ops II":
                        path = values["plutoniuminstance"] + fr'\storage\t6\main'
                        settings[GENERAL["SERVERID"]] = 'Black ops II'
                        mainWindow['configtitle'].update(f'Available configs for {settings[GENERAL["SERVERID"]]}')


                        
                    case "Modern Warfare 3":
                        path = values["plutoniuminstance"] + fr'\storage\iw5\main'
                        settings[GENERAL["SERVERID"]] = 'Modern Warfare 3'
                        mainWindow['configtitle'].update(f'Available configs for {settings[GENERAL["SERVERID"]]}')

                configlist = []
                mainWindow['configlist'].update(values=configlist)

                if os.path.exists(path):
                    configlist = [f for f in os.listdir(path) if f.endswith('.cfg')]
                    mainWindow['configlist'].update(values=configlist)

                if not os.path.exists(path):
                    os.mkdir(path)

            case "Deselect config" | "Refresh config list":
                abort = False
                match values["gameselectserver"]:
                    

                    case "World at War":
                        path = values["plutoniuminstance"] + fr'\storage\t4\main'
                        settings[GENERAL["SERVERID"]] = 'World at War'
                        mainWindow['configtitle'].update(f'Available configs for {settings[GENERAL["SERVERID"]]}')


                        
                    case "Black ops":
                        path = values["plutoniuminstance"] + fr'\storage\t5\main'
                        settings[GENERAL["SERVERID"]] = 'Black ops'
                        mainWindow['configtitle'].update(f'Available configs for {settings[GENERAL["SERVERID"]]}')


                        
                    case "Black ops II":
                        path = values["plutoniuminstance"] + fr'\storage\t6\main'
                        settings[GENERAL["SERVERID"]] = 'Black ops II'
                        mainWindow['configtitle'].update(f'Available configs for {settings[GENERAL["SERVERID"]]}')


                        
                    case "Modern Warfare 3":
                        path = values["plutoniuminstance"] + fr'\storage\iw5\main'
                        settings[GENERAL["SERVERID"]] = 'Modern Warfare 3'
                        mainWindow['configtitle'].update(f'Available configs for {settings[GENERAL["SERVERID"]]}')

                    case _:
                        abort = True
                if abort != True:
                    configList = []
                    mainWindow['configlist'].update(values=configList)

                    if os.path.exists(path):
                        configList = [f for f in os.listdir(path) if f.endswith('.cfg')]
                        mainWindow['configlist'].update(values=configList)

            case "Delete config ":
                abort = False
                match values["gameselectserver"]:

                    case "World at War":
                        path = values["plutoniuminstance"] + fr'/storage/t4/main'
                    case "Black ops":
                        path = values["plutoniuminstance"] + fr'/storage/t5/main'
                    case "Black ops II":
                        path = values["plutoniuminstance"] + fr'/storage/t6/main'
                    case "Modern Warfare 3":
                        path = values["plutoniuminstance"] + fr'/storage/iw5/main'
                    case _:
                        abort = True
                if abort != True:
                    cfgToDelete = ''
                    try:
                        cfgToDelete = values['configlist'][0]
                    except Exception as e:
                        print(e)
                    if cfgToDelete != '':
                        try:
                            os.remove(path + "/" + cfgToDelete)
                        except Exception as e:
                            print(e)
                    
                        mainWindow['configlist'].update(values=[])
                        if os.path.exists(path):
                            configlist = [f for f in os.listdir(path) if f.endswith('.cfg')]
                            mainWindow['configlist'].update(values=configlist)
                    else:
                        ErrorWindow(GENERAL, settings, "noCFG")
            case "Make a config":
                LL.SaveToINI(GENERAL, settings, values)
                LL.LoadFromINI(GENERAL, settings)
                MakeConfigWindow(GENERAL, settings, values["gameselectserver"], values["servermultiplayer"], mainWindow)

            case "Launch server":
                match settings[GENERAL["SERVERID"]]:
                    case "World at War":
                        if values["servermultiplayer"] == True:
                            settings[GENERAL["WAWSERVMULT"]] = True
                            settings[GENERAL["MODEID"]] = 't4mp'
                        else:
                            settings[GENERAL["WAWSERVMULT"]] = False
                            settings[GENERAL["MODEID"]] = 't4sp'
                    case "Black ops":
                        if values["servermultiplayer"] == True:
                            settings[GENERAL["MODEID"]] = 't5mp'
                        else:
                            settings[GENERAL["MODEID"]] = 't5sp'
                    case "Black ops II":
                        if values["servermultiplayer"] == True:
                            settings[GENERAL["MODEID"]] = 't6mp'
                        else:
                            settings[GENERAL["MODEID"]] = 't6zm'
                    case "Modern Warfare 3":
                        settings[GENERAL["MODEID"]] = 'iw5mp'

                LL.SaveToINI(GENERAL, settings, values)
                LL.LoadFromINI(GENERAL, settings)
                if values["configlist"] == []:
                    ErrorWindow(GENERAL, settings, "noCFG")
                else:
                    if values["modlist"] != []:
                        LLG.LaunchServer(GENERAL, settings, values["modlist"][0], values["configlist"][0], values["port"])
                    else:
                        LLG.LaunchServer(GENERAL, settings, '', values["configlist"][0], values["port"])



def ErrorWindow(GENERAL, settings, errorType):
    sg.theme(settings[GENERAL["THEME"]])
    sg.set_options(font=('Cambria', 10))
    message = ''

    errorLayout = [ [sg.Text(message, key='message')],
    [sg.Button('Close')]]

    match errorType:
        case "help":
            message = 'The folder refers to the location at which your game is installed.\nFor example, if you have it installed to C:/games/pluto_t6_fullgame\nThen that is what you would either type or browse for.'
        case "username":
            message = 'The username you selected is invalid.'
        case "T4":
            message = f'The specified folder "{settings[GENERAL["WAW"]]}" \ndoes not contain valid World at War game data.'
        case "T5":
            message = f'The specified folder "{settings[GENERAL["BO1"]]}" \ndoes not contain valid Black ops game data.'
        case "T6":
            message = f'The specified folder "{settings[GENERAL["BO2"]]}" \ndoes not contain valid Black ops II game data.'
        case "IW5":
            message = f'The specified folder "{settings[GENERAL["MW3"]]}" \ndoes not contain valid Modern Warfare 3 game data.'
        case "plutonium":
            message = f'The specified folder "{settings[GENERAL["PLUTONIUMINSTANCE"]]}" \ndoes not contain valid Plutonium launcher data.'
        case "wrongGame":
            message = f'You have selected a mod for {settings[GENERAL["MODID"]]}, \nbut you tried to launch {settings[GENERAL["GAMEID"]]}.'
        case "wrongGameServer":
            message = f'You have selected a mod for {settings[GENERAL["MODID"]]}, \nbut you tried to launch a {settings[GENERAL["SERVERID"]]} server.'
        case "noMod":
            message = 'You do not have a mod selected.'
        case "noCFG":
            message = 'You do not have a config selected.'
        case "not supported extension":
            message = 'The mod you tried to install does not have a supported file extension.'
        case "not standard mod format":
            message = 'The mod you tried to install does not use the standard mod file structure,\nand was not installed.'
        case "failed to install mod":
            message = 'Failed to install the mod.'
        case "7z":
            message = 'You currently do not have 7-zip installed in the LanLauncher Directory,\nand cannot install archived mods using this GUI,\nwould you like to download 7-zip?\n(Requires an active internet connection)'
            errorLayout = [ [sg.Text(message, key="message")],
                            [sg.Button('Yes'), sg.Button('No')]]
        case "7zSuccess":
            message = '7-zip successfully downloaded and installed.'
        case "7zFailDown":
            message = '7-zip was not successfully downloaded.'
        case "7zFailInstall":
            message = '7-zip was not successfully installed.'
        case "multiConfig":
            message = 'Making configs for multiplayer is currently not supported.\nHowever you can still host a multiplayer server if you manually make a config'
        case "custom empty":
            message = 'You selected other, but left the text entry empty.'
        case "must name config":
            message = 'You must set a config name.'
        case "prompt to download gamesettings":
            message = 'You currently do not have the main server configuration files that are needed for Black ops II to host properly.\nWould you like to download them? (Requires an active internet connection)'
            errorLayout = [ [sg.Text(message, key="message")],
                            [sg.Button('Yes '), sg.Button('No')]]
        case "downloaded main configs":
            message = 'Black ops II main configuration files successfully downloaded.'

            
    errorWindow = sg.Window('LanLauncher', errorLayout, icon=('LAN.ico'), finalize=True)
    errorWindow['message'].update(message)
    windowLoop = True
    while (windowLoop == True):
        event, values = errorWindow.read()
        if event == sg.WIN_CLOSED or event == 'Close' or event == 'No':
            windowLoop = False
            errorWindow.close()
        elif event == 'Yes':
            abort = False
            windowLoop = False
            errorWindow.close()
            try:
                wget.download(r"https://raw.githubusercontent.com/JugAndDoubleTap/LanLauncher/main/7z.zip")
            except Exception as e:
                print(e)
                ErrorWindow(GENERAL, settings, '7zFailDown')
                abort = True
            if abort != True:
                try: 
                    ZipFile('7z.zip').extractall(os.getcwd())
                except Exception as e:
                    print(e)
                    ErrorWindow(GENERAL, settings, '7zFailInstall')
                    abort = True
                if abort != True:
                    try: 
                        os.remove(os.getcwd() + "/7z.zip")
                    except Exception as e:
                        print(e)
                    ErrorWindow(GENERAL, settings, '7zSuccess')
        elif event == 'Yes ':
            windowLoop = False
            errorWindow.close()
            LL.DownloadMainConfigs(GENERAL, settings)


                               

def UpdateWindow(GENERAL, settings, values):
    sg.theme(settings[GENERAL["THEME"]])
    sg.set_options(font=('Cambria', 10))
    config = configparser.ConfigParser()
    updatetext = 'There are no updates currently available.'
    update_num = r"0"
    try:
        wget.download(r"https://raw.githubusercontent.com/JugAndDoubleTap/LanLauncher/main/update.ini")
        config.read('update.ini')
        update_num = config.get('Update', 'update number')
    except Exception:
        updatetext = 'Could not check for latest version.'

    if settings[GENERAL["VERSIONNUM"]] < update_num:
        updatetext = f'An update is available,\nwould you like to update to version {update_num}?'
        updatewinlay = [[sg.Text(updatetext)],
                        [sg.Button('Cancel'), sg.Button('Update')]]
    elif settings[GENERAL["VERSIONNUM"]] >= update_num:
        updatewinlay = [[sg.Text(updatetext)],
                        [sg.Button('Close')]]

    update_win = sg.Window("LanLauncher", updatewinlay, icon=('LAN.ico'))
    mainWindow = True
    update = True
    while update == True:
        event, values = update_win.read()
        if event == 'Close':
            try:
                os.remove('update.ini')
                update = False
                update_win.close()
            except Exception:
                update = False
                update_win.close()
        elif event == sg.WIN_CLOSED or event == 'Cancel':
            try:
                os.remove('update.ini')
                update = False
                update_win.close()
            except Exception:
                update = False
                update_win.close()
        elif event == 'Update':
            os.remove('update.ini')
            LL.SaveToINI(GENERAL, settings, values)
            update = False
            update_win.close()
            mainWindow = False
            mainWindow.close()
            subprocess.Popen('LLUpdater.exe', shell=True)
            sys.exit()



def MakeConfigWindow(GENERAL, settings, serverid, multiplayerMode, mainWindow):
    prer4516 = False
    if multiplayerMode == True:
        ErrorWindow(GENERAL, settings, "multiConfig")
        return


    match serverid:
        case "World at War":
            mapSelection =          sg.Column([
                                    [sg.Text("Map selector")],
                                    [sg.Radio("Nacht der Untoten", key="mapnacht" , group_id='mapgroup', default=True)],
                                    [sg.Radio("Verrückt", key="mapverru", group_id='mapgroup')],
                                    [sg.Radio("Shi No Numa", key="mapshi", group_id='mapgroup')],
                                    [sg.Radio("Der Riese", key="mapder", group_id='mapgroup')],                              
                                    [sg.Radio("Other", key="mapother", group_id='mapgroup')],
                                    [sg.Text("Input map name below for custom maps\n(Other must be selected)", font=("Cambria", 8, "bold"))],
                                    [sg.InputText("", key="mapothertext")]], vertical_alignment='top')
        case "Black ops":
            mapSelection =          sg.Column([
                                    [sg.Text("Map selector")],
                                    [sg.Radio("Kino der Toten", key="mapkino" , group_id='mapgroup', default=True)],
                                    [sg.Radio("Five", key="mapfive", group_id='mapgroup')],
                                    [sg.Radio("Ascension", key="mapasc", group_id='mapgroup')],
                                    [sg.Radio("Call of the Dead", key="mapcall", group_id='mapgroup')],
                                    [sg.Radio("Shangri-La", key="mapcall", group_id='mapgroup')],
                                    [sg.Radio("Moon", key="mapcall", group_id='mapgroup')],
                                    [sg.Radio("Dead ops Arcade", key="mapops", group_id='mapgroup')],
                                    [sg.Radio("Nacht der Untoten", key="mapnacht" , group_id='mapgroup')],
                                    [sg.Radio("Verrückt", key="mapverru", group_id='mapgroup')],
                                    [sg.Radio("Shi No Numa", key="mapshi", group_id='mapgroup')],
                                    [sg.Radio("Der Riese", key="mapder", group_id='mapgroup')]], vertical_alignment='top')
        case "Black ops II":
            mapSelection =          [
                                    sg.Column([
                                    #[sg.Text("Pre r4516")],
                                    #[sg.Radio("Yes", key="prer4516", group_id="r4516")],
                                    #[sg.Radio("No", group_id="r4516", default=True)],
                                    [sg.Text("Map selector")],
                                    [sg.Radio("Tranzit", key="mapbus" , group_id='mapgroup', default=True)],
                                    [sg.Radio("Nuke Town", key="mapnuke", group_id='mapgroup')],
                                    [sg.Radio("Die Rise", key="maprise", group_id='mapgroup')],
                                    [sg.Radio("Mob of the Dead", key="mapmob", group_id='mapgroup')],
                                    [sg.Radio("Buried", key="mapburied", group_id='mapgroup')],
                                    [sg.Radio("Origins", key="maporigins", group_id='mapgroup')]], vertical_alignment='top'),
            
                                    sg.Column([
                                    [sg.Text(" ")],
                                    [sg.Radio("Farm Survival", key="mapfarm", group_id='mapgroup')],
                                    [sg.Radio("Town Survival", key="maptown", group_id='mapgroup')],
                                    [sg.Radio("Bus Depot Survival", key="mapdepot", group_id='mapgroup')]], vertical_alignment='bottom'),
                                    ]
            
            
            if not os.path.exists(settings[GENERAL["PLUTONIUMINSTANCE"]] + '/storage/t6/gamesettings'):
                ErrorWindow(GENERAL, settings, "prompt to download gamesettings")
                return
        case "Modern Warfare 3":
            mapSelection = []
            ErrorWindow(GENERAL, settings, "multiConfig")
            return
        case _:
            return


    cofigLayout = [

    [

            mapSelection,

    ],

        [sg.Column([ [sg.Text("")],
            [sg.Text("Name of config without suffix or prefix\nE.G.: DieRise", font=("Cambria", 8, "bold"))],
            [sg.InputText("", key="configname")],
            [sg.Text("")]]),],

    [sg.Button('Close'), sg.Button("Make config")]]
    cofigWindow = sg.Window('LanLauncher', cofigLayout, icon=('LAN.ico'), finalize=True)
    windowLoop = True
    while (windowLoop == True):
        event, values = cofigWindow.read()
        match event:
            case sg.WIN_CLOSED | 'Close':
                windowLoop = False
                cofigWindow.close()
            case 'Make config':
                abort = False

                if values["configname"] == '':
                    ErrorWindow(GENERAL, settings, "must name config")
                    abort = True


                
                match serverid:
                    case "World at War":
                        if values["mapnacht"]:
                            selectedMap = "map nazi_zombie_prototype"
                        elif values["mapverru"]:
                            selectedMap = "map nazi_zombie_asylum"
                        elif values["mapshi"]:
                            selectedMap = "map nazi_zombie_sumpf"
                        elif values["mapder"]:
                            selectedMap = "map nazi_zombie_factory"
                        elif values["mapother"]:
                            if values["mapothertext"] == '':
                                ErrorWindow(GENERAL, settings, "custom empty")
                                abort = True
                            else:
                                selectedMap = "map " + values["mapothertext"]

                    case "Black ops":
                        pass

                    case "Black ops II":
                        #temp solution to make prer4516 never true, as I do not think that I want it included in final release
                        if 1==3: #values["prer4516"]:
                            prer4516 = True
                            if values["mapbus"]:
                                selectedMap = "exec zm_classic_transit.cfg map zm_transit"
                            elif values["mapfarm"]:
                                selectedMap = "exec zm_standard_farm map zm_transit"
                            elif values["maptown"]:
                                selectedMap = "exec zm_standard_town.cfg map zm_transit"
                            elif values["mapdepot"]:
                                selectedMap = "exec zm_standard_transit.cfg map zm_transit"
                            elif values["mapnuke"]:
                                selectedMap = "exec zm_standard_nuked.cfg map zm_nuked"
                            elif values["maprise"]:
                                selectedMap = "exec zm_classic_rooftop.cfg map zm_highrise"
                            elif values["mapmob"]:
                                selectedMap = "exec zm_classic_prison.cfg map zm_prison"
                            elif values["mapburied"]:
                                selectedMap = "exec zm_classic_processing.cfg map zm_buried"
                            elif values["maporigins"]:
                                selectedMap = "exec zm_classic_tomb.cfg map zm_tomb"
                        else:
                            if values["mapbus"]:
                                selectedMap = "execgts zm_classic_transit.cfg map zm_transit"
                            elif values["mapfarm"]:
                                selectedMap = "execgts zm_standard_farm map zm_transit"
                            elif values["maptown"]:
                                selectedMap = "execgts zm_standard_town.cfg map zm_transit"
                            elif values["mapdepot"]:
                                selectedMap = "execgts zm_standard_transit.cfg map zm_transit"
                            elif values["mapnuke"]:
                                selectedMap = "execgts zm_standard_nuked.cfg map zm_nuked"
                            elif values["maprise"]:
                                selectedMap = "execgts zm_classic_rooftop.cfg map zm_highrise"
                            elif values["mapmob"]:
                                selectedMap = "execgts zm_classic_prison.cfg map zm_prison"
                            elif values["mapburied"]:
                                selectedMap = "execgts zm_classic_processing.cfg map zm_buried"
                            elif values["maporigins"]:
                                selectedMap = "execgts zm_classic_tomb.cfg map zm_tomb"

                    case "Modern Warfare 3":
                        pass
                
                if abort != True:
                    LLC.GenerateConfig(GENERAL, settings, serverid, values["configname"], selectedMap, multiplayerMode, prer4516)

                match serverid:
                    case "World at War":
                        path = settings[GENERAL["PLUTONIUMINSTANCE"]] + fr'/storage/t4/main'
                    case "Black ops":
                        path = settings[GENERAL["PLUTONIUMINSTANCE"]] + fr'/storage/t5/main'
                    case "Black ops II":
                        path = settings[GENERAL["PLUTONIUMINSTANCE"]] + fr'/storage/t6/main'
                    case "Modern Warfare 3":
                        path = settings[GENERAL["PLUTONIUMINSTANCE"]] + fr'/storage/iw5/main'

                configList = []
                mainWindow['configlist'].update(values=configList)

                if os.path.exists(path):
                    configList = [f for f in os.listdir(path) if f.endswith('.cfg')]
                    mainWindow['configlist'].update(values=configList)

                windowLoop = False
                cofigWindow.close()
