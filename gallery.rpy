default mc_name = "Zycris"
default callmommy = 0
default persistent.mcname = "Zycris"
label gallery:
    $ galleryevents = [
    #0     #1                   #2              #3
    ["C2", "G0",                "cat_extra_iru",          2 ], #0
    ["C2", "G50",                "g_50",       persistent.g_50_unlock], #1
    ["C2", "G51",                "g_51",       persistent.g_51_unlock], #2
    ["C2", "G52",                "g_52",       persistent.g_52_unlock], #3
    ["C3", "G53",                "g_53",       persistent.g_53_unlock], #4
    ["C3", "G54",                "g_54",       persistent.g_54_unlock], #5
    ["C3", "G55",                "g_55",       persistent.g_55_unlock], #6
    ["C3", "G56",                "g_56",       persistent.g_56_unlock], #7
    ["C3", "G57",                "g_57",       persistent.g_57_unlock], #8
    ["C3", "G58",                "g_58",       persistent.g_58_unlock], #9
    ]
    scene black
    call screen replaygalleryv2()
    return
label rename_mc:
    scene black
    $ persistent.mcname = renpy.input ("Wanna rename the main character? (Default is Zycris, the 'y' is pronounced like the 'i' in 'nice' and the 'i' is pronounced like the 'i' in 'miss')", length=10, default = persistent.mcname).strip()
    call screen replaygalleryv2()

screen replaygalleryv2():
    add gui.main_menu_background #this adds the manin menu background as background
    #add "others/wood.webp" # this was the old image for the gallery background
    textbutton "BACK":
        action [Hide("replaygallery2"), Return()]
        xalign 0.95
        yalign 0.15
        text_size 100
        text_outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
    if callmommy == 1:
        textbutton "Mommy\n{color=#0274bf}Roleplay On{/color}":
            action SetVariable("callmommy", 0)
            xalign 0.99
            yalign 0.65
            text_size 55
            text_outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
    if callmommy == 0:
        textbutton "Mommy\n{color=#d21404}Roleplay Off{/color}":
            action SetVariable("callmommy", 1)
            xalign 0.99
            yalign 0.65
            text_size 55
            text_outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
    textbutton "Your Name: \n{color=#228b22}[persistent.mcname]{/color}":
        action [Call("rename_mc")]
        xalign 0.99
        yalign 0.45
        text_size 55
        text_outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
    use rgalgrit()
    vbar value YScrollValue("vp") xpos 0 xsize 80
    if Unlockcounter >= 10:
        if not Unlockcheat:
            textbutton "Unlock":
                xalign 0.95
                yalign 0.85
                text_size 80
                text_color "#ff0000"
                text_outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
                action ToggleVariable("Unlockcheat")
        else:
            textbutton "Lock":
                xalign 0.95
                yalign 0.85
                text_size 80
                text_outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
                action ToggleVariable("Unlockcheat")
screen rgalgrit():
    vpgrid id "vp":
        xsize 1600
        ysize 980
        xpos 100
        ypos 50
        cols 3
        xspacing 100
        yspacing 34
        mousewheel True
        pagekeys True
        #scrollbars "vertical"
        for e in galleryevents:
            if e[3] == 2:
                imagebutton:
                    idle ("cat_extra_iru")
                    action SetVariable("Unlockcounter", Unlockcounter+1)
            else:
                if Unlockcheat:
                    imagebutton:
                        idle ("{}_l".format(e[2]))
                        hover ("{}".format(e[2]))
                        action Replay("{}".format(e[1]), scope={"mc_name": persistent.mcname, "calling_serena_mommy": callmommy, "calling_s_mom": callmommy}, locked=False )
                else:
                    if e[3] == 1:
                        imagebutton:
                            idle ("{}_l".format(e[2]))
                            hover ("{}".format(e[2]))
                            action Replay("{}".format(e[1]), scope={"mc_name": persistent.mcname, "calling_serena_mommy": callmommy, "calling_s_mom": callmommy})
                    else:
                        imagebutton:
                            idle ("{}_l1".format(e[2]))
                            action NullAction()

default Unlockcounter = 0
default Unlockcheat = False
