# Splash screen
define config.load_failed_label = "loadfailed"
define persistent.agreed3 = 0
define chapter = 0

init python:
    renpy.music.register_channel("effects", "sfx")
    renpy.music.register_channel("background_s", "sfx")
    renpy.music.register_channel("background_s2", "sfx")

define z = Character("[mc_name]", color = "706626")

default invited_misty = 1
default v4_obeyed_athena = 0
default against_athena = 11
default succubus_encountered = 1
default bdsm = 1
default tipped_frankie = 1
default jxj = 8
default affair_w_serena = 1
default killed_specter = 1
default calling_s_mom = 1
default won_stfny_bdsm_ch9 = 1
default told_tr_she_cant_reach_black_belt = 1

# Girl points
default s_aff = 13
default s_trst = 4
default s_res = 9
default s_lst = 17
default a_aff = 12
default a_trst = 10
default a_res = 10
default a_lst = 5
default cndy_aff = 25
default cndy_trst = 15
default cndy_res = 24
default cndy_lst = 25
default cnt_aff = 4
default cnt_trst = 2
default cnt_res = 9
default cnt_lst = 6
default hly_aff = 1
default hly_trst = 3
default hly_res = 5
default hly_lst = 7
default gbrla_aff = 14
default gbrla_trst = 6
default gbrla_res = 1
default gbrla_lst = 13
default stfny_aff = 0
default stfny_trst = 3
default stfny_res = 0
default stfny_lst = 0
default tmra_aff = 2
default tmra_trst = 2
default tmra_res = 10
default tr_lst = 27
default vns_aff = 9
default vns_trst = 6
default vns_res = 1
default vns_lst = 11
default ymi_aff = 5
default ymi_trst = 1
default ymi_res = 5
default ymi_lst = 1
default jnfr_aff = 13
default jnfr_trst = 1
define jnfr_res = 0
default jnfr_lst = 14
default nxi_aff = 2
default nxi_trst = 2
define nxi_res = 0
define nxi_lst = 0
define frnsska_aff = 0
define frnsska_trst = 0
define frnsska_res = 0
default frnsska_lst = 5
default irna_aff = 4
define irna_trst = 0
define irna_res = 0
default irna_lst = 2
default misty_trst = 2
default misty_res = 2
default misty_lst = 13
default misty_aff = 22
#System
define dummy = 0
define came_from_gallery = 0
image species = ParameterizedText(xalign=0.83, yalign=0.35)
image species_value = ParameterizedText(xalign=0.83, yalign=0.41)
image sex = ParameterizedText(xalign=0.60, yalign=0.2)
image sex_value = ParameterizedText(xalign=0.61, yalign=0.26)
image age = ParameterizedText(xalign=0.71, yalign=0.2)
image age_value = ParameterizedText(xalign=0.71, yalign=0.26)
image height1 = ParameterizedText(xalign=0.83, yalign=0.2)
image height1_value = ParameterizedText(xalign=0.83, yalign=0.26)
image weight = ParameterizedText(xalign=0.95, yalign=0.2)
image weight_value = ParameterizedText(xalign=0.94, yalign=0.26)
image rank = ParameterizedText(xalign=0.6, yalign=0.35)
image rank_value = ParameterizedText(xalign=0.6, yalign=0.41)
image trust = ParameterizedText(xalign=0.6, yalign=0.49)
image trust_value = ParameterizedText(xalign=0.6, yalign=0.55)
image affection = ParameterizedText(xalign=0.72, yalign=0.49)
image affection_value = ParameterizedText(xalign=0.71, yalign=0.55)
image respect = ParameterizedText(xalign=0.84, yalign=0.49)
image respect_value = ParameterizedText(xalign=0.83, yalign=0.55)
image lust = ParameterizedText(xalign=0.95, yalign=0.49)
image lust_value = ParameterizedText(xalign=0.95, yalign=0.55)
image name_text = ParameterizedText(xalign=0.5, yalign=0.05)
define s = Character("Seira", color = "46194a")
define a = Character("Anabelle", color = "bfd7db")
define hls = Character("Theseus", color = "fff2c7")
define cndy = Character("Candy", color = "8f254e")
define cnt = Character("Centoria", color = "3286c7")
define hly = Character("Hailey", color = "74abd6")
define hlna = Character("Helena", color = "7d7a4a")
define gbrla = Character("Gabriella", color = "964211")
define stfny = Character("Stephanie", color = "e3d12d")
define tmra = Character("Tamara", color = "8f0000")
define tr = Character("Torr", color = "1a702d")
define vns = Character("Venus", color = "912d2d")
define ymi = Character("Yumi", color = "0091cf")
define srs = Character("Sirius", color = "ffefc2")
define irna = Character("Irena", color = "9a97cc")
define nxi = Character("Nixie", color = "a244c7")
define frnsska = Character("Fransisca", color = "f77440")
define misty = Character("Misty", color = "a80035")
define axs = Character("Axius", color = "d4d4d4")
define athna = Character("Athena", color = "ffe6b5")
define dev = Character("Developer", color = "f00080")
define jnfr = Character("Jeniffer", color = "c44f00")
define krlna = Character("Karolina", color = "19d3e0")
define jamie = Character("Jamie", color = "ffd60a")
define clair = Character("Clair", color = "9c6f43")
define cat = Character("Cat", color="#6e6e6e")
define margot = Character("Margot", color = "cf4442")
define sol = Character("Sol", color="#18aac7")
define specter = Character("Specter", color="#4d3f46")
define mercury = Character("Mercury", color="#e667a6")
define tresha = Character("Tresha", color="#754b17")
define nari = Character("Nari", color="#fff196")
define zilphie = Character("Zilphie", color="#6b5846")
define elnor2 = Character("Elnor", color="#fff5d9")
define alula = Character("Alula", color="#701010")
define solair = Character("Solair", color="#b3b3b3")
define still_needs_to_pick_choices = 0
#Chapter13
define tr_red_belt = 0
define tmra_orange_belt = 0
define apollo = Character("Apollo", color="#b09861")
define helios = Character("Helios", color="#fff8e8")
define auge = Character("Auge", color="#000000")
define nova_rogue = Character("Nova", color="#9d9d9d")
define artemis = Character("Artemis", color="#97f540")
image v13m1 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m1.webm", loop=True)
image v13m2 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m2.webm", loop=True)
image v13m3 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m3.webm", loop=True)
image v13m4 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m4.webm", loop=True)
image v13m5 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m5.webm", loop=True)
image v13m6 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m6.webm", loop=True)
image v13m7 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m7.webm", loop=True)
image v13m8 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m8.webm", loop=True)
image v13m9 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m9.webm", loop=True)
image v13m10 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m10.webm", loop=True)
image v13m11 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m11.webm", loop=True)
image v13m12 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m12.webm", loop=True)
image v13m13 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m13.webm", loop=True)
image v13m14 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m14.webm", loop=True)
image v13m15 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m15.webm", loop=True)
image v13m16 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m16.webm", loop=True)
image v13m17 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m17.webm", loop=True)
image v13m18 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m18.webm", loop=True)
image v13m19 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m19.webm", loop=True)
image v13m20 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m20.webm", loop=True)
image v13m21 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m21.webm", loop=True)
image v13m22 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m22.webm", loop=True)
image v13m23 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m23.webm", loop=True)
image v13m24 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m24.webm", loop=True)
image v13m25 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m25.webm", loop=True)
image v13m26 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m26.webm", loop=True)
image v13m27 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m27.webm", loop=True)
image v13m28 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m28.webm", loop=True)
image v13m29 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m29.webm", loop=True)
image v13m30 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m30.webm", loop=True)
image v13m31 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m31.webm", loop=True)
image v13m32 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m32.webm", loop=True)
image v13m33 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m33.webm", loop=True)
image v13m34 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m34.webm", loop=True)
image v13m35 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m35.webm", loop=True)
image v13m36 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m36.webm", loop=True)
image v13m37 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m37.webm", loop=True)
image v13m38 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m38.webm", loop=True)
image v13m39 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m39.webm", loop=True)
image v13m40 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m40.webm", loop=True)
image v13m41 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m41.webm", loop=True)
image v13m42 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m42.webm", loop=True)
image v13m43 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m43.webm", loop=True)
image v13m44 = Movie(size = (1920,1080), channel="movie", play="2.1/video/v13m44.webm", loop=True)
image credits_ch13 = Movie(size = (1920,1080), channel="movie", play="2.1/video/credits_ch13.webm", loop=True)
default persistent.g_50_unlock = 0
default persistent.g_51_unlock = 0
default persistent.g_52_unlock = 0
default persistent.g_53_unlock = 0
default stfny_clths_ch13 = 2
default had_sex_with_stfny_n_cndy_ch13 = 0

label splashscreen:
    scene black with fade
    pause(1)
    if persistent.agreed3 == 0:
        scene splash2 with fade
        pause(1)
        ""
        pause(1)
        menu:
            "I understand.":
                $ persistent.agreed3 = 1
    scene black with fade
    pause(1)
    return

label start:
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    with Pause(1)
#        Character("Iru", color = "9acd32") "Some edits for Android compability were made."
    dev "If you have a save from Chapter 12 of Season 1, please load it (the game should find it on its own, no need to copy-paste it) and ignore any errors given by the game."
    dev "This will transfer your choices to Season 2."
    dev "If you don't have a save, would like to repick your choices or don't wanna load it for any reason, you can simply skip that step and continue."
    jump default_s01

label loadfailed:
    scene black with fade
    if chapter == 12:
        jump chapter_13
    elif chapter >= 13:
        jump load
    else:
        # Handle load failures for earlier chapters
        "Save file could not be loaded. Please try again or start a new game."
        return

label load:
    scene black with fade
    if chapter >= 13:
        # Already in Season 2, continue normally
        jump chapter_13
    elif chapter == 12:
        # Transitioning from Season 1 to Season 2
        $ still_needs_to_pick_choices = 0
        dev "Transferring choices from Season 1 save..."
        # Add any necessary variable transfers here
        jump chapter_13
    else:
        # Earlier chapter - redirect to appropriate chapter
        if renpy.has_label("chapter_" + str(chapter)):
            jump expression "chapter_" + str(chapter)
        else:
            "Error: Invalid chapter label. Please check your save file or start a new game."
            return

label default_s01:
    menu:
        dev "Or if you wanna play without finishing Season 1 altogether, I ain't gonna stop you."
        "I shall be back (after finishing Season 1).":
            $ MainMenu(confirm=False)()
        "I wanna continue anyway.":
            python:
                mc_name = renpy.input("Wanna rename the main character tho? (Default is Zycris, the 'y' is pronounced like the 'i' in 'nice' and the 'i' is pronounced like the 'i' in 'miss')")

                mc_name = mc_name.strip()

                if not mc_name:
                    mc_name = "Zycris"
            pause(2)
            menu:
                dev "I'll need you to answer some questions for me pls..."
                "Sure!":
                    #Story variables
                    label picking_choices:
                    scene v20679 with dissolve
                    menu:
                        "Did you run across this girl during your adventures?"
                        "Yes.":
                            $ succubus_encountered = 1
                        "No.":
                            $ succubus_encountered = 0
                    scene v4870 with dissolve
                    menu:
                        "Did you choose to fight Athena or leave?"
                        "Fight.":
                            $ v4_obeyed_athena = 0
                            $ against_athena = 11
                        "Leave.":
                            $ v4_obeyed_athena = 1
                            $ against_athena = 9
                    scene v5123 with dissolve
                    menu:
                        "Did you give Frankie a tip?"
                        "Yes.":
                            $ tipped_frankie = 1
                        "No.":
                            $ tipped_frankie = 0
                    scene v5579 with dissolve
                    menu:
                        "Did you have sex with Serena?"
                        "Yes.":
                            $ affair_w_serena = 1
                        "No.":
                            $ affair_w_serena = 0
                    scene v6767 with dissolve
                    menu:
                        "Did you invite Misty to come with you to the ninja village?"
                        "Yes.":
                            $ invited_misty = 1
                        "No.":
                            $ invited_misty = 0
                    scene v8536 with dissolve
                    menu:
                        "Did you kill or spare the specter?"
                        "I killed her.":
                            $ killed_specter = 1
                        "I spared her life.":
                            $ killed_specter = 0
                    scene v1145 with dissolve
                    menu:
                        "Are you sometime roleplaying with Seira?"
                        "Yes, we do mommy roleplaying.":
                            $ calling_s_mom = 1
                        "We don't do that.":
                            $ calling_s_mom = 0
                    scene v9609 with dissolve
                    menu:
                        "Do you indulge in playful BDSM?"
                        "Yes.":
                            $ bdsm = 1
                            menu:
                                "In that case, did you win the BDSM bet against Stephanie?"
                                "Yes.":
                                    $ won_stfny_bdsm_ch9 = 1
                                "Nope.":
                                    $ won_stfny_bdsm_ch9 = 0
                        "Nope.":
                            $ bdsm = 0
                    scene v11735 with dissolve
                    menu:
                        "Did imply that Jenny should leave Jamie?"
                        "Yes.":
                            $ jxj = 10
                        "No.":
                            $ jxj = 12
                    scene v111531 with dissolve
                    menu:
                        "Did you tell Torr that she could one day reach black belt?"
                        "Yes.":
                            $ told_tr_she_cant_reach_black_belt = 1
                        "I said she couldn't do it.":
                            $ told_tr_she_cant_reach_black_belt = 0
                    scene black with fade
                    with Pause(1)
                    dev "Thank you! You can enjoy the game now!"
                "I'm good. Just gimme default choices from Season 1.":
                    dev "Okay imma just make some decisions for you from Season 1. Don't worry though, I'll give you the good ones. {i}Wink. Wink.{/i}"

label chapter_13:
    $ chapter = 13
    scene black with fade
    # Chapter 13 content begins here

    #Name: God of the Sun Act 1

    #1) Intro:
    #Apollo and Helios fight.
    #Apollo's monologue (Does it while he manipulates the sun's brightness.)

    show screen button_1
    play background_s2 "audio/beach.mp3" volume 0.4 fadeout 1.0 fadein 2.0 loop
    play music "audio/Gods' theme (auf grunen wiesen).mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
    scene v131 with Dissolve(1.5)
    with Pause(1.5)
    scene v134 with dissolve
    apollo "Your godhood over the sun is over, Helios."
    apollo "I trust you've noticed the sun has been acting out recently, have you not?"
    scene v132 with Dissolve(1)
    apollo "That was me."
    scene v134 with Dissolve(1)
    apollo "The sun answers to me now."
    apollo "You are no longer its master."
    scene v133 with dissolve
    #Pause
    with Pause(1)
    scene v135 with Dissolve(2)
    helios "..."
    scene v136 with Dissolve(1)
    with Pause(1)
    scene v137 with dissolve
    helios "You misunderstand, boy."
    helios "I'm not the god of the sun."
    helios "I AM the sun."
    show v13m1 with Dissolve(1)
    stop music fadeout 1.0
    play sound "audio/charge_n_hit.mp3" volume 0.4
    $ renpy.pause(7, hard=True)
    scene white with Dissolve(1)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    with Pause(2)
    play background_s "audio/Astral realm.mp3" volume 0.3 fadeout 1.0 fadein 1.0 loop
    scene v138 with Dissolve(1.5)
    play music "audio/Athena's theme.mp3" volume 0.7 fadeout 3.0 fadein 3.0 loop
    athna "..."
    scene v139 with Dissolve(1)
    athna "What's the meaning of this, Auge?"
    scene v1310 with dissolve
    with Pause(1)
    scene v1311 with Dissolve(1.5)
    athna "..."
    with Pause(1)
    scene white with Dissolve (0.1)
    play sound "audio/Effect2.mp3"
    scene v1312
    with Pause(1)
    scene white with Dissolve (0.1)
    play sound "audio/Effect2.mp3"
    scene v1313
    with Pause(1)
    scene v1314 with Dissolve(1.5)
    athna "..."
    #looks at the dent on her shield!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #Continuation: -> Flashback
    #Has a short flash back of scary sirius, which switches to scary Z in a similar shot from after the fury's fight if did fight then
    #Athena looks behind her, Axius is there.
    scene v1315 with dissolve
    athna "Axius."
    scene v1316 with Dissolve(1.5)
    #Flashback to him on the ground defeated by sirius (similar to muzan and yurishi)
    athna "This changes nothing. Procceed as we agreed, Axius."
    scene v1317 with dissolve
    axs "..."
    scene v1318 with dissolve
    axs "Yes... Understood."
    #Athena grabs a godhood orb and gives it to axius.
    scene v1317 with dissolve
    with Pause(1)
    play background_s2 "audio/magic6.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
    scene v1319 with Dissolve(1.5)
    athna "..."
    scene v1320 with Dissolve(1)
    axs "This..."
    axs "But this is..."
    scene v1321 with dissolve
    athna "I know what it is, incubus."
    scene v1322 with Dissolve(1)
    athna "It pains me to see godhood running around this commonly amongst your flithy race, believe me."
    scene v1323 with dissolve
    athna "And I cannot predict the future... However... You will most likely need this..."
    scene v1322 with dissolve
    athna "Now take it."
    scene v1325 with Dissolve(1.5)
    axs "..."
    scene v1326 with dissolve
    axs "You honour me, lady Athena."
    scene v1327 with dissolve
    athna "Hm, hn."
    scene v1328 with dissolve
    athna "Now explain yourself, Auge."
    stop background_s2 fadeout 1.0
    scene v1329 with Dissolve(1)
    athna "What do you know of this? The demon with ichor. Sirius. They're going to meet very soon."
    scene v1330 with Dissolve(1)
    athna "You knew this would happen..."
    athna "You didn't think to warn me?"
    scene v1332 with Dissolve(1.5)
    auge "..."
    scene v1331 with dissolve
    auge "I did not think it would be important."
    auge "They are demi-gods. You are a goddess."
    scene v1333 with Dissolve(1)
    auge "Can they pose a threat to you?"
    scene v1334 with dissolve
    athna "You tell me."
    scene v1332 with Dissolve(1)
    auge "..."
    scene v1331 with dissolve
    auge "God or no god, I shan't reveal the fate of one to others."
    auge "I only revealed the fate of your plans to you out of respect and loyalty. The fate of the demi-gods, however, I shan't reveal."
    scene v1332 with dissolve
    athna "You said my plan would succeed, did you not?"
    scene v1331 with dissolve
    auge "So I did."
    scene v1332 with dissolve
    athna "Will it still?"
    scene v1331 with dissolve
    auge "Of course."
    scene v1333 with Dissolve(1)
    athna "Hmmm..."
    #Axius is just standing there.
    scene v1334 with dissolve
    athna "What are you staring at, incubus..."
    scene v1335 with dissolve
    athna "Begone!" (multiple=2)
    axs "!" (multiple=2)

    scene v1336 with Dissolve(1)
    with Pause(1)
    scene v1337 with Dissolve(1)
    with Pause(1)
    scene v1338 with Dissolve(1)
    #Leaves.
    athna "..."
    scene v1339 with Dissolve(1.5)
    apollo "..." #Beaten up badly.
    scene v1340 with Dissolve(1.5)
    athna "Don't worry, little brother. Gods bleed too. You needn't be ashamed."
    athna "Helios's doing?"
    scene v1342 with dissolve
    apollo "..."
    scene v1340 with dissolve
    athna "You should've been more patient, little brother."
    athna "You shouldn't have gone to face him without my consent."
    athna "I told you you weren't ready."
    scene v1342 with dissolve
    apollo "..."
    scene v1340 with dissolve
    athna "Do not look so sad, little brother. Do not regret."
    athna "We are gods. We do not make mistakes. Regret only makes gods weaker."
    scene v1341 with dissolve
    apollo "..."
    scene v1340 with dissolve
    athna "Now sit down. I'll see to your wounds."
    scene v1342 with dissolve
    with Pause(1)

    #At axius's place, nari, his gf, irena, and nixie report what happened.
    #Later when Irena sees her father with godhood, she gives up her hopes that Z would free her.


#2) Anabelle meets Sirius:
    #z goes looking for anabelle to clear the air.
    scene black with fade
    with Pause(1.5)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    with Pause(1)
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
    scene v1343 with Dissolve(1.5)
    z "(Where's she...)"
    z "(I don't want things to be awkward forever...)"
    z "(Yumi is too busy packing that's probably gonna be my only chance to talk to her alone in a whil-)"
    scene v1344 with Dissolve(1)
    z "..." #Spots her and sirius.
    play music "audio/Sirius's theme.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v1345 with Dissolve(1)
    with Pause(1)
    scene v1346 with Dissolve(1)
    a "Sirius..."
    scene v1347 with Dissolve(1)
    z "(Did she just say-)"
    play sound "audio/rustle.mp3"
    scene v1348
    with vpunch
    a "Sirius!" #Hugs him crying.
    scene v1349 with dissolve
    srs "..." #Tears up.
    scene v1350 with dissolve
    a "You..."
    a "You..."
    scene v1351
    play audio "audio/cloth.mp3"
    with vpunch
    a "How the fuck could you do that?! How?!"
    scene v1352 with dissolve
    a "Writing those letters! Saying that shit about you not deserving us! What's wrong with you!"
    scene v1354 with dissolve
    srs "I'm sorry..."
    scene v1353 with dissolve
    a "Fuck you..."
    scene v1355 with Dissolve(1)
    a "..." #They look at each other.
    srs "..."
    scene v1356 with dissolve
    srs "You've gotten big, little sister..."
    srs "You're more beautiful than ever..."
    a "{i}Sniffs.{/i}"
    srs "I'm sorry..."
    a "..."
    play sound "audio/rustle.mp3"
    scene v1357 with Dissolve(1)
    #Hugs him again.
    with Pause(1.5)
    srs "Annie... Did you come looking for me?"
    scene v1358 with dissolve
    a "Yes..."
    scene v1357 with dissolve
    srs "You've brought Yumi with you, haven't you?"
    scene v1358 with dissolve
    a "Yes..."
    scene v1357 with dissolve
    srs "I'd bet Helena didn't let you leave..."
    scene v1358 with dissolve
    a "No... We ran away..."
    scene v1357 with dissolve
    srs "Heh... Good old Annie..."
    scene v1358 with dissolve
    a "Fuck off..."
    scene v1359 with Dissolve(1)
    z "(Lots of fucks are being thrown around by Anabelle...)"
    scene v1360 with Dissolve(1)
    z "(Now that I think about it, I should give them some privacy...)"
    scene v1361 with Dissolve(1)
    srs "..."
    scene v1362 with dissolve
    #Backs off.
    srs "Hold on..."
    scene v1363 with Dissolve(1.5)
    a "?" (multiple=2)
    z "?" (multiple=2)
    scene v1364 with dissolve
    srs "Do you know this guy, Annie?"
    scene v1365 with Dissolve(1)
    a "That's [mc_name]... He's a good friend..."
    scene v1366 with dissolve
    a "He kinda cought us while we were sneaking out of the village and insisted on coming..." #Smile.
    scene v1367 with dissolve
    srs "..."
    scene v1368 with dissolve
    srs "Is that so..."
    srs "A fellow ninja, then?"
    scene v1369 with Dissolve(1)
    z "Yeah."
    scene v1370 with Dissolve(1)
    srs "I see."
    scene v1371 with Dissolve(1)
    srs "Thank you for helping my sisters, [mc_name]."
    scene v1372 with dissolve
    z "Well, it's the least I could do... I would've been dead already if it weren't for them both..."
    scene v1373 with dissolve
    srs "Hmm..." #Smile.
    scene v1374 with dissolve
    srs "A demi-god?"
    scene v1375 with dissolve
    srs "No... You're different..."
    scene v1376 with dissolve
    srs "..."
    scene v1377 with dissolve
    srs "If I may ask... Are you a demi-god?"
    scene v1378 with dissolve
    z "Well, yes... So I've heard..."
    scene v1379 with dissolve
    srs "You've heard?" #Confused.
    scene v1380 with dissolve
    srs "..."
    scene v1379 with dissolve
    srs "Have we met?"
    scene v1380 with dissolve
    z "..."
    scene v1378 with dissolve
    z "Well, yes. But I was a lot younger."
    scene v1379 with dissolve
    srs "Younger, you say..."
    scene v1381 with dissolve
    srs "!"
    scene v1382 with dissolve
    srs "Elnor."
    srs "It's you. You're his son."
    srs "The one Seira took." #Surprised.
    scene v1383 with dissolve
    z "Yeah... That's me."
    scene v1384 with Dissolve(1)
    srs "..."
    scene v1385 with dissolve
    srs "Heh..." #Sly smile.
    srs "Fate will have its way, huh, Auge?"
    scene v1386 with dissolve
    z "?"
    scene v1387 with dissolve
    srs "Are you staying somewhere close?"
    scene v1388 with dissolve
    a "Yeah... We rented a couple rooms at a nearby inn."
    scene v1389 with dissolve
    srs "[mc_name]. It appears fate has brought us here to meet. I'd like to speak with you. I have plenty to tell you..."
    srs "But first, I'd like to see my youngest sister Yumi, maybe sit with my family and have a chat..."
    scene v1390 with dissolve
    z "Sure."
    z "Let's go to the inn."
    scene v1389 with dissolve
    srs "Lead the way."
    scene v1390 with dissolve
    with Pause(1)
    #Textless transitions of Sirius knocking at the door, Yumi opens half asleep. Realises who it is, hugs him.
#3) At the inn:
    scene black with fade
    with Pause(1.5)
    scene v1391 with Dissolve(1.5)
    with Pause(1)
    play sound "audio/Knocking.mp3"
    #Knocking sound.
    with Pause(1)
    play sound "audio/cloth.mp3"
    scene v1392 with dissolve
    with Pause(1)
    play sound "audio/creaky door.mp3"
    scene v1393 with Dissolve(1)
    with Pause(1)
    scene v1394 with Dissolve(1)
    with Pause(1)
    play sound "audio/Cloth_rustle.wav"
    scene v1395 with Dissolve(1)
    with Pause(1)
    scene black with fade
    with Pause(1.5)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    play background_s "audio/fireplace.mp3" volume 0.8 fadeout 1.0 fadein 1.0 loop
    scene v1396 with Dissolve(1)
    srs "He did."
    scene v1397 with dissolve
    z "But..."
    z "I was just a child... How did I even survive being dropped out of a window?"
    scene v1398 with dissolve
    srs "That I don't know."
    srs "He probably thought your chances of survival would've been better that way, though."
    scene v1397 with dissolve
    z "..."
    scene v1399 with dissolve
    a "What happened after?"
    scene v13100 with dissolve
    srs "Elnor didn't fight back. I just killed him. He just let me do it."
    scene v1399 with dissolve
    a "Maybe he knew he couldn't beat you?"
    scene v13100 with dissolve
    srs "No..."
    srs "For once, I knew for sure I would lose in a fight against someone..."
    srs "I've fought against bad odds... But this guy was different..."
    srs "I wouldn't have won against him... Not back then..."
    scene v1399 with dissolve
    a "But why would he let you kill him?"
    scene v13100 with dissolve
    srs "I don't know..."
    srs "Maybe he just knew it was inevitably over..."
    srs "I might've been the first to get to him, but there were many other strong warriors behind me..."
    srs "Many demi-gods... Ultimately, he would've probably lost..."
    scene v1397 with dissolve
    z "Is that so..."
    scene v1398 with dissolve
    srs "Do you resent me for it?"
    srs "Killing your father?"
    scene v1397 with dissolve
    z "..."
    with Pause(1)
    menu:
        "No.":
            z "Surprisingly I do not."
            z "I don't remember my father..."
            z "I don't see why I should resent you for killing someone I don't really know."
            srs "..."
            scene v1398 with dissolve
            srs "I see..."
            scene v1397 with dissolve
        "Yes.":
            z "A bit..."
            z "I don't have any memories of my father... I wish I had some with him..."
            z "I guess my life would've been very different if my father hadn't been killed."
            z "Not nessesarly better... It might've actually been for the best that Seira was the one to watch over me..."
            z "But..."
            scene v1398 with dissolve
            srs "I understand..."
            scene v1397 with dissolve
        "Do you regret it?":
            z "Well..."
            z "Would you do it again?"
            srs "Hm?"
            z "Seira told me she regretted attacking the incubi."
            z "Anabelle told me you left your order after the attack."
            z "So..."
            z "Was it because you regretted what you did as well?"
            srs "..."
            scene v1398 with dissolve
            srs "I do regret it. Yes."
            srs "I was just a kid. I did what I thought was right."
            scene v1397 with dissolve
            z "..."
            z "I see..."
    a "..."
    scene v1399 with dissolve
    a "Sirius."
    scene v13100 with dissolve
    srs "Yes?"
    scene v1399 with dissolve
    a "You're coming back with us, right?"
    scene v13101 with Dissolve(1)
    srs "I..."
    srs "I can't..."
    srs "There's something I have to d-"
    play sound "audio/chair.mp3" volume 0.6
    scene v13102 with Dissolve(1)
    a "Please."
    a "We've spent all this time not knowing if you're alive or dead, Sirius..."
    a "And we've come this far looking for you..."
    a "You're not gonna leave us right after that, are you?"
    scene v13103 with dissolve
    srs "..."
    scene v13102 with dissolve
    a "Come back to the village with us."
    a "Everyone has missed you."
    a "You know there's no place where you'd be more welcomed, right?"
    scene v13103 with dissolve
    srs "..."
    z "..."
    with Pause(1)
    #Cut to next scene

#4) Go back to ninja village:
    #At the village: Sirius isn't shown at first.
    #They're sneaking in.
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    play background_s2 "audio/Ambient_ninja_village_night.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v13104 with Dissolve(2)
    with Pause(1.5)
    scene v13105 with Dissolve(1)
    z "..."
    scene v13106 with dissolve
    z "(I guess Stephanie is asleep...)"
    #Signals Yumi and Annie to come over.
    scene v13107 with dissolve
    z "We're good, guys!"
    scene v13108 with Dissolve(1)
    #Shine sound effect
    play sound "audio/Shine.mp3"
    z "Coast's clear..."
    play sound "audio/creak.mp3"
    scene v13109
    stfny "Is it now?" #Appears behind him.
    with Pause(0.5)
    play sound "audio/Falling.mp3"
    scene v13110 with vpunch
    z "Fuck!" #Falls on ass up.
    scene v13111 with dissolve
    z "..."
    play sound "audio/creak.mp3"
    scene v13112 with dissolve
    stfny "Hold that pose while I call my mom, please."
    play sound "audio/sword draw.mp3"
    scene v13113 with dissolve
    z "Huh?!"
    z "Wai-"
    show v13m2 with Dissolve(0.75)
    #Kills herself.
    play sound "audio/Stab.mp3"
    $ renpy.pause(4.25, hard=True)
    scene v13114 with dissolve
    z "..."
    z "(Fuck... Of course it was a clone...)"
    with Pause(1)
    #Skip a bit.
    scene v13115 with Dissolve(1.5)
    with Pause(1)
    hlna "You left at the worse time possible, Anabelle."
    hlna "You put all of us at risk..."
    scene v13116 with Dissolve(1)
    hlna "And for what?"
    scene v13117 with dissolve
    hlna "You must've known it was fruitless, no?"
    scene v13118 with Dissolve(1)
    hlna "I mean, what were the odds of actually findi-"
    #Sirius steps into the hut.
    play music "audio/Sirius's theme 2.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v13119 with Dissolve(1)
    with Pause(3)
    scene v13120 with Dissolve(1)
    with Pause(1)
    hlna "..."
    with Pause(3)
    stop music fadeout 3
    #IF doing things with both Seira and Gabbie.
    scene v13121 with Dissolve(1.5)
    z "(I'm fucking tired...)"
    z "(I'm sure they can deal with Helena on their own...)"
    play sound "audio/sliding door.mp3"
    scene v13122 with Dissolve(1)
    with Pause(1)
    if s_lst >= 10 and gbrla_lst >= 7:
        play sound "audio/Door close.mp3"
        stop background_s fadeout 2.0
        stop background_s2 fadeout 2.0
        scene v13123 with Dissolve(1)
        z "..."
        play music "audio/Calm s02.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
        scene v13124 with Dissolve(1)
        z "Oh..."
        scene v13125 with Dissolve(1)
        z "Hey, there..."
        z "Interesting seeing you guys together like this?"
        z "And how did you know I was coming?"
        scene v13126 with dissolve
        s "I saw Stephanie running to her mom, so I made my assumptions."
        s "While you were away, Gabbie's been telling me some stories."
        s "You two have been very naughty, it seems."
        scene v13125 with dissolve
        z "Ehhh..."
        scene v13127 with dissolve
        gbrla "So, Seira and I have been thinking..."
        scene v13126 with dissolve
        s "It might be fun to switch things up a bit, wouldn't you say?"
        s "However, I'm a bit worried you might be too tired for that right now?"
        scene v13125 with dissolve
        z "..."
        with Pause(1)
        menu:
            "I'm kinda too tired...":
                z "Well... I'm a bit worn out from the trip..."
                scene v13126 with dissolve
                s "Of course. We get it, honey."
                scene v13127 with dissolve
                gbrla "Maybe some other time, then. I'll be off to my room."
                scene v13125 with dissolve
                z "Good night, Gabbie..."
                with Pause(1)
                scene black with fade
            "Never too tired for a threesome.":
                label G50:
                    $ persistent.g_50_unlock = 1
                z "Me? Tired? Never!"
                scene v13126 with dissolve
                s "That's nice to hear, Honey..."
                play sound "audio/cloth.mp3"
                scene v13128 with Dissolve(1)
                gbrla "..."
                scene v13129 with dissolve
                gbrla "Wait... What's with this position?"
                scene v13130 with Dissolve(1)
                s "Hush now, honey. Don't worry about a thing. [mc_name] and I are going to spoil you rotten today..." (multiple=2)
                gbrla "Hnn..." (multiple=2)
                play sound "audio/Cloth_rustle.wav"
                scene v13133 with Dissolve(1)
                gbrla "..."
                play sound "audio/cloth.mp3"
                show v13m3 with Dissolve(1) #L=20
                gbrla "Waihhttt... Seira... That's...{w=3}{nw}"
                gbrla "Hnnn~... Ahhhnnn~...{w=2}{nw}"
                s "Mnnnhhhh~...{w=2}{nw}"
                gbrla "Guys... Ahhhh~... What are you...{w=4}{nw}"
                z "Shhhhh... Don't worry Gabbie... Just enjoy it...{w=6}{nw}"
                scene v13131 with Dissolve(1)
                gbrla "Huffhhh... Huhhhfffhhh... Guhhh... Hahhhhh~... Hnnnn~..."
                z "Damn, Seira... I think we pushed her too far..."
                s "Nah, she's just fine, trust me..."
                z "She's delicate, Seira... Her body's not build like yours and mine..."
                scene v13132 with Dissolve(1)
                gbrla "Haannnhhhh~... Cock..."
                gbrla "Huffhhhh... I want the cock... Anhhhh~..."
                z "Oh... I guess she can take more after all..."
                z "Okay, Gabbie... Let's see how much you can handle..."
                play sound "audio/Cloth_rustle.wav"
                show v13m35 with Dissolve(1)
                play background_s "audio/lewd (stolen from Atem)/Sucking.ogg" fadeout 1.0 fadein 1.0 loop
                gbrla "Ghhhkkkmmm~... Ghnnmm~..."
                s "Mnnn~..."
                z "Fuck... You two are crazy..."
                z "Seira... I'm pretty sure Gabbie can't handle this..."
                s "Ghhmmmnn~... She's having... Nmmmm~... ...funnmmmnnn~..."
                gbrla "Ghhhhnnnmmm~... Mmmmnnn~... Uhkkmnnn~..."
                z "..."
                z "I think she's gonna need some air real soon..."
                s "Mnnnn~... Cock is more... Uhhmmmnnn~... ...important than air..."
                s "Hmmmnnnn~... Nmmmnnnnhh~..."
                z "But..."
                z "Ahhh... Fuckkk... She's sucking me like crazy..."
                gbrla "Ghhhhhmmmm~... Hmnnnn~... Nhhhmmm~..."
                z "(Her lips aren't letting my dick go...)"
                gbrla "Khmhmmmnnnn~... Nhhhhhhgggg~... Mmmmnnnn~..."
                z "(I can feel her tongue wrapping around my dick in there too... Fuck...)"
                gbrla "Mmmmnnnhhh~... Ahhnnnn~..."
                z "(This girl... I didn't think she had it in her...)"
                gbrla "Mnnnnhhh~..."
                z "Fuhccckkk... She's really doing well, Seira..."
                s "Hmmmm~... Told you..."
                z "I'm starting to think the whole redhead family was designed to be limitlessly bred..."
                s "Nmmmmnnn~... Don't let... Hmmm~... Fransiska hear you say that..."
                gbrla "Nmmmm~... Ghkkkknmmmmm~... Ahhhhnnnnn~..."
                z "Seira... I'm gonna..."
                z "I'm close..."
                s "Nmmm~... Wait... Don't come yet... Mmmmmnnn~... Stop for a bit..."
                z "Wh-What? Why..."
                s "Just trust me... Mmmm~... I have something better planned..."
                with Pause(1)
                stop background_s fadeout 1.0
                scene v13134 with Dissolve(1)
                s "..."
                gbrla "Ahhnnn~... Dickkkkk..."
                scene v13135 with dissolve
                z "Told you it was too much..."
                gbrla "I want... Ahhnn~... ...cock..."
                show v13m43 with Dissolve(1)
                s "I mean... She looks okay to me..."
                gbrla "Diiiccckkkk..."
                z "..."
                s "Oh, it's not so bad..."
                s "She's just dizzy from..."
                s "Well, you know from what."
                gbrla "Dickkkk... I want dickk..."
                z "..."
                s "I mean... Look, she's talking..."
                gbrla "Cockkk..."
                z "I'm not sure this qualifies as talking..."
                s "..."
                scene v13136 with Dissolve(1)
                s "Hmmm..."
                scene v13137 with dissolve
                z "?"
                play sound "audio/Cloth_rustle.wav"
                scene v13138 with Dissolve(1)
                s "Say..."
                scene v13139 with dissolve
                z "..."
                scene v13140 with dissolve
                z "Where is this going, Seira... You have such an evil look going there..."
                scene v13141 with dissolve
                s "I was just thinking..."
                s "Let's give her what she wants..."
                scene v13140 with dissolve
                z "Is that really a good idea... I don't wanna break her..."
                scene v13141 with dissolve
                s "Look at how she's looking at you."
                scene v13142 with Dissolve(1)
                z "..."
                s "That's a look of anticipation right there."
                play sound "audio/cloth.mp3"
                scene v13143 with Dissolve(1)
                s "Come now. Don't keep the girl waiting..."
                scene v13144 with dissolve
                z "..."
                scene v13145 with Dissolve(1)
                z "Well, I'm not saying no to that..."
                scene v13146 with Dissolve(1)
                z "Here I come, Gabbie."
                show v13m44 with Dissolve(1)
                play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                z "Fuckkk... So tight..."
                gbrla "Ahnnn~... Hannhhh~..."
                gbrla "Fuhhckkk... Ohhhhh~..."
                z "Shit... I'm not going to last..."
                gbrla "Hufffhhnnnn~... Gahhhhnnn~..."
                z "I was about to cum before and..."
                gbrla "Haahhhh~... Ugghhhhh~..."
                z "She's just squeezing me too much..."
                gbrla "Hannnhhh~... [mc_name]..."
                gbrla "Shooohht~... Ughhhnn~... Shoot it inshide..."
                z "Fuck... Are you..."
                gbrla "Hahhhhh~... Hmmnnn~... Inshide pleasshhhhh~..."
                z "Are you sure..."
                gbrla "Yesshhhh~... Ahhhh~ Aaaaaanhhhhh~..."
                gbrla "I'm cumminhhhh~... I'm cummmmm-"
                stop background_s fadeout 1.0
                scene v13147
                play audio "audio/Cloth_rustle.wav"
                play sound "audio/magic 7.mp3"
                with vpunch
                gbrla "AAAGHHHNNNN~..."
                with Pause(1)
                scene v13148 with Dissolve(1)
                gbrla "Hahhhh~... Ahhhhh~..."
                if came_from_gallery == 0:
                    $ gbrla_lst += 5
                show screen button_lst with dissolve
                play sound "audio/stats.wav"
                hide screen button_lst with dissolve
                play audio "audio/Cloth_rustle.wav"
                scene v13149 with dissolve
                s "Do you feel spoiled now, Honey?"
                gbrla "Hahhhh~..."
                play audio "audio/Cloth_rustle.wav"
                scene v13150 with dissolve
                s "I don't think she has the energy to talk anymore, [mc_name]..."
                s "It's okay, we should probably go to sleep anyhow. I'm sure you need some rest."
                scene v13151 with dissolve
                s "?"
                scene v13152 with dissolve
                s "..."
                with Pause(1)
                play sound "audio/Cloth_rustle.wav"
                show v13m28 with Dissolve(1)
                play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                s "Uggghhhh~... Fuuuhhhhckkkk~..."
                s "How can you... Guhhhhh~... Ughhhhhhh~... Ahhhhh~..."
                s "How do you have the energy... Ahhhhh~... Hannnhhh~..."
                s "So hard... Haahhhhh~..."
                s "I'm cumming~... Aaaaahhhh~..."
                s "Ughhh~... Hahhhh~... Waihhhhttt~..."
                s "I came alreadyy~... Ahhhh~... I need a break..."
                s "I'm... Ahhhhhnnn~..."
                s "I can't even think anymore... Ahhhhnnnn~..."
                s "How's your dick still this hard... Ahhhnnn~... Fuhccckkk~..."
                s "I can't... Ughhh~..."
                z "I'm sure a mighty woman like you can at least handle as much as Gabbie did..."
                s "Our bodies are different... Aaaahhhnnn~... We're different kinds of women..."
                s "Hnnnhhh~... Ahhhhh~... Her body can handle being bred all day..."
                s "I have a fighter's build, not a housewife's build... Ahhh~... Ahhhhhh~..."
                z "Seira if your body wasn't meant to be bred I don't know which body was..."
                z "All I can think about everytime I see you standing like a warrior is how much I want to rip off your clothes and make you submit to my dick."
                s "Ahnnn~... Fuckkkk~... You can't say something like th-"
                z "Everytime you stand there all mighty and powerful, I want to knock you off your feet and breed you until you pass out..."
                s "Nhhhhgnnn~... Fuhhhcckkkk~... Stop that... You're gonna make me..."
                z "Disarm you, force you off your dignified warrior stance, take off your shining Keres armour, and fuck you for hours until you submit..."
                s "[mc_name]... If you talk like that..."
                z "I wanna shoot my cum inside you, impregnate you, and turn you into a submissive housewife, who serves no one but my cock..."
                s "Ahhhhhnnn~... You're gonna make me cummm~... I'm gonna cumm~..."
                z "I want you to wait by the door for me to come home every day. Waiting for your chance to worship my dick with your lips."
                s "I'm cumming~... Ahhhhhnnnn~... I'm cumming..."
                with Pause(1)
                stop music fadeout 2.0
                stop background_s fadeout 1.0
                scene v13153
                play audio "audio/magic 7.mp3"
                play sound "audio/Cloth_rustle.wav"
                with vpunch
                s "Ahhhhhhhhhhhhh~..."
                with Pause(1)
                play sound "audio/cloth.mp3"
                scene v13154 with Dissolve(1)
                if came_from_gallery == 0:
                    $ s_lst += 5
                show screen button_lst with dissolve
                play sound "audio/stats.wav"
                hide screen button_lst with dissolve
                z "Hahhh..."
                scene v13155 with Dissolve(1)
                z "(Fuck... I think I spent every bit of energy I had left...)"
                scene v13156 with Dissolve(2)
                z "(I just want some...)"
                scene black with Dissolve(2)
                with Pause(1)
                z "(Sleep...)"
                with Pause(2.5)
                if came_from_gallery == 1:
                    $ came_from_gallery = 0
                $ renpy.end_replay()
#5) Meeting next day:
    with Pause(1.5)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v13157 with Dissolve(2)
    with Pause(1)
    play sound "audio/meow.wav"
    scene v13158 with dissolve
    scene v13159 with dissolve
    z "..."
    scene v13160 with dissolve
    z "What do you think they're talking about?"
    scene v13161 with dissolve
    ymi "Beats me..."
    scene v13162 with dissolve
    ymi "Helena can do her worst. I don't care, we didn't do anything wrong."
    ymi "What's the point of being a ninja if you can't help others. Even more so, your own family."
    scene v13163 with dissolve
    z "..."
    scene v13164 with Dissolve(1)
    srs "{size=-20}Are you sure?{/size}" (multiple=2)
    z "(I can't hear a thing...)" (multiple=2)
    play music "audio/ninja village s02.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v13165 with Dissolve(1)
    tr "..."
    scene v13166 with dissolve
    tr "Who's this?" #Whispering.
    scene v13167 with dissolve
    cndy "I think it's Anabelle's brother." #Whispering.
    scene v13165 with dissolve
    tr "..."
    scene v13166 with dissolve
    tr "Wasn't he like..." #Whispering.
    tr "...probably dead?" #Whispering.
    scene v13168 with dissolve
    cndy "..." #sus.
    scene v13169 with dissolve
    cndy "It's just, Anabelle hasn't seen or heard from him in a while so..."
    scene v13170 with dissolve
    tr "I see..."
    scene v13165 with dissolve
    tr "..."
    scene v13166 with dissolve
    tr "So is he like... Stronger than [mc_name]?"
    scene v13167 with dissolve
    cndy "What?"
    scene v13171 with dissolve
    tr "..."
    scene v13166 with dissolve
    tr "What?"
    tr "I'm just asking..."
    scene v13167 with dissolve
    cndy "How would I know?"
    cndy "And why does that matter?"
    scene v13166 with dissolve
    tr "Just curious..."
    scene v13172 with dissolve
    tmra "Hey, losers. Come to see [mc_name] getting demoted?"
    scene v13173 with Dissolve(1)
    tr "What?"
    cndy "What are you talking about?"
    scene v13174 with dissolve
    tmra "He disobeyed orders and left with Yumi and Anabelle, didn't he?"
    tmra "He's gonna lose points for that."
    tmra "And he just barely made it to red belt, so he's going down..."
    scene v13173 with dissolve
    cndy "..."
    scene v13176 with dissolve
    tr "What about Yumi?"
    scene v13175 with dissolve
    tmra "I mean, it's possible for her too to get demoted."
    tmra "But she's well in the blue belt area. So..."
    #Evil smirk.
    scene v13177 with Dissolve(1)
    tmra "It's probably just gonna be [mc_name]."
    scene v13178 with dissolve
    tr "..." (multiple=2)
    cndy "..." (multiple=2)
    with Pause(1)
    scene v13179 with Dissolve(1)
    hlna "Your arm... And your eye..."
    scene v13180 with dissolve
    hlna "..."
    hlna "Is it true that you fought Athena on the day of the black sun and almost killed her?"
    hlna "How did you-"
    play sound "audio/cloth.mp3"
    scene v13181 with vpunch
    a "Enough questions, Helena! My brother needs to rest before the tournament."
    scene v13182 with dissolve
    z "(Tournament?)" (multiple=2)
    hlna "..." (multiple=2)
    scene v13183 with dissolve
    hlna "You're right..."
    scene v13184 with dissolve
    hlna "Let's catch up later, Sirius."
    scene v13185 with dissolve
    with Pause(1)
    scene v13186 with Dissolve(1)
    hlna "As for you two..."
    hlna "You both lose 30 points for disobeying orders."
    hlna "Additionally, [mc_name]. You will not be rewarded with any points for your last mission as a punishment."
    scene v13187 with dissolve
    z "Bu-"
    scene v13186 with dissolve
    hlna "So... Yumi, you'll still retain your rank as a blue belt..."
    hlna "But for [mc_name], I'm afraid you'll be demoted to purple belt as a result."
    scene v13187 with dissolve
    z "But I only went with them to help."
    z "And strictly speaking there were no orders that said I couldn't."
    scene v13186 with dissolve
    hlna "..."
    scene v13189 with Dissolve(1)
    hlna "I very clearly pointed out that we were in danger and the whole village was on full alarm, [mc_name]."
    hlna "Surely you must realise, you are one of our biggest assets here."
    scene v13190 with dissolve
    hlna "In case of an attack, a ninja as capable as you could really make a difference."
    hlna "A difference between your fellow ninjas dying or making it out alive, [mc_name]."
    scene v13191 with dissolve
    z "..."
    scene v13188 with Dissolve(1)
    with Pause(2)
    scene v13190 with Dissolve(1.5)
    z "..."
    scene v13186 with Dissolve(1)
    hlna "I would like to speak with you alone before the tournament. So kindly swing by my room."
    scene v13192 with Dissolve(1)
    with Pause(1)
    #Leaves.
    scene v13190 with Dissolve(1)
    z "..."
    z "(I didn't realise she thought so highly of me...)"
    z "(I really can't understand this woman... She was so cold to me when I got here, and now she says all this stuff...)"
    z "(Can't say she's wrong, though... She makes a good point...)"
    z "(Let's see what she has to say later...)"
    scene v13193 with Dissolve(1)
    hlna "Candy."
    hlna "You did a great job on your last mission. You recieve 20 points."
    play sound "audio/whoosh.mp3"
    scene v13194 with PushMove(0.1, mode="pushright")
    hlna "Same for you Centoria. You got 20 points as well."
    scene v13193 with dissolve
    hlna "Naturally, neither of you gathered enough points to promote them to red belt."
    scene v13195 with dissolve
    hlna "Torr."
    define tr_red_belt = 0
    define tmra_orange_belt = 0
    scene v13196 with dissolve
    hlna "Seeing how you were the one to kill the oni in your last mission. You'll be recieving 35 points."
    hlna "This means that you'll be promoted to red belt."
    $ tr_red_belt = 1
    scene v13197 with dissolve
    tr "!!!"
    scene v13198 with dissolve
    hlna "Congrats. That's no small feat to climb ranks this quickly."
    scene v13199 with Dissolve(1)
    tr "..."
    scene v13200 with Dissolve(1)
    hlna "Tamara. Seeing how you did a great job being a mission leader and the way you fought the oni, you'll recieve 40 points."
    hlna "Means you're also promoted. You'll recieve the orange belt."
    $ tmra_orange_belt = 1
    scene v13201 with dissolve
    tmra "..." #Smiles.
    scene v13202 with Dissolve(1)
    hlna "I wish I could've said the same to you, [mc_name]. As your performance in the last mission was by far the best."
    scene v13203 with dissolve
    z "..."
    scene v13201 with Dissolve(1)
    hlna "You guys will be recieving your new belts after the tournament."
    hlna "Get some rest for now and try to prepare."
    with Pause(1)
    #Leaves.
    #Following up
    #Other girls speculating about how sirius got his arm cut off and lost his eye.
    scene v13205 with Dissolve(1)
    stfny "Obviously not! Come on!"
    scene v13204 with dissolve
    hly "It's not like he's invincible, Stephanie."
    scene v13206 with dissolve
    vns "What are you guys talking about it?"
    scene v13207 with Dissolve(1)
    hly "I think Sirius lost a battle and lost his eye and arm as a result, Stephie says it's impossible."
    hly "I guess she thinks he did all that to himself or something?"
    scene v13208 with dissolve
    vns "I mean, I can see her point, I guess? Who can actually defeat Sir-"
    play sound "audio/cloth.mp3"
    scene v13209 with vpunch
    hly "No! Don't tell me you agree with her"
    scene v13210 with dissolve
    vns "Eh?! What am I agreeing to here?"
    play sound "audio/Cloth_rustle.wav"
    scene v13211 with dissolve
    stfny "Just admit it. There's no way someone did that to him."
    scene v13212 with dissolve
    hly "No! How else would that have happened?!"
    scene v13213 with dissolve
    vns "What do you suggest then, Steph? Did he do it to himself or something?"
    scene v13214 with dissolve
    stfny "..."
    scene v13215 with dissolve
    hly "Actually, you're the one who changed his eye patch and bandages right?"
    scene v13213 with dissolve
    vns "Yeah?"
    scene v13215 with dissolve
    hly "So? What do you think?"
    scene v13213 with dissolve
    vns "How would I know?"
    scene v13215 with dissolve
    hly "Well... I mean..."
    scene v13211 with dissolve
    stfny "It's Sirius, guys! Who could ever actually beat him, come on!"
    scene v13216 with dissolve
    hly "Well..."
    scene v13217 with dissolve
    with Pause(1.5)
    scene v13218 with dissolve
    with Pause(1.5)
    scene v13219 with dissolve
    with Pause(1.5)
    scene v13220 with Dissolve(1)
    with Pause(1.5)
    scene v13221 with Dissolve(1)
    z "(Awfully hot today...)"
    z "(I wonder what Helena wants to talk about...)"
    with Pause(1)
    play sound "audio/sliding door.mp3"
    stop music fadeout 2.0
    scene v13222 with Dissolve(1)
    with Pause(1)
    z "Oh... I'm sorry... Is this a bad time?"
    scene v13223 with dissolve
    hlna "Not at all."
    scene v13224 with dissolve
    hlna "Come sit next to me."
    scene v13222 with dissolve
    z "..."
    play audio "audio/Cloth_rustle.wav"
    scene v13225 with Dissolve(1)
    hlna "I hope you like tea. I made you some."
    play sound "audio/pick up 2.mp3"
    scene v13226 with dissolve
    z "Sure."
    scene v13227 with dissolve
    hlna "Don't worry, it doesn't mean I'm going to make you stay here long."
    hlna "I just want a quick word. Something I didn't want to say in front of the girls."
    scene v13228 with dissolve
    z "..."
    z "Go on."
    play music "audio/Helena's Theme.mp3" volume 0.25 fadeout 1.0 fadein 1.0 loop
    scene v13229 with dissolve
    hlna "Well you see, [mc_name]... I just wanted to say this..."
    hlna "If ever an attack happens here..."
    scene v13230 with dissolve
    hlna "Aside from the black and brown belts, I want you to grab as many ninjas here as you can and flee."
    scene v13231 with dissolve
    z "Flee?"
    z "To where?"
    scene v13230 with dissolve
    hlna "Anywhere. I'll leave that to your judgment."
    hlna "Obviously you'll have to go south. I would suggest a bigger city like Esyl or one of the elf cities. Maybe even Kalytro."
    scene v13231 with dissolve
    z "..."
    z "Do you really think we'd get attacked here?"
    z "We have two Keres now. Not to mention you and Sirius are black belts."
    scene v13230 with dissolve
    hlna "The southern village had more than two black belts and they were attacked all the same."
    hlna "And the main reason why this kind of attack can have heavy casualties is exactly because the first ninjas to encounter it are unlikely to be the few black belts in the village."
    scene v13231 with dissolve
    z "..."
    z "I see your point."
    scene v13230 with dissolve
    hlna "In a case of an attack, I already let the others know that you'll immediately be promoted to a brown belt and serve as the mission leader."
    scene v13231 with dissolve
    z "What?!"
    scene v13230 with dissolve
    hlna "What I didn't tell them, however, is that you will have only one task... Save as many fellow ninjas as you can. Flee."
    scene v13231 with dissolve
    z "Wait! But why me?"
    scene v13230 with dissolve
    hlna "Of all the ninjas with ranks blue belt and lower, I trust your judgment and ability the most."
    hlna "I was going to inform you about my plan along with the others a few days ago, but you left with Anabelle and Yumi."
    hlna "I'll talk to Yumi about this later, don't worry."
    hlna "Which brings me to one more point on why I wanted to talk to you in private."
    scene v13231 with dissolve
    z "?"
    scene v13230 with dissolve
    hlna "[mc_name]. I trust you realise that the girls look up to you."
    hlna "The ones that have been here for a short while like Torr and Candy see an example to follow. Someone who will be a great ninja someday."
    hlna "And the others who have been here for a few years now see another Sirius in you."
    scene v13231 with dissolve
    z "..."
    scene v13230 with dissolve
    hlna "I appreciate that you were trying to help Anabelle and Yumi. But please take that into account before you make a decision like sneaking out and leaving us behind."
    scene v13231 with dissolve
    z "..."
    scene v13230 with dissolve
    hlna "I need to know that I can count on you, [mc_name]."
    hlna "I know that this is a lot take in.... So I'll give you a while to think about it."
    hlna "You also need to prepare for the tournament."
    scene v13231 with dissolve
    z "..."
    z "Tournament?"
    z "Why is everyone talking about that?"
    play audio "audio/Cloth_rustle.wav"
    scene v13232 with Dissolve(1)
    hlna "Oh, wait. I just realised we need a new draw since Sirius is going to participate."
    scene v13233 with Dissolve(1)
    z "Wait-"
    scene v13234 with Dissolve(1)
    z "..."
    stop music fadeout 3.0
    with Pause(1)
    #Skip.
#6) Helena wants more intensive training so they have a kick out competetion:
    #People are reading the draw which is hanged somewhere.
    stop sound fadeout 1.0
    scene v13235 with Dissolve(2)
    with Pause(1)
    play audio "audio/creak.mp3"
    scene v13236 with Dissolve(1)
    with Pause(1)
    scene v13238 with Dissolve(1)
    tr "..."
    scene v13237 with Dissolve(1)
    with Pause(1)
    cndy "Wait, where am I exact-"
    scene v13239 with vpunch
    cndy "Whaaaaa... They're gonna have me fight Yumi..."
    scene v13240 with dissolve
    cndy "..."
    scene v13241 with dissolve
    cndy "You've also got it bad, Centoria."
    scene v13242 with dissolve
    cnt "Yeah..."
    scene v13243 with dissolve
    z "Yeah... I'm really not feeling very happy about fighting Venus in the first round either."
    scene v13244 with dissolve
    stfny "Amateurs."
    scene v13245 with dissolve
    z "What's that?"
    scene v13246
    play audio "audio/creak.mp3"
    with vpunch
    stfny "Amateurs!"
    scene v13247 with dissolve
    z "..."
    scene v13248 with dissolve
    vns "So if the whole thing is gonna take place in my illusion, how am I supposed to compete?"
    scene v13249 with Dissolve(1)
    stfny "My mom will be the one creating the illusion when you're up."
    scene v13250 with dissolve
    vns "Oooh... I see, I see..."
    scene v13251 with dissolve
    vns "..."
    scene v13252 with Dissolve(1)
    vns "Oh, I'm already up, right?"
    scene v13253 with dissolve
    z "Yup. We're gonna be the first to fight."
    scene v13254 with dissolve
    vns "Hmmm..."
    with Pause(1)

    label tournoment:
    #1: Z vs Venus:
        scene black with fade
        with Pause(1.5)
        stop background_s fadeout 1.0
        stop background_s2 fadeout 1.0
        stop music fadeout 1.0
        stop sound fadeout 1.0
        play music "audio/under pressure michael kobrin.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
        scene v13255 with Dissolve(1.5)
        with Pause(1.5)
        play sound "audio/whoosh cinematic.mp3" volume 0.1
        scene v13256 with Dissolve(1)
        with Pause(1.5)
        scene v13257 with Dissolve(1)
        with Pause(1.5)
        play audio "audio/whoosh cinematic.mp3" volume 0.1
        scene v13258 with Dissolve(1)
        with Pause(1.5)
        scene v13259 with Dissolve(1)
        with Pause(1.5)
        scene v13260 with Dissolve(1)
        vns "..."
        scene v13261 with dissolve
        hlna "Okay, you two. Let me be clear one last time."
        hlna "You win by either killing your opponent or pushing them out of bounds and into the water."
        hlna "You can also surrender at anytime, giving your opponent the win."
        hlna "Now, then. You may begin."
        scene v13262 with dissolve
        with Pause(1.5)
        play audio "audio/Magic 9.mp3"
        play sound "audio/electr.wav" volume 0.1 loop
        scene v13263 with Dissolve(1)
        z "Okay, Venus... Here I c-"
        scene v13264
        play sound "audio/electric-shock.mp3" volume 0.2
        with vpunch
        vns "HYAHH!"
        scene v13265 with Dissolve(1)
        vns "?!"
        play audio "audio/whoosh cinematic.mp3" volume 0.3
        scene v13266 with Dissolve(1)
        with Pause(1.5)
        scene v13267 with Dissolve(1)
        z "Hey... That was mean! I wasn't prepared." (multiple=2)
        vns "..." (multiple=2) #Shocked.
        play sound "audio/electr.wav" volume 0.1 loop
        scene v13268 with Dissolve(1)
        z "I guess it's my turn."
        scene v13269 with Dissolve(1)
        vns "What the... Since when can yo-"
        scene v13270
        play sound "audio/electric-shock.mp3" volume 0.2
        with vpunch
        vns "F-FUCKKK!"
        scene v13271 with dissolve
        scene v13272
        play sound "audio/sword cut 2.mp3"
        with vpunch
        stop music fadeout 3.0
        vns "{i}Gasps.{/i}"
        play sound "audio/Falling2.mp3"
        scene v13273 with Dissolve(1)
        with Pause(1)
        play audio "audio/whoosh cinematic.mp3" volume 0.2
        scene v13274 with Dissolve(1)
        scene white with Dissolve(1)
        with Pause(1.5)
        play background_s2 "audio/Ambient_ninja_village_night.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
        scene v13275 with Dissolve(1.5)
        with Pause(1.5)
        scene v13276 with Dissolve(1)
        stfny "Damn... Venus barely stood a chance..."
        play audio "audio/creak.mp3"
        scene v13277 with dissolve
        stfny "I think I'm almost up, now. Good luck, guys."
        scene v13278 with dissolve
        with Pause(1.5)
        scene v13279 with Dissolve(1)
        with Pause(1.5)
        play audio "audio/tournament.mp3"
        scene v13280 with Dissolve(1)
        with Pause(2.5)
        scene black with fade
        with Pause(1.5)
        scene v13281 with Dissolve(1)
        with Pause(2)
        scene v13282 with Dissolve(1)
        z "Hey, Steph."
        scene v13283 with Dissolve(1)
        stfny "Hey, kid."
        stfny "Nice fighting out there."
        scene v13290 with dissolve
        z "Thanks!"
        z "How did your fight go, I just got here."
        scene v13291 with dissolve
        stfny "Ehhhh..."
        play sound "audio/whoosh.mp3"
        scene v13284 with PushMove(0.1, mode="pushright")
        with Pause(1.5)
        #Show render of her getting stabbed.
        play sound "audio/whoosh.mp3"
        scene v13292 with PushMove(0.1, mode="pushleft")
        z "I see." #He's already sitting down.
        scene v13293 with dissolve
        z "What about the others?"
        play sound "audio/whoosh.mp3"
        scene v13286 with PushMove(0.1, mode="pushright")
        stfny "Yeah... Candy didn't stand much chance."
        play sound "audio/whoosh.mp3"
        scene v13287 with PushMove(0.1, mode="pushright")
        stfny "And neither did Centoria."
        play sound "audio/whoosh.mp3"
        scene v13293 with PushMove(0.1, mode="pushleft")
        z "Oh..."
        z "How about Torr and Tamara. That one must've been exciting?"
        play sound "audio/whoosh.mp3"
        scene v13285 with PushMove(0.1, mode="pushright")
        stfny "Actually yes. Torr won that one."
        play sound "audio/whoosh.mp3"
        scene v13295 with PushMove(0.1, mode="pushleft")
        stfny "That girl is very promising, you know."
        scene v13297 with dissolve
        z "I know."
        scene v13288 with Dissolve(1)
        with Pause(1.5)
        play audio "audio/tournament.mp3"
        scene v13289 with Dissolve(1)
        with Pause(2.5)
        scene v13298 with dissolve
        stfny "..."
        scene v13299 with dissolve
        z "So who's fighting?"
        scene v13300 with dissolve
        stfny "Seira and Anabelle."
        scene v13301 with dissolve
        z "Damn! I have to watch that one."
        scene v13302 with dissolve
        with Pause(1)
        stop background_s fadeout 1.0
        stop background_s2 fadeout 1.0
        scene v13303 with Dissolve(1)
        s "{i}Hyperventilating.{/i}"
        scene v13304 with Dissolve(1)
        a "{i}Out of breath.{/i}"
        scene v13305 with Dissolve(1)
        a "..."
        play audio "audio/sword into wood.mp3"
        scene v13306
        with vpunch
        s "?"
        scene v13307 with dissolve
        a "I lose."
        a "I can't beat you, Seira."
        scene v13308 with dissolve
        s "..."
        play sound "audio/whoosh cinematic.mp3" volume 0.2
        scene v13309 with Dissolve(1)
        scene v13310 with Dissolve(1)
        scene white with Dissolve(1)
        with Pause(1)
        #Illusion is over.
        play background_s2 "audio/Ambient_ninja_village_night.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
        scene v13313 with Dissolve(1)
        z "Oh..."
        z "Well, I guess not even Anabelle can beat Seira."
        scene v13311 with Dissolve(1)
        with Pause(1.5)
        play audio "audio/tournament.mp3"
        scene v13312 with Dissolve(1)
        with Pause(2.5)
        scene v13314 with Dissolve(1)
        z "(What exactly is she doing in this position of hers...)"
        play audio "audio/creak.mp3"
        scene v13315 with Dissolve(1)
        stfny "Hmmm..."
        scene v13316 with dissolve
        stfny "Aren't you up next?"
        scene v13315 with dissolve
        z "Oh, right..."
        z "What does round two look like, by the way?"
        scene v13317 with dissolve
        #Render of round two
        stfny "Well, you'll be facing Hailey. Sirius will be facing Yumi. Which is a shame because I could've totally beaten Yumi there..."
        scene v13315 with dissolve
        z "..."
        scene v13316 with dissolve
        stfny "And then the last match is Seira and Torr."
        scene v13315 with dissolve
        z "Damn... Torr has it rough, huh..."
        scene v13318 with dissolve
        stfny "Well, speak for yourself. Your opponent is not to be underestimated, you know."
        stfny "Don't go tarnishing my teaching, you hear?"
        scene v13319 with dissolve
        z "Ehhhh... I'll do my best..."
        scene v13320 with dissolve
        stfny "I know, dearest. You're my most talented student after all."
        if stfny_lst >= 3:
            scene v13321 with dissolve
            z "Why thank-"
            scene v13322 with dissolve
            stfny "Talented in several areas too, aren't you..."
            play music "audio/the last unicorn.mp3" volume 0.05 fadeout 1.0 fadein 1.0 loop
            show v13m6 with dissolve
            z "{i}Gulps."
            z "(I feel like I know where this might be going...)"
            define stfny_clths_ch13 = 2
            define had_sex_with_stfny_n_cndy_ch13 = 0
            with Pause(1)
            menu:
                "Take it further.":
                    with Pause(1)
                    label G51:
                        $ persistent.g_51_unlock = 1
                    scene v13325 with dissolve
                    z "(Welp, you asked for it, Stephie.)"
                    hide v13m6
                    z "Let me just..."
                    screen stop_stfny_ch13:
                        imagebutton:
                            xanchor 0.5
                            yanchor 0.5
                            xpos 0.07
                            ypos 0.96
                            idle "images/Buttons/stop_u.png"
                            hover "images/Buttons/stop_h.png"
                            action Jump("z_leaves_ch13")
                    if came_from_gallery == 0:
                        show screen stop_stfny_ch13
                    $ stfny_clths_ch13 = 1
                    show v13m7 with dissolve
                    play sound "audio/whoosh.mp3"
                    $ renpy.pause(9, hard=True)
                    show v13m8 with dissolve
                    $ renpy.pause(6, hard=True)
                    $ stfny_clths_ch13 = 0
                    show v13m9 with dissolve
                    $ renpy.pause(0.5, hard=True)
                    play sound "audio/Cloth_rustle.wav"
                    $ renpy.pause(8.5, hard=True)
                    show v13m10 with dissolve
                    play background_s "audio/lewd (stolen from Atem)/Sex slow.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                    stfny "Hnnn~... What are you... Ahhh~..."
                    stfny "Mnnn~... Hnnn~..."
                    stfny "[mc_name]... We shouldn't push it... Ahn~..."
                    stfny "Someone could come any second..."
                    z "Don't worry... You're the only one who's gonna come..."
                    stfny "Fuhhnn~... You littl-"
                    hide screen stop_stfny_ch13
                    hly "Tamara!"
                    scene v13327
                    play sound "audio/RecordScratch (thanks senpai).ogg"
                    stop music
                    stop background_s
                    with vpunch
                    stfny "!!!"
                    hly "Tamara? Are you there?!"
                    scene v13328 with dissolve
                    stfny "Fuck! Hide!"
                    scene v13329 with Dissolve(1)
                    with Pause(1)
                    scene v13331 with Dissolve(1)
                    hly "..."
                    scene v13332 with dissolve
                    hly "Stephanie?"
                    scene v13333 with dissolve
                    hly "Did you see Tamara? I've been looking all around for her."
                    play background_s "audio/lewd (stolen from Atem)/Sex slow.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                    show v13m11 with Dissolve(1)
                    stfny "T-Tamara?"
                    stfny "Nnnnnooo?"
                    hly "What on earth are you doing there?"
                    stfny "Oh, this? I'm just streching..."
                    hly "..."
                    play music "audio/the last unicorn.mp3" volume 0.05 fadeout 1.0 fadein 1.0 loop
                    play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                    show v13m12 with Dissolve(1)
                    hly "Wait, I can't see you properly from here... Are you naked?"
                    stfny "O-Of course not... Hahhhh~..."
                    stfny "I'm just... Hnnnn~..."
                    hly "Why are you so sweaty?"
                    stfny "Well... Hahhh~... Ahhhh~... You know... The illusion is usually intense enough for you to sweat in real life, right?"
                    hly "Oohhh... I guess you had it rough against Sirius."
                    hly "You should go take a shower, honey. Almost everyone does it after each round. I just didn't really sweat a lot in the first round, so I didn't need to."
                    stfny "Ahhh~... Ohhhh~... I see... Hnnn~..."
                    hly "Which reminds me... Maybe Tamara is taking a shower?"
                    stfny "{size=-10}Fuck! The showers are this way!{/size}"
                    stfny "{size=-10}We need to stop, [mc_name]!{/size}"
                    z "{size=-10}Fuck... Easier said than done... It feels too good to stop!{/size}"
                    stfny "{size=-10}She's fucking coming over!{/size}"
                    stfny "{size=-10}Ahhhnnn~... Fuck... I'm cumming... I'm cumming...{/size}"
                    stfny "{size=-10}Hahhhh~... She's gonna find us like this while I fucking cum...{/size}"
                    play sound "audio/whoosh.mp3"
                    stop background_s
                    scene v13343 with PushMove(0.1, mode="pushright")
                    cndy "Uhmmm... Hailey?" (multiple=2)
                    hly "?" (multiple=2)
                    scene v13344 with Dissolve(1)
                    hly "Yeah?"
                    scene v13345 with dissolve
                    cndy "Did you see Torr? I wanted to borrow a shirt from her but I couldn't find her at the showers."
                    scene v13344 with dissolve
                    hly "Torr? Yeah... She's in her room, I think?"
                    play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                    show v13m13 with Dissolve(1)
                    cndy "Eh? She didn't take a shower?"
                    hly "I'm not sure... But she has to get ready for the next round doesn't she?"
                    cndy "Next round?"
                    cndy "Oh, she won the first match?"
                    hly "Yup. It was close but she beat Tamara."
                    hly "Speaking of which, you were at the showers?"
                    cndy "Yeah, why?"
                    hly "Was Tamara there?"
                    cndy "Yeah. I wanted to borrow one of her shirts, but it was too small."
                    cndy "Oooh. So that's why she was there and Torr wasn't."
                    stop background_s
                    scene v13346 with Dissolve(1)
                    hly "Well, thank you, honey. I'll go look for my sister."
                    scene v13347 with dissolve
                    cndy "..."
                    scene v13348 with dissolve
                    cndy "{i}Yawns.{/i}"
                    play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.3 fadeout 1.0 fadein 1.0 loop
                    scene v13349 with dissolve
                    with Pause(1)
                    "{i}Sex sounds.{/i}"
                    scene v13350 with dissolve
                    cndy "?"
                    scene v13351 with dissolve
                    with Pause(1)
                    scene v13352 with Dissolve(1)
                    cndy "..."
                    with Pause(1)
                    play sound "audio/creak.mp3"
                    play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                    show v13m14 with Dissolve(1)
                    cndy "..."
                    stfny "Nhhhmmm~... Nnmmmm~..."
                    z "Huffhhh..."
                    stfny "Mnnn~... Hmmmmm~... Ahmmmnn~..."
                    cndy "..."
                    scene v13353 with Dissolve(1)
                    cndy "(What the-)"
                    play sound "audio/whoosh.mp3"
                    scene v13354 with dissolve
                    cndy "Ah!{w=0.7}{nw}"
                    play sound "audio/Falling2.mp3"
                    stop background_s fadeout 1.0
                    stop background_s2 fadeout 1.0
                    stop music fadeout 1.0
                    scene v13355 with vpunch
                    cndy "Aww..."
                    scene v13356 with Dissolve(1)
                    stfny "Waiihhhtthhh... Shhtoohhhpppff~..."
                    z "Too late... I'm gonna fucking c-"
                    scene v13357
                    play audio "audio/creak.mp3"
                    play sound "audio/magic 7.mp3"
                    with vpunch
                    stfny "Ahhhnnn~!" (multiple=2)
                    z "Fuhhhcckkk!" (multiple=2)
                    with Pause(1)
                    play sound "audio/Falling2.mp3"
                    scene v13358 with Dissolve(1)
                    stfny "Gahhhh..."
                    if came_from_gallery == 0:
                        $ stfny_lst += 4
                    show screen button_lst with dissolve
                    play sound "audio/stats.wav"
                    hide screen button_lst with dissolve
                    play sound "audio/whoosh.mp3"
                    scene v13359 with PushMove(0.1, mode="pushright")
                    z "..."
                    play background_s2 "audio/heartbeat.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
                    scene v13360 with Dissolve(1)
                    cndy "..."
                    scene v13361 with Dissolve(1)
                    z "(Someone is totally there... I can't hear them breathing...)"
                    with Pause(1)
                    if cndy_lst < 17:
                        jump let_it_go_ch13
                    menu:
                        "Let it go.":
                            label let_it_go_ch13:
                            stop background_s2 fadeout 1.0
                            z "(Oh, well. Hopefully, they didn't notice anything.)"
                            z "(I should get ready for my next match anyway.)"
                            scene v13362 with Dissolve(1)
                            with Pause(1)
                            scene v13363 with Dissolve(1)
                            cndy "(That was close...)"
                            with Pause(1.5)
                            if came_from_gallery == 1:
                                $ came_from_gallery = 0
                            $ renpy.end_replay()
                        "Check who it is.":
                            $ had_sex_with_stfny_n_cndy_ch13 = 1
                            with Pause(1)
                            stop background_s2 fadeout 1.0
                            show v13m15 with dissolve
                            $ renpy.pause(0.5, hard=True)
                            play sound "audio/whoosh cinematic.mp3" volume 0.3
                            $ renpy.pause(2.5, hard=True)
                            scene v13364 with dissolve
                            z "Well, well, well... What do we have here..."
                            scene v13365 with dissolve
                            z "Didn't your mom tell you it's rude to eavesdrop on poeple, Candy?"
                            scene v13366
                            play sound "audio/Slap2.mp3"
                            with vpunch
                            z "Looks like we're gonna have to teach you a lesson!" (multiple=2)
                            cndy "!" (multiple=2)
                            scene v13367 with dissolve
                            with Pause(2)
                            play music "audio/the last unicorn.mp3" volume 0.05 fadeout 1.0 fadein 1.0 loop
                            play background_s "audio/lewd (stolen from Atem)/Sex slow-meduim.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                            show v13m16 with Dissolve(1)
                            cndy "Nhhhhmm~... Aaahhhhnnn~..."
                            stfny "..."
                            z "Damn, Candy... If you weren't so tight my dick might've given up after blasting a load inside Stehpy here..."
                            stfny "H-Hey... Don't tell her that..."
                            z "She already saw us, Stephanie... And you're literally sitting there naked in front of her..."
                            cndy "Ahhhnn~... I'm shorrryyy~..."
                            stfny "Fuck... Listen, Candy... I can explain..."
                            cndy "Ahhhh~... Hahh~..."
                            z "I don't think she cares right now, Stephie..."
                            cndy "Ahhh~... I... Haaaannnhh~..."
                            stfny "..."
                            stfny "Fuck... There goes my respect as your teacher..."
                            cndy "Hnnn~... Mmmm~..."
                            z "Maybe she'll come to see you as a really cool teacher... I mean, I do."
                            stfny "..."
                            cndy "Stephhhhh~... Ahhnnn~..."
                            cndy "Ahhh~... Hahhh~... Nhhhnn~..."
                            z "Fuck... I'm gonna cum..."
                            stfny "Wait a second..."
                            stfny "Should you really cum inside her?!"
                            cndy "Ahhh~... Yesshhhh~... Insiiihhddde~..."
                            stfny "You should really pul-"
                            stop background_s fadeout 1.0
                            with Pause(1)
                            scene v13368
                            play audio "audio/creak.mp3"
                            play sound "audio/magic 7.mp3"
                            with vpunch
                            cndy "NGGHHH~!"
                            show v13m17 with Dissolve(1)
                            play background_s "audio/lewd (stolen from Atem)/Sex slow-meduim.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                            stfny "Waihhht~... I need to r- Ahhhh~... Rest..."
                            stfny "Ahhh~... Water... At least... Hahh~... Gimme water..."
                            z "Can't see any water around here... I'm sure you can wait a bit more..."
                            stfny "Ahhh~... Candy... Don't look... I'm making a dumb face... Ahhnn~..."
                            z "Don't worry, I don't think she has the energy to look anywhere..."
                            stfny "Okayy... Ahhhnn~..."
                            stfny "Waihht... What about your... Nhhnn~... Match?"
                            z "Oh..."
                            z "It's okay... I'm about to cum anyway..."
                            z "I'll leave right after." (multiple=2)
                            stfny "Ahhn~... Wait... You're about to-" (multiple=2)
                            z "Fuck... I'm cumming, Stephie..."
                            stfny "Wait... Ahhh~... Maybe do it outside? Hahh~... Don't get me pregn-"
                            z "Too late..."
                            stop background_s fadeout 1.0
                            with Pause(1)
                            scene v13369
                            play audio "audio/creak.mp3"
                            play sound "audio/magic 7.mp3"
                            with vpunch
                            stop music fadeout 2.0
                            stfny "Aaaahhhhh~!"
                            play sound "audio/cloth.mp3"
                            scene v13370 with Dissolve(1)
                            z "Fuck... I'm totally spent..."
                            scene v13371 with Dissolve(1)
                            if came_from_gallery == 0:
                                $ stfny_lst += 2
                                $ cndy_lst += 5
                            show screen button_lst with dissolve
                            play sound "audio/stats.wav"
                            hide screen button_lst with dissolve
                            z "You guys okay, down there?"
                            "{i}Both giggling.{/i}"
                            z "I'll take that as a yes?"
                            z "Anyway, I need to go..."
                            z "See ya, guys..."
                            with Pause(1)
                            if came_from_gallery == 1:
                                $ came_from_gallery = 0
                            $ renpy.end_replay()
                "You need to leave and get ready.":
                    scene v13324 with vpunch
                    label z_leaves_ch13:
                    hide screen stop_stfny_ch13
                    play sound "audio/RecordScratch (thanks senpai).ogg"
                    stop music
                    z "Wait a fucking second!"
                    play sound "audio/creak.mp3"
                    if stfny_clths_ch13 == 2:
                        scene v13334 with vpunch
                    elif stfny_clths_ch13 == 1:
                        scene v13335 with vpunch
                    else:
                        scene v13336 with vpunch
                    z "I need to go! My match is gonna start soon!"
                    hide v13m6
                    hide v13m7
                    hide v13m8
                    hide v13m9
                    hide v13m10
                    z "Wish me luck!"
                    if stfny_clths_ch13 == 2:
                        scene v13337 with Dissolve(1)
                    elif stfny_clths_ch13 == 1:
                        scene v13338 with Dissolve(1)
                    else:
                        scene v13339 with Dissolve(1)
                    stfny "Yup! Good luck, kiddo! Break a leg!"
                    if stfny_clths_ch13 == 2:
                        scene v13340 with dissolve
                    elif stfny_clths_ch13 == 1:
                        scene v13341 with dissolve
                    else:
                        scene v13342 with dissolve
                    z "{size=-10}THANKS!{/size}"
                    with Pause(1.5)
        else:
            scene v13321 with dissolve
            z "Why thank you."
            scene v13320 with dissolve
            stfny "Now go get ready. You have a difficult match ahead of you."
            scene v13321 with dissolve
            z "Yup."
            z "See you later, Stephie."
            stfny "Hmm."
            with Pause(1.5)
        scene black with fade
        with Pause(1.5)
        stop background_s fadeout 1.0
        stop background_s2 fadeout 1.0
        stop music fadeout 1.0
        stop sound fadeout 1.0
        with Pause(1)
        play music "audio/under pressure michael kobrin.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
        scene v13372 with Dissolve(1.5)
        with Pause(1.5)
        scene v13373 with Dissolve(1)
        with Pause(1)
        play audio "audio/Magic 9.mp3"
        scene v13374 with Dissolve(1)
        with Pause(1)
        scene v13375 with Dissolve(1)
        z "..."
        scene v13376 with Dissolve(1)
        z "(What's with the pins...)"
        play sound "audio/Cloth_rustle.wav"
        scene v13377 with dissolve
        z "(They feel very dangerous for some reason...)"
        z "(I absolutely can't get hit b-)"
        show v13m18 with Dissolve(0.25)
        $ renpy.pause(0.6, hard=True)
        play audio "audio/whoosh.mp3"
        play sound "audio/sword into wood.mp3"
        $ renpy.pause(0.1, hard=True)
        scene v13378
        with vpunch
        with Pause(1)
        scene v13380 with Dissolve(1)
        z "(Fuck! That was close!)"
        scene v13381 with dissolve
        z "(Seems this is gonna be harder than Venus's fight...)"
        scene v13382 with Dissolve(1)
        z "(She's smirking?)"
        scene v13383 with Dissolve(1)
        z "(What is she-)"
        play sound "audio/Stab.mp3"
        scene v13384
        with vpunch
        z "!"
        scene v13385 with PushMove(0.05, mode="pushright")
        z "..."
        scene v13386
        play sound "audio/Falling2.mp3"
        with vpunch
        z "Ughhh!"
        z "(Fuck... That hurt...)"
        z "(How... Why did my own arm attack me without me noticing...)"
        with Pause(1)
        play audio "audio/Magic 9.mp3"
        scene v13387 with Dissolve(1)
        hly "..."
        with Pause(1)
        play sound "audio/sword cut 2.mp3"
        scene v13388 with vpunch
        z "UGHHH!"
        show v13m19 with dissolve
        z "(What the-){w=0.5}{nw}"
        play sound "audio/sword cut.mp3"
        $ renpy.pause(2.5, hard=True)
        play audio "audio/Stab.mp3" volume 0.8
        scene v13389
        play sound "audio/electric-shock.mp3" volume 0.4
        with vpunch
        hly "!!!"
        play background_s2 "audio/heartbeat.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
        show v13m20 with dissolve
        $ renpy.pause(2, hard=True)
        z "(I get it now...){w=1.5}{nw}"
        z "(If she hits me with a pin, she can control the part of my body that was hit using her doll.){w=5}{nw}"
        z "(I guess I must've gotten hit by a pin somehow...){w=3}{nw}"
        $ renpy.pause(4.5, hard=True)
        play audio "audio/Stab.mp3"
        stop background_s2
        $ renpy.pause(2.5, hard=True)
        scene v13391 with dissolve
        hly "..."
        scene v13392 with dissolve
        hly "F-Fuck..."
        scene v13393 with PushMove(0.05, mode="pushright")
        play sound "audio/Falling2.mp3"
        play audio "audio/whoosh.mp3"
        with vpunch
        hly "EEEEK!"
        scene v13394 with dissolve
        z "..."
        play sound "audio/Cloth_rustle.wav"
        scene v13395 with Dissolve(1)
        hly "Phew..."
        play sound "audio/sword draw.mp3"
        scene v13396 with dissolve
        hly "I must admit I almost thought I had lost a moment ago..."
        scene v13397 with dissolve
        play sound "audio/whoosh cinematic.mp3" volume 0.4
        show v13m21 with Dissolve(0.25)
        $ renpy.pause(1.7, hard=True)
        scene v13398 with Dissolve(0.8)
        with Pause(1.5)
        scene v13399 with Dissolve(1.2)
        hly "..."
        stop background_s fadeout 1.0
        stop background_s2 fadeout 1.0
        stop music fadeout 1.0
        stop sound fadeout 1.0
        play background_s2 "audio/Ambient_ninja_village_night.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
        scene v13400 with Dissolve(1)
        with Pause(1.5)
        scene v13401 with Dissolve(1)
        tr "..." (multiple=2)
        cnt "..." (multiple=2)
        play audio "audio/explosion (long).mp3" volume 0.2
        with Pause(0.15)
        scene v13402 with vpunch
        with vpunch
        with vpunch
        with vpunch
        with vpunch
        with vpunch
        with vpunch
        with vpunch
        with Pause(1)
        with vpunch
        with vpunch
        with vpunch
        with vpunch
        with vpunch
        tr "..." (multiple=2)
        cnt "..." (multiple=2)
        scene v13403 with Dissolve(1)
        with Pause(1.5)
        play audio "audio/tournament.mp3"
        scene v13404 with Dissolve(1)
        with Pause(2.5)
        if had_sex_with_stfny_n_cndy_ch13 == 1:
            play sound "audio/whoosh.mp3"
            scene v13405 with PushMove(0.1, mode="pushright")
            cndy "Uhmm... Guys?"
            scene v13406 with Dissolve(1)
            tr "..."
            tr "The fuck happened to you two?!"
            scene v13407 with dissolve
            cndy "Welllll... You know..."
            cndy "I just came out of the shower and wanted to borrow a shirt from you... But I couldn't find you, so..."
            scene v13406 with dissolve
            tr "..."
            tr "And your pants?"
            scene v13407 with dissolve
            cndy "I didn't know what to match the shirt with, you see..."
            scene v13406 with dissolve
            tr "..."
            tr "Wait, Stephanie? Why are you naked too, then?"
            scene v13408 with dissolve
            stfny "I was..."
            stfny "Helping Candy find something to wear! Yes!"
            stfny "And then Candy was feeling shy being the only one naked! So I took off my clothes too, you see..."
            scene v13407 with dissolve
            cndy "Anyway, the details aren't important... Can you grab us some clothes now, please..."
            scene v13406 with dissolve
            tr "..."
            tr "Sure... Gimme a minute..."
            with Pause(1.5)
        scene black with fade
        with Pause(1.5)
        scene v13409 with Dissolve(1.5)
        cndy "..."
        scene v13410 with dissolve
        a "Mind if I join you?"
        play audio "audio/creak.mp3"
        scene v13411 with Dissolve(1)
        a "Are my siblings up yet?"
        scene v13412 with dissolve
        cndy "Yeah. I think Sirius is winning."
        scene v13411 with dissolve
        a "How did [mc_name] do? Did he win?"
        scene v13412 with dissolve
        cndy "It was close, but he won, yeah."
        scene v13413 with dissolve
        a "Hmmm..."
        show v13m22 with dissolve
        $ renpy.pause(0.5, hard=True)
        play sound "audio/whoosh cinematic.mp3" volume 0.1
        stop background_s fadeout 1.0
        stop background_s2 fadeout 1.0
        $ renpy.pause(1.2, hard=True)
        scene black with dissolve
        play background_s2 "audio/heartbeat.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
        show v13m23 with Dissolve(1.5)
        with Pause(1)
        ymi "{i}Hyperventilating.{/i}"
        a "It's not looking good for Yumi..."
        cndy "Why is she just standing there?"
        a "She's cornered..."
        cndy "But she can run to the left or right."
        a "No."
        a "Sirius's lance has a very big range. Not to mention he tends to launch magic projectiles while swinging it, increasing the range of his attacks even further."
        a "And that thing is extremely heavy. I can't even lift it, and Sirius can swing it really quickly, so you can imagine the momentum it would deliver if you were to be hit by it ."
        a "Even if he doesn't hit a vital spot or punches a hole in you with it, you can kiss half the bones in your body goodbye once it touches you at that speed."
        cndy "Gods..."
        with Pause(1)
        stop background_s2 fadeout 1.0
        scene v13414 with Dissolve(1)
        cndy "So it's over for Yumi?"
        a "She might yet have a trick or two to play..."
        play audio "audio/whoosh.mp3"
        scene v13415 with PushMove(0.1, mode="pushright")
        with Pause(1)
        play sound "audio/Punch2.mp3"
        scene v13416 with vpunch
        srs "UGH!"
        play sound "audio/Falling2.mp3"
        scene v13417 with PushMove(0.05, mode="pushright")
        with vpunch
        with Pause(0.3)
        cndy "A clone?!"
        scene v13418 with Dissolve(1)
        play sound "audio/whoosh cinematic.mp3" volume 0.2
        scene v13419 with Dissolve(1)
        cndy "She distracted him! Maybe her real body could atta-"
        play sound "audio/Stab.mp3"
        scene v13420 with vpunch
        ymi "Guhhhggg!"
        scene v13421 with dissolve
        cndy "Oh, no..."
        play audio "audio/blood squirt.mp3"
        scene v13422 with vpunch
        ymi "UGHH!"
        scene v13423 with dissolve
        ymi "..."
        scene v13424 with Dissolve(1)
        with Pause(1)
        a "I suppose that was probably the best strategy in the situation she was in..."
        cndy "So it was not possible for her to defeat Sirius?"
        scene v13425 with Dissolve(1)
        a "Yumi? I don't think so, honey..."
        a "I don't think any of the ninjas in the village can even touch Sirius..."
        scene v13426 with Dissolve(1)
        a "Maybe Seira can give him a hard time, though... I can't be sure..."
        scene v13427 with Dissolve(1)
        play sound "audio/whoosh cinematic.mp3" volume 0.2
        scene v13428 with Dissolve(1)
        scene white with Dissolve(1)
        with Pause(1.5)
        scene v13429 with Dissolve(1)
        with Pause(1.5)
        play audio "audio/tournament.mp3"
        scene v13430 with Dissolve(1)
        with Pause(2.5)
        scene black with fade
        with Pause(1.5)
        stop background_s fadeout 1.0
        stop background_s2 fadeout 1.0
        stop music fadeout 1.0
        stop sound fadeout 1.0
        play background_s2 "audio/Ambient_ninja_village_night.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
        scene v13431 with Dissolve(1)
        with Pause(1)
        scene v13435 with dissolve
        cndy "Do you guys think Torr might somehow win this one?"
        scene v13432 with dissolve
        z "Nope."
        scene v13433 with dissolve
        a "I don't want to be mean, but I'll have to agree with [mc_name]..."
        a "Torr should play on her strengths... In this case, it would be the fire magic she can use."
        a "Trouble is, Seira's reflexes are very sharp, you can't expect to hit her with a projectile from a distance..."
        scene v13432 with dissolve
        z "Yeah. I can confirm that. One time, I couldn't even touch her after transforming and you guys know how fast I can move after I transform..."
        scene v13433 with dissolve
        a "Yeah... You basically teleport..."
        scene v13434 with dissolve
        cndy "..."
        scene v13436 with dissolve
        a "Torr will need a solid strategy to actually beat Seira. Raw strength or magic isn't going to play in her favour here..."
        a "But in her case, she definitely didn't have enough time to put together a good strategy. One of the main points of the tournament is that you won't know for sure who you're fighting the next round."
        a "It's a test of how well you can improvise and do your best fighting someone stronger than you, which is why the low ranking ninjas were purposefully matched with higher ranked ones in the first round."
        stop background_s fadeout 1.0
        stop background_s2 fadeout 1.0
        scene v13438 with Dissolve(1.5)
        play music "audio/ZvsFury.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
        a "That aside, in Torr's case, she probably doesn't have nearly enough experience fighting overwhelmingly stronger opponents like Seira to strategise accordingly..."
        scene v13439 with Dissolve(1)
        z "I think the only chance Torr would've had in this case, is Seira tremendously underestimating her... Which knowing Seira, she won't."
        with Pause(1)
        play background_s "audio/Magic (Fire) Loop.mp3" volume 0.3 fadeout 1.0 fadein 1.0 loop
        scene v13440 with Dissolve(1)
        cndy "..."
        scene v13441 with Dissolve(1)
        cndy "She's going to use the fire ball!"
        scene v13442 with Dissolve(1)
        cndy "What happens if that hits Seira?"
        z "I don't think even Seira can survive that."
        a "Agreed."
        with Pause(1)
        show v13m24 with dissolve #L=2.85 sec
        $ renpy.pause(0.25, hard=True)
        play sound "audio/Magic5.mp3"
        stop background_s
        $ renpy.pause(0.75, hard=True)
        play audio "audio/explosion2 (loud).mp3"
        $ renpy.pause(1.85, hard=True)
        scene black
        play sound "audio/sword cut 2.mp3"
        stop music
        with vpunch
        cndy "AAAH!"
        with Pause(1)
        scene v13443 with Dissolve(1.5)
        with Pause(2)
        play sound "audio/whoosh cinematic.mp3" volume 0.3
        scene v13444 with Dissolve(2)
        scene white with Dissolve(2)
        with Pause(1.5)
        play background_s2 "audio/Ambient_ninja_village_night.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
        scene v13445 with Dissolve(1)
        z "Well, I'd better be off... I wanna take a quick shower before my match."
        scene v13446 with Dissolve(1)
        with Pause(1.5)
        scene v13447 with Dissolve(1)
        with Pause(1.5)
        play audio "audio/tournament.mp3"
        scene v13448 with Dissolve(1)

        if tr_lst >= 18 and cndy_lst >= 17:
            with Pause(2.5)
            label G52:
                $ persistent.g_52_unlock = 1
            stop background_s fadeout 1.0
            stop background_s2 fadeout 1.0
            stop music fadeout 1.0
            stop sound fadeout 1.0
            scene v13449 with Dissolve(1)
            tr "Ughhh... Fucking shoes..."
            z "Ohh..."
            scene v13450 with Dissolve(1)
            z "Torr... I could come back later..."
            play audio "audio/Cloth_rustle.wav"
            scene v13451 with dissolve
            tr "No, no. There's no need for that. You've seen me with less clothes that this, didn't you?"
            play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
            scene v13452 with Dissolve(1)
            z "Sure, I have. Doesn't mean you don't have the right for privacy anymore."
            scene v13453 with dissolve
            tr "I know. Thanks, [mc_name]."
            scene v13452 with dissolve
            z "I expected you to be feeling down after your fight."
            scene v13454 with dissolve
            tr "Eh. It's okay. Defeating a Keres is still well out of my league."
            scene v13453 with dissolve
            tr "Plus, Seira was really nice. She pointed out the flaws in my strategy. But she actually said it was pretty good overall."
            tr "She even said, I might've had a chance if she didn't know about my fire balls. So that's a nice condfidence boost."
            scene v13452 with dissolve
            z "Sounds like Seira."
            scene v13453 with dissolve
            tr "I now know how you came to be so strong. Being trained by someone like her and all."
            tr "Of course, you're also quite talented, aren't you..."
            scene v13452 with dissolve
            z "Hm? Who are you and what have you done with Torr?"
            scene v13454 with dissolve
            tr "Heh, seeing how I'm the higher ranking ninja now, I thought I might give my underclassmate some compliments."
            scene v13452 with dissolve
            z "Okay, you're back to normal."
            z "You almost sounded like Candy a moment ago."
            scene v13453 with dissolve
            tr "Did I? If I were Candy with my boobs out, you'd probably be balls deep inside me right now."
            scene v13452 with dissolve
            z "Heh... Maybe..."
            scene v13453 with dissolve
            tr "Speaking of which..."
            scene v13454 with dissolve
            tr "You have some time before your next match, don't you?"
            scene v13452 with dissolve
            z "I guess so."
            z "(I think I can see where this is going...)"
            scene v13454 with dissolve
            tr "I've been thinking..."
            scene v13453 with dissolve
            tr "Can you do what you do to Candy to me?"
            scene v13452 with dissolve
            z "Huh?"
            z "(Ok I didn't expect this...)"
            scene v13453 with dissolve
            tr "You know... How you're rough with her when you two..."
            scene v13452 with dissolve
            z "Wait, how do you-"
            scene v13454 with dissolve
            tr "We talked about it, you know..."
            scene v13453 with dissolve
            tr "And her experience seems to be different from mine..."
            tr "So I wanna try her experience. If you get what I mean."
            tr "I want you to be rough with me. To manhandle me like you do her."
            scene v13452 with dissolve
            z "..."
            with Pause(1)
            menu:
                "Sure.":
                    z "Well, if that's what you want..."
                    scene v13453 with dissolve
                    tr "Nice... How do we-"
                    play sound "audio/Cloth_rustle.wav"
                    scene v13455
                    with vpunch
                    tr "MHMMM!"
                    scene v13456 with dissolve
                    tr "Mnn~..."
                    scene v13457 with dissolve
                    tr "Hahhh~..."
                    play sound "audio/cloth.mp3"
                    scene v13458
                    with vpunch
                    tr "Aaah!"
                    play sound "audio/Falling2.mp3"
                    scene v13459 with PushMove(0.05, mode="pushup")
                    with vpunch
                    tr "!"
                    scene v13460 with dissolve
                    tr "..."
                    play sound "audio/Cloth_rustle.wav"
                    scene v13461
                    with vpunch
                    tr "GUUHH~!"
                    play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                    show v13m4 with Dissolve(1)
                    tr "Fuhhhckkk~... I wasn't ready..."
                    z "You're pretty wet though..."
                    tr "I know... Hanhhh~... Ahhh~..."
                    tr "Should we... Hahhh~... Should we be doing this here..."
                    z "Probably not..."
                    tr "Someone could come in... Hahhh~... Any second..."
                    z "Do you wanna stop, then?"
                    tr "Ahh~... Hnn~... Fuck..."
                    tr "Fuhhckk no~... Keep ramming me..."
                    z "I thought not..."
                    tr "Hahhh~... I'm close... [mc_name]... I'm close..."
                    z "Go ahead and come... Don't hold back..."
                    tr "Fuhhhckkk~... I can't think straight... Ahhh~... Hahh~..."
                    tr "I'm... Mmmmnn~... Hahhh~... I'm..."
                    tr "I'm cumming... Ahh~... Hahh~... Hanhh~..."
                    z "I'm gonna cum too..."
                    tr "Shoot it... Ahh~... Hannhh~... Shoot it inside..."
                    if tmra_lst >= 7:
                        play sound "audio/creaky door.mp3"
                        "{i}Door opens.{/i}"
                        tr "Fuhhcck~... What was that..."
                        z "I don't know..."
                        tr "Someone... Ahhh~... Someone just came in... We need to stop..."
                        z "Yeah... Lemme just..."
                        play sound "audio/Falling2.mp3"
                        play audio "audio/magic 7.mp3"
                        stop background_s
                        stop background_s2
                        stop music
                        scene v13462 with vpunch
                        z "Ughh... Fuck..." (multiple=2)
                        tr "Aaaahhh~..." (multiple=2)
                        play sound "audio/Cloth_rustle.wav"
                        scene v13463 with Dissolve(1)
                        tr "Hahhh~... Fuck... That was..."
                        z "That was amazing, but we need t-"
                        scene v13464 with dissolve
                        tmra "Torr?!"
                        scene v13465 with Dissolve(1)
                        tmra "What's all that noi-"
                        scene v13466 with Dissolve(1)
                        z "..."
                        tmra "What th-"
                        tmra "..."
                        with Pause(1)
                        play audio "audio/camera.mp3"
                        scene black
                        with Pause(0.5)
                        play sound "audio/Falling2.mp3"
                        with vpunch
                        with vpunch
                        with vpunch
                        with vpunch
                        tmra "AAAH!"
                        with Pause(0.5)
                        play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
                        play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                        show v13m5 with Dissolve(1)
                        tmra "Aaaahhh~... Ahhhhh~... Fuhcckkk~..."
                        tr "How do you like that Tamara?"
                        tmra "It feelshhh..."
                        tr "Yes?"
                        tmra "Ahh~... It's... Hahh~... Doesn't feel that good... Ahh~..."
                        tr "Really? You're making a really dumb face down there..."
                        tr "Almost like you're losing it from the pleasure..."
                        tmra "That'th nohhht... Ahhh~..."
                        tr "You can't even speak properly..."
                        tr "Just admit it. You love getting piped like the little slut you are..."
                        tmra "Ahh~... Noooo~... I'm not a shlut..."
                        tmra "You and Candy... Ahhh~... You're the slutsss~..."
                        tmra "How long... Ahhh~... ...have you two been fucking him..."
                        tmra "Ahhh~... Just because you can't resist his... Ahhh~... ...huge di-"
                        tmra "Ahhhhh~ Huge asshole behaviour..."
                        tr "Play nice, Tamara..."
                        scene v13472 with Dissolve(1)
                        tr "You look really cute... Seems you already came a few times..."
                        play audio "audio/kiss.mp3"
                        scene v13473 with dissolve
                        tmra "Thut uppp..." (multiple=2)
                        tr "Ah!" (multiple=2)
                        scene v13474 with dissolve
                        tmra "Ahh~... Waihht~... What are you-"
                        scene v13475 with vpunch
                        tr "Eeep! Don't bite it!"
                        scene v13476 with dissolve
                        tr "Hannhh~... Fuhhhcckkk~..."
                        scene v13477 with Dissolve(1)
                        tmra "Hmmn~..."
                        z "..."
                        menu:
                            "Push Tamara's face closer to Torr's and make them make out.":
                                play sound "audio/Cloth_rustle.wav"
                                scene v13478 with vpunch
                                tmra "Ahh~!" (multiple=2)
                                tr "?!" (multiple=2)
                                play audio "audio/kiss.mp3"
                                scene v13479 with hpunch
                                tmra "HMNN~!" (multiple=2)
                                tr "HMMM?!" (multiple=2)
                                scene v13480 with Dissolve(1)
                                z "Be nice to each other, you two..."
                                show v13m40 with Dissolve(1)
                                tmra "Hmmnn~... Mnnn~..."
                                tr "Mmmmhhnnn~..."
                                z "Look at you getting along... So cute..."
                                tmra "Nmmmmnn~... Mhhhnn~..."
                                tr "Hmmmn~... Ahhmmmm~..."
                                z "Two besties putting their differences behind and joining their lips..."
                                tr "Hmmmnnn~... Fuhhhmm~..."
                                tmra "Ihmmmmmnn~... Fuhhhmmm~..."
                                z "Tamara... I'm gonna cum..."
                                z "I hope you're ready... I'm shooting it inside you..."
                                tmra "Hmmnnn~?! Inmmmm~! Mhhhnnn~!"
                                z "Yeah. I don't understand... I'm gonna cum..."
                                tmra "Mhhhmmmmnnn~!"
                                tmra "Hmmmm-"
                                play audio "audio/creak.mp3"
                                play sound "audio/magic 7.mp3"
                                stop background_s fadeout 1.0
                                stop background_s2 fadeout 1.0
                                scene v13481 with hpunch
                                tmra "AAAHHHHH~!" (multiple=2)
                                tr "Ahh~?!" (multiple=2)
                            "Keep fucking Tamara like this.":
                                show v13m5 with Dissolve(1)
                                tmra "Aaaannh~... Waihhtt~..."
                                z "Come back here, Tamara."
                                tr "That was rude, Tamara..."
                                tr "Don't suck on other people's nipples without permission."
                                tmra "Hahh~... It's your fault..."
                                tr "Come on, apologise."
                                tmra "Nooo~... Ahhh~... Fuck you..."
                                tr "If you say you're sorry [mc_name] might creampie you."
                                tmra "Ahhh~... C-Creampie?! Waihht~..."
                                z "Wait, I never agreed to this..."
                                tr "Come on, we need to put cocky Tamara in her place, [mc_name]..."
                                tr "If she behaves like a good girl, would you creampie her?"
                                z "I mean..."
                                tr "What do you say, Tamara? Are you a good girl?"
                                tmra "Ahh~... Fuhcckk~..."
                                tr "Now, now. Tamara. No cursing."
                                tr "Just say you're sorry. And [mc_name] will shoot all his warm load inside you."
                                tmra "Hnnn~... Ahhh~... Inshide..."
                                tr "Yup, yup. All of it inside you."
                                tr "In return for one small sorry."
                                tr "Good deal, no?"
                                tmra "Ahh~... Hahhhhh~... Anhhh~..."
                                tmra "I'm... Mmmmnn~... Hahhh~... I'm..."
                                tmra "I'm cumming... Ahh~... Hahh~... Hanhh~..."
                                z "I'm gonna cum too..."
                                tr "Shoot it... Ahh~... Hannhh~... Shoot it inside..."
                                if tmra_lst >= 7:
                                    play sound "audio/creaky door.mp3"
                                    "{i}Door opens.{/i}"
                                    tr "Fuhhcck~... What was that..."
                                    z "I don't know..."
                                    tr "Someone... Ahhh~... Someone just came in... We need to stop..."
                                    z "Yeah... Lemme just..."
                                    play sound "audio/Falling2.mp3"
                                    play audio "audio/magic 7.mp3"
                                    stop background_s
                                    stop background_s2
                                    stop music
                                    scene v13462 with vpunch
                                    z "Ughh... Fuck..." (multiple=2)
                                    tr "Aaaahhh~..." (multiple=2)
                                    play sound "audio/Cloth_rustle.wav"
                                    scene v13463 with Dissolve(1)
                                    tr "Hahhh~... Fuck... That was..."
                                    z "That was amazing, but we need t-"
                                    scene v13464 with dissolve
                                    tmra "Torr?!"
                                    scene v13465 with Dissolve(1)
                                    tmra "What's all that noi-"
                                    scene v13466 with Dissolve(1)
                                    z "..."
                                    tmra "What th-"
                                    tmra "..."
                                    with Pause(1)
                                    play audio "audio/camera.mp3"
                                    scene black
                                    with Pause(0.5)
                                    play sound "audio/Falling2.mp3"
                                    with vpunch
                                    with vpunch
                                    with vpunch
                                    with vpunch
                                    tmra "AAAH!"
                                    with Pause(0.5)
                                    play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
                                    play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                                    show v13m5 with Dissolve(1)
                                    tmra "Aaaahhh~... Ahhhhh~... Fuhcckkk~..."
                                    tr "How do you like that Tamara?"
                                    tmra "It feelshhh..."
                                    tr "Yes?"
                                    tmra "Ahh~... It's... Hahh~... Doesn't feel that good... Ahh~..."
                                    tr "Really? You're making a really dumb face down there..."
                                    tr "Almost like you're losing it from the pleasure..."
                                    tmra "That'th nohhht... Ahhh~..."
                                    tr "You can't even speak properly..."
                                    tr "Just admit it. You love getting piped like the little slut you are..."
                                    tmra "Ahh~... Noooo~... I'm not a shlut..."
                                    tmra "You and Candy... Ahhh~... You're the slutsss~..."
                                    tmra "How long... Ahhh~... ...have you two been fucking him..."
                                    tmra "Ahhh~... Just because you can't resist his... Ahhh~... ...huge di-"
                                    tmra "Ahhhhh~ Huge asshole behaviour..."
                                    tr "Play nice, Tamara..."
                                    scene v13472 with Dissolve(1)
                                    tr "You look really cute... Seems you already came a few times..."
                                    play audio "audio/kiss.mp3"
                                    scene v13473 with dissolve
                                    tmra "Thut uppp..." (multiple=2)
                                    tr "Ah!" (multiple=2)
                                    scene v13474 with dissolve
                                    tmra "Ahh~... Waihht~... What are you-"
                                    scene v13475 with vpunch
                                    tr "Eeep! Don't bite it!"
                                    scene v13476 with dissolve
                                    tr "Hannhh~... Fuhhhcckkk~..."
                                    scene v13477 with Dissolve(1)
                                    tmra "Hmmn~..."
                                    z "..."
                                    menu:
                                        "Push Tamara's face closer to Torr's and make them make out.":
                                            play sound "audio/Cloth_rustle.wav"
                                            scene v13478 with vpunch
                                            tmra "Ahh~!" (multiple=2)
                                            tr "?!" (multiple=2)
                                            play audio "audio/kiss.mp3"
                                            scene v13479 with hpunch
                                            tmra "HMNN~!" (multiple=2)
                                            tr "HMMM?!" (multiple=2)
                                            scene v13480 with Dissolve(1)
                                            z "Be nice to each other, you two..."
                                            show v13m40 with Dissolve(1)
                                            tmra "Hmmnn~... Mnnn~..."
                                            tr "Mmmmhhnnn~..."
                                            z "Look at you getting along... So cute..."
                                            tmra "Nmmmmnn~... Mhhhnn~..."
                                            tr "Hmmmn~... Ahhmmmm~..."
                                            z "Two besties putting their differences behind and joining their lips..."
                                            tr "Hmmmnnn~... Fuhhhmm~..."
                                            tmra "Ihmmmmmnn~... Fuhhhmmm~..."
                                            z "Tamara... I'm gonna cum..."
                                            z "I hope you're ready... I'm shooting it inside you..."
                                            tmra "Hmmnnn~?! Inmmmm~! Mhhhnnn~!"
                                            z "Yeah. I don't understand... I'm gonna cum..."
                                            tmra "Mhhhmmmmnnn~!"
                                            tmra "Hmmmm-"
                                            play audio "audio/creak.mp3"
                                            play sound "audio/magic 7.mp3"
                                            stop background_s fadeout 1.0
                                            stop background_s2 fadeout 1.0
                                            scene v13481 with hpunch
                                            tmra "AAAHHHHH~!" (multiple=2)
                                            tr "Ahh~?!" (multiple=2)
                                        "Keep fucking Tamara like this.":
                                            show v13m5 with Dissolve(1)
                                            tmra "Aaaannh~... Waihhtt~..."
                                            z "Come back here, Tamara."
                                            tr "That was rude, Tamara..."
                                            tr "Don't suck on other people's nipples without permission."
                                            tmra "Hahh~... It's your fault..."
                                            tr "Come on, apologise."
                                            tmra "Nooo~... Ahhh~... Fuck you..."
                                            tr "If you say you're sorry [mc_name] might creampie you."
                                            tmra "Ahhh~... C-Creampie?! Waihht~..."
                                            z "Wait, I never agreed to this..."
                                            tr "Come on, we need to put cocky Tamara in her place, [mc_name]..."
                                            tr "If she behaves like a good girl, would you creampie her?"
                                            z "I mean..."
                                            tr "What do you say, Tamara? Are you a good girl?"
                                            tmra "Ahh~... Fuhcckk~..."
                                            tr "Now, now. Tamara. No cursing."
                                            tr "Just say you're sorry. And [mc_name] will shoot all his warm load inside you."
                                            tmra "Hnnn~... Ahhh~... Inshide..."
                                            tr "Yup, yup. All of it inside you."
                                            tr "In return for one small sorry."
                                            tr "Good deal, no?"
                                            tmra "Ahh~... Hahhhhh~... Anhhh~..."
                                            tmra "I'm... Mmmmnn~... Hahhh~... I'm..."
                                            tmra "I'm cumming... Ahh~... Hahh~... Hanhh~..."
                                            z "I'm gonna cum too..."
                                            tr "Shoot it... Ahh~... Hannhh~... Shoot it inside..."
                                            if tmra_lst >= 7:
                                                play sound "audio/creaky door.mp3"
                                                "{i}Door opens.{/i}"
                                                tr "Fuhhcck~... What was that..."
                                                z "I don't know..."
                                                tr "Someone... Ahhh~... Someone just came in... We need to stop..."
                                                z "Yeah... Lemme just..."
                                                play sound "audio/Falling2.mp3"
                                                play audio "audio/magic 7.mp3"
                                                stop background_s
                                                stop background_s2
                                                stop music
                                                scene v13462 with vpunch
                                                z "Ughh... Fuck..." (multiple=2)
                                                tr "Aaaahhh~..." (multiple=2)
                                                play sound "audio/Cloth_rustle.wav"
                                                scene v13463 with Dissolve(1)
                                                tr "Hahhh~... Fuck... That was..."
                                                z "That was amazing, but we need t-"
                                                scene v13464 with dissolve
                                                tmra "Torr?!"
                                                scene v13465 with Dissolve(1)
                                                tmra "What's all that noi-"
                                                scene v13466 with Dissolve(1)
                                                z "..."
                                                tmra "What th-"
                                                tmra "..."
                                                with Pause(1)
                                                play audio "audio/camera.mp3"
                                                scene black
                                                with Pause(0.5)
                                                play sound "audio/Falling2.mp3"
                                                with vpunch
                                                with vpunch
                                                with vpunch
                                                with vpunch
                                                tmra "AAAH!"
                                                with Pause(0.5)
                                                play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
                                                play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                                                show v13m5 with Dissolve(1)
                                                tmra "Aaaahhh~... Ahhhhh~... Fuhcckkk~..."
                                                tr "How do you like that Tamara?"
                                                tmra "It feelshhh..."
                                                tr "Yes?"
                                                tmra "Ahh~... It's... Hahh~... Doesn't feel that good... Ahh~..."
                                                tr "Really? You're making a really dumb face down there..."
                                                tr "Almost like you're losing it from the pleasure..."
                                                tmra "That'th nohhht... Ahhh~..."
                                                tr "You can't even speak properly..."
                                                tr "Just admit it. You love getting piped like the little slut you are..."
                                                tmra "Ahh~... Noooo~... I'm not a shlut..."
                                                tmra "You and Candy... Ahhh~... You're the slutsss~..."
                                                tmra "How long... Ahhh~... ...have you two been fucking him..."
                                                tmra "Ahhh~... Just because you can't resist his... Ahhh~... ...huge di-"
                                                tmra "Ahhhhh~ Huge asshole behaviour..."
                                                tr "Play nice, Tamara..."
                                                scene v13472 with Dissolve(1)
                                                tr "You look really cute... Seems you already came a few times..."
                                                play audio "audio/kiss.mp3"
                                                scene v13473 with dissolve
                                                tmra "Thut uppp..." (multiple=2)
                                                tr "Ah!" (multiple=2)
                                                scene v13474 with dissolve
                                                tmra "Ahh~... Waihht~... What are you-"
                                                scene v13475 with vpunch
                                                tr "Eeep! Don't bite it!"
                                                scene v13476 with dissolve
                                                tr "Hannhh~... Fuhhhcckkk~..."
                                                scene v13477 with Dissolve(1)
                                                tmra "Hmmn~..."
                                                z "..."
                                                menu:
                                                    "Push Tamara's face closer to Torr's and make them make out.":
                                                        play sound "audio/Cloth_rustle.wav"
                                                        scene v13478 with vpunch
                                                        tmra "Ahh~!" (multiple=2)
                                                        tr "?!" (multiple=2)
                                                        play audio "audio/kiss.mp3"
                                                        scene v13479 with hpunch
                                                        tmra "HMNN~!" (multiple=2)
                                                        tr "HMMM?!" (multiple=2)
                                                        scene v13480 with Dissolve(1)
                                                        z "Be nice to each other, you two..."
                                                        show v13m40 with Dissolve(1)
                                                        tmra "Hmmnn~... Mnnn~..."
                                                        tr "Mmmmhhnnn~..."
                                                        z "Look at you getting along... So cute..."
                                                        tmra "Nmmmmnn~... Mhhhnn~..."
                                                        tr "Hmmmn~... Ahhmmmm~..."
                                                        z "Two besties putting their differences behind and joining their lips..."
                                                        tr "Hmmmnnn~... Fuhhhmm~..."
                                                        tmra "Ihmmmmmnn~... Fuhhhmmm~..."
                                                        z "Tamara... I'm gonna cum..."
                                                        z "I hope you're ready... I'm shooting it inside you..."
                                                        tmra "Hmmnnn~?! Inmmmm~! Mhhhnnn~!"
                                                        z "Yeah. I don't understand... I'm gonna cum..."
                                                        tmra "Mhhhmmmmnnn~!"
                                                        tmra "Hmmmm-"
                                                        play audio "audio/creak.mp3"
                                                        play sound "audio/magic 7.mp3"
                                                        stop background_s fadeout 1.0
                                                        stop background_s2 fadeout 1.0
                                                        scene v13481 with hpunch
                                                        tmra "AAAHHHHH~!" (multiple=2)
                                                        tr "Ahh~?!" (multiple=2)
                                                    "Keep fucking Tamara like this.":
                                                        show v13m5 with Dissolve(1)
                                                        tmra "Aaaannh~... Waihhtt~..."
                                                        z "Come back here, Tamara."
                                                        tr "That was rude, Tamara..."
                                                        tr "Don't suck on other people's nipples without permission."
                                                        tmra "Hahh~... It's your fault..."
                                                        tr "Come on, apologise."
                                                        tmra "Nooo~... Ahhh~... Fuck you..."
                                                        tr "If you say you're sorry [mc_name] might creampie you."
                                                        tmra "Ahhh~... C-Creampie?! Waihht~..."
                                                        z "Wait, I never agreed to this..."
                                                        tr "Come on, we need to put cocky Tamara in her place, [mc_name]..."
                                                        tr "If she behaves like a good girl, would you creampie her?"
                                                        z "I mean..."
                                                        tr "What do you say, Tamara? Are you a good girl?"
                                                        tmra "Ahh~... Fuhcckk~..."
                                                        tr "Now, now. Tamara. No cursing."
                                                        tr "Just say you're sorry. And [mc_name] will shoot all his warm load inside you."
                                                        tmra "Hnnn~... Ahhh~... Inshide..."
                                                        tr "Yup, yup. All of it inside you."
                                                        tr "In return for one small sorry."
                                                        tr "Good deal, no?"
                                                        tmra "Ahh~... Hahhhhh~... Anhhh~..."
                                                        tmra "I'm... Mmmmnn~... Hahhh~... I'm..."
                                                        tmra "I'm cumming... Ahh~... Hahh~... Hanhh~..."
                                                        z "I'm gonna cum too..."
                                                        tr "Shoot it... Ahh~... Hannhh~... Shoot it inside..."
                                                        if tmra_lst >= 7:
                                                            play sound "audio/creaky door.mp3"
                                                            "{i}Door opens.{/i}"
                                                            tr "Fuhhcck~... What was that..."
                                                            z "I don't know..."
                                                            tr "Someone... Ahhh~... Someone just came in... We need to stop..."
                                                            z "Yeah... Lemme just..."
                                                            play sound "audio/Falling2.mp3"
                                                            play audio "audio/magic 7.mp3"
                                                            stop background_s
                                                            stop background_s2
                                                            stop music
                                                            scene v13462 with vpunch
                                                            z "Ughh... Fuck..." (multiple=2)
                                                            tr "Aaaahhh~..." (multiple=2)
                                                            play sound "audio/Cloth_rustle.wav"
                                                            scene v13463 with Dissolve(1)
                                                            tr "Hahhh~... Fuck... That was..."
                                                            z "That was amazing, but we need t-"
                                                            scene v13464 with dissolve
                                                            tmra "Torr?!"
                                                            scene v13465 with Dissolve(1)
                                                            tmra "What's all that noi-"
                                                            scene v13466 with Dissolve(1)
                                                            z "..."
                                                            tmra "What th-"
                                                            tmra "..."
                                                            with Pause(1)
                                                            play audio "audio/camera.mp3"
                                                            scene black
                                                            with Pause(0.5)
                                                            play sound "audio/Falling2.mp3"
                                                            with vpunch
                                                            with vpunch
                                                            with vpunch
                                                            with vpunch
                                                            tmra "AAAH!"
                                                            with Pause(0.5)
                                                            play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
                                                            play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                                                            show v13m5 with Dissolve(1)
                                                            tmra "Aaaahhh~... Ahhhhh~... Fuhcckkk~..."
                                                            tr "How do you like that Tamara?"
                                                            tmra "It feelshhh..."
                                                            tr "Yes?"
                                                            tmra "Ahh~... It's... Hahh~... Doesn't feel that good... Ahh~..."
                                                            tr "Really? You're making a really dumb face down there..."
                                                            tr "Almost like you're losing it from the pleasure..."
                                                            tmra "That'th nohhht... Ahhh~..."
                                                            tr "You can't even speak properly..."
                                                            tr "Just admit it. You love getting piped like the little slut you are..."
                                                            tmra "Ahh~... Noooo~... I'm not a shlut..."
                                                            tmra "You and Candy... Ahhh~... You're the slutsss~..."
                                                            tmra "How long... Ahhh~... ...have you two been fucking him..."
                                                            tmra "Ahhh~... Just because you can't resist his... Ahhh~... ...huge di-"
                                                            tmra "Ahhhhh~ Huge asshole behaviour..."
                                                            tr "Play nice, Tamara..."
                                                            scene v13472 with Dissolve(1)
                                                            tr "You look really cute... Seems you already came a few times..."
                                                            play audio "audio/kiss.mp3"
                                                            scene v13473 with dissolve
                                                            tmra "Thut uppp..." (multiple=2)
                                                            tr "Ah!" (multiple=2)
                                                            scene v13474 with dissolve
                                                            tmra "Ahh~... Waihht~... What are you-"
                                                            scene v13475 with vpunch
                                                            tr "Eeep! Don't bite it!"
                                                            scene v13476 with dissolve
                                                            tr "Hannhh~... Fuhhhcckkk~..."
                                                            scene v13477 with Dissolve(1)
                                                            tmra "Hmmn~..."
                                                            z "..."
                                                            menu:
                                                                "Push Tamara's face closer to Torr's and make them make out.":
                                                                    play sound "audio/Cloth_rustle.wav"
                                                                    scene v13478 with vpunch
                                                                    tmra "Ahh~!" (multiple=2)
                                                                    tr "?!" (multiple=2)
                                                                    play audio "audio/kiss.mp3"
                                                                    scene v13479 with hpunch
                                                                    tmra "HMNN~!" (multiple=2)
                                                                    tr "HMMM?!" (multiple=2)
                                                                    scene v13480 with Dissolve(1)
                                                                    z "Be nice to each other, you two..."
                                                                    show v13m40 with Dissolve(1)
                                                                    tmra "Hmmnn~... Mnnn~..."
                                                                    tr "Mmmmhhnnn~..."
                                                                    z "Look at you getting along... So cute..."
                                                                    tmra "Nmmmmnn~... Mhhhnn~..."
                                                                    tr "Hmmmn~... Ahhmmmm~..."
                                                                    z "Two besties putting their differences behind and joining their lips..."
                                                                    tr "Hmmmnnn~... Fuhhhmm~..."
                                                                    tmra "Ihmmmmmnn~... Fuhhhmmm~..."
                                                                    z "Tamara... I'm gonna cum..."
                                                                    z "I hope you're ready... I'm shooting it inside you..."
                                                                    tmra "Hmmnnn~?! Inmmmm~! Mhhhnnn~!"
                                                                    z "Yeah. I don't understand... I'm gonna cum..."
                                                                    tmra "Mhhhmmmmnnn~!"
                                                                    tmra "Hmmmm-"
                                                                    play audio "audio/creak.mp3"
                                                                    play sound "audio/magic 7.mp3"
                                                                    stop background_s fadeout 1.0
                                                                    stop background_s2 fadeout 1.0
                                                                    scene v13481 with hpunch
                                                                    tmra "AAAHHHHH~!" (multiple=2)
                                                                    tr "Ahh~?!" (multiple=2)
                                                                "Keep fucking Tamara like this.":
                                                                    show v13m5 with Dissolve(1)
                                                                    tmra "Aaaannh~... Waihhtt~..."
                                                                    z "Come back here, Tamara."
                                                                    tr "That was rude, Tamara..."
                                                                    tr "Don't suck on other people's nipples without permission."
                                                                    tmra "Hahh~... It's your fault..."
                                                                    tr "Come on, apologise."
                                                                    tmra "Nooo~... Ahhh~... Fuck you..."
                                                                    tr "If you say you're sorry [mc_name] might creampie you."
                                                                    tmra "Ahhh~... C-Creampie?! Waihht~..."
                                                                    z "Wait, I never agreed to this..."
                                                                    tr "Come on, we need to put cocky Tamara in her place, [mc_name]..."
                                                                    tr "If she behaves like a good girl, would you creampie her?"
                                                                    z "I mean..."
                                                                    tr "What do you say, Tamara? Are you a good girl?"
                                                                    tmra "Ahh~... Fuhcckk~..."
                                                                    tr "Now, now. Tamara. No cursing."
                                                                    tr "Just say you're sorry. And [mc_name] will shoot all his warm load inside you."
                                                                    tmra "Hnnn~... Ahhh~... Inshide..."
                                                                    tr "Yup, yup. All of it inside you."
                                                                    tr "In return for one small sorry."
                                                                    tr "Good deal, no?"
                                                                    tmra "Ahh~... Hahhhhh~... Anhhh~..."
                                                                    tmra "I'm... Mmmmnn~... Hahhh~... I'm..."
                                                                    tmra "I'm cumming... Ahh~... Hahh~... Hanhh~..."
                                                                    z "I'm gonna cum too..."
                                                                    tr "Shoot it... Ahh~... Hannhh~... Shoot it inside..."
                                                                    if tmra_lst >= 7:
                                                                        play sound "audio/creaky door.mp3"
                                                                        "{i}Door opens.{/i}"
                                                                        tr "Fuhhcck~... What was that..."
                                                                        z "I don't know..."
                                                                        tr "Someone... Ahhh~... Someone just came in... We need to stop..."
                                                                        z "Yeah... Lemme just..."
                                                                        play sound "audio/Falling2.mp3"
                                                                        play audio "audio/magic 7.mp3"
                                                                        stop background_s
                                                                        stop background_s2
                                                                        stop music
                                                                        scene v13462 with vpunch
                                                                        z "Ughh... Fuck..." (multiple=2)
                                                                        tr "Aaaahhh~..." (multiple=2)
                                                                        play sound "audio/Cloth_rustle.wav"
                                                                        scene v13463 with Dissolve(1)
                                                                        tr "Hahhh~... Fuck... That was..."
                                                                        z "That was amazing, but we need t-"
                                                                        scene v13464 with dissolve
                                                                        tmra "Torr?!"
                                                                        scene v13465 with Dissolve(1)
                                                                        tmra "What's all that noi-"
                                                                        scene v13466 with Dissolve(1)
                                                                        z "..."
                                                                        tmra "What th-"
                                                                        tmra "..."
                                                                        with Pause(1)
                                                                        play audio "audio/camera.mp3"
                                                                        scene black
                                                                        with Pause(0.5)
                                                                        play sound "audio/Falling2.mp3"
                                                                        with vpunch
                                                                        with vpunch
                                                                        with vpunch
                                                                        with vpunch
                                                                        tmra "AAAH!"
                                                                        with Pause(0.5)
                                                                        play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
                                                                        play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                                                                        show v13m5 with Dissolve(1)
                                                                        tmra "Aaaahhh~... Ahhhhh~... Fuhcckkk~..."
                                                                        tr "How do you like that Tamara?"
                                                                        tmra "It feelshhh..."
                                                                        tr "Yes?"
                                                                        tmra "Ahh~... It's... Hahh~... Doesn't feel that good... Ahh~..."
                                                                        tr "Really? You're making a really dumb face down there..."
                                                                        tr "Almost like you're losing it from the pleasure..."
                                                                        tmra "That'th nohhht... Ahhh~..."
                                                                        tr "You can't even speak properly..."
                                                                        tr "Just admit it. You love getting piped like the little slut you are..."
                                                                        tmra "Ahh~... Noooo~... I'm not a shlut..."
                                                                        tmra "You and Candy... Ahhh~... You're the slutsss~..."
                                                                        tmra "How long... Ahhh~... ...have you two been fucking him..."
                                                                        tmra "Ahhh~... Just because you can't resist his... Ahhh~... ...huge di-"
                                                                        tmra "Ahhhhh~ Huge asshole behaviour..."
                                                                        tr "Play nice, Tamara..."
                                                                        scene v13472 with Dissolve(1)
                                                                        tr "You look really cute... Seems you already came a few times..."
                                                                        play audio "audio/kiss.mp3"
                                                                        scene v13473 with dissolve
                                                                        tmra "Thut uppp..." (multiple=2)
                                                                        tr "Ah!" (multiple=2)
                                                                        scene v13474 with dissolve
                                                                        tmra "Ahh~... Waihht~... What are you-"
                                                                        scene v13475 with vpunch
                                                                        tr "Eeep! Don't bite it!"
                                                                        scene v13476 with dissolve
                                                                        tr "Hannhh~... Fuhhhcckkk~..."
                                                                        scene v13477 with Dissolve(1)
                                                                        tmra "Hmmn~..."
                                                                        z "..."
                                                                        menu:
                                                                            "Push Tamara's face closer to Torr's and make them make out.":
                                                                                play sound "audio/Cloth_rustle.wav"
                                                                                scene v13478 with vpunch
                                                                                tmra "Ahh~!" (multiple=2)
                                                                                tr "?!" (multiple=2)
                                                                                play audio "audio/kiss.mp3"
                                                                                scene v13479 with hpunch
                                                                                tmra "HMNN~!" (multiple=2)
                                                                                tr "HMMM?!" (multiple=2)
                                                                                scene v13480 with Dissolve(1)
                                                                                z "Be nice to each other, you two..."
                                                                                show v13m40 with Dissolve(1)
                                                                                tmra "Hmmnn~... Mnnn~..."
                                                                                tr "Mmmmhhnnn~..."
                                                                                z "Look at you getting along... So cute..."
                                                                                tmra "Nmmmmnn~... Mhhhnn~..."
                                                                                tr "Hmmmn~... Ahhmmmm~..."
                                                                                z "Two besties putting their differences behind and joining their lips..."
                                                                                tr "Hmmmnnn~... Fuhhhmm~..."
                                                                                tmra "Ihmmmmmnn~... Fuhhhmmm~..."
                                                                                z "Tamara... I'm gonna cum..."
                                                                                z "I hope you're ready... I'm shooting it inside you..."
                                                                                tmra "Hmmnnn~?! Inmmmm~! Mhhhnnn~!"
                                                                                z "Yeah. I don't understand... I'm gonna cum..."
                                                                                tmra "Mhhhmmmmnnn~!"
                                                                                tmra "Hmmmm-"
                                                                                play audio "audio/creak.mp3"
                                                                                play sound "audio/magic 7.mp3"
                                                                                stop background_s fadeout 1.0
                                                                                stop background_s2 fadeout 1.0
                                                                                scene v13481 with hpunch
                                                                                tmra "AAAHHHHH~!" (multiple=2)
                                                                                tr "Ahh~?!" (multiple=2)
                                                                            "Keep fucking Tamara like this.":
                                                                                show v13m5 with Dissolve(1)
                                                                                tmra "Aaaannh~... Waihhtt~..."
                                                                                z "Come back here, Tamara."
                                                                                tr "That was rude, Tamara..."
                                                                                tr "Don't suck on other people's nipples without permission."
                                                                                tmra "Hahh~... It's your fault..."
                                                                                tr "Come on, apologise."
                                                                                tmra "Nooo~... Ahhh~... Fuck you..."
                                                                                tr "If you say you're sorry [mc_name] might creampie you."
                                                                                tmra "Ahhh~... C-Creampie?! Waihht~..."
                                                                                z "Wait, I never agreed to this..."
                                                                                tr "Come on, we need to put cocky Tamara in her place, [mc_name]..."
                                                                                tr "If she behaves like a good girl, would you creampie her?"
                                                                                z "I mean..."
                                                                                tr "What do you say, Tamara? Are you a good girl?"
                                                                                tmra "Ahh~... Fuhcckk~..."
                                                                                tr "Now, now. Tamara. No cursing."
                                                                                tr "Just say you're sorry. And [mc_name] will shoot all his warm load inside you."
                                                                                tmra "Hnnn~... Ahhh~... Inshide..."
                                                                                tr "Yup, yup. All of it inside you."
                                                                                tr "In return for one small sorry."
                                                                                tr "Good deal, no?"
                                                                                tmra "Ahh~... Hahhhhh~... Anhhh~..."
                                                                                tmra "I'm... Mmmmnn~... Hahhh~... I'm..."
                                                                                tmra "I'm cumming... Ahh~... Hahh~... Hanhh~..."
                                                                                z "I'm gonna cum too..."
                                                                                tr "Shoot it... Ahh~... Hannhh~... Shoot it inside..."
                                                                                if tmra_lst >= 7:
                                                                                    play sound "audio/creaky door.mp3"
                                                                                    "{i}Door opens.{/i}"
                                                                                    tr "Fuhhcck~... What was that..."
                                                                                    z "I don't know..."
                                                                                    tr "Someone... Ahhh~... Someone just came in... We need to stop..."
                                                                                    z "Yeah... Lemme just..."
                                                                                    play sound "audio/Falling2.mp3"
                                                                                    play audio "audio/magic 7.mp3"
                                                                                    stop background_s
                                                                                    stop background_s2
                                                                                    stop music
                                                                                    scene v13462 with vpunch
                                                                                    z "Ughh... Fuck..." (multiple=2)
                                                                                    tr "Aaaahhh~..." (multiple=2)
                                                                                    play sound "audio/Cloth_rustle.wav"
                                                                                    scene v13463 with Dissolve(1)
                                                                                    tr "Hahhh~... Fuck... That was..."
                                                                                    z "That was amazing, but we need t-"
                                                                                    scene v13464 with dissolve
                                                                                    tmra "Torr?!"
                                                                                    scene v13465 with Dissolve(1)
                                                                                    tmra "What's all that noi-"
                                                                                    scene v13466 with Dissolve(1)
                                                                                    z "..."
                                                                                    tmra "What th-"
                                                                                    tmra "..."
                                                                                    with Pause(1)
                                                                                    play audio "audio/camera.mp3"
                                                                                    scene black
                                                                                    with Pause(0.5)
                                                                                    play sound "audio/Falling2.mp3"
                                                                                    with vpunch
                                                                                    with vpunch
                                                                                    with vpunch
                                                                                    with vpunch
                                                                                    tmra "AAAH!"
                                                                                    with Pause(0.5)
                                                                                    play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
                                                                                    play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                                                                                    show v13m5 with Dissolve(1)
                                                                                    tmra "Aaaahhh~... Ahhhhh~... Fuhcckkk~..."
                                                                                    tr "How do you like that Tamara?"
                                                                                    tmra "It feelshhh..."
                                                                                    tr "Yes?"
                                                                                    tmra "Ahh~... It's... Hahh~... Doesn't feel that good... Ahh~..."
                                                                                    tr "Really? You're making a really dumb face down there..."
                                                                                    tr "Almost like you're losing it from the pleasure..."
                                                                                    tmra "That'th nohhht... Ahhh~..."
                                                                                    tr "You can't even speak properly..."
                                                                                    tr "Just admit it. You love getting piped like the little slut you are..."
                                                                                    tmra "Ahh~... Noooo~... I'm not a shlut..."
                                                                                    tmra "You and Candy... Ahhh~... You're the slutsss~..."
                                                                                    tmra "How long... Ahhh~... ...have you two been fucking him..."
                                                                                    tmra "Ahhh~... Just because you can't resist his... Ahhh~... ...huge di-"
                                                                                    tmra "Ahhhhh~ Huge asshole behaviour..."
                                                                                    tr "Play nice, Tamara..."
                                                                                    scene v13472 with Dissolve(1)
                                                                                    tr "You look really cute... Seems you already came a few times..."
                                                                                    play audio "audio/kiss.mp3"
                                                                                    scene v13473 with dissolve
                                                                                    tmra "Thut uppp..." (multiple=2)
                                                                                    tr "Ah!" (multiple=2)
                                                                                    scene v13474 with dissolve
                                                                                    tmra "Ahh~... Waihht~... What are you-"
                                                                                    scene v13475 with vpunch
                                                                                    tr "Eeep! Don't bite it!"
                                                                                    scene v13476 with dissolve
                                                                                    tr "Hannhh~... Fuhhhcckkk~..."
                                                                                    scene v13477 with Dissolve(1)
                                                                                    tmra "Hmmn~..."
                                                                                    z "..."
                                                                                    menu:
                                                                                        "Push Tamara's face closer to Torr's and make them make out.":
                                                                                            play sound "audio/Cloth_rustle.wav"
                                                                                            scene v13478 with vpunch
                                                                                            tmra "Ahh~!" (multiple=2)
                                                                                            tr "?!" (multiple=2)
                                                                                            play audio "audio/kiss.mp3"
                                                                                            scene v13479 with hpunch
                                                                                            tmra "HMNN~!" (multiple=2)
                                                                                            tr "HMMM?!" (multiple=2)
                                                                                            scene v13480 with Dissolve(1)
                                                                                            z "Be nice to each other, you two..."
                                                                                            show v13m40 with Dissolve(1)
                                                                                            tmra "Hmmnn~... Mnnn~..."
                                                                                            tr "Mmmmhhnnn~..."
                                                                                            z "Look at you getting along... So cute..."
                                                                                            tmra "Nmmmmnn~... Mhhhnn~..."
                                                                                            tr "Hmmmn~... Ahhmmmm~..."
                                                                                            z "Two besties putting their differences behind and joining their lips..."
                                                                                            tr "Hmmmnnn~... Fuhhhmm~..."
                                                                                            tmra "Ihmmmmmnn~... Fuhhhmmm~..."
                                                                                            z "Tamara... I'm gonna cum..."
                                                                                            z "I hope you're ready... I'm shooting it inside you..."
                                                                                            tmra "Hmmnnn~?! Inmmmm~! Mhhhnnn~!"
                                                                                            z "Yeah. I don't understand... I'm gonna cum..."
                                                                                            tmra "Mhhhmmmmnnn~!"
                                                                                            tmra "Hmmmm-"
                                                                                            play audio "audio/creak.mp3"
                                                                                            play sound "audio/magic 7.mp3"
                                                                                            stop background_s fadeout 1.0
                                                                                            stop background_s2 fadeout 1.0
                                                                                            scene v13481 with hpunch
                                                                                            tmra "AAAHHHHH~!" (multiple=2)
                                                                                            tr "Ahh~?!" (multiple=2)
                                                                                        "Keep fucking Tamara like this.":
                                                                                            show v13m5 with Dissolve(1)
                                                                                            tmra "Aaaannh~... Waihhtt~..."
                                                                                            z "Come back here, Tamara."
                                                                                            tr "That was rude, Tamara..."
                                                                                            tr "Don't suck on other people's nipples without permission."
                                                                                            tmra "Hahh~... It's your fault..."
                                                                                            tr "Come on, apologise."
                                                                                            tmra "Nooo~... Ahhh~... Fuck you..."
                                                                                            tr "If you say you're sorry [mc_name] might creampie you."
                                                                                            tmra "Ahhh~... C-Creampie?! Waihht~..."
                                                                                            z "Wait, I never agreed to this..."
                                                                                            tr "Come on, we need to put cocky Tamara in her place, [mc_name]..."
                                                                                            tr "If she behaves like a good girl, would you creampie her?"
                                                                                            z "I mean..."
                                                                                            tr "What do you say, Tamara? Are you a good girl?"
                                                                                            tmra "Ahh~... Fuhcckk~..."
                                                                                            tr "Now, now. Tamara. No cursing."
                                                                                            tr "Just say you're sorry. And [mc_name] will shoot all his warm load inside you."
                                                                                            tmra "Hnnn~... Ahhh~... Inshide..."
                                                                                            tr "Yup, yup. All of it inside you."
                                                                                            tr "In return for one small sorry."
                                                                                            tr "Good deal, no?"
                                                                                            tmra "Ahh~... Hahhhhh~... Anhhh~..."
                                                                                            tmra "I'm... Mmmmnn~... Hahhh~... I'm..."
                                                                                            tmra "I'm cumming... Ahh~... Hahh~... Hanhh~..."
                                                                                            z "I'm gonna cum too..."
                                                                                            tr "Shoot it... Ahh~... Hannhh~... Shoot it inside..."
                                                                                            if tmra_lst >= 7:
                                                                                                play sound "audio/creaky door.mp3"
                                                                                                "{i}Door opens.{/i}"
                                                                                                tr "Fuhhcck~... What was that..."
                                                                                                z "I don't know..."
                                                                                                tr "Someone... Ahhh~... Someone just came in... We need to stop..."
                                                                                                z "Yeah... Lemme just..."
                                                                                                play sound "audio/Falling2.mp3"
                                                                                                play audio "audio/magic 7.mp3"
                                                                                                stop background_s
                                                                                                stop background_s2
                                                                                                stop music
                                                                                                scene v13462 with vpunch
                                                                                                z "Ughh... Fuck..." (multiple=2)
                                                                                                tr "Aaaahhh~..." (multiple=2)
                                                                                                play sound "audio/Cloth_rustle.wav"
                                                                                                scene v13463 with Dissolve(1)
                                                                                                tr "Hahhh~... Fuck... That was..."
                                                                                                z "That was amazing, but we need t-"
                                                                                                scene v13464 with dissolve
                                                                                                tmra "Torr?!"
                                                                                                scene v13465 with Dissolve(1)
                                                                                                tmra "What's all that noi-"
                                                                                                scene v13466 with Dissolve(1)
                                                                                                z "..."
                                                                                                tmra "What th-"
                                                                                                tmra "..."
                                                                                                with Pause(1)
                                                                                                play audio "audio/camera.mp3"
                                                                                                scene black
                                                                                                with Pause(0.5)
                                                                                                play sound "audio/Falling2.mp3"
                                                                                                with vpunch
                                                                                                with vpunch
                                                                                                with vpunch
                                                                                                with vpunch
                                                                                                tmra "AAAH!"
                                                                                                with Pause(0.5)
                                                                                                play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
                                                                                                play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                                                                                                show v13m5 with Dissolve(1)
                                                                                                tmra "Aaaahhh~... Ahhhhh~... Fuhcckkk~..."
                                                                                                tr "How do you like that Tamara?"
                                                                                                tmra "It feelshhh..."
                                                                                                tr "Yes?"
                                                                                                tmra "Ahh~... It's... Hahh~... Doesn't feel that good... Ahh~..."
                                                                                                tr "Really? You're making a really dumb face down there..."
                                                                                                tr "Almost like you're losing it from the pleasure..."
                                                                                                tmra "That'th nohhht... Ahhh~..."
                                                                                                tr "You can't even speak properly..."
                                                                                                tr "Just admit it. You love getting piped like the little slut you are..."
                                                                                                tmra "Ahh~... Noooo~... I'm not a shlut..."
                                                                                                tmra "You and Candy... Ahhh~... You're the slutsss~..."
                                                                                                tmra "How long... Ahhh~... ...have you two been fucking him..."
                                                                                                tmra "Ahhh~... Just because you can't resist his... Ahhh~... ...huge di-"
                                                                                                tmra "Ahhhhh~ Huge asshole behaviour..."
                                                                                                tr "Play nice, Tamara..."
                                                                                                scene v13472 with Dissolve(1)
                                                                                                tr "You look really cute... Seems you already came a few times..."
                                                                                                play audio "audio/kiss.mp3"
                                                                                                scene v13473 with dissolve
                                                                                                tmra "Thut uppp..." (multiple=2)
                                                                                                tr "Ah!" (multiple=2)
                                                                                                scene v13474 with dissolve
                                                                                                tmra "Ahh~... Waihht~... What are you-"
                                                                                                scene v13475 with vpunch
                                                                                                tr "Eeep! Don't bite it!"
                                                                                                scene v13476 with dissolve
                                                                                                tr "Hannhh~... Fuhhhcckkk~..."
                                                                                                scene v13477 with Dissolve(1)
                                                                                                tmra "Hmmn~..."
                                                                                                z "..."
                                                                                                menu:
                                                                                                    "Push Tamara's face closer to Torr's and make them make out.":
                                                                                                        play sound "audio/Cloth_rustle.wav"
                                                                                                        scene v13478 with vpunch
                                                                                                        tmra "Ahh~!" (multiple=2)
                                                                                                        tr "?!" (multiple=2)
                                                                                                        play audio "audio/kiss.mp3"
                                                                                                        scene v13479 with hpunch
                                                                                                        tmra "HMNN~!" (multiple=2)
                                                                                                        tr "HMMM?!" (multiple=2)
                                                                                                        scene v13480 with Dissolve(1)
                                                                                                        z "Be nice to each other, you two..."
                                                                                                        show v13m40 with Dissolve(1)
                                                                                                        tmra "Hmmnn~... Mnnn~..."
                                                                                                        tr "Mmmmhhnnn~..."
                                                                                                        z "Look at you getting along... So cute..."
                                                                                                        tmra "Nmmmmnn~... Mhhhnn~..."
                                                                                                        tr "Hmmmn~... Ahhmmmm~..."
                                                                                                        z "Two besties putting their differences behind and joining their lips..."
                                                                                                        tr "Hmmmnnn~... Fuhhhmm~..."
                                                                                                        tmra "Ihmmmmmnn~... Fuhhhmmm~..."
                                                                                                        z "Tamara... I'm gonna cum..."
                                                                                                        z "I hope you're ready... I'm shooting it inside you..."
                                                                                                        tmra "Hmmnnn~?! Inmmmm~! Mhhhnnn~!"
                                                                                                        z "Yeah. I don't understand... I'm gonna cum..."
                                                                                                        tmra "Mhhhmmmmnnn~!"
                                                                                                        tmra "Hmmmm-"
                                                                                                        play audio "audio/creak.mp3"
                                                                                                        play sound "audio/magic 7.mp3"
                                                                                                        stop background_s fadeout 1.0
                                                                                                        stop background_s2 fadeout 1.0
                                                                                                        scene v13481 with hpunch
                                                                                                        tmra "AAAHHHHH~!" (multiple=2)
                                                                                                        tr "Ahh~?!" (multiple=2)
                                                                                                    "Keep fucking Tamara like this.":
                                                                                                        show v13m5 with Dissolve(1)
                                                                                                        tmra "Aaaannh~... Waihhtt~..."
                                                                                                        z "Come back here, Tamara."
                                                                                                        tr "That was rude, Tamara..."
                                                                                                        tr "Don't suck on other people's nipples without permission."
                                                                                                        tmra "Hahh~... It's your fault..."
                                                                                                        tr "Come on, apologise."
                                                                                                        tmra "Nooo~... Ahhh~... Fuck you..."
                                                                                                        tr "If you say you're sorry [mc_name] might creampie you."
                                                                                                        tmra "Ahhh~... C-Creampie?! Waihht~..."
                                                                                                        z "Wait, I never agreed to this..."
                                                                                                        tr "Come on, we need to put cocky Tamara in her place, [mc_name]..."
                                                                                                        tr "If she behaves like a good girl, would you creampie her?"
                                                                                                        z "I mean..."
                                                                                                        tr "What do you say, Tamara? Are you a good girl?"
                                                                                                        tmra "Ahh~... Fuhcckk~..."
                                                                                                        tr "Now, now. Tamara. No cursing."
                                                                                                        tr "Just say you're sorry. And [mc_name] will shoot all his warm load inside you."
                                                                                                        tmra "Hnnn~... Ahhh~... Inshide..."
                                                                                                        tr "Yup, yup. All of it inside you."
                                                                                                        tr "In return for one small sorry."
                                                                                                        tr "Good deal, no?"
                                                                                                        tmra "Ahh~... Hahhhhh~... Anhhh~..."
                                                                                                        tmra "I'm... Mmmmnn~... Hahhh~... I'm..."
                                                                                                        tmra "I'm cumming... Ahh~... Hahh~... Hanhh~..."
                                                                                                        z "I'm gonna cum too..."
                                                                                                        tr "Shoot it... Ahh~... Hannhh~... Shoot it inside..."
                                                                                                        if tmra_lst >= 7:
                                                                                                            play sound "audio/creaky door.mp3"
                                                                                                            "{i}Door opens.{/i}"
                                                                                                            tr "Fuhhcck~... What was that..."
                                                                                                            z "I don't know..."
                                                                                                            tr "Someone... Ahhh~... Someone just came in... We need to stop..."
                                                                                                            z "Yeah... Lemme just..."
                                                                                                            play sound "audio/Falling2.mp3"
                                                                                                            play audio "audio/magic 7.mp3"
                                                                                                            stop background_s
                                                                                                            stop background_s2
                                                                                                            stop music
                                                                                                            scene v13462 with vpunch
                                                                                                            z "Ughh... Fuck..." (multiple=2)
                                                                                                            tr "Aaaahhh~..." (multiple=2)
                                                                                                            play sound "audio/Cloth_rustle.wav"
                                                                                                            scene v13463 with Dissolve(1)
                                                                                                            tr "Hahhh~... Fuck... That was..."
                                                                                                            z "That was amazing, but we need t-"
                                                                                                            scene v13464 with dissolve
                                                                                                            tmra "Torr?!"
                                                                                                            scene v13465 with Dissolve(1)
                                                                                                            tmra "What's all that noi-"
                                                                                                            scene v13466 with Dissolve(1)
                                                                                                            z "..."
                                                                                                            tmra "What th-"
                                                                                                            tmra "..."
                                                                                                            with Pause(1)
                                                                                                            play audio "audio/camera.mp3"
                                                                                                            scene black
                                                                                                            with Pause(0.5)
                                                                                                            play sound "audio/Falling2.mp3"
                                                                                                            with vpunch
                                                                                                            with vpunch
                                                                                                            with vpunch
                                                                                                            with vpunch
                                                                                                            tmra "AAAH!"
                                                                                                            with Pause(0.5)
                                                                                                            play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
                                                                                                            play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                                                                                                            show v13m5 with Dissolve(1)
                                                                                                            tmra "Aaaahhh~... Ahhhhh~... Fuhcckkk~..."
                                                                                                            tr "How do you like that Tamara?"
                                                                                                            tmra "It feelshhh..."
                                                                                                            tr "Yes?"
                                                                                                            tmra "Ahh~... It's... Hahh~... Doesn't feel that good... Ahh~..."
                                                                                                            tr "Really? You're making a really dumb face down there..."
                                                                                                            tr "Almost like you're losing it from the pleasure..."
                                                                                                            tmra "That'th nohhht... Ahhh~..."
                                                                                                            tr "You can't even speak properly..."
                                                                                                            tr "Just admit it. You love getting piped like the little slut you are..."
                                                                                                            tmra "Ahh~... Noooo~... I'm not a shlut..."
                                                                                                            tmra "You and Candy... Ahhh~... You're the slutsss~..."
                                                                                                            tmra "How long... Ahhh~... ...have you two been fucking him..."
                                                                                                            tmra "Ahhh~... Just because you can't resist his... Ahhh~... ...huge di-"
                                                                                                            tmra "Ahhhhh~ Huge asshole behaviour..."
                                                                                                            tr "Play nice, Tamara..."
                                                                                                            scene v13472 with Dissolve(1)
                                                                                                            tr "You look really cute... Seems you already came a few times..."
                                                                                                            play audio "audio/kiss.mp3"
                                                                                                            scene v13473 with dissolve
                                                                                                            tmra "Thut uppp..." (multiple=2)
                                                                                                            tr "Ah!" (multiple=2)
                                                                                                            scene v13474 with dissolve
                                                                                                            tmra "Ahh~... Waihht~... What are you-"
                                                                                                            scene v13475 with vpunch
                                                                                                            tr "Eeep! Don't bite it!"
                                                                                                            scene v13476 with dissolve
                                                                                                            tr "Hannhh~... Fuhhhcckkk~..."
                                                                                                            scene v13477 with Dissolve(1)
                                                                                                            tmra "Hmmn~..."
                                                                                                            z "..."
                                                                                                            menu:
                                                                                                                "Push Tamara's face closer to Torr's and make them make out.":
                                                                                                                    play sound "audio/Cloth_rustle.wav"
                                                                                                                    scene v13478 with vpunch
                                                                                                                    tmra "Ahh~!" (multiple=2)
                                                                                                                    tr "?!" (multiple=2)
                                                                                                                    play audio "audio/kiss.mp3"
                                                                                                                    scene v13479 with hpunch
                                                                                                                    tmra "HMNN~!" (multiple=2)
                                                                                                                    tr "HMMM?!" (multiple=2)
                                                                                                                    scene v13480 with Dissolve(1)
                                                                                                                    z "Be nice to each other, you two..."
                                                                                                                    show v13m40 with Dissolve(1)
                                                                                                                    tmra "Hmmnn~... Mnnn~..."
                                                                                                                    tr "Mmmmhhnnn~..."
                                                                                                                    z "Look at you getting along... So cute..."
                                                                                                                    tmra "Nmmmmnn~... Mhhhnn~..."
                                                                                                                    tr "Hmmmn~... Ahhmmmm~..."
                                                                                                                    z "Two besties putting their differences behind and joining their lips..."
                                                                                                                    tr "Hmmmnnn~... Fuhhhmm~..."
                                                                                                                    tmra "Ihmmmmmnn~... Fuhhhmmm~..."
                                                                                                                    z "Tamara... I'm gonna cum..."
                                                                                                                    z "I hope you're ready... I'm shooting it inside you..."
                                                                                                                    tmra "Hmmnnn~?! Inmmmm~! Mhhhnnn~!"
                                                                                                                    z "Yeah. I don't understand... I'm gonna cum..."
                                                                                                                    tmra "Mhhhmmmmnnn~!"
                                                                                                                    tmra "Hmmmm-"
                                                                                                                    play audio "audio/creak.mp3"
                                                                                                                    play sound "audio/magic 7.mp3"
                                                                                                                    stop background_s fadeout 1.0
                                                                                                                    stop background_s2 fadeout 1.0
                                                                                                                    scene v13481 with hpunch
                                                                                                                    tmra "AAAHHHHH~!" (multiple=2)
                                                                                                                    tr "Ahh~?!" (multiple=2)
                                                                                                                "Keep fucking Tamara like this.":
                                                                                                                    show v13m5 with Dissolve(1)
                                                                                                                    tmra "Aaaannh~... Waihhtt~..."
                                                                                                                    z "Come back here, Tamara."
                                                                                                                    tr "That was rude, Tamara..."
                                                                                                                    tr "Don't suck on other people's nipples without permission."
                                                                                                                    tmra "Hahh~... It's your fault..."
                                                                                                                    tr "Come on, apologise."
                                                                                                                    tmra "Nooo~... Ahhh~... Fuck you..."
                                                                                                                    tr "If you say you're sorry [mc_name] might creampie you."
                                                                                                                    tmra "Ahhh~... C-Creampie?! Waihht~..."
                                                                                                                    z "Wait, I never agreed to this..."
                                                                                                                    tr "Come on, we need to put cocky Tamara in her place, [mc_name]..."
                                                                                                                    tr "If she behaves like a good girl, would you creampie her?"
                                                                                                                    z "I mean..."
                                                                                                                    tr "What do you say, Tamara? Are you a good girl?"
                                                                                                                    tmra "Ahh~... Fuhcckk~..."
                                                                                                                    tr "Now, now. Tamara. No cursing."
                                                                                                                    tr "Just say you're sorry. And [mc_name] will shoot all his warm load inside you."
                                                                                                                    tmra "Hnnn~... Ahhh~... Inshide..."
                                                                                                                    tr "Yup, yup. All of it inside you."
                                                                                                                    tr "In return for one small sorry."
                                                                                                                    tr "Good deal, no?"
                                                                                                                    tmra "Ahh~... Hahhhhh~... Anhhh~..."
                                                                                                                    tmra "I'm... Mmmmnn~... Hahhh~... I'm..."
                                                                                                                    tmra "I'm cumming... Ahh~... Hahh~... Hanhh~..."
                                                                                                                    z "I'm gonna cum too..."
                                                                                                                    tr "Shoot it... Ahh~... Hannhh~... Shoot it inside..."
                                                                                                                    if tmra_lst >= 7:
                                                                                                                        play sound "audio/creaky door.mp3"
                                                                                                                        "{i}Door opens.{/i}"
                                                                                                                        tr "Fuhhcck~... What was that..."
                                                                                                                        z "I don't know..."
                                                                                                                        tr "Someone... Ahhh~... Someone just came in... We need to stop..."
                                                                                                                        z "Yeah... Lemme just..."
                                                                                                                        play sound "audio/Falling2.mp3"
                                                                                                                        play audio "audio/magic 7.mp3"
                                                                                                                        stop background_s
                                                                                                                        stop background_s2
                                                                                                                        stop music
                                                                                                                        scene v13462 with vpunch
                                                                                                                        z "Ughh... Fuck..." (multiple=2)
                                                                                                                        tr "Aaaahhh~..." (multiple=2)
                                                                                                                        play sound "audio/Cloth_rustle.wav"
                                                                                                                        scene v13463 with Dissolve(1)
                                                                                                                        tr "Hahhh~... Fuck... That was..."
                                                                                                                        z "That was amazing, but we need t-"
                                                                                                                        scene v13464 with dissolve
                                                                                                                        tmra "Torr?!"
                                                                                                                        scene v13465 with Dissolve(1)
                                                                                                                        tmra "What's all that noi-"
                                                                                                                        scene v13466 with Dissolve(1)
                                                                                                                        z "..."
                                                                                                                        tmra "What th-"
                                                                                                                        tmra "..."
                                                                                                                        with Pause(1)
                                                                                                                        play audio "audio/camera.mp3"
                                                                                                                        scene black
                                                                                                                        with Pause(0.5)
                                                                                                                        play sound "audio/Falling2.mp3"
                                                                                                                        with vpunch
                                                                                                                        with vpunch
                                                                                                                        with vpunch
                                                                                                                        with vpunch
                                                                                                                        tmra "AAAH!"
                                                                                                                        with Pause(0.5)
                                                                                                                        play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
                                                                                                                        play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                                                                                                                        show v13m5 with Dissolve(1)
                                                                                                                        tmra "Aaaahhh~... Ahhhhh~... Fuhcckkk~..."
                                                                                                                        tr "How do you like that Tamara?"
                                                                                                                        tmra "It feelshhh..."
                                                                                                                        tr "Yes?"
                                                                                                                        tmra "Ahh~... It's... Hahh~... Doesn't feel that good... Ahh~..."
                                                                                                                        tr "Really? You're making a really dumb face down there..."
                                                                                                                        tr "Almost like you're losing it from the pleasure..."
                                                                                                                        tmra "That'th nohhht... Ahhh~..."
                                                                                                                        tr "You can't even speak properly..."
                                                                                                                        tr "Just admit it. You love getting piped like the little slut you are..."
                                                                                                                        tmra "Ahh~... Noooo~... I'm not a shlut..."
                                                                                                                        tmra "You and Candy... Ahhh~... You're the slutsss~..."
                                                                                                                        tmra "How long... Ahhh~... ...have you two been fucking him..."
                                                                                                                        tmra "Ahhh~... Just because you can't resist his... Ahhh~... ...huge di-"
                                                                                                                        tmra "Ahhhhh~ Huge asshole behaviour..."
                                                                                                                        tr "Play nice, Tamara..."
                                                                                                                        scene v13472 with Dissolve(1)
                                                                                                                        tr "You look really cute... Seems you already came a few times..."
                                                                                                                        play audio "audio/kiss.mp3"
                                                                                                                        scene v13473 with dissolve
                                                                                                                        tmra "Thut uppp..." (multiple=2)
                                                                                                                        tr "Ah!" (multiple=2)
                                                                                                                        scene v13474 with dissolve
                                                                                                                        tmra "Ahh~... Waihht~... What are you-"
                                                                                                                        scene v13475 with vpunch
                                                                                                                        tr "Eeep! Don't bite it!"
                                                                                                                        scene v13476 with dissolve
                                                                                                                        tr "Hannhh~... Fuhhhcckkk~..."
                                                                                                                        scene v13477 with Dissolve(1)
                                                                                                                        tmra "Hmmn~..."
                                                                                                                        z "..."
                                                                                                                        menu:
                                                                                                                            "Push Tamara's face closer to Torr's and make them make out.":
                                                                                                                                play sound "audio/Cloth_rustle.wav"
                                                                                                                                scene v13478 with vpunch
                                                                                                                                tmra "Ahh~!" (multiple=2)
                                                                                                                                tr "?!" (multiple=2)
                                                                                                                                play audio "audio/kiss.mp3"
                                                                                                                                scene v13479 with hpunch
                                                                                                                                tmra "HMNN~!" (multiple=2)
                                                                                                                                tr "HMMM?!" (multiple=2)
                                                                                                                                scene v13480 with Dissolve(1)
                                                                                                                                z "Be nice to each other, you two..."
                                                                                                                                show v13m40 with Dissolve(1)
                                                                                                                                tmra "Hmmnn~... Mnnn~..."
                                                                                                                                tr "Mmmmhhnnn~..."
                                                                                                                                z "Look at you getting along... So cute..."
                                                                                                                                tmra "Nmmmmnn~... Mhhhnn~..."
                                                                                                                                tr "Hmmmn~... Ahhmmmm~..."
                                                                                                                                z "Two besties putting their differences behind and joining their lips..."
                                                                                                                                tr "Hmmmnnn~... Fuhhhmm~..."
                                                                                                                                tmra "Ihmmmmmnn~... Fuhhhmmm~..."
                                                                                                                                z "Tamara... I'm gonna cum..."
                                                                                                                                z "I hope you're ready... I'm shooting it inside you..."
                                                                                                                                tmra "Hmmnnn~?! Inmmmm~! Mhhhnnn~!"
                                                                                                                                z "Yeah. I don't understand... I'm gonna cum..."
                                                                                                                                tmra "Mhhhmmmmnnn~!"
                                                                                                                                tmra "Hmmmm-"
                                                                                                                                play audio "audio/creak.mp3"
                                                                                                                                play sound "audio/magic 7.mp3"
                                                                                                                                stop background_s fadeout 1.0
                                                                                                                                stop background_s2 fadeout 1.0
                                                                                                                                scene v13481 with hpunch
                                                                                                                                tmra "AAAHHHHH~!" (multiple=2)
                                                                                                                                tr "Ahh~?!" (multiple=2)
                                                                                                                            "Keep fucking Tamara like this.":
                                                                                                                                show v13m5 with Dissolve(1)
                                                                                                                                tmra "Aaaannh~... Waihhtt~..."
                                                                                                                                z "Come back here, Tamara."
                                                                                                                                tr "That was rude, Tamara..."
                                                                                                                                tr "Don't suck on other people's nipples without permission."
                                                                                                                                tmra "Hahh~... It's your fault..."
                                                                                                                                tr "Come on, apologise."
                                                                                                                                tmra "Nooo~... Ahhh~... Fuck you..."
                                                                                                                                tr "If you say you're sorry [mc_name] might creampie you."
                                                                                                                                tmra "Ahhh~... C-Creampie?! Waihht~..."
                                                                                                                                z "Wait, I never agreed to this..."
                                                                                                                                tr "Come on, we need to put cocky Tamara in her place, [mc_name]..."
                                                                                                                                tr "If she behaves like a good girl, would you creampie her?"
                                                                                                                                z "I mean..."
                                                                                                                                tr "What do you say, Tamara? Are you a good girl?"
                                                                                                                                tmra "Ahh~... Fuhcckk~..."
                                                                                                                                tr "Now, now. Tamara. No cursing."
                                                                                                                                tr "Just say you're sorry. And [mc_name] will shoot all his warm load inside you."
                                                                                                                                tmra "Hnnn~... Ahhh~... Inshide..."
                                                                                                                                tr "Yup, yup. All of it inside you."
                                                                                                                                tr "In return for one small sorry."
                                                                                                                                tr "Good deal, no?"
                                                                                                                                tmra "Ahh~... Hahhhhh~... Anhhh~..."
                                                                                                                                tmra "I'm... Mmmmnn~... Hahhh~... I'm..."
                                                                                                                                tmra "I'm cumming... Ahh~... Hahh~... Hanhh~..."
                                                                                                                                z "I'm gonna cum too..."
                                                                                                                                tr "Shoot it... Ahh~... Hannhh~... Shoot it inside..."
                                                                                                                                if tmra_lst >= 7:
                                                                                                                                    play sound "audio/creaky door.mp3"
                                                                                                                                    "{i}Door opens.{/i}"
                                                                                                                                    tr "Fuhhcck~... What was that..."
                                                                                                                                    z "I don't know..."
                                                                                                                                    tr "Someone... Ahhh~... Someone just came in... We need to stop..."
                                                                                                                                    z "Yeah... Lemme just..."
                                                                                                                                    play sound "audio/Falling2.mp3"
                                                                                                                                    play audio "audio/magic 7.mp3"
                                                                                                                                    stop background_s
                                                                                                                                    stop background_s2
                                                                                                                                    stop music
                                                                                                                                    scene v13462 with vpunch
                                                                                                                                    z "Ughh... Fuck..." (multiple=2)
                                                                                                                                    tr "Aaaahhh~..." (multiple=2)
                                                                                                                                    play sound "audio/Cloth_rustle.wav"
                                                                                                                                    scene v13463 with Dissolve(1)
                                                                                                                                    tr "Hahhh~... Fuck... That was..."
                                                                                                                                    z "That was amazing, but we need t-"
                                                                                                                                    scene v13464 with dissolve
                                                                                                                                    tmra "Torr?!"
                                                                                                                                    scene v13465 with Dissolve(1)
                                                                                                                                    tmra "What's all that noi-"
                                                                                                                                    scene v13466 with Dissolve(1)
                                                                                                                                    z "..."
                                                                                                                                    tmra "What th-"
                                                                                                                                    tmra "..."
                                                                                                                                    with Pause(1)
                                                                                                                                    play audio "audio/camera.mp3"
                                                                                                                                    scene black
                                                                                                                                    with Pause(0.5)
                                                                                                                                    play sound "audio/Falling2.mp3"
                                                                                                                                    with vpunch
                                                                                                                                    with vpunch
                                                                                                                                    with vpunch
                                                                                                                                    with vpunch
                                                                                                                                    tmra "AAAH!"
                                                                                                                                    with Pause(0.5)
                                                                                                                                    play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
                                                                                                                                    play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                                                                                                                                    show v13m5 with Dissolve(1)
                                                                                                                                    tmra "Aaaahhh~... Ahhhhh~... Fuhcckkk~..."
                                                                                                                                    tr "How do you like that Tamara?"
                                                                                                                                    tmra "It feelshhh..."
                                                                                                                                    tr "Yes?"
                                                                                                                                    tmra "Ahh~... It's... Hahh~... Doesn't feel that good... Ahh~..."
                                                                                                                                    tr "Really? You're making a really dumb face down there..."
                                                                                                                                    tr "Almost like you're losing it from the pleasure..."
                                                                                                                                    tmra "That'th nohhht... Ahhh~..."
                                                                                                                                    tr "You can't even speak properly..."
                                                                                                                                    tr "Just admit it. You love getting piped like the little slut you are..."
                                                                                                                                    tmra "Ahh~... Noooo~... I'm not a shlut..."
                                                                                                                                    tmra "You and Candy... Ahhh~... You're the slutsss~..."
                                                                                                                                    tmra "How long... Ahhh~... ...have you two been fucking him..."
                                                                                                                                    tmra "Ahhh~... Just because you can't resist his... Ahhh~... ...huge di-"
                                                                                                                                    tmra "Ahhhhh~ Huge asshole behaviour..."
                                                                                                                                    tr "Play nice, Tamara..."
                                                                                                                                    scene v13472 with Dissolve(1)
                                                                                                                                    tr "You look really cute... Seems you already came a few times..."
                                                                                                                                    play audio "audio/kiss.mp3"
                                                                                                                                    scene v13473 with dissolve
                                                                                                                                    tmra "Thut uppp..." (multiple=2)
                                                                                                                                    tr "Ah!" (multiple=2)
                                                                                                                                    scene v13474 with dissolve
                                                                                                                                    tmra "Ahh~... Waihht~... What are you-"
                                                                                                                                    scene v13475 with vpunch
                                                                                                                                    tr "Eeep! Don't bite it!"
                                                                                                                                    scene v13476 with dissolve
                                                                                                                                    tr "Hannhh~... Fuhhhcckkk~..."
                                                                                                                                    scene v13477 with Dissolve(1)
                                                                                                                                    tmra "Hmmn~..."
                                                                                                                                    z "..."
                                                                                                                                    menu:
                                                                                                                                        "Push Tamara's face closer to Torr's and make them make out.":
                                                                                                                                            play sound "audio/Cloth_rustle.wav"
                                                                                                                                            scene v13478 with vpunch
                                                                                                                                            tmra "Ahh~!" (multiple=2)
                                                                                                                                            tr "?!" (multiple=2)
                                                                                                                                            play audio "audio/kiss.mp3"
                                                                                                                                            scene v13479 with hpunch
                                                                                                                                            tmra "HMNN~!" (multiple=2)
                                                                                                                                            tr "HMMM?!" (multiple=2)
                                                                                                                                            scene v13480 with Dissolve(1)
                                                                                                                                            z "Be nice to each other, you two..."
                                                                                                                                            show v13m40 with Dissolve(1)
                                                                                                                                            tmra "Hmmnn~... Mnnn~..."
                                                                                                                                            tr "Mmmmhhnnn~..."
                                                                                                                                            z "Look at you getting along... So cute..."
                                                                                                                                            tmra "Nmmmmnn~... Mhhhnn~..."
                                                                                                                                            tr "Hmmmn~... Ahhmmmm~..."
                                                                                                                                            z "Two besties putting their differences behind and joining their lips..."
                                                                                                                                            tr "Hmmmnnn~... Fuhhhmm~..."
                                                                                                                                            tmra "Ihmmmmmnn~... Fuhhhmmm~..."
                                                                                                                                            z "Tamara... I'm gonna cum..."
                                                                                                                                            z "I hope you're ready... I'm shooting it inside you..."
                                                                                                                                            tmra "Hmmnnn~?! Inmmmm~! Mhhhnnn~!"
                                                                                                                                            z "Yeah. I don't understand... I'm gonna cum..."
                                                                                                                                            tmra "Mhhhmmmmnnn~!"
                                                                                                                                            tmra "Hmmmm-"
                                                                                                                                            play audio "audio/creak.mp3"
                                                                                                                                            play sound "audio/magic 7.mp3"
                                                                                                                                            stop background_s fadeout 1.0
                                                                                                                                            stop background_s2 fadeout 1.0
                                                                                                                                            scene v13481 with hpunch
                                                                                                                                            tmra "AAAHHHHH~!" (multiple=2)
                                                                                                                                            tr "Ahh~?!" (multiple=2)
                                                                                                                                        "Keep fucking Tamara like this.":
                                                                                                                                            show v13m5 with Dissolve(1)
                                                                                                                                            tmra "Aaaannh~... Waihhtt~..."
                                                                                                                                            z "Come back here, Tamara."
                                                                                                                                            tr "That was rude, Tamara..."
                                                                                                                                            tr "Don't suck on other people's nipples without permission."
                                                                                                                                            tmra "Hahh~... It's your fault..."
                                                                                                                                            tr "Come on, apologise."
                                                                                                                                            tmra "Nooo~... Ahhh~... Fuck you..."
                                                                                                                                            tr "If you say you're sorry [mc_name] might creampie you."
                                                                                                                                            tmra "Ahhh~... C-Creampie?! Waihht~..."
                                                                                                                                            z "Wait, I never agreed to this..."
                                                                                                                                            tr "Come on, we need to put cocky Tamara in her place, [mc_name]..."
                                                                                                                                            tr "If she behaves like a good girl, would you creampie her?"
                                                                                                                                            z "I mean..."
                                                                                                                                            tr "What do you say, Tamara? Are you a good girl?"
                                                                                                                                            tmra "Ahh~... Fuhcckk~..."
                                                                                                                                            tr "Now, now. Tamara. No cursing."
                                                                                                                                            tr "Just say you're sorry. And [mc_name] will shoot all his warm load inside you."
                                                                                                                                            tmra "Hnnn~... Ahhh~... Inshide..."
                                                                                                                                            tr "Yup, yup. All of it inside you."
                                                                                                                                            tr "In return for one small sorry."
                                                                                                                                            tr "Good deal, no?"
                                                                                                                                            tmra "Ahh~... Hahhhhh~... Anhhh~..."
                                                                                                                                            tmra "I'm... Mmmmnn~... Hahhh~... I'm..."
                                                                                                                                            tmra "I'm cumming... Ahh~... Hahh~... Hanhh~..."
                                                                                                                                            z "I'm gonna cum too..."
                                                                                                                                            tr "Shoot it... Ahh~... Hannhh~... Shoot it inside..."
                                                                                                                                            if tmra_lst >= 7:
                                                                                                                                                play sound "audio/creaky door.mp3"
                                                                                                                                                "{i}Door opens.{/i}"
                                                                                                                                                tr "Fuhhcck~... What was that..."
                                                                                                                                                z "I don't know..."
                                                                                                                                                tr "Someone... Ahhh~... Someone just came in... We need to stop..."
                                                                                                                                                z "Yeah... Lemme just..."
                                                                                                                                                play sound "audio/Falling2.mp3"
                                                                                                                                                play audio "audio/magic 7.mp3"
                                                                                                                                                stop background_s
                                                                                                                                                stop background_s2
                                                                                                                                                stop music
                                                                                                                                                scene v13462 with vpunch
                                                                                                                                                z "Ughh... Fuck..." (multiple=2)
                                                                                                                                                tr "Aaaahhh~..." (multiple=2)
                                                                                                                                                play sound "audio/Cloth_rustle.wav"
                                                                                                                                                scene v13463 with Dissolve(1)
                                                                                                                                                tr "Hahhh~... Fuck... That was..."
                                                                                                                                                z "That was amazing, but we need t-"
                                                                                                                                                scene v13464 with dissolve
                                                                                                                                                tmra "Torr?!"
                                                                                                                                                scene v13465 with Dissolve(1)
                                                                                                                                                tmra "What's all that noi-"
                                                                                                                                                scene v13466 with Dissolve(1)
                                                                                                                                                z "..."
                                                                                                                                                tmra "What th-"
                                                                                                                                                tmra "..."
                                                                                                                                                with Pause(1)
                                                                                                                                                play audio "audio/camera.mp3"
                                                                                                                                                scene black
                                                                                                                                                with Pause(0.5)
                                                                                                                                                play sound "audio/Falling2.mp3"
                                                                                                                                                with vpunch
                                                                                                                                                with vpunch
                                                                                                                                                with vpunch
                                                                                                                                                with vpunch
                                                                                                                                                tmra "AAAH!"
                                                                                                                                                with Pause(0.5)
                                                                                                                                                play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
                                                                                                                                                play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                                                                                                                                                show v13m5 with Dissolve(1)
                                                                                                                                                tmra "Aaaahhh~... Ahhhhh~... Fuhcckkk~..."
                                                                                                                                                tr "How do you like that Tamara?"
                                                                                                                                                tmra "It feelshhh..."
                                                                                                                                                tr "Yes?"
                                                                                                                                                tmra "Ahh~... It's... Hahh~... Doesn't feel that good... Ahh~..."
                                                                                                                                                tr "Really? You're making a really dumb face down there..."
                                                                                                                                                tr "Almost like you're losing it from the pleasure..."
                                                                                                                                                tmra "That'th nohhht... Ahhh~..."
                                                                                                                                                tr "You can't even speak properly..."
                                                                                                                                                tr "Just admit it. You love getting piped like the little slut you are..."
                                                                                                                                                tmra "Ahh~... Noooo~... I'm not a shlut..."
                                                                                                                                                tmra "You and Candy... Ahhh~... You're the slutsss~..."
                                                                                                                                                tmra "How long... Ahhh~... ...have you two been fucking him..."
                                                                                                                                                tmra "Ahhh~... Just because you can't resist his... Ahhh~... ...huge di-"
                                                                                                                                                tmra "Ahhhhh~ Huge asshole behaviour..."
                                                                                                                                                tr "Play nice, Tamara..."
                                                                                                                                                scene v13472 with Dissolve(1)
                                                                                                                                                tr "You look really cute... Seems you already came a few times..."
                                                                                                                                                play audio "audio/kiss.mp3"
                                                                                                                                                scene v13473 with dissolve
                                                                                                                                                tmra "Thut uppp..." (multiple=2)
                                                                                                                                                tr "Ah!" (multiple=2)
                                                                                                                                                scene v13474 with dissolve
                                                                                                                                                tmra "Ahh~... Waihht~... What are you-"
                                                                                                                                                scene v13475 with vpunch
                                                                                                                                                tr "Eeep! Don't bite it!"
                                                                                                                                                scene v13476 with dissolve
                                                                                                                                                tr "Hannhh~... Fuhhhcckkk~..."
                                                                                                                                                scene v13477 with Dissolve(1)
                                                                                                                                                tmra "Hmmn~..."
                                                                                                                                                z "..."
                                                                                                                                                menu:
                                                                                                                                                    "Push Tamara's face closer to Torr's and make them make out.":
                                                                                                                                                        play sound "audio/Cloth_rustle.wav"
                                                                                                                                                        scene v13478 with vpunch
                                                                                                                                                        tmra "Ahh~!" (multiple=2)
                                                                                                                                                        tr "?!" (multiple=2)
                                                                                                                                                        play audio "audio/kiss.mp3"
                                                                                                                                                        scene v13479 with hpunch
                                                                                                                                                        tmra "HMNN~!" (multiple=2)
                                                                                                                                                        tr "HMMM?!" (multiple=2)
                                                                                                                                                        scene v13480 with Dissolve(1)
                                                                                                                                                        z "Be nice to each other, you two..."
                                                                                                                                                        show v13m40 with Dissolve(1)
                                                                                                                                                        tmra "Hmmnn~... Mnnn~..."
                                                                                                                                                        tr "Mmmmhhnnn~..."
                                                                                                                                                        z "Look at you getting along... So cute..."
                                                                                                                                                        tmra "Nmmmmnn~... Mhhhnn~..."
                                                                                                                                                        tr "Hmmmn~... Ahhmmmm~..."
                                                                                                                                                        z "Two besties putting their differences behind and joining their lips..."
                                                                                                                                                        tr "Hmmmnnn~... Fuhhhmm~..."
                                                                                                                                                        tmra "Ihmmmmmnn~... Fuhhhmmm~..."
                                                                                                                                                        z "Tamara... I'm gonna cum..."
                                                                                                                                                        z "I hope you're ready... I'm shooting it inside you..."
                                                                                                                                                        tmra "Hmmnnn~?! Inmmmm~! Mhhhnnn~!"
                                                                                                                                                        z "Yeah. I don't understand... I'm gonna cum..."
                                                                                                                                                        tmra "Mhhhmmmmnnn~!"
                                                                                                                                                        tmra "Hmmmm-"
                                                                                                                                                        play audio "audio/creak.mp3"
                                                                                                                                                        play sound "audio/magic 7.mp3"
                                                                                                                                                        stop background_s fadeout 1.0
                                                                                                                                                        stop background_s2 fadeout 1.0
                                                                                                                                                        scene v13481 with hpunch
                                                                                                                                                        tmra "AAAHHHHH~!" (multiple=2)
                                                                                                                                                        tr "Ahh~?!" (multiple=2)
                                                                                                                                                    "Keep fucking Tamara like this.":
                                                                                                                                                        show v13m5 with Dissolve(1)
                                                                                                                                                        tmra "Aaaannh~... Waihhtt~..."
                                                                                                                                                        z "Come back here, Tamara."
                                                                                                                                                        tr "That was rude, Tamara..."
                                                                                                                                                        tr "Don't suck on other people's nipples without permission."
                                                                                                                                                        tmra "Hahh~... It's your fault..."
                                                                                                                                                        tr "Come on, apologise."
                                                                                                                                                        tmra "Nooo~... Ahhh~... Fuck you..."
                                                                                                                                                        tr "If you say you're sorry [mc_name] might creampie you."
                                                                                                                                                        tmra "Ahhh~... C-Creampie?! Waihht~..."
                                                                                                                                                        z "Wait, I never agreed to this..."
                                                                                                                                                        tr "Come on, we need to put cocky Tamara in her place, [mc_name]..."
                                                                                                                                                        tr "If she behaves like a good girl, would you creampie her?"
                                                                                                                                                        z "I mean..."
                                                                                                                                                        tr "What do you say, Tamara? Are you a good girl?"
                                                                                                                                                        tmra "Ahh~... Fuhcckk~..."
                                                                                                                                                        tr "Now, now. Tamara. No cursing."
                                                                                                                                                        tr "Just say you're sorry. And [mc_name] will shoot all his warm load inside you."
                                                                                                                                                        tmra "Hnnn~... Ahhh~... Inshide..."
                                                                                                                                                        tr "Yup, yup. All of it inside you."
                                                                                                                                                        tr "In return for one small sorry."
                                                                                                                                                        tr "Good deal, no?"
                                                                                                                                                        tmra "Ahh~... Hahhhhh~... Anhhh~..."
                                                                                                                                                        tmra "I'm... Mmmmnn~... Hahhh~... I'm..."
                                                                                                                                                        tmra "I'm cumming... Ahh~... Hahh~... Hanhh~..."
                                                                                                                                                        z "I'm gonna cum too..."
                                                                                                                                                        tr "Shoot it... Ahh~... Hannhh~... Shoot it inside..."
                                                                                                                                                        if tmra_lst >= 7:
                                                                                                                                                            play sound "audio/creaky door.mp3"
                                                                                                                                                            "{i}Door opens.{/i}"
                                                                                                                                                            tr "Fuhhcck~... What was that..."
                                                                                                                                                            z "I don't know..."
                                                                                                                                                            tr "Someone... Ahhh~... Someone just came in... We need to stop..."
                                                                                                                                                            z "Yeah... Lemme just..."
                                                                                                                                                            play sound "audio/Falling2.mp3"
                                                                                                                                                            play audio "audio/magic 7.mp3"
                                                                                                                                                            stop background_s
                                                                                                                                                            stop background_s2
                                                                                                                                                            stop music
                                                                                                                                                            scene v13462 with vpunch
                                                                                                                                                            z "Ughh... Fuck..." (multiple=2)
                                                                                                                                                            tr "Aaaahhh~..." (multiple=2)
                                                                                                                                                            play sound "audio/Cloth_rustle.wav"
                                                                                                                                                            scene v13463 with Dissolve(1)
                                                                                                                                                            tr "Hahhh~... Fuck... That was..."
                                                                                                                                                            z "That was amazing, but we need t-"
                                                                                                                                                            scene v13464 with dissolve
                                                                                                                                                            tmra "Torr?!"
                                                                                                                                                            scene v13465 with Dissolve(1)
                                                                                                                                                            tmra "What's all that noi-"
                                                                                                                                                            scene v13466 with Dissolve(1)
                                                                                                                                                            z "..."
                                                                                                                                                            tmra "What th-"
                                                                                                                                                            tmra "..."
                                                                                                                                                            with Pause(1)
                                                                                                                                                            play audio "audio/camera.mp3"
                                                                                                                                                            scene black
                                                                                                                                                            with Pause(0.5)
                                                                                                                                                            play sound "audio/Falling2.mp3"
                                                                                                                                                            with vpunch
                                                                                                                                                            with vpunch
                                                                                                                                                            with vpunch
                                                                                                                                                            with vpunch
                                                                                                                                                            tmra "AAAH!"
                                                                                                                                                            with Pause(0.5)
                                                                                                                                                            play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
                                                                                                                                                            play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                                                                                                                                                            show v13m5 with Dissolve(1)
                                                                                                                                                            tmra "Aaaahhh~... Ahhhhh~... Fuhcckkk~..."
                                                                                                                                                            tr "How do you like that Tamara?"
                                                                                                                                                            tmra "It feelshhh..."
                                                                                                                                                            tr "Yes?"
                                                                                                                                                            tmra "Ahh~... It's... Hahh~... Doesn't feel that good... Ahh~..."
                                                                                                                                                            tr "Really? You're making a really dumb face down there..."
                                                                                                                                                            tr "Almost like you're losing it from the pleasure..."
                                                                                                                                                            tmra "That'th nohhht... Ahhh~..."
                                                                                                                                                            tr "You can't even speak properly..."
                                                                                                                                                            tr "Just admit it. You love getting piped like the little slut you are..."
                                                                                                                                                            tmra "Ahh~... Noooo~... I'm not a shlut..."
                                                                                                                                                            tmra "You and Candy... Ahhh~... You're the slutsss~..."
                                                                                                                                                            tmra "How long... Ahhh~... ...have you two been fucking him..."
                                                                                                                                                            tmra "Ahhh~... Just because you can't resist his... Ahhh~... ...huge di-"
                                                                                                                                                            tmra "Ahhhhh~ Huge asshole behaviour..."
                                                                                                                                                            tr "Play nice, Tamara..."
                                                                                                                                                            scene v13472 with Dissolve(1)
                                                                                                                                                            tr "You look really cute... Seems you already came a few times..."
                                                                                                                                                            play audio "audio/kiss.mp3"
                                                                                                                                                            scene v13473 with dissolve
                                                                                                                                                            tmra "Thut uppp..." (multiple=2)
                                                                                                                                                            tr "Ah!" (multiple=2)
                                                                                                                                                            scene v13474 with dissolve
                                                                                                                                                            tmra "Ahh~... Waihht~... What are you-"
                                                                                                                                                            scene v13475 with vpunch
                                                                                                                                                            tr "Eeep! Don't bite it!"
                                                                                                                                                            scene v13476 with dissolve
                                                                                                                                                            tr "Hannhh~... Fuhhhcckkk~..."
                                                                                                                                                            scene v13477 with Dissolve(1)
                                                                                                                                                            tmra "Hmmn~..."
                                                                                                                                                            z "..."
                                                                                                                                                            menu:
                                                                                                                                                                "Push Tamara's face closer to Torr's and make them make out.":
                                                                                                                                                                    play sound "audio/Cloth_rustle.wav"
                                                                                                                                                                    scene v13478 with vpunch
                                                                                                                                                                    tmra "Ahh~!" (multiple=2)
                                                                                                                                                                    tr "?!" (multiple=2)
                                                                                                                                                                    play audio "audio/kiss.mp3"
                                                                                                                                                                    scene v13479 with hpunch
                                                                                                                                                                    tmra "HMNN~!" (multiple=2)
                                                                                                                                                                    tr "HMMM?!" (multiple=2)
                                                                                                                                                                    scene v13480 with Dissolve(1)
                                                                                                                                                                    z "Be nice to each other, you two..."
                                                                                                                                                                    show v13m40 with Dissolve(1)
                                                                                                                                                                    tmra "Hmmnn~... Mnnn~..."
                                                                                                                                                                    tr "Mmmmhhnnn~..."
                                                                                                                                                                    z "Look at you getting along... So cute..."
                                                                                                                                                                    tmra "Nmmmmnn~... Mhhhnn~..."
                                                                                                                                                                    tr "Hmmmn~... Ahhmmmm~..."
                                                                                                                                                                    z "Two besties putting their differences behind and joining their lips..."
                                                                                                                                                                    tr "Hmmmnnn~... Fuhhhmm~..."
                                                                                                                                                                    tmra "Ihmmmmmnn~... Fuhhhmmm~..."
                                                                                                                                                                    z "Tamara... I'm gonna cum..."
                                                                                                                                                                    z "I hope you're ready... I'm shooting it inside you..."
                                                                                                                                                                    tmra "Hmmnnn~?! Inmmmm~! Mhhhnnn~!"
                                                                                                                                                                    z "Yeah. I don't understand... I'm gonna cum..."
                                                                                                                                                                    tmra "Mhhhmmmmnnn~!"
                                                                                                                                                                    tmra "Hmmmm-"
                                                                                                                                                                    play audio "audio/creak.mp3"
                                                                                                                                                                    play sound "audio/magic 7.mp3"
                                                                                                                                                                    stop background_s fadeout 1.0
                                                                                                                                                                    stop background_s2 fadeout 1.0
                                                                                                                                                                    scene v13481 with hpunch
                                                                                                                                                                    tmra "AAAHHHHH~!" (multiple=2)
                                                                                                                                                                    tr "Ahh~?!" (multiple=2)
                                                                                                                                                                "Keep fucking Tamara like this.":
                                                                                                                                                                    show v13m5 with Dissolve(1)
                                                                                                                                                                    tmra "Aaaannh~... Waihhtt~..."
                                                                                                                                                                    z "Come back here, Tamara."
                                                                                                                                                                    tr "That was rude, Tamara..."
                                                                                                                                                                    tr "Don't suck on other people's nipples without permission."
                                                                                                                                                                    tmra "Hahh~... It's your fault..."
                                                                                                                                                                    tr "Come on, apologise."
                                                                                                                                                                    tmra "Nooo~... Ahhh~... Fuck you..."
                                                                                                                                                                    tr "If you say you're sorry [mc_name] might creampie you."
                                                                                                                                                                    tmra "Ahhh~... C-Creampie?! Waihht~..."
                                                                                                                                                                    z "Wait, I never agreed to this..."
                                                                                                                                                                    tr "Come on, we need to put cocky Tamara in her place, [mc_name]..."
                                                                                                                                                                    tr "If she behaves like a good girl, would you creampie her?"
                                                                                                                                                                    z "I mean..."
                                                                                                                                                                    tr "What do you say, Tamara? Are you a good girl?"
                                                                                                                                                                    tmra "Ahh~... Fuhcckk~..."
                                                                                                                                                                    tr "Now, now. Tamara. No cursing."
                                                                                                                                                                    tr "Just say you're sorry. And [mc_name] will shoot all his warm load inside you."
                                                                                                                                                                    tmra "Hnnn~... Ahhh~... Inshide..."
                                                                                                                                                                    tr "Yup, yup. All of it inside you."
                                                                                                                                                                    tr "In return for one small sorry."
                                                                                                                                                                    tr "Good deal, no?"
                                                                                                                                                                    tmra "Ahh~... Hahhhhh~... Anhhh~..."
                                                                                                                                                                    tmra "I'm... Mmmmnn~... Hahhh~... I'm..."
                                                                                                                                                                    tmra "I'm cumming... Ahh~... Hahh~... Hanhh~..."
                                                                                                                                                                    z "I'm gonna cum too..."
                                                                                                                                                                    tr "Shoot it... Ahh~... Hannhh~... Shoot it inside..."
                                                                                                                                                                    if tmra_lst >= 7:
                                                                                                                                                                        play sound "audio/creaky door.mp3"
                                                                                                                                                                        "{i}Door opens.{/i}"
                                                                                                                                                                        tr "Fuhhcck~... What was that..."
                                                                                                                                                                        z "I don't know..."
                                                                                                                                                                        tr "Someone... Ahhh~... Someone just came in... We need to stop..."
                                                                                                                                                                        z "Yeah... Lemme just..."
                                                                                                                                                                        play sound "audio/Falling2.mp3"
                                                                                                                                                                        play audio "audio/magic 7.mp3"
                                                                                                                                                                        stop background_s
                                                                                                                                                                        stop background_s2
                                                                                                                                                                        stop music
                                                                                                                                                                        scene v13462 with vpunch
                                                                                                                                                                        z "Ughh... Fuck..." (multiple=2)
                                                                                                                                                                        tr "Aaaahhh~..." (multiple=2)
                                                                                                                                                                        play sound "audio/Cloth_rustle.wav"
                                                                                                                                                                        scene v13463 with Dissolve(1)
                                                                                                                                                                        tr "Hahhh~... Fuck... That was..."
                                                                                                                                                                        z "That was amazing, but we need t-"
                                                                                                                                                                        scene v13464 with dissolve
                                                                                                                                                                        tmra "Torr?!"
                                                                                                                                                                        scene v13465 with Dissolve(1)
                                                                                                                                                                        tmra "What's all that noi-"
                                                                                                                                                                        scene v13466 with Dissolve(1)
                                                                                                                                                                        z "..."
                                                                                                                                                                        tmra "What th-"
                                                                                                                                                                        tmra "..."
                                                                                                                                                                        with Pause(1)
                                                                                                                                                                        play audio "audio/camera.mp3"
                                                                                                                                                                        scene black
                                                                                                                                                                        with Pause(0.5)
                                                                                                                                                                        play sound "audio/Falling2.mp3"
                                                                                                                                                                        with vpunch
                                                                                                                                                                        with vpunch
                                                                                                                                                                        with vpunch
                                                                                                                                                                        with vpunch
                                                                                                                                                                        tmra "AAAH!"
                                                                                                                                                                        with Pause(0.5)
                                                                                                                                                                        play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
                                                                                                                                                                        play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                                                                                                                                                                        show v13m5 with Dissolve(1)
                                                                                                                                                                        tmra "Aaaahhh~... Ahhhhh~... Fuhcckkk~..."
                                                                                                                                                                        tr "How do you like that Tamara?"
                                                                                                                                                                        tmra "It feelshhh..."
                                                                                                                                                                        tr "Yes?"
                                                                                                                                                                        tmra "Ahh~... It's... Hahh~... Doesn't feel that good... Ahh~..."
                                                                                                                                                                        tr "Really? You're making a really dumb face down there..."
                                                                                                                                                                        tr "Almost like you're losing it from the pleasure..."
                                                                                                                                                                        tmra "That'th nohhht... Ahhh~..."
                                                                                                                                                                        tr "You can't even speak properly..."
                                                                                                                                                                        tr "Just admit it. You love getting piped like the little slut you are..."
                                                                                                                                                                        tmra "Ahh~... Noooo~... I'm not a shlut..."
                                                                                                                                                                        tmra "You and Candy... Ahhh~... You're the slutsss~..."
                                                                                                                                                                        tmra "How long... Ahhh~... ...have you two been fucking him..."
                                                                                                                                                                        tmra "Ahhh~... Just because you can't resist his... Ahhh~... ...huge di-"
                                                                                                                                                                        tmra "Ahhhhh~ Huge asshole behaviour..."
                                                                                                                                                                        tr "Play nice, Tamara..."
                                                                                                                                                                        scene v13472 with Dissolve(1)
                                                                                                                                                                        tr "You look really cute... Seems you already came a few times..."
                                                                                                                                                                        play audio "audio/kiss.mp3"
                                                                                                                                                                        scene v13473 with dissolve
                                                                                                                                                                        tmra "Thut uppp..." (multiple=2)
                                                                                                                                                                        tr "Ah!" (multiple=2)
                                                                                                                                                                        scene v13474 with dissolve
                                                                                                                                                                        tmra "Ahh~... Waihht~... What are you-"
                                                                                                                                                                        scene v13475 with vpunch
                                                                                                                                                                        tr "Eeep! Don't bite it!"
                                                                                                                                                                        scene v13476 with dissolve
                                                                                                                                                                        tr "Hannhh~... Fuhhhcckkk~..."
                                                                                                                                                                        scene v13477 with Dissolve(1)
                                                                                                                                                                        tmra "Hmmn~..."
                                                                                                                                                                        z "..."
                                                                                                                                                                        menu:
                                                                                                                                                                            "Push Tamara's face closer to Torr's and make them make out.":
                                                                                                                                                                                play sound "audio/Cloth_rustle.wav"
                                                                                                                                                                                scene v13478 with vpunch
                                                                                                                                                                                tmra "Ahh~!" (multiple=2)
                                                                                                                                                                                tr "?!" (multiple=2)
                                                                                                                                                                                play audio "audio/kiss.mp3"
                                                                                                                                                                                scene v13479 with hpunch
                                                                                                                                                                                tmra "HMNN~!" (multiple=2)
                                                                                                                                                                                tr "HMMM?!" (multiple=2)
                                                                                                                                                                                scene v13480 with Dissolve(1)
                                                                                                                                                                                z "Be nice to each other, you two..."
                                                                                                                                                                                show v13m40 with Dissolve(1)
                                                                                                                                                                                tmra "Hmmnn~... Mnnn~..."
                                                                                                                                                                                tr "Mmmmhhnnn~..."
                                                                                                                                                                                z "Look at you getting along... So cute..."
                                                                                                                                                                                tmra "Nmmmmnn~... Mhhhnn~..."
                                                                                                                                                                                tr "Hmmmn~... Ahhmmmm~..."
                                                                                                                                                                                z "Two besties putting their differences behind and joining their lips..."
                                                                                                                                                                                tr "Hmmmnnn~... Fuhhhmm~..."
                                                                                                                                                                                tmra "Ihmmmmmnn~... Fuhhhmmm~..."
                                                                                                                                                                                z "Tamara... I'm gonna cum..."
                                                                                                                                                                                z "I hope you're ready... I'm shooting it inside you..."
                                                                                                                                                                                tmra "Hmmnnn~?! Inmmmm~! Mhhhnnn~!"
                                                                                                                                                                                z "Yeah. I don't understand... I'm gonna cum..."
                                                                                                                                                                                tmra "Mhhhmmmmnnn~!"
                                                                                                                                                                                tmra "Hmmmm-"
                                                                                                                                                                                play audio "audio/creak.mp3"
                                                                                                                                                                                play sound "audio/magic 7.mp3"
                                                                                                                                                                                stop background_s fadeout 1.0
                                                                                                                                                                                stop background_s2 fadeout 1.0
                                                                                                                                                                                scene v13481 with hpunch
                                                                                                                                                                                tmra "AAAHHHHH~!" (multiple=2)
                                                                                                                                                                                tr "Ahh~?!" (multiple=2)
                                                                                                                                                                            "Keep fucking Tamara like this.":
                                                                                                                                                                                show v13m5 with Dissolve(1)
                                                                                                                                                                                tmra "Aaaannh~... Waihhtt~..."
                                                                                                                                                                                z "Come back here, Tamara."
                                                                                                                                                                                tr "That was rude, Tamara..."
                                                                                                                                                                                tr "Don't suck on other people's nipples without permission."
                                                                                                                                                                                tmra "Hahh~... It's your fault..."
                                                                                                                                                                                tr "Come on, apologise."
                                                                                                                                                                                tmra "Nooo~... Ahhh~... Fuck you..."
                                                                                                                                                                                tr "If you say you're sorry [mc_name] might creampie you."
                                                                                                                                                                                tmra "Ahhh~... C-Creampie?! Waihht~..."
                                                                                                                                                                                z "Wait, I never agreed to this..."
                                                                                                                                                                                tr "Come on, we need to put cocky Tamara in her place, [mc_name]..."
                                                                                                                                                                                tr "If she behaves like a good girl, would you creampie her?"
                                                                                                                                                                                z "I mean..."
                                                                                                                                                                                tr "What do you say, Tamara? Are you a good girl?"
                                                                                                                                                                                tmra "Ahh~... Fuhcckk~..."
                                                                                                                                                                                tr "Now, now. Tamara. No cursing."
                                                                                                                                                                                tr "Just say you're sorry. And [mc_name] will shoot all his warm load inside you."
                                                                                                                                                                                tmra "Hnnn~... Ahhh~... Inshide..."
                                                                                                                                                                                tr "Yup, yup. All of it inside you."
                                                                                                                                                                                tr "In return for one small sorry."
                                                                                                                                                                                tr "Good deal, no?"
                                                                                                                                                                                tmra "Ahh~... Hahhhhh~... Anhhh~..."
                                                                                                                                                                                tmra "I'm... Mmmmnn~... Hahhh~... I'm..."
                                                                                                                                                                                tmra "I'm cumming... Ahh~... Hahh~... Hanhh~..."
                                                                                                                                                                                z "I'm gonna cum too..."
                                                                                                                                                                                tr "Shoot it... Ahh~... Hannhh~... Shoot it inside..."
                                                                                                                                                                                if tmra_lst >= 7:
                                                                                                                                                                                    play sound "audio/creaky door.mp3"
                                                                                                                                                                                    "{i}Door opens.{/i}"
                                                                                                                                                                                    tr "Fuhhcck~... What was that..."
                                                                                                                                                                                    z "I don't know..."
                                                                                                                                                                                    tr "Someone... Ahhh~... Someone just came in... We need to stop..."
                                                                                                                                                                                    z "Yeah... Lemme just..."
                                                                                                                                                                                    play sound "audio/Falling2.mp3"
                                                                                                                                                                                    play audio "audio/magic 7.mp3"
                                                                                                                                                                                    stop background_s
                                                                                                                                                                                    stop background_s2
                                                                                                                                                                                    stop music
                                                                                                                                                                                    scene v13462 with vpunch
                                                                                                                                                                                    z "Ughh... Fuck..." (multiple=2)
                                                                                                                                                                                    tr "Aaaahhh~..." (multiple=2)
                                                                                                                                                                                    play sound "audio/Cloth_rustle.wav"
                                                                                                                                                                                    scene v13463 with Dissolve(1)
                                                                                                                                                                                    tr "Hahhh~... Fuck... That was..."
                                                                                                                                                                                    z "That was amazing, but we need t-"
                                                                                                                                                                                    scene v13464 with dissolve
                                                                                                                                                                                    tmra "Torr?!"
                                                                                                                                                                                    scene v13465 with Dissolve(1)
                                                                                                                                                                                    tmra "What's all that noi-"
                                                                                                                                                                                    scene v13466 with Dissolve(1)
                                                                                                                                                                                    z "..."
                                                                                                                                                                                    tmra "What th-"
                                                                                                                                                                                    tmra "..."
                                                                                                                                                                                    with Pause(1)
                                                                                                                                                                                    play audio "audio/camera.mp3"
                                                                                                                                                                                    scene black
                                                                                                                                                                                    with Pause(0.5)
                                                                                                                                                                                    play sound "audio/Falling2.mp3"
                                                                                                                                                                                    with vpunch
                                                                                                                                                                                    with vpunch
                                                                                                                                                                                    with vpunch
                                                                                                                                                                                    with vpunch
                                                                                                                                                                                    tmra "AAAH!"
                                                                                                                                                                                    with Pause(0.5)
                                                                                                                                                                                    play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
                                                                                                                                                                                    play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                                                                                                                                                                                    show v13m5 with Dissolve(1)
                                                                                                                                                                                    tmra "Aaaahhh~... Ahhhhh~... Fuhcckkk~..."
                                                                                                                                                                                    tr "How do you like that Tamara?"
                                                                                                                                                                                    tmra "It feelshhh..."
                                                                                                                                                                                    tr "Yes?"
                                                                                                                                                                                    tmra "Ahh~... It's... Hahh~... Doesn't feel that good... Ahh~..."
                                                                                                                                                                                    tr "Really? You're making a really dumb face down there..."
                                                                                                                                                                                    tr "Almost like you're losing it from the pleasure..."
                                                                                                                                                                                    tmra "That'th nohhht... Ahhh~..."
                                                                                                                                                                                    tr "You can't even speak properly..."
                                                                                                                                                                                    tr "Just admit it. You love getting piped like the little slut you are..."
                                                                                                                                                                                    tmra "Ahh~... Noooo~... I'm not a shlut..."
                                                                                                                                                                                    tmra "You and Candy... Ahhh~... You're the slutsss~..."
                                                                                                                                                                                    tmra "How long... Ahhh~... ...have you two been fucking him..."
                                                                                                                                                                                    tmra "Ahhh~... Just because you can't resist his... Ahhh~... ...huge di-"
                                                                                                                                                                                    tmra "Ahhhhh~ Huge asshole behaviour..."
                                                                                                                                                                                    tr "Play nice, Tamara..."
                                                                                                                                                                                    scene v13472 with Dissolve(1)
                                                                                                                                                                                    tr "You look really cute... Seems you already came a few times..."
                                                                                                                                                                                    play audio "audio/kiss.mp3"
                                                                                                                                                                                    scene v13473 with dissolve
                                                                                                                                                                                    tmra "Thut uppp..." (multiple=2)
                                                                                                                                                                                    tr "Ah!" (multiple=2)
                                                                                                                                                                                    scene v13474 with dissolve
                                                                                                                                                                                    tmra "Ahh~... Waihht~... What are you-"
                                                                                                                                                                                    scene v13475 with vpunch
                                                                                                                                                                                    tr "Eeep! Don't bite it!"
                                                                                                                                                                                    scene v13476 with dissolve
                                                                                                                                                                                    tr "Hannhh~... Fuhhhcckkk~..."
                                                                                                                                                                                    scene v13477 with Dissolve(1)
                                                                                                                                                                                    tmra "Hmmn~..."
                                                                                                                                                                                    z "..."
                                                                                                                                                                                    menu:
                                                                                                                                                                                        "Push Tamara's face closer to Torr's and make them make out.":
                                                                                                                                                                                            play sound "audio/Cloth_rustle.wav"
                                                                                                                                                                                            scene v13478 with vpunch
                                                                                                                                                                                            tmra "Ahh~!" (multiple=2)
                                                                                                                                                                                            tr "?!" (multiple=2)
                                                                                                                                                                                            play audio "audio/kiss.mp3"
                                                                                                                                                                                            scene v13479 with hpunch
                                                                                                                                                                                            tmra "HMNN~!" (multiple=2)
                                                                                                                                                                                            tr "HMMM?!" (multiple=2)
                                                                                                                                                                                            scene v13480 with Dissolve(1)
                                                                                                                                                                                            z "Be nice to each other, you two..."
                                                                                                                                                                                            show v13m40 with Dissolve(1)
                                                                                                                                                                                            tmra "Hmmnn~... Mnnn~..."
                                                                                                                                                                                            tr "Mmmmhhnnn~..."
                                                                                                                                                                                            z "Look at you getting along... So cute..."
                                                                                                                                                                                            tmra "Nmmmmnn~... Mhhhnn~..."
                                                                                                                                                                                            tr "Hmmmn~... Ahhmmmm~..."
                                                                                                                                                                                            z "Two besties putting their differences behind and joining their lips..."
                                                                                                                                                                                            tr "Hmmmnnn~... Fuhhhmm~..."
                                                                                                                                                                                            tmra "Ihmmmmmnn~... Fuhhhmmm~..."
                                                                                                                                                                                            z "Tamara... I'm gonna cum..."
                                                                                                                                                                                            z "I hope you're ready... I'm shooting it inside you..."
                                                                                                                                                                                            tmra "Hmmnnn~?! Inmmmm~! Mhhhnnn~!"
                                                                                                                                                                                            z "Yeah. I don't understand... I'm gonna cum..."
                                                                                                                                                                                            tmra "Mhhhmmmmnnn~!"
                                                                                                                                                                                            tmra "Hmmmm-"
                                                                                                                                                                                            play audio "audio/creak.mp3"
                                                                                                                                                                                            play sound "audio/magic 7.mp3"
                                                                                                                                                                                            stop background_s fadeout 1.0
                                                                                                                                                                                            stop background_s2 fadeout 1.0
                                                                                                                                                                                            scene v13481 with hpunch
                                                                                                                                                                                            tmra "AAAHHHHH~!" (multiple=2)
                                                                                                                                                                                            tr "Ahh~?!" (multiple=2)
                                                                                                                                                                                        "Keep fucking Tamara like this.":
                                                                                                                                                                                            show v13m5 with Dissolve(1)
                                                                                                                                                                                            tmra "Aaaannh~... Waihhtt~..."
                                                                                                                                                                                            z "Come back here, Tamara."
                                                                                                                                                                                            tr "That was rude, Tamara..."
                                                                                                                                                                                            tr "Don't suck on other people's nipples without permission."
                                                                                                                                                                                            tmra "Hahh~... It's your fault..."
                                                                                                                                                                                            tr "Come on, apologise."
                                                                                                                                                                                            tmra "Nooo~... Ahhh~... Fuck you..."
                                                                                                                                                                                            tr "If you say you're sorry [mc_name] might creampie you."
                                                                                                                                                                                            tmra "Ahhh~... C-Creampie?! Waihht~..."
                                                                                                                                                                                            z "Wait, I never agreed to this..."
                                                                                                                                                                                            tr "Come on, we need to put cocky Tamara in her place, [mc_name]..."
                                                                                                                                                                                            tr "If she behaves like a good girl, would you creampie her?"
                                                                                                                                                                                            z "I mean..."
                                                                                                                                                                                            tr "What do you say, Tamara? Are you a good girl?"
                                                                                                                                                                                            tmra "Ahh~... Fuhcckk~..."
                                                                                                                                                                                            tr "Now, now. Tamara. No cursing."
                                                                                                                                                                                            tr "Just say you're sorry. And [mc_name] will shoot all his warm load inside you."
                                                                                                                                                                                            tmra "Hnnn~... Ahhh~... Inshide..."
                                                                                                                                                                                            tr "Yup, yup. All of it inside you."
                                                                                                                                                                                            tr "In return for one small sorry."
                                                                                                                                                                                            tr "Good deal, no?"
                                                                                                                                                                                            tmra "Ahh~... Hahhhhh~... Anhhh~..."
                                                                                                                                                                                            tmra "I'm... Mmmmnn~... Hahhh~... I'm..."
                                                                                                                                                                                            tmra "I'm cumming... Ahh~... Hahh~... Hanhh~..."
                                                                                                                                                                                            z "I'm gonna cum too..."
                                                                                                                                                                                            tr "Shoot it... Ahh~... Hannhh~... Shoot it inside..."
                                                                                                                                                                                            if tmra_lst >= 7:
                                                                                                                                                                                                play sound "audio/creaky door.mp3"
                                                                                                                                                                                                "{i}Door opens.{/i}"
                                                                                                                                                                                                tr "Fuhhcck~... What was that..."
                                                                                                                                                                                                z "I don't know..."
                                                                                                                                                                                                tr "Someone... Ahhh~... Someone just came in... We need to stop..."
                                                                                                                                                                                                z "Yeah... Lemme just..."
                                                                                                                                                                                                play sound "audio/Falling2.mp3"
                                                                                                                                                                                                play audio "audio/magic 7.mp3"
                                                                                                                                                                                                stop background_s
                                                                                                                                                                                                stop background_s2
                                                                                                                                                                                                stop music
                                                                                                                                                                                                scene v13462 with vpunch
                                                                                                                                                                                                z "Ughh... Fuck..." (multiple=2)
                                                                                                                                                                                                tr "Aaaahhh~..." (multiple=2)
                                                                                                                                                                                                play sound "audio/Cloth_rustle.wav"
                                                                                                                                                                                                scene v13463 with Dissolve(1)
                                                                                                                                                                                                tr "Hahhh~... Fuck... That was..."
                                                                                                                                                                                                z "That was amazing, but we need t-"
                                                                                                                                                                                                scene v13464 with dissolve
                                                                                                                                                                                                tmra "Torr?!"
                                                                                                                                                                                                scene v13465 with Dissolve(1)
                                                                                                                                                                                                tmra "What's all that noi-"
                                                                                                                                                                                                scene v13466 with Dissolve(1)
                                                                                                                                                                                                z "..."
                                                                                                                                                                                                tmra "What th-"
                                                                                                                                                                                                tmra "..."
                                                                                                                                                                                                with Pause(1)
                                                                                                                                                                                                play audio "audio/camera.mp3"
                                                                                                                                                                                                scene black
                                                                                                                                                                                                with Pause(0.5)
                                                                                                                                                                                                play sound "audio/Falling2.mp3"
                                                                                                                                                                                                with vpunch
                                                                                                                                                                                                with vpunch
                                                                                                                                                                                                with vpunch
                                                                                                                                                                                                with vpunch
                                                                                                                                                                                                tmra "AAAH!"
                                                                                                                                                                                                with Pause(0.5)
                                                                                                                                                                                                play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
                                                                                                                                                                                                play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                                                                                                                                                                                                show v13m5 with Dissolve(1)
                                                                                                                                                                                                tmra "Aaaahhh~... Ahhhhh~... Fuhcckkk~..."
                                                                                                                                                                                                tr "How do you like that Tamara?"
                                                                                                                                                                                                tmra "It feelshhh..."
                                                                                                                                                                                                tr "Yes?"
                                                                                                                                                                                                tmra "Ahh~... It's... Hahh~... Doesn't feel that good... Ahh~..."
                                                                                                                                                                                                tr "Really? You're making a really dumb face down there..."
                                                                                                                                                                                                tr "Almost like you're losing it from the pleasure..."
                                                                                                                                                                                                tmra "That'th nohhht... Ahhh~..."
                                                                                                                                                                                                tr "You can't even speak properly..."
                                                                                                                                                                                                tr "Just admit it. You love getting piped like the little slut you are..."
                                                                                                                                                                                                tmra "Ahh~... Noooo~... I'm not a shlut..."
                                                                                                                                                                                                tmra "You and Candy... Ahhh~... You're the slutsss~..."
                                                                                                                                                                                                tmra "How long... Ahhh~... ...have you two been fucking him..."
                                                                                                                                                                                                tmra "Ahhh~... Just because you can't resist his... Ahhh~... ...huge di-"
                                                                                                                                                                                                tmra "Ahhhhh~ Huge asshole behaviour..."
                                                                                                                                                                                                tr "Play nice, Tamara..."
                                                                                                                                                                                                scene v13472 with Dissolve(1)
                                                                                                                                                                                                tr "You look really cute... Seems you already came a few times..."
                                                                                                                                                                                                play audio "audio/kiss.mp3"
                                                                                                                                                                                                scene v13473 with dissolve
                                                                                                                                                                                                tmra "Thut uppp..." (multiple=2)
                                                                                                                                                                                                tr "Ah!" (multiple=2)
                                                                                                                                                                                                scene v13474 with dissolve
                                                                                                                                                                                                tmra "Ahh~... Waihht~... What are you-"
                                                                                                                                                                                                scene v13475 with vpunch
                                                                                                                                                                                                tr "Eeep! Don't bite it!"
                                                                                                                                                                                                scene v13476 with dissolve
                                                                                                                                                                                                tr "Hannhh~... Fuhhhcckkk~..."
                                                                                                                                                                                                scene v13477 with Dissolve(1)
                                                                                                                                                                                                tmra "Hmmn~..."
                                                                                                                                                                                                z "..."
                                                                                                                                                                                                menu:
                                                                                                                                                                                                    "Push Tamara's face closer to Torr's and make them make out.":
                                                                                                                                                                                                        play sound "audio/Cloth_rustle.wav"
                                                                                                                                                                                                        scene v13478 with vpunch
                                                                                                                                                                                                        tmra "Ahh~!" (multiple=2)
                                                                                                                                                                                                        tr "?!" (multiple=2)
                                                                                                                                                                                                        play audio "audio/kiss.mp3"
                                                                                                                                                                                                        scene v13479 with hpunch
                                                                                                                                                                                                        tmra "HMNN~!" (multiple=2)
                                                                                                                                                                                                        tr "HMMM?!" (multiple=2)
                                                                                                                                                                                                        scene v13480 with Dissolve(1)
                                                                                                                                                                                                        z "Be nice to each other, you two..."
                                                                                                                                                                                                        show v13m40 with Dissolve(1)
                                                                                                                                                                                                        tmra "Hmmnn~... Mnnn~..."
                                                                                                                                                                                                        tr "Mmmmhhnnn~..."
                                                                                                                                                                                                        z "Look at you getting along... So cute..."
                                                                                                                                                                                                        tmra "Nmmmmnn~... Mhhhnn~..."
                                                                                                                                                                                                        tr "Hmmmn~... Ahhmmmm~..."
                                                                                                                                                                                                        z "Two besties putting their differences behind and joining their lips..."
                                                                                                                                                                                                        tr "Hmmmnnn~... Fuhhhmm~..."
                                                                                                                                                                                                        tmra "Ihmmmmmnn~... Fuhhhmmm~..."
                                                                                                                                                                                                        z "Tamara... I'm gonna cum..."
                                                                                                                                                                                                        z "I hope you're ready... I'm shooting it inside you..."
                                                                                                                                                                                                        tmra "Hmmnnn~?! Inmmmm~! Mhhhnnn~!"
                                                                                                                                                                                                        z "Yeah. I don't understand... I'm gonna cum..."
                                                                                                                                                                                                        tmra "Mhhhmmmmnnn~!"
                                                                                                                                                                                                        tmra "Hmmmm-"
                                                                                                                                                                                                        play audio "audio/creak.mp3"
                                                                                                                                                                                                        play sound "audio/magic 7.mp3"
                                                                                                                                                                                                        stop background_s fadeout 1.0
                                                                                                                                                                                                        stop background_s2 fadeout 1.0
                                                                                                                                                                                                        scene v13481 with hpunch
                                                                                                                                                                                                        tmra "AAAHHHHH~!" (multiple=2)
                                                                                                                                                                                                        tr "Ahh~?!" (multiple=2)
                                                                                                                                                                                                    "Keep fucking Tamara like this.":
                                                                                                                                                                                                        show v13m5 with Dissolve(1)
                                                                                                                                                                                                        tmra "Aaaannh~... Waihhtt~..."
                                                                                                                                                                                                        z "Come back here, Tamara."
                                                                                                                                                                                                        tr "That was rude, Tamara..."
                                                                                                                                                                                                        tr "Don't suck on other people's nipples without permission."
                                                                                                                                                                                                        tmra "Hahh~... It's your fault..."
                                                                                                                                                                                                        tr "Come on, apologise."
                                                                                                                                                                                                        tmra "Nooo~... Ahhh~... Fuck you..."
                                                                                                                                                                                                        tr "If you say you're sorry [mc_name] might creampie you."
                                                                                                                                                                                                        tmra "Ahhh~... C-Creampie?! Waihht~..."
                                                                                                                                                                                                        z "Wait, I never agreed to this..."
                                                                                                                                                                                                        tr "Come on, we need to put cocky Tamara in her place, [mc_name]..."
                                                                                                                                                                                                        tr "If she behaves like a good girl, would you creampie her?"
                                                                                                                                                                                                        z "I mean..."
                                                                                                                                                                                                        tr "What do you say, Tamara? Are you a good girl?"
                                                                                                                                                                                                        tmra "Ahh~... Fuhcckk~..."
                                                                                                                                                                                                        tr "Now, now. Tamara. No cursing."
                                                                                                                                                                                                        tr "Just say you're sorry. And [mc_name] will shoot all his warm load inside you."
                                                                                                                                                                                                        tmra "Hnnn~... Ahhh~... Inshide..."
                                                                                                                                                                                                        tr "Yup, yup. All of it inside you."
                                                                                                                                                                                                        tr "In return for one small sorry."
                                                                                                                                                                                                        tr "Good deal, no?"
                                                                                                                                                                                                        tmra "Ahh~... Hahhhhh~... Anhhh~..."
                                                                                                                                                                                                        tmra "I'm... Mmmmnn~... Hahhh~... I'm..."
                                                                                                                                                                                                        tmra "I'm cumming... Ahh~... Hahh~... Hanhh~..."
                                                                                                                                                                                                        z "I'm gonna cum too..."
                                                                                                                                                                                                        tr "Shoot it... Ahh~... Hannhh~... Shoot it inside..."
                                                                                                                                                                                                        if tmra_lst >= 7:
                                                                                                                                                                                                            play sound "audio/creaky door.mp3"
                                                                                                                                                                                                            "{i}Door opens.{/i}"
                                                                                                                                                                                                            tr "Fuhhcck~... What was that..."
                                                                                                                                                                                                            z "I don't know..."
                                                                                                                                                                                                            tr "Someone... Ahhh~... Someone just came in... We need to stop..."
                                                                                                                                                                                                            z "Yeah... Lemme just..."
                                                                                                                                                                                                            play sound "audio/Falling2.mp3"
                                                                                                                                                                                                            play audio "audio/magic 7.mp3"
                                                                                                                                                                                                            stop background_s
                                                                                                                                                                                                            stop background_s2
                                                                                                                                                                                                            stop music
                                                                                                                                                                                                            scene v13462 with vpunch
                                                                                                                                                                                                            z "Ughh... Fuck..." (multiple=2)
                                                                                                                                                                                                            tr "Aaaahhh~..." (multiple=2)
                                                                                                                                                                                                            play sound "audio/Cloth_rustle.wav"
                                                                                                                                                                                                            scene v13463 with Dissolve(1)
                                                                                                                                                                                                            tr "Hahhh~... Fuck... That was..."
                                                                                                                                                                                                            z "That was amazing, but we need t-"
                                                                                                                                                                                                            scene v13464 with dissolve
                                                                                                                                                                                                            tmra "Torr?!"
                                                                                                                                                                                                            scene v13465 with Dissolve(1)
                                                                                                                                                                                                            tmra "What's all that noi-"
                                                                                                                                                                                                            scene v13466 with Dissolve(1)
                                                                                                                                                                                                            z "..."
                                                                                                                                                                                                            tmra "What th-"
                                                                                                                                                                                                            tmra "..."
                                                                                                                                                                                                            with Pause(1)
                                                                                                                                                                                                            play audio "audio/camera.mp3"
                                                                                                                                                                                                            scene black
                                                                                                                                                                                                            with Pause(0.5)
                                                                                                                                                                                                            play sound "audio/Falling2.mp3"
                                                                                                                                                                                                            with vpunch
                                                                                                                                                                                                            with vpunch
                                                                                                                                                                                                            with vpunch
                                                                                                                                                                                                            with vpunch
                                                                                                                                                                                                            tmra "AAAH!"
                                                                                                                                                                                                            with Pause(0.5)
                                                                                                                                                                                                            play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
                                                                                                                                                                                                            play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                                                                                                                                                                                                            show v13m5 with Dissolve(1)
                                                                                                                                                                                                            tmra "Aaaahhh~... Ahhhhh~... Fuhcckkk~..."
                                                                                                                                                                                                            tr "How do you like that Tamara?"
                                                                                                                                                                                                            tmra "It feelshhh..."
                                                                                                                                                                                                            tr "Yes?"
                                                                                                                                                                                                            tmra "Ahh~... It's... Hahh~... Doesn't feel that good... Ahh~..."
                                                                                                                                                                                                            tr "Really? You're making a really dumb face down there..."
                                                                                                                                                                                                            tr "Almost like you're losing it from the pleasure..."
                                                                                                                                                                                                            tmra "That'th nohhht... Ahhh~..."
                                                                                                                                                                                                            tr "You can't even speak properly..."
                                                                                                                                                                                                            tr "Just admit it. You love getting piped like the little slut you are..."
                                                                                                                                                                                                            tmra "Ahh~... Noooo~... I'm not a shlut..."
                                                                                                                                                                                                            tmra "You and Candy... Ahhh~... You're the slutsss~..."
                                                                                                                                                                                                            tmra "How long... Ahhh~... ...have you two been fucking him..."
                                                                                                                                                                                                            tmra "Ahhh~... Just because you can't resist his... Ahhh~... ...huge di-"
                                                                                                                                                                                                            tmra "Ahhhhh~ Huge asshole behaviour..."
                                                                                                                                                                                                            tr "Play nice, Tamara..."
                                                                                                                                                                                                            scene v13472 with Dissolve(1)
                                                                                                                                                                                                            tr "You look really cute... Seems you already came a few times..."
                                                                                                                                                                                                            play audio "audio/kiss.mp3"
                                                                                                                                                                                                            scene v13473 with dissolve
                                                                                                                                                                                                            tmra "Thut uppp..." (multiple=2)
                                                                                                                                                                                                            tr "Ah!" (multiple=2)
                                                                                                                                                                                                            scene v13474 with dissolve
                                                                                                                                                                                                            tmra "Ahh~... Waihht~... What are you-"
                                                                                                                                                                                                            scene v13475 with vpunch
                                                                                                                                                                                                            tr "Eeep! Don't bite it!"
                                                                                                                                                                                                            scene v13476 with dissolve
                                                                                                                                                                                                            tr "Hannhh~... Fuhhhcckkk~..."
                                                                                                                                                                                                            scene v13477 with Dissolve(1)
                                                                                                                                                                                                            tmra "Hmmn~..."
                                                                                                                                                                                                            z "..."
                                                                                                                                                                                                            menu:
                                                                                                                                                                                                                "Push Tamara's face closer to Torr's and make them make out.":
                                                                                                                                                                                                                    play sound "audio/Cloth_rustle.wav"
                                                                                                                                                                                                                    scene v13478 with vpunch
                                                                                                                                                                                                                    tmra "Ahh~!" (multiple=2)
                                                                                                                                                                                                                    tr "?!" (multiple=2)
                                                                                                                                                                                                                    play audio "audio/kiss.mp3"
                                                                                                                                                                                                                    scene v13479 with hpunch
                                                                                                                                                                                                                    tmra "HMNN~!" (multiple=2)
                                                                                                                                                                                                                    tr "HMMM?!" (multiple=2)
                                                                                                                                                                                                                    scene v13480 with Dissolve(1)
                                                                                                                                                                                                                    z "Be nice to each other, you two..."
                                                                                                                                                                                                                    show v13m40 with Dissolve(1)
                                                                                                                                                                                                                    tmra "Hmmnn~... Mnnn~..."
                                                                                                                                                                                                                    tr "Mmmmhhnnn~..."
                                                                                                                                                                                                                    z "Look at you getting along... So cute..."
                                                                                                                                                                                                                    tmra "Nmmmmnn~... Mhhhnn~..."
                                                                                                                                                                                                                    tr "Hmmmn~... Ahhmmmm~..."
                                                                                                                                                                                                                    z "Two besties putting their differences behind and joining their lips..."
                                                                                                                                                                                                                    tr "Hmmmnnn~... Fuhhhmm~..."
                                                                                                                                                                                                                    tmra "Ihmmmmmnn~... Fuhhhmmm~..."
                                                                                                                                                                                                                    z "Tamara... I'm gonna cum..."
                                                                                                                                                                                                                    z "I hope you're ready... I'm shooting it inside you..."
                                                                                                                                                                                                                    tmra "Hmmnnn~?! Inmmmm~! Mhhhnnn~!"
                                                                                                                                                                                                                    z "Yeah. I don't understand... I'm gonna cum..."
                                                                                                                                                                                                                    tmra "Mhhhmmmmnnn~!"
                                                                                                                                                                                                                    tmra "Hmmmm-"
                                                                                                                                                                                                                    play audio "audio/creak.mp3"
                                                                                                                                                                                                                    play sound "audio/magic 7.mp3"
                                                                                                                                                                                                                    stop background_s fadeout 1.0
                                                                                                                                                                                                                    stop background_s2 fadeout 1.0
                                                                                                                                                                                                                    scene v13481 with hpunch
                                                                                                                                                                                                                    tmra "AAAHHHHH~!" (multiple=2)
                                                                                                                                                                                                                    tr "Ahh~?!" (multiple=2)
                                                                                                                                                                                                                "Keep fucking Tamara like this.":
                                                                                                                                                                                                                    show v13m5 with Dissolve(1)
                                                                                                                                                                                                                    tmra "Aaaannh~... Waihhtt~..."
                                                                                                                                                                                                                    z "Come back here, Tamara."
                                                                                                                                                                                                                    tr "That was rude, Tamara..."
                                                                                                                                                                                                                    tr "Don't suck on other people's nipples without permission."
                                                                                                                                                                                                                    tmra "Hahh~... It's your fault..."
                                                                                                                                                                                                                    tr "Come on, apologise."
                                                                                                                                                                                                                    tmra "Nooo~... Ahhh~... Fuck you..."
                                                                                                                                                                                                                    tr "If you say you're sorry [mc_name] might creampie you."
                                                                                                                                                                                                                    tmra "Ahhh~... C-Creampie?! Waihht~..."
                                                                                                                                                                                                                    z "Wait, I never agreed to this..."
                                                                                                                                                                                                                    tr "Come on, we need to put cocky Tamara in her place, [mc_name]..."
                                                                                                                                                                                                                    tr "If she behaves like a good girl, would you creampie her?"
                                                                                                                                                                                                                    z "I mean..."
                                                                                                                                                                                                                    tr "What do you say, Tamara? Are you a good girl?"
                                                                                                                                                                                                                    tmra "Ahh~... Fuhcckk~..."
                                                                                                                                                                                                                    tr "Now, now. Tamara. No cursing."
                                                                                                                                                                                                                    tr "Just say you're sorry. And [mc_name] will shoot all his warm load inside you."
                                                                                                                                                                                                                    tmra "Hnnn~... Ahhh~... Inshide..."
                                                                                                                                                                                                                    tr "Yup, yup. All of it inside you."
                                                                                                                                                                                                                    tr "In return for one small sorry."
                                                                                                                                                                                                                    tr "Good deal, no?"
                                                                                                                                                                                                                    tmra "Ahh~... Hahhhhh~... Anhhh~..."
                                                                                                                                                                                                                    tmra "I'm... Mmmmnn~... Hahhh~... I'm..."
                                                                                                                                                                                                                    tmra "I'm cumming... Ahh~... Hahh~... Hanhh~..."
                                                                                                                                                                                                                    z "I'm gonna cum too..."
                                                                                                                                                                                                                    tr "Shoot it... Ahh~... Hannhh~... Shoot it inside..."
                                                                                                                                                                                                                    if tmra_lst >= 7:
                                                                                                                                                                                                                        play sound "audio/creaky door.mp3"
                                                                                                                                                                                                                        "{i}Door opens.{/i}"
                                                                                                                                                                                                                        tr "Fuhhcck~... What was that..."
                                                                                                                                                                                                                        z "I don't know..."
                                                                                                                                                                                                                        tr "Someone... Ahhh~... Someone just came in... We need to stop..."
                                                                                                                                                                                                                        z "Yeah... Lemme just..."
                                                                                                                                                                                                                        play sound "audio/Falling2.mp3"
                                                                                                                                                                                                                        play audio "audio/magic 7.mp3"
                                                                                                                                                                                                                        stop background_s
                                                                                                                                                                                                                        stop background_s2
                                                                                                                                                                                                                        stop music
                                                                                                                                                                                                                        scene v13462 with vpunch
                                                                                                                                                                                                                        z "Ughh... Fuck..." (multiple=2)
                                                                                                                                                                                                                        tr "Aaaahhh~..." (multiple=2)
                                                                                                                                                                                                                        play sound "audio/Cloth_rustle.wav"
                                                                                                                                                                                                                        scene v13463 with Dissolve(1)
                                                                                                                                                                                                                        tr "Hahhh~... Fuck... That was..."
                                                                                                                                                                                                                        z "That was amazing, but we need t-"
                                                                                                                                                                                                                        scene v13464 with dissolve
                                                                                                                                                                                                                        tmra "Torr?!"
                                                                                                                                                                                                                        scene v13465 with Dissolve(1)
                                                                                                                                                                                                                        tmra "What's all that noi-"
                                                                                                                                                                                                                        scene v13466 with Dissolve(1)
                                                                                                                                                                                                                        z "..."
                                                                                                                                                                                                                        tmra "What th-"
                                                                                                                                                                                                                        tmra "..."
                                                                                                                                                                                                                        with Pause(1)
                                                                                                                                                                                                                        play audio "audio/camera.mp3"
                                                                                                                                                                                                                        scene black
                                                                                                                                                                                                                        with Pause(0.5)
                                                                                                                                                                                                                        play sound "audio/Falling2.mp3"
                                                                                                                                                                                                                        with vpunch
                                                                                                                                                                                                                        with vpunch
                                                                                                                                                                                                                        with vpunch
                                                                                                                                                                                                                        with vpunch
                                                                                                                                                                                                                        tmra "AAAH!"
                                                                                                                                                                                                                        with Pause(0.5)
                                                                                                                                                                                                                        play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
                                                                                                                                                                                                                        play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                                                                                                                                                                                                                        show v13m5 with Dissolve(1)
                                                                                                                                                                                                                        tmra "Aaaahhh~... Ahhhhh~... Fuhcckkk~..."
                                                                                                                                                                                                                        tr "How do you like that Tamara?"
                                                                                                                                                                                                                        tmra "It feelshhh..."
                                                                                                                                                                                                                        tr "Yes?"
                                                                                                                                                                                                                        tmra "Ahh~... It's... Hahh~... Doesn't feel that good... Ahh~..."
                                                                                                                                                                                                                        tr "Really? You're making a really dumb face down there..."
                                                                                                                                                                                                                        tr "Almost like you're losing it from the pleasure..."
                                                                                                                                                                                                                        tmra "That'th nohhht... Ahhh~..."
                                                                                                                                                                                                                        tr "You can't even speak properly..."
                                                                                                                                                                                                                        tr "Just admit it. You love getting piped like the little slut you are..."
                                                                                                                                                                                                                        tmra "Ahh~... Noooo~... I'm not a shlut..."
                                                                                                                                                                                                                        tmra "You and Candy... Ahhh~... You're the slutsss~..."
                                                                                                                                                                                                                        tmra "How long... Ahhh~... ...have you two been fucking him..."
                                                                                                                                                                                                                        tmra "Ahhh~... Just because you can't resist his... Ahhh~... ...huge di-"
                                                                                                                                                                                                                        tmra "Ahhhhh~ Huge asshole behaviour..."
                                                                                                                                                                                                                        tr "Play nice, Tamara..."
                                                                                                                                                                                                                        scene v13472 with Dissolve(1)
                                                                                                                                                                                                                        tr "You look really cute... Seems you already came a few times..."
                                                                                                                                                                                                                        play audio "audio/kiss.mp3"
                                                                                                                                                                                                                        scene v13473 with dissolve
                                                                                                                                                                                                                        tmra "Thut uppp..." (multiple=2)
                                                                                                                                                                                                                        tr "Ah!" (multiple=2)
                                                                                                                                                                                                                        scene v13474 with dissolve
                                                                                                                                                                                                                        tmra "Ahh~... Waihht~... What are you-"
                                                                                                                                                                                                                        scene v13475 with vpunch
                                                                                                                                                                                                                        tr "Eeep! Don't bite it!"
                                                                                                                                                                                                                        scene v13476 with dissolve
                                                                                                                                                                                                                        tr "Hannhh~... Fuhhhcckkk~..."
                                                                                                                                                                                                                        scene v13477 with Dissolve(1)
                                                                                                                                                                                                                        tmra "Hmmn~..."
                                                                                                                                                                                                                        z "..."
                                                                                                                                                                                                                        menu:
                                                                                                                                                                                                                            "Push Tamara's face closer to Torr's and make them make out.":
                                                                                                                                                                                                                                play sound "audio/Cloth_rustle.wav"
                                                                                                                                                                                                                                scene v13478 with vpunch
                                                                                                                                                                                                                                tmra "Ahh~!" (multiple=2)
                                                                                                                                                                                                                                tr "?!" (multiple=2)
                                                                                                                                                                                                                                play audio "audio/kiss.mp3"
                                                                                                                                                                                                                                scene v13479 with hpunch
                                                                                                                                                                                                                                tmra "HMNN~!" (multiple=2)
                                                                                                                                                                                                                                tr "HMMM?!" (multiple=2)
                                                                                                                                                                                                                                scene v13480 with Dissolve(1)
                                                                                                                                                                                                                                z "Be nice to each other, you two..."
                                                                                                                                                                                                                                show v13m40 with Dissolve(1)
                                                                                                                                                                                                                                tmra "Hmmnn~... Mnnn~..."
                                                                                                                                                                                                                                tr "Mmmmhhnnn~..."
                                                                                                                                                                                                                                z "Look at you getting along... So cute..."
                                                                                                                                                                                                                                tmra "Nmmmmnn~... Mhhhnn~..."
                                                                                                                                                                                                                                tr "Hmmmn~... Ahhmmmm~..."
                                                                                                                                                                                                                                z "Two besties putting their differences behind and joining their lips..."
                                                                                                                                                                                                                                tr "Hmmmnnn~... Fuhhhmm~..."
                                                                                                                                                                                                                                tmra "Ihmmmmmnn~... Fuhhhmmm~..."
                                                                                                                                                                                                                                z "Tamara... I'm gonna cum..."
                                                                                                                                                                                                                                z "I hope you're ready... I'm shooting it inside you..."
                                                                                                                                                                                                                                tmra "Hmmnnn~?! Inmmmm~! Mhhhnnn~!"
                                                                                                                                                                                                                                z "Yeah. I don't understand... I'm gonna cum..."
                                                                                                                                                                                                                                tmra "Mhhhmmmmnnn~!"
                                                                                                                                                                                                                                tmra "Hmmmm-"
                                                                                                                                                                                                                                play audio "audio/creak.mp3"
                                                                                                                                                                                                                                play sound "audio/magic 7.mp3"
                                                                                                                                                                                                                                stop background_s fadeout 1.0
                                                                                                                                                                                                                                stop background_s2 fadeout 1.0
                                                                                                                                                                                                                                scene v13481 with hpunch
                                                                                                                                                                                                                                tmra "AAAHHHHH~!" (multiple=2)
                                                                                                                                                                                                                                tr "Ahh~?!" (multiple=2)
                                                                                                                                                                                                                            "Keep fucking Tamara like this.":
                                                                                                                                                                                                                                show v13m5 with Dissolve(1)
                                                                                                                                                                                                                                tmra "Aaaannh~... Waihhtt~..."
                                                                                                                                                                                                                                z "Come back here, Tamara."
                                                                                                                                                                                                                                tr "That was rude, Tamara..."
                                                                                                                                                                                                                                tr "Don't suck on other people's nipples without permission."
                                                                                                                                                                                                                                tmra "Hahh~... It's your fault..."
                                                                                                                                                                                                                                tr "Come on, apologise."
                                                                                                                                                                                                                                tmra "Nooo~... Ahhh~... Fuck you..."
                                                                                                                                                                                                                                tr "If you say you're sorry [mc_name] might creampie you."
                                                                                                                                                                                                                                tmra "Ahhh~... C-Creampie?! Waihht~..."
                                                                                                                                                                                                                                z "Wait, I never agreed to this..."
                                                                                                                                                                                                                                tr "Come on, we need to put cocky Tamara in her place, [mc_name]..."
                                                                                                                                                                                                                                tr "If she behaves like a good girl, would you creampie her?"
                                                                                                                                                                                                                                z "I mean..."
                                                                                                                                                                                                                                tr "What do you say, Tamara? Are you a good girl?"
                                                                                                                                                                                                                                tmra "Ahh~... Fuhcckk~..."
                                                                                                                                                                                                                                tr "Now, now. Tamara. No cursing."
                                                                                                                                                                                                                                tr "Just say you're sorry. And [mc_name] will shoot all his warm load inside you."
                                                                                                                                                                                                                                tmra "Hnnn~... Ahhh~... Inshide..."
                                                                                                                                                                                                                                tr "Yup, yup. All of it inside you."
                                                                                                                                                                                                                                tr "In return for one small sorry."
                                                                                                                                                                                                                                tr "Good deal, no?"
                                                                                                                                                                                                                                tmra "Ahh~... Hahhhhh~... Anhhh~..."
                                                                                                                                                                                                                                tmra "I'm... Mmmmnn~... Hahhh~... I'm..."
                                                                                                                                                                                                                                tmra "I'm cumming... Ahh~... Hahh~... Hanhh~..."
                                                                                                                                                                                                                                z "I'm gonna cum too..."
                                                                                                                                                                                                                                tr "Shoot it... Ahh~... Hannhh~... Shoot it inside..."
                                                                                                                                                                                                                                if tmra_lst >= 7:
                                                                                                                                                                                                                                    play sound "audio/creaky door.mp3"
                                                                                                                                                                                                                                    "{i}Door opens.{/i}"
                                                                                                                                                                                                                                    tr "Fuhhcck~... What was that..."
                                                                                                                                                                                                                                    z "I don't know..."
                                                                                                                                                                                                                                    tr "Someone... Ahhh~... Someone just came in... We need to stop..."
                                                                                                                                                                                                                                    z "Yeah... Lemme just..."
                                                                                                                                                                                                                                    play sound "audio/Falling2.mp3"
                                                                                                                                                                                                                                    play audio "audio/magic 7.mp3"
                                                                                                                                                                                                                                    stop background_s
                                                                                                                                                                                                                                    stop background_s2
                                                                                                                                                                                                                                    stop music
                                                                                                                                                                                                                                    scene v13462 with vpunch
                                                                                                                                                                                                                                    z "Ughh... Fuck..." (multiple=2)
                                                                                                                                                                                                                                    tr "Aaaahhh~..." (multiple=2)
                                                                                                                                                                                                                                    play sound "audio/Cloth_rustle.wav"
                                                                                                                                                                                                                                    scene v13463 with Dissolve(1)
                                                                                                                                                                                                                                    tr "Hahhh~... Fuck... That was..."
                                                                                                                                                                                                                                    z "That was amazing, but we need t-"
                                                                                                                                                                                                                                    scene v13464 with dissolve
                                                                                                                                                                                                                                    tmra "Torr?!"
                                                                                                                                                                                                                                    scene v13465 with Dissolve(1)
                                                                                                                                                                                                                                    tmra "What's all that noi-"
                                                                                                                                                                                                                                    scene v13466 with Dissolve(1)
                                                                                                                                                                                                                                    z "..."
                                                                                                                                                                                                                                    tmra "What th-"
                                                                                                                                                                                                                                    tmra "..."
                                                                                                                                                                                                                                    with Pause(1)
                                                                                                                                                                                                                                    play audio "audio/camera.mp3"
                                                                                                                                                                                                                                    scene black
                                                                                                                                                                                                                                    with Pause(0.5)
                                                                                                                                                                                                                                    play sound "audio/Falling2.mp3"
                                                                                                                                                                                                                                    with vpunch
                                                                                                                                                                                                                                    with vpunch
                                                                                                                                                                                                                                    with vpunch
                                                                                                                                                                                                                                    with vpunch
                                                                                                                                                                                                                                    tmra "AAAH!"
                                                                                                                                                                                                                                    with Pause(0.5)
                                                                                                                                                                                                                                    play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
                                                                                                                                                                                                                                    play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                                                                                                                                                                                                                                    show v13m5 with Dissolve(1)
                                                                                                                                                                                                                                    tmra "Aaaahhh~... Ahhhhh~... Fuhcckkk~..."
                                                                                                                                                                                                                                    tr "How do you like that Tamara?"
                                                                                                                                                                                                                                    tmra "It feelshhh..."
                                                                                                                                                                                                                                    tr "Yes?"
                                                                                                                                                                                                                                    tmra "Ahh~... It's... Hahh~... Doesn't feel that good... Ahh~..."
                                                                                                                                                                                                                                    tr "Really? You're making a really dumb face down there..."
                                                                                                                                                                                                                                    tr "Almost like you're losing it from the pleasure..."
                                                                                                                                                                                                                                    tmra "That'th nohhht... Ahhh~..."
                                                                                                                                                                                                                                    tr "You can't even speak properly..."
                                                                                                                                                                                                                                    tr "Just admit it. You love getting piped like the little slut you are..."
                                                                                                                                                                                                                                    tmra "Ahh~... Noooo~... I'm not a shlut..."
                                                                                                                                                                                                                                    tmra "You and Candy... Ahhh~... You're the slutsss~..."
                                                                                                                                                                                                                                    tmra "How long... Ahhh~... ...have you two been fucking him..."
                                                                                                                                                                                                                                    tmra "Ahhh~... Just because you can't resist his... Ahhh~... ...huge di-"
                                                                                                                                                                                                                                    tmra "Ahhhhh~ Huge asshole behaviour..."
                                                                                                                                                                                                                                    tr "Play nice, Tamara..."
                                                                                                                                                                                                                                    scene v13472 with Dissolve(1)
                                                                                                                                                                                                                                    tr "You look really cute... Seems you already came a few times..."
                                                                                                                                                                                                                                    play audio "audio/kiss.mp3"
                                                                                                                                                                                                                                    scene v13473 with dissolve
                                                                                                                                                                                                                                    tmra "Thut uppp..." (multiple=2)
                                                                                                                                                                                                                                    tr "Ah!" (multiple=2)
                                                                                                                                                                                                                                    scene v13474 with dissolve
                                                                                                                                                                                                                                    tmra "Ahh~... Waihht~... What are you-"
                                                                                                                                                                                                                                    scene v13475 with vpunch
                                                                                                                                                                                                                                    tr "Eeep! Don't bite it!"
                                                                                                                                                                                                                                    scene v13476 with dissolve
                                                                                                                                                                                                                                    tr "Hannhh~... Fuhhhcckkk~..."
                                                                                                                                                                                                                                    scene v13477 with Dissolve(1)
                                                                                                                                                                                                                                    tmra "Hmmn~..."
                                                                                                                                                                                                                                    z "..."
                                                                                                                                                                                                                                    menu:
                                                                                                                                                                                                                                        "Push Tamara's face closer to Torr's and make them make out.":
                                                                                                                                                                                                                                            play sound "audio/Cloth_rustle.wav"
                                                                                                                                                                                                                                            scene v13478 with vpunch
                                                                                                                                                                                                                                            tmra "Ahh~!" (multiple=2)
                                                                                                                                                                                                                                            tr "?!" (multiple=2)
                                                                                                                                                                                                                                            play audio "audio/kiss.mp3"
                                                                                                                                                                                                                                            scene v13479 with hpunch
                                                                                                                                                                                                                                            tmra "HMNN~!" (multiple=2)
                                                                                                                                                                                                                                            tr "HMMM?!" (multiple=2)
                                                                                                                                                                                                                                            scene v13480 with Dissolve(1)
                                                                                                                                                                                                                                            z "Be nice to each other, you two..."
                                                                                                                                                                                                                                            show v13m40 with Dissolve(1)
                                                                                                                                                                                                                                            tmra "Hmmnn~... Mnnn~..."
                                                                                                                                                                                                                                            tr "Mmmmhhnnn~..."
                                                                                                                                                                                                                                            z "Look at you getting along... So cute..."
                                                                                                                                                                                                                                            tmra "Nmmmmnn~... Mhhhnn~..."
                                                                                                                                                                                                                                            tr "Hmmmn~... Ahhmmmm~..."
                                                                                                                                                                                                                                            z "Two besties putting their differences behind and joining their lips..."
                                                                                                                                                                                                                                            tr "Hmmmnnn~... Fuhhhmm~..."
                                                                                                                                                                                                                                            tmra "Ihmmmmmnn~... Fuhhhmmm~..."
                                                                                                                                                                                                                                            z "Tamara... I'm gonna cum..."
                                                                                                                                                                                                                                            z "I hope you're ready... I'm shooting it inside you..."
                                                                                                                                                                                                                                            tmra "Hmmnnn~?! Inmmmm~! Mhhhnnn~!"
                                                                                                                                                                                                                                            z "Yeah. I don't understand... I'm gonna cum..."
                                                                                                                                                                                                                                            tmra "Mhhhmmmmnnn~!"
                                                                                                                                                                                                                                            tmra "Hmmmm-"
                                                                                                                                                                                                                                            play audio "audio/creak.mp3"
                                                                                                                                                                                                                                            play sound "audio/magic 7.mp3"
                                                                                                                                                                                                                                            stop background_s fadeout 1.0
                                                                                                                                                                                                                                            stop background_s2 fadeout 1.0
                                                                                                                                                                                                                                            scene v13481 with hpunch
                                                                                                                                                                                                                                            tmra "AAAHHHHH~!" (multiple=2)
                                                                                                                                                                                                                                            tr "Ahh~?!" (multiple=2)
                                                                                                                                                                                                                                        "Keep fucking Tamara like this.":
                                                                                                                                                                                                                                            show v13m5 with Dissolve(1)
                                                                                                                                                                                                                                            tmra "Aaaannh~... Waihhtt~..."
                                                                                                                                                                                                                                            z "Come back here, Tamara."
                                                                                                                                                                                                                                            tr "That was rude, Tamara..."
                                                                                                                                                                                                                                            tr "Don't suck on other people's nipples without permission."
                                                                                                                                                                                                                                            tmra "Hahh~... It's your fault..."
                                                                                                                                                                                                                                            tr "Come on, apologise."
                                                                                                                                                                                                                                            tmra "Nooo~... Ahhh~... Fuck you..."
                                                                                                                                                                                                                                            tr "If you say you're sorry [mc_name] might creampie you."
                                                                                                                                                                                                                                            tmra "Ahhh~... C-Creampie?! Waihht~..."
                                                                                                                                                                                                                                            z "Wait, I never agreed to this..."
                                                                                                                                                                                                                                            tr "Come on, we need to put cocky Tamara in her place, [mc_name]..."
                                                                                                                                                                                                                                            tr "If she behaves like a good girl, would you creampie her?"
                                                                                                                                                                                                                                            z "I mean..."
                                                                                                                                                                                                                                            tr "What do you say, Tamara? Are you a good girl?"
                                                                                                                                                                                                                                            tmra "Ahh~... Fuhcckk~..."
                                                                                                                                                                                                                                            tr "Now, now. Tamara. No cursing."
                                                                                                                                                                                                                                            tr "Just say you're sorry. And [mc_name] will shoot all his warm load inside you."
                                                                                                                                                                                                                                            tmra "Hnnn~... Ahhh~... Inshide..."
                                                                                                                                                                                                                                            tr "Yup, yup. All of it inside you."
                                                                                                                                                                                                                                            tr "In return for one small sorry."
                                                                                                                                                                                                                                            tr "Good deal, no?"
                                                                                                                                                                                                                                            tmra "Ahh~... Hahhhhh~... Anhhh~..."
                                                                                                                                                                                                                                            tmra "I'm... Mmmmnn~... Hahhh~... I'm..."
                                                                                                                                                                                                                                            tmra "I'm cumming... Ahh~... Hahh~... Hanhh~..."
                                                                                                                                                                                                                                            z "I'm gonna cum too..."
                                                                                                                                                                                                                                            tr "Shoot it... Ahh~... Hannhh~... Shoot it inside..."
                                                                                                                                                                                                                                            if tmra_lst >= 7:
                                                                                                                                                                                                                                                play sound "audio/creaky door.mp3"
                                                                                                                                                                                                                                                "{i}Door opens.{/i}"
                                                                                                                                                                                                                                                tr "Fuhhcck~... What was that..."
                                                                                                                                                                                                                                                z "I don't know..."
                                                                                                                                                                                                                                                tr "Someone... Ahhh~... Someone just came in... We need to stop..."
                                                                                                                                                                                                                                                z "Yeah... Lemme just..."
                                                                                                                                                                                                                                                play sound "audio/Falling2.mp3"
                                                                                                                                                                                                                                                play audio "audio/magic 7.mp3"
                                                                                                                                                                                                                                                stop background_s
                                                                                                                                                                                                                                                stop background_s2
                                                                                                                                                                                                                                                stop music
                                                                                                                                                                                                                                                scene v13462 with vpunch
                                                                                                                                                                                                                                                z "Ughh... Fuck..." (multiple=2)
                                                                                                                                                                                                                                                tr "Aaaahhh~..." (multiple=2)
                                                                                                                                                                                                                                                play sound "audio/Cloth_rustle.wav"
                                                                                                                                                                                                                                                scene v13463 with Dissolve(1)
                                                                                                                                                                                                                                                tr "Hahhh~... Fuck... That was..."
                                                                                                                                                                                                                                                z "That was amazing, but we need t-"
                                                                                                                                                                                                                                                scene v13464 with dissolve
                                                                                                                                                                                                                                                tmra "Torr?!"
                                                                                                                                                                                                                                                scene v13465 with Dissolve(1)
                                                                                                                                                                                                                                                tmra "What's all that noi-"
                                                                                                                                                                                                                                                scene v13466 with Dissolve(1)
                                                                                                                                                                                                                                                z "..."
                                                                                                                                                                                                                                                tmra "What th-"
                                                                                                                                                                                                                                                tmra "..."
                                                                                                                                                                                                                                                with Pause(1)
                                                                                                                                                                                                                                                play audio "audio/camera.mp3"
                                                                                                                                                                                                                                                scene black
                                                                                                                                                                                                                                                with Pause(0.5)
                                                                                                                                                                                                                                                play sound "audio/Falling2.mp3"
                                                                                                                                                                                                                                                with vpunch
                                                                                                                                                                                                                                                with vpunch
                                                                                                                                                                                                                                                with vpunch
                                                                                                                                                                                                                                                with vpunch
                                                                                                                                                                                                                                                tmra "AAAH!"
                                                                                                                                                                                                                                                with Pause(0.5)
                                                                                                                                                                                                                                                play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
                                                                                                                                                                                                                                                play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                                                                                                                                                                                                                                                show v13m5 with Dissolve(1)
                                                                                                                                                                                                                                                tmra "Aaaahhh~... Ahhhhh~... Fuhcckkk~..."
                                                                                                                                                                                                                                                tr "How do you like that Tamara?"
                                                                                                                                                                                                                                                tmra "It feelshhh..."
                                                                                                                                                                                                                                                tr "Yes?"
                                                                                                                                                                                                                                                tmra "Ahh~... It's... Hahh~... Doesn't feel that good... Ahh~..."
                                                                                                                                                                                                                                                tr "Really? You're making a really dumb face down there..."
                                                                                                                                                                                                                                                tr "Almost like you're losing it from the pleasure..."
                                                                                                                                                                                                                                                tmra "That'th nohhht... Ahhh~..."
                                                                                                                                                                                                                                                tr "You can't even speak properly..."
                                                                                                                                                                                                                                                tr "Just admit it. You love getting piped like the little slut you are..."
                                                                                                                                                                                                                                                tmra "Ahh~... Noooo~... I'm not a shlut..."
                                                                                                                                                                                                                                                tmra "You and Candy... Ahhh~... You're the slutsss~..."
                                                                                                                                                                                                                                                tmra "How long... Ahhh~... ...have you two been fucking him..."
                                                                                                                                                                                                                                                tmra "Ahhh~... Just because you can't resist his... Ahhh~... ...huge di-"
                                                                                                                                                                                                                                                tmra "Ahhhhh~ Huge asshole behaviour..."
                                                                                                                                                                                                                                                tr "Play nice, Tamara..."
                                                                                                                                                                                                                                                scene v13472 with Dissolve(1)
                                                                                                                                                                                                                                                tr "You look really cute... Seems you already came a few times..."
                                                                                                                                                                                                                                                play audio "audio/kiss.mp3"
                                                                                                                                                                                                                                                scene v13473 with dissolve
                                                                                                                                                                                                                                                tmra "Thut uppp..." (multiple=2)
                                                                                                                                                                                                                                                tr "Ah!" (multiple=2)
                                                                                                                                                                                                                                                scene v13474 with dissolve
                                                                                                                                                                                                                                                tmra "Ahh~... Waihht~... What are you-"
                                                                                                                                                                                                                                                scene v13475 with vpunch
                                                                                                                                                                                                                                                tr "Eeep! Don't bite it!"
                                                                                                                                                                                                                                                scene v13476 with dissolve
                                                                                                                                                                                                                                                tr "Hannhh~... Fuhhhcckkk~..."
                                                                                                                                                                                                                                                scene v13477 with Dissolve(1)
                                                                                                                                                                                                                                                tmra "Hmmn~..."
                                                                                                                                                                                                                                                z "..."
                                                                                                                                                                                                                                                menu:
                                                                                                                                                                                                                                                    "Push Tamara's face closer to Torr's and make them make out.":
                                                                                                                                                                                                                                                        play sound "audio/Cloth_rustle.wav"
                                                                                                                                                                                                                                                        scene v13478 with vpunch
                                                                                                                                                                                                                                                        tmra "Ahh~!" (multiple=2)
                                                                                                                                                                                                                                                        tr "?!" (multiple=2)
                                                                                                                                                                                                                                                        play audio "audio/kiss.mp3"
                                                                                                                                                                                                                                                        scene v13479 with hpunch
                                                                                                                                                                                                                                                        tmra "HMNN~!" (multiple=2)
                                                                                                                                                                                                                                                        tr "HMMM?!" (multiple=2)
                                                                                                                                                                                                                                                        scene v13480 with Dissolve(1)
                                                                                                                                                                                                                                                        z "Be nice to each other, you two..."
                                                                                                                                                                                                                                                        show v13m40 with Dissolve(1)
                                                                                                                                                                                                                                                        tmra "Hmmnn~... Mnnn~..."
                                                                                                                                                                                                                                                        tr "Mmmmhhnnn~..."
                                                                                                                                                                                                                                                        z "Look at you getting along... So cute..."
                                                                                                                                                                                                                                                        tmra "Nmmmmnn~... Mhhhnn~..."
                                                                                                                                                                                                                                                        tr "Hmmmn~... Ahhmmmm~..."
                                                                                                                                                                                                                                                        z "Two besties putting their differences behind and joining their lips..."
                                                                                                                                                                                                                                                        tr "Hmmmnnn~... Fuhhhmm~..."
                                                                                                                                                                                                                                                        tmra "Ihmmmmmnn~... Fuhhhmmm~..."
                                                                                                                                                                                                                                                        z "Tamara... I'm gonna cum..."
                                                                                                                                                                                                                                                        z "I hope you're ready... I'm shooting it inside you..."
                                                                                                                                                                                                                                                        tmra "Hmmnnn~?! Inmmmm~! Mhhhnnn~!"
                                                                                                                                                                                                                                                        z "Yeah. I don't understand... I'm gonna cum..."
                                                                                                                                                                                                                                                        tmra "Mhhhmmmmnnn~!"
                                                                                                                                                                                                                                                        tmra "Hmmmm-"
                                                                                                                                                                                                                                                        play audio "audio/creak.mp3"
                                                                                                                                                                                                                                                        play sound "audio/magic 7.mp3"
                                                                                                                                                                                                                                                        stop background_s fadeout 1.0
                                                                                                                                                                                                                                                        stop background_s2 fadeout 1.0
                                                                                                                                                                                                                                                        scene v13481 with hpunch
                                                                                                                                                                                                                                                        tmra "AAAHHHHH~!" (multiple=2)
                                                                                                                                                                                                                                                        tr "Ahh~?!" (multiple=2)
                                                                                                                                                                                                                                                    "Keep fucking Tamara like this.":
                                                                                                                                                                                                                                                        show v13m5 with Dissolve(1)
                                                                                                                                                                                                                                                        tmra "Aaaannh~... Waihhtt~..."
                                                                                                                                                                                                                                                        z "Come back here, Tamara."
                                                                                                                                                                                                                                                        tr "That was rude, Tamara..."
                                                                                                                                                                                                                                                        tr "Don't suck on other people's nipples without permission."
                                                                                                                                                                                                                                                        tmra "Hahh~... It's your fault..."
                                                                                                                                                                                                                                                        tr "Come on, apologise."
                                                                                                                                                                                                                                                        tmra "Nooo~... Ahhh~... Fuck you..."
                                                                                                                                                                                                                                                        tr "If you say you're sorry [mc_name] might creampie you."
                                                                                                                                                                                                                                                        tmra "Ahhh~... C-Creampie?! Waihht~..."
                                                                                                                                                                                                                                                        z "Wait, I never agreed to this..."
                                                                                                                                                                                                                                                        tr "Come on, we need to put cocky Tamara in her place, [mc_name]..."
                                                                                                                                                                                                                                                        tr "If she behaves like a good girl, would you creampie her?"
                                                                                                                                                                                                                                                        z "I mean..."
                                                                                                                                                                                                                                                        tr "What do you say, Tamara? Are you a good girl?"
                                                                                                                                                                                                                                                        tmra "Ahh~... Fuhcckk~..."
                                                                                                                                                                                                                                                        tr "Now, now. Tamara. No cursing."
                                                                                                                                                                                                                                                        tr "Just say you're sorry. And [mc_name] will shoot all his warm load inside you."
                                                                                                                                                                                                                                                        tmra "Hnnn~... Ahhh~... Inshide..."
                                                                                                                                                                                                                                                        tr "Yup, yup. All of it inside you."
                                                                                                                                                                                                                                                        tr "In return for one small sorry."
                                                                                                                                                                                                                                                        tr "Good deal, no?"
                                                                                                                                                                                                                                                        tmra "Ahh~... Hahhhhh~... Anhhh~..."
                                                                                                                                                                                                                                                        tmra "I'm... Mmmmnn~... Hahhh~... I'm..."
                                                                                                                                                                                                                                                        tmra "I'm cumming... Ahh~... Hahh~... Hanhh~..."
                                                                                                                                                                                                                                                        z "I'm gonna cum too..."
                                                                                                                                                                                                                                                        tr "Shoot it... Ahh~... Hannhh~... Shoot it inside..."
                                                                                                                                                                                                                                                        if tmra_lst >= 7:
                                                                                                                                                                                                                                                            play sound "audio/creaky door.mp3"
                                                                                                                                                                                                                                                            "{i}Door opens.{/i}"
                                                                                                                                                                                                                                                            tr "Fuhhcck~... What was that..."
                                                                                                                                                                                                                                                            z "I don't know..."
                                                                                                                                                                                                                                                            tr "Someone... Ahhh~... Someone just came in... We need to stop..."
                                                                                                                                                                                                                                                            z "Yeah... Lemme just..."
                                                                                                                                                                                                                                                            play sound "audio/Falling2.mp3"
                                                                                                                                                                                                                                                            play audio "audio/magic 7.mp3"
                                                                                                                                                                                                                                                            stop background_s
                                                                                                                                                                                                                                                            stop background_s2
                                                                                                                                                                                                                                                            stop music
                                                                                                                                                                                                                                                            scene v13462 with vpunch
                                                                                                                                                                                                                                                            z "Ughh... Fuck..." (multiple=2)
                                                                                                                                                                                                                                                            tr "Aaaahhh~..." (multiple=2)
                                                                                                                                                                                                                                                            play sound "audio/Cloth_rustle.wav"
                                                                                                                                                                                                                                                            scene v13463 with Dissolve(1)
                                                                                                                                                                                                                                                            tr "Hahhh~... Fuck... That was..."
                                                                                                                                                                                                                                                            z "That was amazing, but we need t-"
                                                                                                                                                                                                                                                            scene v13464 with dissolve
                                                                                                                                                                                                                                                            tmra "Torr?!"
                                                                                                                                                                                                                                                            scene v13465 with Dissolve(1)
                                                                                                                                                                                                                                                            tmra "What's all that noi-"
                                                                                                                                                                                                                                                            scene v13466 with Dissolve(1)
                                                                                                                                                                                                                                                            z "..."
                                                                                                                                                                                                                                                            tmra "What th-"
                                                                                                                                                                                                                                                            tmra "..."
                                                                                                                                                                                                                                                            with Pause(1)
                                                                                                                                                                                                                                                            play audio "audio/camera.mp3"
                                                                                                                                                                                                                                                            scene black
                                                                                                                                                                                                                                                            with Pause(0.5)
                                                                                                                                                                                                                                                            play sound "audio/Falling2.mp3"
                                                                                                                                                                                                                                                            with vpunch
                                                                                                                                                                                                                                                            with vpunch
                                                                                                                                                                                                                                                            with vpunch
                                                                                                                                                                                                                                                            with vpunch
                                                                                                                                                                                                                                                            tmra "AAAH!"
                                                                                                                                                                                                                                                            with Pause(0.5)
                                                                                                                                                                                                                                                            play music "audio/ZxMistyCh11.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
                                                                                                                                                                                                                                                            play background_s "audio/lewd (stolen from Atem)/Sex medium.ogg" volume 0.6 fadeout 1.0 fadein 1.0 loop
                                                                                                                                                                                                                                                            show v13m5 with Dissolve(1)
                                                                                                                                                                                                                                                            tmra "Aaaahhh~... Ahhhhh~... Fuhcckkk~..."
                                                                                                                                                                                                                                                            tr "How do you like that Tamara?"
                                                                                                                                                                                                                                                            tmra "It feelshhh..."
                                                                                                                                                                                                                                                            tr "Yes?"
                                                                                                                                                                                                                                                            tmra "Ahh~... It's... Hahh~... Doesn't feel that good... Ahh~..."
                                                                                                                                                                                                                                                            tr "Really? You're making a really dumb face down there..."
                                                                                                                                                                                                                                                            tr "Almost like you're losing it from the pleasure..."
                                                                                                                                                                                                                                                            tmra "That'th nohhht... Ahhh~..."
                                                                                                                                                                                                                                                            tr "You can't even speak properly..."
                                                                                                                                                                                                                                                            tr "Just admit it. You love getting piped like the little slut you are..."
                                                                                                                                                                                                                                                            tmra "Ahh~... Noooo~... I'm not a shlut..."
                                                                                                                                                                                                                                                            tmra "You and Candy... Ahhh~... You're the slutsss~..."
                                                                                                                                                                                                                                                            tmra "How long... Ahhh~... ...have you two been fucking him..."
                                                                                                                                                                                                                                                            tmra "Ahhh~... Just because you can't resist his... Ahhh~... ...huge di-"
                                                                                                                                                                                                                                                            tmra "Ahhhhh~ Huge asshole behaviour..."
                                                                                                                                                                                                                                                            tr "Play nice, Tamara..."
                                                                                                                                                                                                                                                            scene v13472 with Dissolve(1)
                                                                                                                                                                                                                                                            tr "You look really cute... Seems you already came a few times..."
                                                                                                                                                                                                                                                            play audio "audio/kiss.mp3"
                                                                                                                                                                                                                                                            scene v13473 with dissolve
                                                                                                                                                                                                                                                            tmra "Thut uppp..." (multiple=2)
                                                                                                                                                                                                                                                            tr "Ah!" (multiple=2)
                                                                                                                                                                                                                                                            scene v13474 with dissolve
                                                                                                                                                                                                                                                            tmra "Ahh~... Waihht~... What are you-"
                                                                                                                                                                                                                                                            scene v13475 with vpunch
                                                                                                                                                                                                                                                            tr "Eeep! Don't bite it!"
                                                                                                                                                                                                                                                            scene v13476 with dissolve
                                                                                                                                                                                                                                                            tr "Hannhh~... Fuhhhcckkk~..."
                                                                                                                                                                                                                                                            scene v13477 with Dissolve(1)
                                                                                                                                                                                                                                                            tmra "Hmmn~..."
                                                                                                                                                                                                                                                            z "..."
                                                                                                                                                                                                                                                            menu:
                                                                                                                                                                                                                                                                "Push Tamara's face closer to Torr's and make them make out.":
                                                                                                                                                                                                                                                                    play sound "audio/Cloth_rustle.wav"
                                                                                                                                                                                                                                                                    scene v13478 with vpunch
                                                                                                                                                                                                                                                                    tmra "Ahh~!" (multiple=2)
                                                                                                                                                                                                                                                                    tr "?!" (multiple=2)
                                                                                                                                                                                                                                                                    play audio "audio/kiss.mp3"
                                                                                                                                                                                                                                                                    scene v13479 with hpunch
                                                                                                                                                                                                                                                                    tmra "HMNN~!" (multiple=2)
                                                                                                                                                                                                                                                                    tr "HMMM?!" (multiple=2)
                                                                                                                                                                                                                                                                    scene v13480 with Dissolve(1)
                                                                                                                                                                                                                                                                    z "Be nice to each other, you two..."
                                                                                                                                                                                                                                                                    show v13m40 with Dissolve(1)
                                                                                                                                                                                                                                                                    tmra "Hmmnn~... Mnnn~..."
                                                                                                                                                                                                                                                                    tr "Mmmmhhnnn~..."
                                                                                                                                                                                                                                                                    z "Look at you getting along... So cute..."
                                                                                                                                                                                                                                                                    tmra "Nmmmmnn~... Mhhhnn~..."
                                                                                                                                                                                                                                                                    tr "Hmmmn~... Ahhmmmm~..."
                                                                                                                                                                                                                                                                    z "Two besties putting their differences behind and joining their lips..."
                                                                                                                                                                                                                                                                    tr "Hmmmnnn~... Fuhhhmm~..."
                                                                                                                                                                                                                                                                    tmra "Ihmmmmmnn~... Fuhhhmmm~..."
                                                                                                                                                                                                                                                                    z "Tamara... I'm gonna cum..."
                                                                                                                                                                                                                                                                    z "I hope you're ready... I'm shooting it inside you..."
                                                                                                                                                                                                                                                                    tmra "Hmmnnn~?! Inmmmm~! Mhhhnnn~!"
                                                                                                                                                                                                                                                                    z "Yeah. I don't understand... I'm gonna cum..."
                                                                                                                                                                                                                                                                    tmra "Mhhhmmmmnnn~!"
                                                                                                                                                                                                                                                                    tmra "Hmmmm-"
                                                                                                                                                                                                                                                                    play audio "audio/creak.mp3"
                                                                                                                                                                                                                                                                    play sound "audio/magic 7.mp3"
                                                                                                                                                                                                                                                                    stop background_s fadeout 1.0