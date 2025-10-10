import os, subprocess
import LLWindows as LLW

def Launch(GENERAL, settings, modSelection):
    exePath = "/bin/plutonium-bootstrapper-win32.exe"

    if not settings[GENERAL["USERNAME"]] != "":
        LLW.ErrorWindow(GENERAL, settings, "username")
        # cancels launching if the username is blank
        return
    
    if not os.path.exists(settings[GENERAL["PLUTONIUMINSTANCE"]] + exePath):
        LLW.ErrorWindow(GENERAL, settings, "plutonium")
        # cancels launching if the directory for plutonium is invalid
        return

    match settings[GENERAL["GAMEID"]]:
        case "World at War":
            settings[GENERAL["ACTIVEGAME"]] = settings[GENERAL["WAW"]]
            if not os.path.isfile(settings[GENERAL["ACTIVEGAME"]] + "/main/iw_00.iwd"):
                LLW.ErrorWindow(GENERAL, settings, "T4")
                # cancels launching if the directory for world at war is invalid
                return
            
        case "Black ops":
            settings[GENERAL["ACTIVEGAME"]] = settings[GENERAL["BO1"]]
            if not os.path.isfile(settings[GENERAL["ACTIVEGAME"]] + "/main/iw_00.iwd"):
                LLW.ErrorWindow(GENERAL, settings, "T5")
                # cancels launching if the directory for black ops is invalid
                return

        case "Black ops II":
            settings[GENERAL["ACTIVEGAME"]] = settings[GENERAL["BO2"]]
            if not os.path.isfile(settings[GENERAL["ACTIVEGAME"]] + "/zone/all/base.ipak"):
                LLW.ErrorWindow(GENERAL, settings, "T6")
                # cancels launching if the directory for black ops 2 is invalid
                return

        case "Modern Warfare 3":
            settings[GENERAL["ACTIVEGAME"]] = settings[GENERAL["MW3"]]
            if not os.path.isfile(settings[GENERAL["ACTIVEGAME"]] + "/main/iw_00.iwd"):
                LLW.ErrorWindow(GENERAL, settings, "IW5")
                # cancels launching if the directory for modern warfare 3 is invalid
                return

    # default launch with no mods selected
    launchPlutonium = rf'"{settings[GENERAL["PLUTONIUMINSTANCE"]] + exePath}" {settings[GENERAL["MODEID"]]} "{settings[GENERAL["ACTIVEGAME"]]}" +name "{settings[GENERAL["USERNAME"]]}" -lan'

    if modSelection != '':
        if not settings[GENERAL["GAMEID"]] == settings[GENERAL["MODID"]]:
            LLW.ErrorWindow(GENERAL, settings, "wrongGame")
            # cancels launching if the mod is selected for the wrong game
            return
        else:
            # sets to launch with a mod
            modSelection = fr'"mods/{modSelection}"'
            launchPlutonium = rf'"{settings[GENERAL["PLUTONIUMINSTANCE"]] + exePath}" {settings[GENERAL["MODEID"]]} "{settings[GENERAL["ACTIVEGAME"]]}" +name "{settings[GENERAL["USERNAME"]]}" -lan +set fs_game {modSelection}'

    subprocess.Popen(launchPlutonium, cwd=settings[GENERAL["PLUTONIUMINSTANCE"]])


def LaunchServer(GENERAL, settings, modSelection, configSelection, port):
    exePath = "/bin/plutonium-bootstrapper-win32.exe"

    
    if not os.path.exists(settings[GENERAL["PLUTONIUMINSTANCE"]] + exePath):
        LLW.ErrorWindow(GENERAL, settings, "plutonium")
        # cancels launching if the directory for plutonium is invalid
        return

    match settings[GENERAL["SERVERID"]]:
        case "World at War":
            settings[GENERAL["ACTIVEGAME"]] = settings[GENERAL["WAW"]]
            if settings[GENERAL["WAWSERVMULT"]] == False:
                settings[GENERAL["WAWSERVMULT"]] == "+set zombiemode 1"
            else:
                settings[GENERAL["WAWSERVMULT"]] == ""
            if not os.path.isfile(settings[GENERAL["ACTIVEGAME"]] + "/main/iw_00.iwd"):
                LLW.ErrorWindow(GENERAL, settings, "T4")
                # cancels launching if the directory for world at war is invalid
                return
            
        case "Black ops":
            settings[GENERAL["ACTIVEGAME"]] = settings[GENERAL["BO1"]]
            if not os.path.isfile(settings[GENERAL["ACTIVEGAME"]] + "/main/iw_00.iwd"):
                LLW.ErrorWindow(GENERAL, settings, "T5")
                # cancels launching if the directory for black ops is invalid
                return

        case "Black ops II":
            if not os.path.exists(settings[GENERAL["PLUTONIUMINSTANCE"]] + '/storage/t6/gamesettings'):
                LLW.ErrorWindow(GENERAL, settings, "prompt to download gamesettings")
                return
            
            settings[GENERAL["ACTIVEGAME"]] = settings[GENERAL["BO2"]]
            if not os.path.isfile(settings[GENERAL["ACTIVEGAME"]] + "/zone/all/base.ipak"):
                LLW.ErrorWindow(GENERAL, settings, "T6")
                # cancels launching if the directory for black ops 2 is invalid
                return

        case "Modern Warfare 3":
            settings[GENERAL["ACTIVEGAME"]] = settings[GENERAL["MW3"]]
            if not os.path.isfile(settings[GENERAL["ACTIVEGAME"]] + "/main/iw_00.iwd"):
                LLW.ErrorWindow(GENERAL, settings, "IW5")
                # cancels launching if the directory for modern warfare 3 is invalid
                return

    # default launch with no mods selected
    launchServer = rf'"{settings[GENERAL["PLUTONIUMINSTANCE"]] + exePath}" {settings[GENERAL["MODEID"]]} "{settings[GENERAL["ACTIVEGAME"]]}" -lan -dedicated {settings[GENERAL["WAWSERVMULT"]]} +exec {configSelection} +set net_port {port} +map_rotate'

    if modSelection != '':
        if not settings[GENERAL["SERVERID"]] == settings[GENERAL["MODID"]]:
            LLW.ErrorWindow(GENERAL, settings, "wrongGameServer")
            # cancels launching if the mod is selected for the wrong game
            return
        else:
            # sets to launch with a mod
            modSelection = fr'"mods/{modSelection}"'
            launchServer = rf'"{settings[GENERAL["PLUTONIUMINSTANCE"]] + exePath}" {settings[GENERAL["MODEID"]]} "{settings[GENERAL["ACTIVEGAME"]]}" -lan -dedicated {settings[GENERAL["WAWSERVMULT"]]} +set fs_game {modSelection} +exec {configSelection} +set net_port {port} +map_rotate'

    subprocess.Popen(launchServer, cwd=settings[GENERAL["PLUTONIUMINSTANCE"]])
