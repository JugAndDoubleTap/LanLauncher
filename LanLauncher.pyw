import subprocess, os, shutil, argparse, configparser, glob, wget
import LLWindows as LLW
import LLGameStarter as LLG

def main():
    # sets up argument parser for commandline argument usage
    parser = argparse.ArgumentParser(description='LanLauncher, for when you want to launch plutonium without an active internet connection!')
    parser.add_argument('-name', type=str, help='username that you will use example: "JugAndDoubleTap",  default is the one you set in the GUI', default=None)
    parser.add_argument('-plutoniumdir', type=str, help='location at which your plutonium folder is stored example: "C:/user/(name)/appdata/local/plutonium", by default uses the one that was set in the GUI, Must be used with -nogui', default=None)
    parser.add_argument('-mode', type=str, help='mode selector, either input "MP" or "ZM", MUST be used with -nogui', default="ZM")
    parser.add_argument('-gamedir', type=str, help='location at which your game is stored example: "C:/games/cod world at war", by default uses the one that was set in the GUI, MUST be used with -nogui', default=None)
    parser.add_argument('-gameid', type=str, help='accepts game id to set the game, such as T4, T5, T6, IW5, MUST be used with -nogui', default=None)
    parser.add_argument('-nogui', action='store_true', help='launches with no gui')
    args = parser.parse_args()

    # dictionary of all settings variable names, to use as enums for array indexing
    GENERAL = {
        "VERSIONNUM" : 0,
        "THEME" : 1,
        "USERNAME" : 2,
        "PLUTONIUMINSTANCE" : 3,
        "WAW" : 4,
        "BO1" : 5,
        "BO2" : 6, 
        "MW3" : 7,
        "MODID" : 8,
        "GAMEID" : 9,
        "SERVERID" : 10,
        "MODEID" : 11,
        "NOGUI" : 12,
        "WAWSERVMULT" : 13,
        "ACTIVEGAME" : 14
    }
    # initilizes array size based on dictionary, and sets all indexes to '' (empty) to start off
    settings = [''] * len(GENERAL)

    # assigning items to array index via dictionary example for me
    #settingsArray[GENERAL["WAW"]] = "/games/general/waw/"
    #print(settingsArray[GENERAL["WAW"]])
    # output : /games/general/waw/
    
    # sets the version number
    settings[GENERAL["VERSIONNUM"]] = "2.0.0"
    # sets default theme
    settings[GENERAL["THEME"]] = "DarkAmber"


    if os.path.isfile("LanLauncher.ini"):
        # load cfg function
        LoadFromINI(GENERAL, settings)

    # this is only used when PLUTONIUMINSTANCE is not set, such as when running for the first time, or if it is deleted from the ini
    if settings[GENERAL["PLUTONIUMINSTANCE"]] == '':
        # sets the plutonium instance to the default installation location for plutonium if PLUTONIUMINSTANCE is Null
        if os.path.exists(r"C:/Users/" + os.getlogin() + r"/AppData/Local/Plutonium"):
           settings[GENERAL["PLUTONIUMINSTANCE"]] = r"C:/Users/" + os.getlogin() + r"/AppData/Local/Plutonium"

    if args.nogui == False:
        # normal launch
        LLW.MainWindow(GENERAL, settings)
    else:
        # no gui launch
        settings[GENERAL["NOGUI"]] = "True"

        # if a custom location to a plutonium instance is provided in the cmd args then this is used 
        if args.plutoniumdir != None:
            settings[GENERAL["PLUTONIUMINSTANCE"]] = args.plutoniumdir
        # if a name is provided using commandline arguments then this is used
        if args.name != None:
            settings[GENERAL["USERNAME"]] = args.name
        match args.gameid.upper():
            case "T4":
                if args.mode.upper() == "MP":
                    settings[GENERAL["MODEID"]] = "t4mp"
                else:
                     settings[GENERAL["MODEID"]] = "t4sp"

                settings[GENERAL["GAMEID"]] = "World at War"
                # sets gamedir if a custom location is provdied
                if args.gamedir != None:
                    settings[GENERAL["WAW"]] = args.gamedir
                LLG.Launch(GENERAL, settings, '')
            case "T5":
                if args.mode.upper() == "MP":
                    settings[GENERAL["MODEID"]] = "t5mp"
                else:
                    settings[GENERAL["MODEID"]] = "t5sp"
                
                settings[GENERAL["GAMEID"]] = "Black ops"
                # sets gamedir if a custom location is provdied
                if args.gamedir != None:
                    settings[GENERAL["BO1"]] = args.gamedir
                LLG.Launch(GENERAL, settings, '')
            case "T6":
                if args.mode.upper() == "MP":
                    settings[GENERAL["MODEID"]] = "t6mp"
                else:
                    settings[GENERAL["MODEID"]] = "t6zm"

                settings[GENERAL["GAMEID"]] = "Black ops II"
                # sets gamedir if a custom location is provdied
                if args.gamedir != None:
                    settings[GENERAL["BO2"]] = args.gamedir
                LLG.Launch(GENERAL, settings, '')
            case "IW5":
                settings[GENERAL["MODEID"]] = "iw5mp"
                settings[GENERAL["GAMEID"]] = "Modern Warfare 3"
                # sets gamedir if a custom location is provdied
                if args.gamedir != None:
                    settings[GENERAL["MW3"]] = args.gamedir
                LLG.Launch(GENERAL, settings, '')
            case _:
                print("No valid game selected.")
        

def SaveToINI(GENERAL, settings, values):
        config = configparser.ConfigParser()

        if not os.path.isfile("LanLauncher.ini"):
            config['LanLauncher'] = {'username': str(values["username"]),
            'plutonium folder': str(values["plutoniuminstance"]),
            'world at war folder': str(values["waw"]),
            'black ops 1 folder': str(values["bo1"]),
            'black ops 2 folder': str(values["bo2"]),
            'modernwarfare 3 folder': str(values["mw3"]),
            'theme': settings[GENERAL["THEME"]]}
            with open('LanLauncher.ini', 'w') as INIFILE:
                config.write(INIFILE)
        else:
            config.read('LanLauncher.ini')
            config.set('LanLauncher', 'username', str(values["username"]))
            config.set('LanLauncher', 'world at war folder', str(values["waw"]))
            config.set('LanLauncher', 'black ops 1 folder', str(values["bo1"]))
            config.set('LanLauncher', 'black ops 2 folder', str(values["bo2"]))
            config.set('LanLauncher', 'modernwarfare 3 folder', str(values["mw3"]))
            config.set('LanLauncher', 'plutonium folder', str(values["plutoniuminstance"]))
            config.set('LanLauncher', 'theme', settings[GENERAL["THEME"]])
            with open('LanLauncher.ini', 'w') as INIFILE:
                config.write(INIFILE)

def LoadFromINI(GENERAL, settings):
        config = configparser.ConfigParser()

        config.read('LanLauncher.ini')
        try:
            settings[GENERAL["USERNAME"]] = config.get('LanLauncher', 'username')
        except Exception as e:
            print(e)
            config.set('LanLauncher', 'username', settings[GENERAL["USERNAME"]])
        try:
            settings[GENERAL["PLUTONIUMINSTANCE"]] = config.get('LanLauncher', 'plutonium folder')
        except Exception as e:
            print(e)
            config.set('LanLauncher', 'plutonium folder', settings[GENERAL["PLUTONIUMINSTANCE"]])
        try:
            settings[GENERAL["WAW"]] = config.get('LanLauncher', 'world at war folder')
        except Exception as e:
            print(e)
            config.set('LanLauncher', 'world at war folder', settings[GENERAL["WAW"]])
        try:
            settings[GENERAL["BO1"]] = config.get('LanLauncher', 'black ops 1 folder')
        except Exception as e:
            print(e)
            config.set('LanLauncher', 'black ops 1 folder', settings[GENERAL["BO1"]])
        try:
            settings[GENERAL["BO2"]] = config.get('LanLauncher', 'black ops 2 folder')
        except Exception as e:
            print(e)
            config.set('LanLauncher', 'black ops 2 folder', settings[GENERAL["BO2"]])
        try:
            settings[GENERAL["MW3"]] = config.get('LanLauncher', 'modernwarfare 3 folder')
        except Exception as e:
            print(e)
            config.set('LanLauncher', 'modernwarfare 3 folder', settings[GENERAL["MW3"]])
        try:
            settings[GENERAL["THEME"]] = config.get('LanLauncher', 'theme')
        except Exception as e:
            print(e)
            config.set('LanLauncher', 'theme', settings[GENERAL["THEME"]])


def ExtractArchive(modfolder, mapexe):
    fourLetterExtension = mapexe[-4:]
    threeLetterExtension = mapexe[-3:]


    if threeLetterExtension.lower() == ".7z":
        fileName = mapexe[:-3]
    else:
        match fourLetterExtension.lower():
            case ".zip":
                fileName = os.path.basename(mapexe)[:-4]
            case ".rar":
                fileName = os.path.basename(mapexe)[:-4]
            case ".exe":
                fileName = os.path.basename(mapexe)[:-4]
            case _:
                return "not supported extension"
    try:
        mapexecon = f'"{mapexe}"'
        modfoldercon = f'"{modfolder}"'
        modfoldercontemp = f'"{modfolder}/TEMP"'
        modfolderFileName = os.path.join(modfolder, fileName.replace(" ", "_"))
        sevz = rf'"{os.getcwd()}\7z\7z.exe"'
        

        if not os.path.exists(modfolder + "/TEMP"):
            os.mkdir(modfolder + "/TEMP")
        else:
            shutil.rmtree(modfolder + "/TEMP")
            os.mkdir(modfolder + "/TEMP")


        subprocess.Popen(fr'{sevz} x -y -o{modfoldercontemp} {mapexecon}', creationflags=0x00000010, shell=True ,cwd=os.getcwd() + r"/7z").wait()

        if os.path.isfile(modfolder + "/TEMP/mod.ff") or os.path.isdir(modfolder + "/TEMP/scripts") or os.path.isdir(modfolder + "/TEMP/images") or os.path.isdir(modfolder + "/TEMP/maps"):
            if glob.glob(os.path.join(modfolder, "TEMP", "*.lua")) or glob.glob(os.path.join(modfolder, "TEMP", "*.gsc")):
                shutil.rmtree(modfolder + "/TEMP")
                return "not standard mod format"
                
            shutil.rmtree(modfolder + "/TEMP")

            os.mkdir(modfolderFileName)
            subprocess.Popen(fr'{sevz} x -y -o"{modfolderFileName}" {mapexecon}', creationflags=0x00000010, shell=True ,cwd=os.getcwd() + r"/7z").wait()

            if os.path.exists(modfolder + '/$PLUGINSDIR'):
                shutil.rmtree(modfolder +  '/$PLUGINSDIR')
        else:
            if glob.glob(os.path.join(modfolder, "TEMP", "*", "*.lua")) or glob.glob(os.path.join(modfolder, "TEMP", "*", "*.gsc")):
                shutil.rmtree(modfolder + "/TEMP")
                return "not standard mod format"
                
            shutil.rmtree(modfolder + "/TEMP")
            subprocess.Popen(fr'{sevz} x -y -o{modfoldercon} {mapexecon}', creationflags=0x00000010, shell=True ,cwd=os.getcwd() + r"/7z").wait()
            if os.path.exists(modfolder + '/$PLUGINSDIR'):
                shutil.rmtree(modfolder +  '/$PLUGINSDIR')

    except Exception as e:
            print(e)
            return "failed to install mod"
    
    return "standard mod format"




def DownloadMainConfigs(GENERAL, settings):
    downloadList = [
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/conf.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/ctf.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/dem.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/dm.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/dom.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/gun.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/hq.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/koth.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/oic.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/oneflag.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/sas.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/sd.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/shrp.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/tdm.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/zm_classic_prison.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/zm_classic_processing.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/zm_classic_rooftop.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/zm_classic_tomb.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/zm_classic_transit.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/zm_cleansed_diner.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/zm_cleansed_street.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/zm_grief_cellblock.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/zm_grief_farm.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/zm_grief_street.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/zm_grief_town.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/zm_grief_transit.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/zm_standard_farm.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/zm_standard_nuked.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/zm_standard_town.cfg",
                    r"https://raw.githubusercontent.com/xerxes-at/T6ServerConfigs/refs/heads/master/localappdata/Plutonium/storage/t6/gamesettings/zm_standard_transit.cfg"]

    
    destinationList = [
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/conf.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/ctf.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/dem.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/dm.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/dom.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/gun.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/hq.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/koth.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/oic.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/oneflag.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/sas.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/sd.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/shrp.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/tdm.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/zm_classic_prison.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/zm_classic_processing.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/zm_classic_rooftop.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/zm_classic_tomb.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/zm_classic_transit.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/zm_cleansed_diner.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/zm_cleansed_street.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/zm_grief_cellblock.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/zm_grief_farm.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/zm_grief_street.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/zm_grief_town.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/zm_grief_transit.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/zm_standard_farm.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/zm_standard_nuked.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/zm_standard_town.cfg",
                    fr"{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings/zm_standard_transit.cfg"]
    try:
        os.mkdir(fr'{settings[GENERAL["PLUTONIUMINSTANCE"]]}/storage/t6/gamesettings')
        downloadItems = list(zip(downloadList, destinationList))
        for downloadUrl, destinationPath in downloadItems:
            wget.download(downloadUrl, destinationPath)
        LLW.ErrorWindow(GENERAL, settings, "downloaded main configs")
    except Exception as e:
        print(e)       

if __name__ == "__main__":
    main()