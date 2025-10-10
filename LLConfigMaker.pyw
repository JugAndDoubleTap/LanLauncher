import os

def GenerateConfig(GENERAL, settings, serverid, configName, selectedMap, multiplayerMode, prer4516):
    configType = ''

    match serverid:
        case "World at War":
            path = settings[GENERAL["PLUTONIUMINSTANCE"]] + fr'/storage/t4/main/'
            configType = "t4"
        case "Black ops":
            path = settings[GENERAL["PLUTONIUMINSTANCE"]] + fr'/storage/t5/main/'
            configType = "t5"
        case "Black ops II":
            path = settings[GENERAL["PLUTONIUMINSTANCE"]] + fr'/storage/t6/main/'
            configType = "t6"
        case "Modern Warfare 3":
            path = settings[GENERAL["PLUTONIUMINSTANCE"]] + fr'/storage/iw5/main/'
            configType = "iw5"
            multiplayerMode = True


    if multiplayerMode:
        configName = "mp_" + configName.replace(" ", "_")
        configType = configType + "mp"
    else:
        configName = "zm_" + configName.replace(" ", "_")
        configType = configType + "zm"

    if prer4516:
        configName = configName + "_Pre_r4516"


    match configType:
        case "t4mp":
            mapRotation = 'set sv_maprotationcurrent ""'
        case "t4zm":
            mapRotation = 'set sv_maprotationcurrent ""'
        case "t5mp":
            mapRotation = ''
        case "t5zm":
            mapRotation = ''
        case "t6mp":
            mapRotation = 'map_rotate'
        case "t6zm":
            mapRotation = 'map_rotate'
        case "iw5mp":
            mapRotation = ''


    cfg = rf'''set sp_minplayers 1
    set g_password ""
    set rcon_rate_limit "500"

    rconWhitelistAdd "127.0.0.1"
    rconWhitelistAdd "192.168.0.7"
    rconWhitelistAdd "10.0.0.12"
    rconWhitelistAdd "172.16.8.7"

    set sv_maxclients "4"
    set sv_maxRate "25000"
    set sv_pure "0"
    set scr_game_spectatetype "1"
    set g_gravity "800"
    set g_speed "190"
    set bullet_penetration_affected_by_team false
    set perk_weapRateEnhanced false

    set rate "25000"
    set g_antilag "1"
    set sv_fps "20"

    set sv_allowDownload "0"
    set sv_wwwDownload "0"
    set sv_wwwBaseURL ""
    set sv_wwwDlDisconnected "0"

    set g_log "{configName}.log"
    set g_logSync "2"
    set logfile "2"
    set sv_kickBanTime "300"

    set fire_audio_random_max_duration "1000"
    set fire_audio_repeat_duration "1500"
    set fire_spread_probability "0"
    set fire_stage1_burn_time "3000"
    set fire_stage2_burn_time "0"
    set fire_stage3_burn_time "0"
    set fire_world_damage "20"
    set fire_world_damage_duration "8"
    set fire_world_damage_rate "0.25"
    set flareDisableEffects "0"

    demo_enabled 0
               
    set sv_mapRotation "{selectedMap}"
    {mapRotation}'''

    with open(f'{path}{configName}.cfg', 'w') as file:
        file.write(cfg)



        





