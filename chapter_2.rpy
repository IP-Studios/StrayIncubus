label season2_chapter_2:
    $ chapter = 14
    default mercury_ch14_met = 0
    define lumi = Character("Lumi", color = "f5c13d")
    define mercury = Character("Mercury", color = "ad0011")
    define jacq = Character("Jacqueline", color = "628b94")
    define alura = Character("Alura", color = "a80041")
    define helda = Character("Helda", color = "007cad")
    define Tenebra = Character("Tenebra", color = "a69049")
    default cnt_helping_edge_cndy = 0 #Moved to the beginning of the script.
    default cndy_hrny_cntr_ch14 = 0 #Moved to the beginning of the script.
    default edged_cndy = 0
    default times_spanked_cndy_ch14 = 0
    default gave_up_edging_cndy = 0
    default vns_kinky = 10 #Move up to the begginig of the script!!!!!
    image Horny_position = ParameterizedText(xalign=0.05, yalign=0.05)
    screen ch14_btn_tickle_cndy:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.42
            ypos 0.72
            idle "images/2.2/others/ch2_cndy_1.png"
            hover "images/2.2/others/ch2_cndy_1h.png"
            action Jump("ch14_tickle_cndy")
    screen ch14_btn_finger_cndy:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.43
            ypos 0.89
            idle "images/2.2/others/ch2_cndy_2.png"
            hover "images/2.2/others/ch2_cndy_2h.png"
            action Jump("ch14_finger_cndy")
    screen ch14_btn_spank_cndy:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.63
            ypos 0.75
            idle "images/2.2/others/ch2_cndy_3.png"
            hover "images/2.2/others/ch2_cndy_3h.png"
            action Jump("ch14_spank_cndy")
    screen ch14_btn_kiss_cndy:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.455
            ypos 0.27
            idle "images/2.2/others/ch2_cndy_4.png"
            hover "images/2.2/others/ch2_cndy_4h.png"
            action Jump("ch14_kiss_cndy")
    screen ch14_btn_choke_cndy:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.62
            ypos 0.31
            idle "images/2.2/others/ch2_cndy_5.png"
            hover "images/2.2/others/ch2_cndy_5h.png"
            action Jump("ch14_choke_cndy")
    screen ch14_btn_boobs_cndy:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.4
            ypos 0.5
            idle "images/2.2/others/ch2_cndy_6.png"
            hover "images/2.2/others/ch2_cndy_6h.png"
            action Jump("ch14_boobs_cndy")
    screen ch14_btn_cntxcndy:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.15
            ypos 0.5
            idle "images/2.2/others/ch2_cndy_7.png"
            hover "images/2.2/others/ch2_cndy_7h.png"
            action Jump("ch14_cntxcndy")
    screen ch14_btn_stop_cndy:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.87
            ypos 0.5
            idle "images/2.2/others/ch2_cndy_8.png"
            hover "images/2.2/others/ch2_cndy_8h.png"
            action Jump("gave_up_ch14")
    screen ch14_btn_spank_cndy2:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.58
            ypos 0.73
            idle "images/2.2/others/ch2_cndy_3.png"
            hover "images/2.2/others/ch2_cndy_3h.png"
            action Call("action_spank_cndy")
    screen ch14_btn_spank_cndy_stop:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.87
            ypos 0.5
            idle "images/2.2/others/ch2_cndy_8.png"
            hover "images/2.2/others/ch2_cndy_8h.png"
            action renpy.curry(renpy.end_interaction)(True)
    screen ch14_btn_finger_cndy_stop:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.87
            ypos 0.5
            idle "images/2.2/others/ch2_cndy_8.png"
            hover "images/2.2/others/ch2_cndy_8h.png"
            action Jump("stopped_fingering_ch14")
    screen ch14_btn_fight:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.25
            ypos 0.5
            idle "images/2.2/others/ch14 b3.png"
            hover "images/2.2/others/ch14 b3.png"
            hovered Call("hovering_fight")
            action Jump("ch14_fight")
    screen ch14_btn_leave:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.75
            ypos 0.5
            idle "images/2.2/others/ch14 b2.png"
            hover "images/2.2/others/ch14 b2.png"
            hovered Call("hovering_leave")
            action Jump("ch14_leave")
    screen ch14_btn_negotiate:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.48
            ypos 0.88
            idle "images/2.2/others/ch14 b1.png"
            hover "images/2.2/others/ch14 b1.png"
            hovered Call("hovering_negotiate")
            action Jump("ch14_negotiate")
    screen pixel:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.01
            ypos 0.01
            idle "images/2.2/others/pixel.png"
            hover "images/2.2/others/pixel.png"
            action NullAction()
    image v14m1 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m1.webm", loop=True)
    image v14m2 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m2.webm", loop=True)
    image v14m3 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m3.webm", loop=True)
    image v14m4 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m4.webm", loop=True)
    image v14m5 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m5.webm", loop=True)
    image v14m6 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m6.webm", loop=True)
    image v14m7 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m7.webm", loop=True)
    image v14m8 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m8.webm", loop=True)
    image v14m9 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m9.webm", loop=True)
    image v14m10 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m10.webm", loop=True)
    image v14m11 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m11.webm", loop=True)
    image v14m12 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m12.webm", loop=True)
    image v14m13 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m13.webm", loop=True)
    image v14m14 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m14.webm", loop=True)
    image v14m15 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m15.webm", loop=True)
    image v14m16 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m16.webm", loop=True)
    image v14m17 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m17.webm", loop=True)
    image v14m18 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m18.webm", loop=True)
    image v14m19 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m19.webm", loop=True)
    image v14m20 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m20.webm", loop=True)
    image v14m21 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m21.webm", loop=True)
    image v14m22 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m22.webm", loop=True)
    image v14m23 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m23.webm", loop=True)
    image v14m24 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m24.webm", loop=True)
    image v14m25 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m25.webm", loop=True)
    image v14m26 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m26.webm", loop=True)
    image v14m27 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m27.webm", loop=True)
    image v14m28 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m28.webm", loop=True)
    image v14m29 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m29.webm", loop=True)
    image v14m30 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m30.webm", loop=True)
    image v14m31 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m31.webm", loop=True)
    image v14m32 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m32.webm", loop=True)
    image v14m33 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m33.webm", loop=True)
    image v14m34 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m34.webm", loop=True)
    image v14m35 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m35.webm", loop=True)
    image v14m36 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m36.webm", loop=True)
    image v14m37 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m37.webm", loop=True)
    image v14m38 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m38.webm", loop=True)
    image v14m39 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m39.webm", loop=True)
    image v14m40 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m40.webm", loop=True)
    image v14m41 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m41.webm", loop=True)
    image v14m42 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m42.webm", loop=True)
    image v14m43 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m43.webm", loop=True)
    image v14m44 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m44.webm", loop=True)
    image v14m45 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m45.webm", loop=True)
    image v14m46 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m46.webm", loop=True)
    image v14m47 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m47.webm", loop=True)
    image v14m48 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m48.webm", loop=True)
#    image v14m49 = Movie(size = (1920,1080), channel="movie", play="2.2/video/v14m49.webm", loop=True)
    default persistent.g_54_unlock = 0
    default persistent.g_55_unlock = 0
    default persistent.g_56_unlock = 0
    default persistent.g_57_unlock = 0
    default persistent.g_58_unlock = 0
    #The chapter starts here
#1) Intro:
    pause(1.5)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    play background_s2 "audio/Ambient_ninja_village_night.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v141 with Dissolve(1.5)
    pause(1.5)
    play music "audio/Town of the faceless god 2.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v142 with Dissolve(1)
    Character("Widow", color = "858585") "..."
    scene v143 with Dissolve(2)
    Character("Widow", color = "858585") "..."
    scene v144 with Dissolve(1)
    hlna "..."
    scene v145 with dissolve
    hlna "What's going on here?"
    hlna "A funeral?"
    scene v146 with Dissolve(1)
    Character("Boy", color = "574f3e") "You're a ninja!"
    Character("Boy", color = "574f3e") "You have to help us! My father! He-"
    scene v147 with dissolve
    Character("Widow", color = "858585") "Hunter!"
    Character("Widow", color = "858585") "Ninja or not, the lady can't bring your father back, honey."
    Character("Boy", color = "574f3e") "But..."
    scene v148 with dissolve
    Character("Widow", color = "858585") "Thank you for your concern... But my husband died of illness..."
    scene v149 with Dissolve(1)
    Character("Widow", color = "858585") "There's nothing you can do to help us..."
    pause(1)
    scene v1410 with Dissolve(1)
    Character("Widow", color = "858585") "..."
    scene v1411 with Dissolve(1.5)
    pause(2)
    scene v1412 with Dissolve(1.5)
    Character("Widow", color = "858585") "{i}Crying.{/i}"
    scene v1413 with Dissolve(1.5)
    Character("Widow", color = "858585") "{i}Crying.{/i}"
    pause(1)
    scene v1414 with Dissolve(1)
    pause(1)
    play sound "audio/open book.mp3"
    scene v1415 with Dissolve(1)
    pause(1)
    "To the ninja village..."
    "A member of your village once visited our village long ago on the day I had to bury my husband."
    "I lied and said my husband died of illness. My brave son wanted to tell the truth that day, to tell that in fact his father was murdered. But I stopped him."
#2) Ninja village 1st morning:
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.6 fadeout 1.0 fadein 1.0 loop
    scene v1416 with Dissolve(2)
    stop music fadeout 1.0
    "Today. I buried my son. Murdered. Perhaps by the same monster that killed his father."
    "Please. Help us. Help our town. Please."
    "A monster lies in the shadows in Brethren. A monster which has taken countless lives over the past years."
    pause(2)
    "Help."
    scene v1417 with dissolve
    stfny "This one sounds tough..."
    scene v1418 with dissolve
    stfny "..." #Looks at helena looking at the trapped creature.
    scene v1419 with Dissolve(1)
    pause(1)
    scene v1420 with Dissolve(1)
    hlna "..."
    play sound "audio/creak.mp3"
    scene v1421 with dissolve
    stfny "Mom." (multiple=2)
    hlna "Hm?" (multiple=2)
    scene v1422 with dissolve
    stfny "I think this is an A-ranked mission, right?"
    scene v1423 with dissolve
    hlna "..." #Looks surprised.
    scene v1424 with dissolve
    stfny "Is something wrong?"
    play sound "audio/open book.mp3"
    scene v1425 with dissolve
    hlna "Where is this from?"
    scene v1426 with dissolve
    stfny "A small town called Brethren."
    scene v1427 with dissolve
    hlna "Is it now..."
    scene v1426 with dissolve
    stfny "You know it?"
    scene v1425 with dissolve
    hlna "You can say that... I've been there once or twice..."
    scene v1428 with dissolve
    hlna "..."
    scene v1425 with dissolve
    hlna "A-ranked. Yes."
    scene v1429 with Dissolve(1)
    stfny "We have three missions that need attending to now."
    scene v1430 with Dissolve(1)
    stfny "The letters have really piled up..."
    scene v1431 with dissolve
    stfny "Should we really have stopped taking missions last week?"
    stfny "And why are we back to accepting them again?"
    scene v1432 with dissolve
    stfny "Is it because we were already attacked by this thing?"
    scene v1433 with dissolve
    stfny "Is it the same as the thing that attacked the other ninja village?"
    scene v1434 with dissolve
    hlna "..."
    scene v1435 with dissolve
    hlna "It's certainly similar..."
    scene v1436 with dissolve
    stfny "So you think we should be safe now?"
    stfny "If there's two of them, there could be more, right?"
    scene v1434 with dissolve
    hlna "..."
    scene v1435 with dissolve
    hlna "Still, we can't stay on full alert forever, Stephanie."
    hlna "That aside, I never would've thought we would deal with the attack with such ease."
    hlna "The southern village took a handful of casualties, some of which were high ranking ones, and half of the village was burnt down..."
    scene v1437 with dissolve
    stfny "..."
    scene v1438 with dissolve
    stfny "I guess we have our golden boy to thank for that, don't we?"
    scene v1439 with dissolve
    hlna "We do indeed."
    scene v1440 with dissolve
    pause(2)
#3) Z's dream:
    #Switch to Z.
    #Z is dreaming:
    #    The ninja village is distroyed and he's looking if someone else survived.
    #    Athena and Apollo are standing looking at it.
    #    Athena says that only one person can stop them according to Auge and looks towards a figure which Z thinks it's him.
    scene black with Dissolve(2)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(1)
    play music "audio/Town of the faceless god.mp3" volume 0.4 fadeout 2.0 fadein 2.0 loop
    pause(1)
    scene v1441 with Dissolve(2)
    play background_s "audio/fireplace.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
    pause(2)
    scene v1442 with Dissolve(1)
    z "..."
    scene v1443 with Dissolve(1)
    z "Anyone..."
    z "Did anyone make it..."
    scene v1444 with Dissolve(1)
    z "Guys..."
    z "Seira... Torr... Candy..."
    z "..."
    play sound "audio/rustle 2.mp3"
    scene v1445 with dissolve
    #Hears sth.
    z "?!"
    scene v1446 with Dissolve(1)
    #Athena and Apollo are looking from above at it.
    athna "..."
    scene v1447 with dissolve
    athna "We are almost done, dear brother."
    scene v1448 with dissolve
    athna "There stands only one who could possibly get in our way."
    athna "Auge said as soon as we kill him, it's over."
    athna "We will have won."
    scene v1449 with Dissolve(1)
    z "..."
    play audio "audio/Magic 9.mp3"
    scene v1450 with dissolve
    z "Athena!" #Z is standing in front of them.
    z "I will fucking kill you!"
    scene v1451 with Dissolve(1)
    athna "Let's get this over with, Apollo."
    #They attack him.
    pause(1)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene v1452 with Dissolve(1)
    pause(1)
    scene v1453 with Dissolve(1)
    pause(1)
    play audio "audio/cloth.mp3"
    scene v1454
    with vpunch
    #He wakes up.
    z "!!!"
    scene v1455 with Dissolve(1)
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
    z "..."
    z "(Those fucking dreams...)"
    scene v1456 with dissolve
    z "..."
    #Looks down.
    play music "audio/kalm (no panik) 2.mp3" volume 0.3 fadeout 1.0 fadein 1.0 loop
    scene v1457 with Dissolve(1)
    z "..."
    #Margot is measuring his dick again.
    z "You again..."
    play audio "audio/cloth.mp3"
    scene v1458 with dissolve
    margot "Can't blame a girl for being curious."
    scene v1459 with dissolve
    margot "I can see it's still the same size."
    scene v1460 with dissolve
    z "The fuck else did you expect..."
    play audio "audio/cloth.mp3"
    scene v1461 with dissolve
    margot "The experiment had to be conducted all the same, stud."
    margot "I could brew you something for the nightmares, by the way."
    scene v1462 with dissolve
    z "Who says I'm having nightmares?"
    z "And I'm not sure I'd wanna consume anything you brew..."
    scene v1463 with dissolve
    margot "If you say so, stud. The offer stands, though."
    scene v1461 with dissolve
    margot "You haven't slept, last night, right?"
    margot "I guess it's kinda because of us... Not to mention you saved our lives."
    scene v1464 with dissolve
    margot "You can visit me any time you want. I could show you how grateful I am for last night."
    play sound "audio/Cloth_rustle.wav"
    scene v1465 with Dissolve(1)
    pause(1)
    play sound "audio/Cloth_rustle.wav"
    scene v1466 with Dissolve(1)
    margot "Bye!"
    scene v1467 with dissolve
    #Gets up.
    #Leaves.
    z "..."
    z "(This fucking girl...)"
    pause(2)
#4) Meeting:
    scene black with Dissolve(2)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(1)
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    pause(1)
    scene v1468 with Dissolve(2)
    pause(2)
    scene v1469 with dissolve
    z "Hey, guys."
    play music "audio/ninja village s02.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v1470 with dissolve
    stfny "Well, well, well... If it isn-"
    play sound "audio/whoosh.mp3"
    scene v1471 with hpunch
    cndy "Hey, [mc_name]!" #Waltzes in.
    scene v1472 with dissolve
    tr "Is it true you took on that thing on your own?!"
    scene v1473 with Dissolve(1)
    z "..."
    z "Yes..."
    scene v1474 with dissolve
    tr "You can use lightning?!"
    scene v1473 with dissolve
    z "Apparently so..."
    z "I used it in the tournament against Venus, didn't you see that?"
    scene v1475 with dissolve
    tr "No... I was getting ready for my fight..."
    scene v1476 with dissolve
    tr "Can you teach me?"
    play sound "audio/Cloth_rustle.wav"
    scene v1477 with Dissolve(1)
    pause(1)
    scene v1478 with dissolve
    z "Lightning?"
    scene v1479 with dissolve
    tr "Yup!"
    play sound "audio/Cloth_rustle.wav"
    scene v1480 with hpunch
    cndy "Hey! Teach me too!"
    scene v1481 with dissolve
    tr "Eh?! Since when do you care about stuff like that?"
    scene v1482 with dissolve
    cndy "I always care about stuff like that!"
    scene v1483 with dissolve
    pause(1)
    scene v1484 with dissolve
    pause(1)
    #They're susing each other.
    scene v1485 with dissolve
    z "I wouldn't mind teaching it, but shouldn't you guys ask Venus? She's the expert lightning user."
    scene v1486 with dissolve
    tr "I guess, but I don't like her as much as I like you."
    scene v1487 with Dissolve(1)
    z "..."
    scene v1488 with dissolve
    tr "..." #realises.
    scene v1489
    play sound "audio/Punch2.mp3"
    with vpunch
    tr "N-Not like I like you or anything!"
    scene v1490 with dissolve
    tr "I just really dislike Venus... Yeah..."
    scene v1491 with dissolve
    tr "?!"
    scene v1492
    play sound "audio/whoosh.mp3"
    with hpunch
    tr "Ah! No! I didn't mean it like tha-"
    #helena comes in
    scene v1493 with Dissolve(1)
    hlna "Very damn hot today, isn't it?"
    scene v1494 with dissolve
    hlna "That makes everyone, I suppose. Shall we begin?"
    scene v1495 with dissolve
    pause(1)
    scene v1496 with Dissolve(1)
    tr "..." (multiple=2)
    vns "..." (multiple=2)
    scene v1497 with Dissolve(1)
    hlna "I'm going to get straight to the point here..."
    scene v1498 with dissolve
    hlna "We have two main things to do today; assigning points gained in the tournament, and assigning you guys to your missions. Everyone present here will be assigned to one, actually."
    scene v1499 with dissolve
    tr "Separately?"
    scene v14100 with dissolve
    hlna "No. Three missions will be assigned to three teams."
    scene v1499 with dissolve
    tr "Ah..."
    scene v14100 with dissolve
    hlna "Points first, though."
    #Whispers to candy:
    scene v14103 with Dissolve(1)
    tr "This my favourite part..."
    scene v14101 with Dissolve(1)
    hlna "Venus, Tamara, Candy, Centoria, and Stephanie will receive no points, I'm afraid."
    scene v14103 with Dissolve(1)
    hlna "Hailey and Yumi will get ten points each for winning a round." (multiple=2)
    tr "{size=-10}I wonder how many points I'll get for beating the midget.{/size}" (multiple=2)
    scene v14102 with dissolve
    hlna "Torr." (multiple=2)
    tr "?!" (multiple=2)
    play sound "audio/Cloth_rustle.wav"
    scene v14104 with Dissolve(1)
    hlna "You won one round, that's ten points."
    hlna "And you beat a ninja one rank higher than you, that's twenty five more."
    hlna "Adding up your points, you have a total of 117 points."
    scene v14105 with dissolve
    tr "Ah?!"
    scene v14106 with dissolve
    tr "I'm so close to orange belt!"
    scene v14104 with dissolve
    hlna "Indeed you are. You only need 13 more points."
    play sound "audio/Cloth_rustle.wav"
    scene v14107 with Dissolve(1)
    hlna "[mc_name]."
    z "..."
    hlna "Your last deduction sent you back to purple belt having 53 points in total."
    hlna "However, you won three rounds, giving you five each. Means you get 15 points."
    scene v14108 with dissolve
    hlna "You also defeated two brown belts. Venus and Hailey. Each win gives you 40 points. So that's 95 in total so far."
    $ stfny_res += 3
    $ a_res += 3
    $ cndy_res += 3
    $ hly_res += 3
    $ ymi_res += 3
    $ tmra_res += 3
    $ cnt_res += 3
    $ vns_res += 3
    show screen button_res with dissolve
    play sound "audio/stats.wav"
    hide screen button_res with dissolve
    scene v14109 with Dissolve(1)
    tr "Oh! He made yellow already!"
    play sound "audio/Cloth_rustle.wav"
    scene v14110 with dissolve
    cndy "No, he didn't! He has 148 points in total!"
    scene v14111 with dissolve
    tr "What?! No, he has..."
    play background_s "audio/clock.mp3" volume 0.6 fadeout 1.0 fadein 1.0 loop
    scene v14112 with Dissolve(1)
    pause(1)
    scene v14113 with dissolve
    pause(1)
    scene v14114 with dissolve
    pause(1)
    scene v14115 with dissolve
    pause(1)
    #Calculating meme again.
    #Fails to calculate and smoke comes out of her head.
    play background_s "audio/alarm clock.mp3" volume 0.6
    scene v14116 with vpunch
    tr "Agghhh..."
    stop background_s fadeout 1.0
    play sound "audio/Cloth_rustle.wav"
    scene v14117 with vpunch
    cndy "Ah! Torr!"
    scene v14118 with Dissolve(1)
    hlna "And you beat me, a black belt. You'll receive 45 points for that."
    hlna "You are therefore promoted to yellow belt."
    scene v14119 with Dissolve(1)
    cndy "Oh... He did make yellow after all."
    scene v14120 with dissolve
    cndy "Congrats-" #Turns to z.
    #He's surrouned by the higher ranking girls talking to him.
    scene v14121 with dissolve
    tr "..." #Gets up
    scene v14122 with Dissolve(1)
    cndy "..."
    scene v14123 with Dissolve(1)
    cndy "I guess [mc_name] is on the high ranking side now..."
    scene v14124 with dissolve
    tr "Hmm..."
    scene v14125 with dissolve
    tr "Why do you not look happy about it?"
    scene v14126
    play sound "audio/whoosh.mp3"
    with hpunch
    cndy "Oh! No, no! I didn't mean it like that!"
    scene v14127 with dissolve
    cndy "..."
    scene v14128 with dissolve
    cndy "But doesn't that mean he's probably not gonna go on missions with us anymore, cuz he'll mostly get high ranking missions."
    scene v14129 with dissolve
    tr "..."
    scene v14130 with dissolve
    cndy "Also... Did he get taller?" #Height pose.
    scene v14131 with dissolve
    tr "I think so, yes..."
    scene v14132 with Dissolve(1)
    cndy "He also put on some muscle, didn't he..."
    scene v14133 with dissolve
    tr "I guess so..."
    scene v14134 with dissolve
    cndy "Is that some facial hair on his chin..."
    scene v14135 with dissolve
    tr "..."
    scene v14133 with dissolve
    tr "I think it's just dirt."
    scene v14134 with dissolve
    cndy "No, I'm pretty sure it's facial hair."
    scene v14135 with dissolve
    tr "..."
    #Hlna interrupts:
    scene v14136 with Dissolve(1)
    hlna "Now. The missions."
    hlna "First team will be Torr, Tamara, and Anabelle."
    scene v14137 with dissolve
    tmra "Anabelle?"
    tmra "Shouldn't the Keres stay in the village at all time unless absolutel-"
    scene v14138 with dissolve
    hlna "Yes, Tamara. But we have Seira here too. And Anabelle could use the distraction."
    scene v14139 with Dissolve(1)
    tmra "..." (multiple=2)
    a "..." (multiple=2)
    scene v14140
    play sound "audio/Slap2.mp3"
    with hpunch
    tr "My first real high ranking mission!"
    scene v14141 with dissolve
    hlna "You three will be going to a village two days south east of here. Two women have gone missing there."
    hlna "The mission is ranked C and the mission leader will be Anabelle."
    hlna "Do take great care, you three. This might as well end up proving to be an A-ranked mission for all we know. Whatever took the woman could be anything from a goblin to a higher demon."
    scene v14142 with dissolve
    a "Heard, Helena."
    scene v14143 with Dissolve(1)
    hlna "Candy, Centoria, Yumi, and Stephanie. A village south west has reported suspicious activity in the forest nearby."
    hlna "We believe it's probably bandits smuggling something. Their reports suggest it's a handful of them. However, should this be way bigger than that, report back here, so we can move in a larger force."
    scene v14144 with dissolve
    stop music fadeout 6.0
    hlna "The current mission rank is D, and the mission leader will be Stephanie."
    scene v14145 with Dissolve(1)
    hlna "For our last mission..."
    hlna "[mc_name], Venus, and Hailey will be going to Brethren."
    hlna "However, if any of you has any reservations about going there, I'd understand."
    scene v14146 with dissolve
    z "..."
    scene v14147 with dissolve
    pause(1)
    scene v14148 with dissolve
    pause(1)
    #Everyone is looking at him meme.
    scene v14149 with dissolve
    z "What the..."
    scene v14150 with dissolve
    z "Why is everyone looking at me?!"
    scene v14151 with dissolve
    z "Why would I not want to go there?"
    scene v14152 with Dissolve(1)
    play music "audio/Zycris's theme s02 1.mp3" volume 0.4 fadeout 1.0 fadein 4.0 loop
    pause(1)
    scene v14153 with dissolve
    hlna "You don't know?"
    scene v14152 with dissolve
    z "Know what?"
    scene v14154 with dissolve
    hlna "This particular town is known-"
    hlna "Well, rumoured to have one of the few entrances to the incubi underground city."
    scene v14152 with dissolve
    z "It is?!"
    scene v14153 with dissolve
    hlna "Yes. It's said that underneath the town is a tunnel that leads there."
    scene v14152 with dissolve
    z "And there's an entrance to the tunnel there?"
    scene v14153 with dissolve
    hlna "Again, it's only a rumour, but that's what they say."
    scene v14152 with dissolve
    z "And it's still working?"
    scene v14154 with dissolve
    hlna "I have no idea honestly."
    scene v14152 with dissolve
    z "..."
    z "So why exactly do we need to go to this town?"
    pause(2)
    #Rest of the explanation comes later.
#5) Candy, Torr, and Centoria:
    if cndy_lst >= 18 and tr_lst >= 20 and cnt_lst >= 2:
        scene black with Dissolve(2)
        pause(1)
        stop background_s fadeout 1.0
        stop background_s2 fadeout 1.0
        stop music fadeout 1.0
        stop sound fadeout 1.0
        pause(2)
        scene v14155 with Dissolve(2)
        play music "audio/Calm s02.mp3" volume 0.15 fadeout 1.0 fadein 1.0 loop
        pause(1)
        cndy "Not here..."
        play sound "audio/sliding door.mp3"
        scene v14156 with dissolve
        cndy "Torr!"
        scene v14157 with Dissolve(1)
        tr "What?"
        scene v14158 with dissolve
        cndy "Have you been stealing my bras?"
        scene v14157 with dissolve
        tr "What? No!"
        tr "They don't even fit me!"
        scene v14158 with dissolve
        cndy "Yeah?"
        scene v14157 with dissolve
        tr "Yeah."
        scene v14158 with dissolve
        cndy "What are you wearing right now?"
        scene v14157 with dissolve
        tr "What?"
        scene v14159 with dissolve
        tr "This is my yellow bra!"
        scene v14158 with dissolve
        cndy "Looks kinda like one of mine..."
        scene v14157 with dissolve
        tr "It's not!"
        scene v14160 with dissolve
        cndy "Hmmm..."
        scene v14161 with dissolve
        cndy "..."
        scene v14162 with dissolve
        cndy "Take off your shirt, then. Let me have a look."
        scene v14163 with dissolve
        tr "What?"
        tr "Why should I?"
        scene v14164 with dissolve
        cndy "What, are you shy or something? I'm literally standing topless here!"
        scene v14165 with dissolve
        tr "I'm not shy! I just don't know why I need to take off my shirt!"
        scene v14164 with dissolve
        cndy "Come onnnnn! I need to find my clothes before we leave on our missions tomorrow!"
        scene v14165 with dissolve
        tr "Just trust me! I'm not wearing your bra!"
        scene v14164 with dissolve
        cndy "Then prove it!"
        scene v14165 with dissolve
        tr "No!"
        play sound "audio/Falling2.mp3"
        scene v14166 with vpunch
        cndy "Come on! Just show me!" (multiple=2) #Attacks
        cnt "!" (multiple=2)
        scene v14167 with Dissolve(1)
        cnt "Guys! Calm down!"
        play sound "audio/Cloth_rustle.wav"
        scene v14168 with dissolve
        cndy "Easy for you to say!"
        scene v14169
        play sound "audio/whoosh.mp3"
        with hpunch
        cndy "You don't even wear bras!" (multiple=2) #Takes off her shirt
        cnt "?!" (multiple=2)
        play sound "audio/Falling2.mp3"
        scene v14170 with vpunch
        tr "See? It's not your bra, okay?" #Already topless
        scene v14171 with dissolve
        cndy "..."
        scene v14172 with dissolve
        cndy "I've also been missing a couple of panties..."
        scene v14173 with dissolve
        tr "Oh, come the fuck on! You can't blame me for all of th-"
        play sound "audio/Cloth_rustle.wav"
        scene v14174
        with hpunch
        #Takes off torr's shorts.
        tr "?!"
        play sound "audio/Cloth_rustle.wav"
        scene v14175 with dissolve
        cndy "..."
        scene v14176 with dissolve
        tr "Now you've done it!"
        stop music
        play audio "audio/camera.mp3"
        scene black
        pause(0.1)
        play sound "audio/explosion (long).mp3" volume 0.4
        pause(0.4)
        with vpunch
        with vpunch
        with vpunch
        with vpunch
        with vpunch
        with vpunch
        pause(1.5)
        play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
        scene v14177 with Dissolve(1.5)
        pause(2)
        scene v14178 with Dissolve(1)
        pause(2)
        play sound "audio/sliding door.mp3"
        stop background_s fadeout 1.0
        stop background_s2 fadeout 1.0
        scene v14179 with Dissolve(1)
        #Switch to Z outside the room.
        #Opens the door.
        z "Hey, guys..."
        z "Just wanted to check on you before tomorrow's mi-"
        scene v14180 with dissolve
        z "..."
        scene v14181
        play sound "audio/Slap2.mp3"
        with hpunch
        cndy "Eeeep!"
        play audio "audio/camera.mp3"
        scene black
        pause(2)
        scene v14182 with Dissolve(1)
        #They're all mostly naked, centoria because she was trying to pull them away from each other.
        #They all blush. Torr spanks candy again.
        play music "audio/Calm s02.mp3" volume 0.15 fadeout 1.0 fadein 1.0 loop
        z "..."
        z "(Need to break the ice...)"
        scene v14183 with dissolve
        z "How is your preperation, guys?"
        scene v14184 with dissolve
        cndy "It would've been much easier if someone wasn't stealing my clothes..."
        scene v14185 with dissolve
        tr "I'm not stealing anything!"
        scene v14186 with dissolve
        z "(Oopsie... Not working...)"
        scene v14187 with dissolve
        z "Candy. I see you changed your hair up a little."
        play sound "audio/Cloth_rustle.wav"
        scene v14188 with dissolve
        cndy "Oh? You noticed?"
        cndy "Do you like it?"
        scene v14189 with dissolve
        z "Yeah. It looks nice on y-"
        play sound "audio/Cloth_rustle.wav"
        scene v14190 with dissolve
        tr "Hey! How about my hair? I also change it up all the time! How come you only notice it on Candy!"
        play sound "audio/Cloth_rustle.wav"
        scene v14191 with dissolve
        cnt "I also tried something different with my hair..."
        scene v14192 with dissolve
        z "(Fuck... Nothing is working here... It's just getting worse.)"
        scene v14193 with Dissolve(1)
        tr "You're the one who recommended I bun it like this! Were you trying to make me look worse?!"
        scene v14194 with dissolve
        cndy "What? No! It's just more convenient if it's not all over your face!"
        scene v14193 with dissolve
        tr "Yeah, right! You-"
        scene v14195 with dissolve
        z "Guys, guys."
        z "How about a game?"
        scene v14198 with dissolve
        tr "..." (multiple=2)
        cndy "..." (multiple=2)
        scene v14196 with dissolve
        cndy "A game?"
        scene v14197 with dissolve
        tr "What kind of game?"
        scene v14198 with dissolve
        z "(Okay... That seems to have calmed them down a bit... That's a good start.)"
        z "Jenny, Gabbie, and I used to play it all the time when we were young."
        z "It's called rock paper scissors."
        scene v14197 with dissolve
        tr "What's that?"
        scene v14199 with Dissolve(1)
        cnt "Oh! The princess and I used to play it all the time!"
        cnt "Basically, you make a shape with your hand that represents either rock, paper, or scissors."
        cnt "Rock beats scissors, scissors beats paper, and paper beats rock."
        play sound "audio/Cloth_rustle.wav"
        scene v14200 with dissolve
        cndy "So like a cycle of who beats whom?"
        scene v14201 with dissolve
        cnt "Exactly."
        cnt "And if you lose, you have to do something the winner tells you to do."
        scene v14202 with dissolve
        z "What?"
        scene v14203 with dissolve
        cnt "What?"
        scene v14202 with dissolve
        z "(We didn't play it like that... But now that I think about it, this could be verrrrry interesting with those three...)"
        pause(1)
        menu:
            "Tell Centoria the dare part wasn't included in the game you played.":
                z "When we used to play, the part were the loser has to do something the winner picks wasn't included..."
                scene v14203 with dissolve
                cnt "Oh?"
                scene v14202 with dissolve
                z "I'd say let's make the game as friendly as possible for now?"
                scene v14203 with dissolve
                cnt "Sure."
                scene v14202 with dissolve
                pause(1)
                scene v14204 with Dissolve(2)
                pause(1)
                "You play a couple of innocent rounds of rock paper scissors with the girls and leave them to prepare for tomorrow..."
                pause(2)
                #Skip
                #One render of them playing innocently.
            "Don't object to it.":
                z "Nothing... That actually sounds interesting..."
                z "Since there's more than two people, which is the defualt for this game, here's what we used to do..."
                #Figures to explain.
                label G54:
                    $ persistent.g_54_unlock = 1
                scene v14205 with Dissolve(1.5)
                z "The two people opposite to each other will check who won between the two of them."
                scene v14206 with dissolve
                z "Then, the two people left will check who won between them."
                scene v14207 with dissolve
                z "So, someone will have two wins, while the other will have just one win."
                scene v14208 with Dissolve(1)
                z "In the case of a tie, the two people who tie will not get to tell the person who they tied with to do anything."
                z "They also wouldn't qualify to the next round, so to speak."
                z "Each person gets to tell all the people they defeated to do one thing."
                z "How does that sound?"
                scene v14209 with dissolve
                cnt "Sure." (multiple=2)
                cndy "Okay." (multiple=2)
                scene v14210 with Dissolve(1)
                tr "{size=-10}Paper beats scissors...{/size}"
                tr "{size=-10}Rock beats scissors...{/size}"
                tr "{size=-10}Scissors beats-{/size}" #Whispering to herself to remember.
                scene v14211 with dissolve
                z "Let's start?" (multiple=2) #Interupted by z.
                tr "?!" (multiple=2)
                scene r_p_s_expln with Dissolve(1)
                z "Rock..."
                z "Paper..."
                z "Scissors!"
                play sound "audio/whoosh.mp3"
                scene v14213 with dissolve
                pause(1)
                #Refer to excel sheet.
                label round_1_of_r_p_s:
                   z "Okay, so I tell Centoria and Candy to do something, and Candy tells Torr to do something."
                   scene v14218 with Dissolve(1)
                   z "Centoria..."
                   z "Stand on your hands for 10 seconds."
                   scene v14219 with dissolve
                   cnt "Hmmm... I'm not sure I can..."
                   play sound "audio/Cloth_rustle.wav"
                   scene v14220 with Dissolve(1)
                   cnt "I'll try..."
                   #Struggling but pulls it off.
                   pause(1)
                   play sound "audio/creak.mp3"
                   scene v14221 with Dissolve(1)
                   cnt "..."
                   scene v14222 with dissolve
                   cnt "Ughh..."
                   scene v14223 with Dissolve(1)
                   z "Candy..."
                   z "Go behind Centoria standing on her hands, stick your face out from behind her and make stupid faces for as long as she's there."
                   cndy "..."
                   scene v14224 with dissolve
                   cndy "Okay..."
                   scene v14225 with Dissolve(1)
                   cndy "..."
                   scene v14226 with dissolve
                   cndy "Hmmmm..."
                   scene v14227 with Dissolve(1)
                   cndy "Something like..."
                   scene v14228 with dissolve
                   cndy "Thiiitth?"
                   scene v14229 with dissolve
                   z "{i}Chuckles.{/i} Yep."
                   play sound "audio/Cloth_rustle.wav"
                   scene v14230 with Dissolve(1)
                   cnt "{i}Sighs.{/i} That was difficult..."
                   scene v14231 with Dissolve(1)
                   cndy "Now it's my turn."
                   play sound "audio/whoosh.mp3"
                   scene v14232 with PushMove(0.1, mode="pushright")
                   cndy "Torr, take off your top." #Evil smile.
                   scene v14233 with dissolve
                   tr "Ughhh... I knew you'd go for something like that."
                   play audio "audio/cloth.mp3"
                   scene v14234 with dissolve
                   #Takes off her top.
                   pause(1)
                   scene v14235 with Dissolve(1)
                   tr "Here! Happy?"
                   scene v14236 with dissolve
                   cndy "Very."
                   scene v14237 with Dissolve(1)
                   z "..."
                   z "(Okay, I wasn't even expecting that... I guess the girls are going in that direction...)"
                   scene v14238 with dissolve
                   z "Okay, next round?"
                   scene v14239 with Dissolve(1)
                   tr "Yeah. I'll show you when I win this round, Candy."
                   scene v14240 with dissolve
                   tr "I get the game now, I'm going to be winning from now on." #Evil smile.
                   scene v14241 with dissolve
                   pause(1)
                label round_2_of_r_p_s:
                   scene r_p_s_expln with Dissolve(1)
                   z "Rock..."
                   z "Paper..."
                   z "Scissors!"
                   play sound "audio/whoosh.mp3"
                   scene v14214 with dissolve
                   pause(1)
                   z "..."
                   tr "What?!"
                   z "I guess only Candy gets to tell Torr to do something."
                   scene v14242 with Dissolve(1)
                   cndy "Take off your shorts."
                   scene v14243 with dissolve
                   tr "Aaaaggghhh..." #Annoyed.
                   play audio "audio/cloth.mp3"
                   scene v14244 with Dissolve(1)
                   tr "..."
                   play sound "audio/Cloth_rustle.wav"
                   scene v14245 with Dissolve(1)
                   #Strips.
                   #She's now naked.
                   tr "Next round, please?"
                   scene v14246 with dissolve
                   z "Sure..."
                   pause(1)
                label round_3_of_r_p_s:
                   scene r_p_s_expln with Dissolve(1)
                   z "Rock..."
                   z "Paper..."
                   z "Scissors!"
                   play sound "audio/whoosh.mp3"
                   scene v14215 with dissolve
                   pause(1)
                   tr "Fuck!"
                   scene v14247 with Dissolve(1)
                   cnt "I guess I can tel-"
                   play sound "audio/Cloth_rustle.wav"
                   scene v14248 with dissolve
                   cndy "Wait, wait."
                   #Whispers sth to cnt
                   play sound "audio/Cloth_rustle.wav"
                   scene v14249 with dissolve
                   pause(1.5)
                   scene v14250 with dissolve
                   pause(1.5)
                   scene v14251 with dissolve
                   pause(1.5)
                   scene v14252 with dissolve
                   cnt "..."
                   scene v14253 with dissolve
                   cndy "Sounds nice, right?"
                   scene v14254 with dissolve
                   cnt "..."
                   scene v14255 with dissolve
                   cnt "Yeah..."
                   scene v14254 with dissolve
                   pause(1)
                   play sound "audio/Cloth_rustle.wav"
                   scene v14256 with Dissolve(1)
                   cnt "[mc_name]..."
                   scene v14257 with dissolve
                   cnt "Can you please t-take out your..."
                   cnt "Your penis?"
                   scene v14258 with dissolve
                   z "..."
                   z "Okay..."
                   scene v14259 with Dissolve(1)
                   pause(1)
                   play audio "audio/cloth.mp3"
                   scene v14260 with Dissolve(1)
                   pause(1)
                   #Takes off his pants.
                   scene v14261 with Dissolve(1)
                   cndy "Torr..."
                   cndy "Try to make [mc_name] cum."
                   scene v14262 with dissolve
                   tr "..."
                   scene v14263 with dissolve
                   tr "Fiiine..."
                   play sound "audio/Cloth_rustle.wav"
                   scene v14264 with Dissolve(1)
                   pause(1.5)
                   scene v14265 with dissolve
                   cndy "Ahuh! Wait, I didn't finish."
                   cndy "You're not allowed to use your hands, mouth, or well... put it inside you."
                   tr "..."
                   scene v14266 with dissolve
                   tr "How the fuck am I supposed to do that then?!"
                   scene v14265 with dissolve
                   cndy "That's your problem..." #Evil smile.
                   scene v14267
                   play sound "audio/creak.mp3"
                   with vpunch
                   tr "You fuck-"
                   scene v14268 with dissolve
                   z "Wait, Torr."
                   scene v14269 with Dissolve(1)
                   z "I have a plan."
                   scene v14270 with dissolve
                   tr "..."
                   scene v14269 with dissolve
                   z "Bend over."
                   pause(1)
                   scene v14271 with Dissolve(1)
                   tr "..."
                   #Grabs her hips.
                   scene v14272 with dissolve
                   tr "Wait! We can't put it inside, remember?"
                   scene v14273 with dissolve
                   z "I know, I know."
                   show v14m2 with Dissolve(0.75)
                   $ renpy.pause(4, hard=True)
                   #Slides it between her buttcheeks.
                   scene v14274 with dissolve
                   tr "Ah!"
                   tr "What are you-"
                   show v14m3 with Dissolve(1)
                   pause(1)
                   #Hotdogs her animation.
                   tr "Ohhh~..."
                   pause(1)
                   tr "Hahh~... Can you..."
                   pause(1)
                   tr "Can you actaully cum like this?"
                   pause(1)
                   z "I'm not sure..."
                   pause(1)
                   scene v14275 with Dissolve(1)
                   cnt "..." (multiple=2) #Embarrassed af.
                   cndy "..." (multiple=2) #Watching intently.
                   tr "Fuck~..."
                   scene v14276 with dissolve
                   cnt "Are they gonna..."
                   cndy "Hm?"
                   cnt "Are they really doing this in front of us?"
                   scene v14277 with dissolve
                   cndy "That was the plan, right?"
                   scene v14275 with dissolve
                   cnt "But to do it infornt of others like this..."
                   scene v14276 with dissolve
                   cnt "It's so indecent..."
                   scene v14277 with dissolve
                   cndy "Trust me, Centoria... This is one of the least indecent things that will happen today if we continue with the game..."
                   scene v14275 with dissolve
                   pause(1)
                   hide v14m3
                   show v14m3 with Dissolve(1)
                   pause(1)
                   tr "Ahnnn~... Are you close..."
                   z "Not just yet..."
                   tr "I see..."
                   tr "Hnnn~... I'm not complaining... Just asking..."
                   z "I think we have to pick up the pace..."
                   tr "But-"
                   pause(1)
                   show v14m4 with Dissolve(1)
                   pause(1)
                   #Picks up the pace.
                   tr "Ahhh~... Fuck... This feels good..."
                   cndy "I'm glad you're enjoying yourself, Torr."
                   tr "Fuck you, you're enjoying this more than I am, aren't you..."
                   cndy "I'm not the one making the 'please slide it inside me already' face."
                   tr "Ahhh~... I'm not making any faces..."
                   cndy "You totally are..."
                   tr "Fuck..."
                   tr "[mc_name]..."
                   z "Yeah?"
                   tr "Are you... Ahhh~..."
                   tr "Hahh~... Are you there yet?"
                   z "Nope... But this feels really good though..."
                   tr "Are you... Nghh~..."
                   tr "Are you sure we should be going this fast?"
                   z "If I'm going to cum from this, then yes."
                   z "Why? Are you tired or something?"
                   tr "Ahhh~... No... Hahhh~..."
                   pause(1)
                   show v14m5 with Dissolve(1)
                   hide v14m3
                   tr "But you're going really fast..."
                   tr "Ahhn~..."
                   tr "It's gonna be hard to control where your dick goes..."
                   tr "Nghhhnnn~..."
                   tr "What if..."
                   tr "Ohhhh~..."
                   show v14m6 with dissolve
                   tr "What if it accidentally slipped inside my butt-{w=3}{nw}"
                   #Slips inside her butthole.
                   scene v14278
                   play sound "audio/RecordScratch (thanks senpai).ogg"
                   stop music
                   with vpunch
                   tr "Agghhh~!"
                   play audio "audio/camera.mp3"
                   scene black
                   if came_from_gallery == 0:
                       $ tr_lst += 2
                   show screen button_lst with dissolve
                   play sound "audio/stats.wav"
                   hide screen button_lst with dissolve
                   pause(2)
                   #Skip a bit.
                   scene v14279 with Dissolve(1)
                   pause(1)
                   tr "..."
                   z "Sorry about that..."
                   tr "..."
                   scene v14280 with dissolve
                   tr "It's not your fault... It's Candy's with her weird instructions..."
                   play sound "audio/Cloth_rustle.wav"
                   scene v14281 with dissolve
                   play music "audio/Calm s02.mp3" volume 0.15 fadeout 1.0 fadein 1.0 loop
                   cndy "Oopsie..."
                   cndy "I-"
                   scene v14282 with dissolve
                   tr "Next round please."
                   scene v14281 with dissolve
                   cndy "Bu-"
                   scene v14283 with dissolve
                   tr "Next round."
                   cndy "..."
                   pause(1)
                label round_4_of_r_p_s:
                   scene r_p_s_expln with Dissolve(1)
                   z "Rock..."
                   z "Paper..."
                   z "Scissors!"
                   play sound "audio/whoosh.mp3"
                   scene v14216 with dissolve
                   pause(1)
                   tr "..."
                   play sound "audio/creak.mp3"
                   scene v14284 with vpunch
                   tr "Yes! Fuck you! In your face, Candy!"
                   scene v14285 with dissolve
                   cndy "..."
                   scene v14286 with dissolve
                   tr "Oh, I also get to tell [mc_name] to do something..."
                   scene v14287 with dissolve
                   pause(1)
                   scene v14288 with Dissolve(1)
                   tr "Candy..."
                   tr "Strip."
                   cndy "..."
                   scene v14289 with dissolve
                   cndy "Which part of my cloth-"
                   scene v14288 with dissolve
                   tr "All of it."
                   cndy "..."
                   scene v14290
                   play sound "audio/creak.mp3"
                   with vpunch
                   cndy "Wait! She can do that?"
                   scene v14291 with dissolve
                   z "..." (multiple=2)
                   cnt "..." (multiple=2)
                   z "Can't see why not."
                   cndy "..."
                   scene v14292 with dissolve
                   cndy "I should've done that from the beginning." #Facepalms
                   play sound "audio/Cloth_rustle.wav"
                   scene v14293 with Dissolve(1)
                   cndy "Fine..." #Stands up
                   play sound "audio/cloth.mp3"
                   scene v14294 with Dissolve(1)
                   pause(1.5)
                   play sound "audio/Zip.mp3"
                   scene v14295 with Dissolve(1)
                   pause(1.5)
                   play sound "audio/Cloth_rustle.wav"
                   scene v14296 with Dissolve(1)
                   pause(1.5)
                   #Strips.
                   scene v14297 with Dissolve(1)
                   cndy "..."
                   scene v14298 with dissolve
                   tr "[mc_name]..."
                   scene v14299 with dissolve
                   tr "Edge her as much as you can..."
                   scene v14300 with dissolve
                   tr "But don't let her cum..."
                   tr "And you can't put your dick inside her either."
                   tr "That should teach you..."
                   scene v14297 with dissolve
                   z "..."
                   scene v14301 with Dissolve(1)
                   z "(Meanwhile, should I make Centoria do something...)"
                   pause(1)
                   menu:
                      "Have Centoria help you with edging Candy.":
                           $ cnt_helping_edge_cndy = 1
                           scene v14302 with Dissolve(1)
                           z "Centoria."
                           z "You'll help me with the task Torr gave me."
                           cnt "..."
                           scene v14303 with dissolve
                           cnt "O-Okay..."
                           scene v14304 with dissolve
                           z "..."
                      "Give Centoria her task after you're done with Candy.":
                           z "..."
                   pause(1)
                   scene v14305 with Dissolve(1)
                   z "So, Candy..."
                   z "What shall I do with you..."
                   show v14m7 with Dissolve(1)
                   $ renpy.pause(6.2, hard=True)

                   #Touches her waist.
                   #Slides his hand up her body.

                   #Horny counter, if she reaches the maximum she cums.
                   #Buttons on the render placed on her body:
                   #    Make out with her. +3 horny per section
                   #    Lift her from her neck chokeholding her. +4 horny
                   #    Play with her boobs. +2 horny
                   #    Tickle her (She's not ticklish!!!) +0 horny
                   #    Finger her. +7 horny per section
                   #    Spank her. +5 horny per spank
                   label ch14_menu_cndy:
                      show v14m8 with Dissolve(1)
                      pause(1)
                      if cndy_hrny_cntr_ch14 >= 100:
                           show Horny_position Text("{color=#fc0303}Horny%=[cndy_hrny_cntr_ch14]{/color}", size=50)
                      elif cndy_hrny_cntr_ch14 >= 90:
                           show Horny_position Text("{color=#fc0352}Horny%=[cndy_hrny_cntr_ch14]{/color}", size=50)
                      else:
                           show Horny_position Text("{color=#ffdbe7}Horny%=[cndy_hrny_cntr_ch14]{/color}", size=50)
                      show screen ch14_btn_tickle_cndy
                      show screen ch14_btn_finger_cndy
                      show screen ch14_btn_spank_cndy
                      show screen ch14_btn_kiss_cndy
                      show screen ch14_btn_choke_cndy
                      show screen ch14_btn_boobs_cndy
                      if cnt_helping_edge_cndy >= 1:
                           show screen ch14_btn_cntxcndy
                      call screen ch14_btn_stop_cndy

                   label ch14_tickle_cndy:
                      call hide_all_ch14 from _call_hide_all_ch14
                      #Not ticklish
                      pause(1)
                      scene v14329 with Dissolve(1)
                      cndy "..."
                      scene v14330 with Dissolve(1)
                      z "Hehehe..."
                      scene v14331 with Dissolve(1)
                      z "Still acting tough?"
                      show v14m10 with dissolve
                      $ renpy.pause(3, hard=True)
                      scene v14332 with dissolve
                      cndy "..."
                      scene v14333 with dissolve
                      z "..."
                      pause(1)
                      hide v14m8
                      jump ch14_menu_cndy
                   label ch14_finger_cndy:
                      call hide_all_ch14 from _call_hide_all_ch14_1
                      #Per section + 10
                      pause(1)
                      scene v14334 with Dissolve(1)
                      cndy "..."
                      scene v14335 with dissolve
                      z "You know... When it comes to things like this... I believe in a simple approach."
                      scene v14336 with dissolve
                      cndy "Ahhh~..."
                      scene v14337 with dissolve
                      z "This is objectively the best spot for me to work here, isn't it?"
                      play audio "audio/creak.mp3"
                      scene v14338 with dissolve
                      cndy "Ahhhnnn~..."
                      show v14m11 with dissolve
                      pause(1)
                      show screen ch14_btn_finger_cndy_stop
                      cndy "Ahhh~... Hahh~..."
                      cndy "Hnnn~... Ahh~..."
                      cndy "You... Ahhh~... Ahhhhhh~..."
                      $ cndy_hrny_cntr_ch14 += 10
                      pause(1)
                      if cndy_hrny_cntr_ch14 >= 100:
                           hide screen ch14_btn_finger_cndy_stop
                           scene v14371
                           play audio "audio/creak.mp3"
                           with vpunch
                           cndy "Annnhhhh~!" (multiple=2)
                           z "?!" (multiple=2)
                           if came_from_gallery == 0:
                               $ cndy_lst += 3
                           show screen button_lst with dissolve
                           play sound "audio/stats.wav"
                           hide screen button_lst with dissolve
                           $ cndy_hrny_cntr_ch14 = 0
                           $ edged_cndy = 0
                           pause(1)
                           jump ch14_after_edging_cndy
                      cndy "Gods... This is... Ahhh~..."
                      cndy "[mc_name]... Ahhh~... You..."
                      cndy "Ahhh~... If you keep hitting this spot..."
                      $ cndy_hrny_cntr_ch14 += 10
                      pause(1)
                      if cndy_hrny_cntr_ch14 >= 100:
                           hide screen ch14_btn_finger_cndy_stop
                           scene v14371
                           play audio "audio/creak.mp3"
                           with vpunch
                           cndy "Annnhhhh~!" (multiple=2)
                           z "?!" (multiple=2)
                           if came_from_gallery == 0:
                               $ cndy_lst += 3
                           show screen button_lst with dissolve
                           play sound "audio/stats.wav"
                           hide screen button_lst with dissolve
                           $ cndy_hrny_cntr_ch14 = 0
                           $ edged_cndy = 0
                           pause(1)
                           jump ch14_after_edging_cndy
                      cndy "Ahhhn~..."
                      cndy "Mmmmmnn~..."
                      cndy "Ohhh~... Your fingers are way bigger than mine..."
                      $ cndy_hrny_cntr_ch14 += 10
                      pause(1)
                      if cndy_hrny_cntr_ch14 >= 100:
                           hide screen ch14_btn_finger_cndy_stop
                           scene v14371
                           play audio "audio/creak.mp3"
                           with vpunch
                           cndy "Annnhhhh~!" (multiple=2)
                           z "?!" (multiple=2)
                           if came_from_gallery == 0:
                               $ cndy_lst += 3
                           show screen button_lst with dissolve
                           play sound "audio/stats.wav"
                           hide screen button_lst with dissolve
                           $ cndy_hrny_cntr_ch14 = 0
                           $ edged_cndy = 0
                           pause(1)
                           jump ch14_after_edging_cndy
                      cndy "Hnnnn~... This is nothing like when I..."
                      cndy "Mmn~... When I do it myself..."
                      cndy "Ahhhhhh~... Ahhhn~..."
                      $ cndy_hrny_cntr_ch14 += 10
                      pause(1)
                      if cndy_hrny_cntr_ch14 >= 100:
                           hide screen ch14_btn_finger_cndy_stop
                           scene v14371
                           play audio "audio/creak.mp3"
                           with vpunch
                           cndy "Annnhhhh~!" (multiple=2)
                           z "?!" (multiple=2)
                           if came_from_gallery == 0:
                               $ cndy_lst += 3
                           show screen button_lst with dissolve
                           play sound "audio/stats.wav"
                           hide screen button_lst with dissolve
                           $ cndy_hrny_cntr_ch14 = 0
                           $ edged_cndy = 0
                           pause(1)
                           jump ch14_after_edging_cndy
                      label stopped_fingering_ch14:
                           hide screen ch14_btn_finger_cndy_stop
                      z "(Let's not push it too much... I might make her cum if I keep this up...)"
                      scene v14337 with Dissolve(1)
                      pause(1)
                      hide v14m8
                      jump ch14_menu_cndy

                   label ch14_spank_cndy:
                      call hide_all_ch14 from _call_hide_all_ch14_2
                      #Per spank + 15
                      pause(1)
                      scene v14339 with Dissolve(1)
                      cndy "..."
                      scene v14340 with dissolve
                      z "Bend over leaning on the wall, will you?"
                      scene v14339 with dissolve
                      cndy "..."
                      pause(1)
                      scene v14341 with Dissolve(1)
                      label idle_spank_cndy:
                      pause(1)
                      if cndy_hrny_cntr_ch14 >= 100:
                           scene v14372
                           play sound "audio/creak.mp3"
                           with vpunch
                           cndy "Annnhhhh~!" (multiple=2)
                           z "?!" (multiple=2)
                           if came_from_gallery == 0:
                               $ cndy_lst += 3
                           show screen button_lst with dissolve
                           play sound "audio/stats.wav"
                           hide screen button_lst with dissolve
                           $ cndy_hrny_cntr_ch14 = 0
                           $ edged_cndy = 0
                           pause(1)
                           jump ch14_after_edging_cndy
                      else:
                           if times_spanked_cndy_ch14 <= 3:
                               show v14m12 with Dissolve(1)
                           else:
                               show v14m14 with Dissolve(1)
                           pause(1)
                           hide v14m13
                           hide v14m15
                           show screen ch14_btn_spank_cndy2
                           call screen ch14_btn_spank_cndy_stop
                           call hide_all_ch14 from _call_hide_all_ch14_3
                           pause(1)
                           if times_spanked_cndy_ch14 <= 3:
                               scene v14343 with Dissolve(1)
                           else:
                               scene v14342 with Dissolve(1)
                           pause(1)
                           scene v14344 with Dissolve(1)
                           cndy "Hmmm~..."
                           pause(1)
                           hide v14m8
                           jump ch14_menu_cndy

                   label ch14_kiss_cndy:
                      call hide_all_ch14 from _call_hide_all_ch14_4
                      pause(1)
                      scene v14306 with Dissolve(1)
                      cndy "..."
                      scene v14307 with Dissolve(1)
                      cndy "Ah..."
                      play audio "audio/kiss.mp3"
                      scene v14308 with Dissolve(1)
                      cndy "Hmmm!"
                      scene v14309 with Dissolve(1)
                      cndy "Mmm~..."
                      scene v14310 with Dissolve(1)
                      cndy "Annhh~..."
                      scene v14311 with Dissolve(1)
                      cndy "Hanhhh~..."
                      play audio "audio/kiss.mp3"
                      scene v14312 with Dissolve(1)
                      cndy "Mffhhhmmm~..."
                      scene v14313 with Dissolve(1)
                      $ cndy_hrny_cntr_ch14 += 10
                      cndy "Mmmmmmm~..."
                      if cndy_hrny_cntr_ch14 >= 100:
                           scene v14368
                           play sound "audio/creak.mp3"
                           with vpunch
                           cndy "Annnhhhh~!" (multiple=2)
                           z "?!" (multiple=2)
                           if came_from_gallery == 0:
                               $ cndy_lst += 3
                           show screen button_lst with dissolve
                           play sound "audio/stats.wav"
                           hide screen button_lst with dissolve
                           $ cndy_hrny_cntr_ch14 = 0
                           $ edged_cndy = 0
                           pause(1)
                           jump ch14_after_edging_cndy
                      else:
                           scene v14314 with Dissolve(1)
                           cndy "Hanhhh~..."
                           scene v14315 with Dissolve(1)
                           cndy "..."
                           pause(1)
                           hide v14m8
                           jump ch14_menu_cndy

                   label ch14_choke_cndy:
                      call hide_all_ch14 from _call_hide_all_ch14_5
                      pause(1)
                      scene v14316 with Dissolve(1)
                      cndy "..."
                      play sound "audio/creak.mp3"
                      scene v14317 with Dissolve(1)
                      cndy "Ughhh..."
                      scene v14318 with Dissolve(1)
                      cndy "Hagghhhh..."
                      scene v14319 with Dissolve(1)
                      cndy "Guhhhggkkkk!"
                      scene v14320 with Dissolve(1)
                      cndy "Hunggghhhh~..."
                      scene v14321 with Dissolve(1)
                      $ cndy_hrny_cntr_ch14 += 15
                      cndy "Nugghhhh~..."
                      if cndy_hrny_cntr_ch14 >= 100:
                           scene v14369
                           play sound "audio/creak.mp3"
                           with vpunch
                           cndy "Annnhhhh~!" (multiple=2)
                           z "?!" (multiple=2)
                           if came_from_gallery == 0:
                               $ cndy_lst += 3
                           show screen button_lst with dissolve
                           play sound "audio/stats.wav"
                           hide screen button_lst with dissolve
                           $ cndy_hrny_cntr_ch14 = 0
                           $ edged_cndy = 0
                           pause(1)
                           jump ch14_after_edging_cndy
                      else:
                           play sound "audio/Cloth_rustle.wav"
                           scene v14322 with Dissolve(1)
                           cndy "..."
                           z "..."
                           scene v14323
                           play sound "audio/Falling2.mp3"
                           with vpunch
                           cndy "Ahhhh~..."
                           scene v14324 with Dissolve(1)
                           z "Are you okay down there?"
                           cndy "Ahhh~... Yeshhh~..."
                           pause(1)
                           hide v14m8
                           jump ch14_menu_cndy

                   label ch14_boobs_cndy:
                      call hide_all_ch14 from _call_hide_all_ch14_6
                      $ cndy_hrny_cntr_ch14 += 7
                      pause(1)
                      scene v14325 with Dissolve(1)
                      cndy "..."
                      scene v14326 with Dissolve(1)
                      cndy "..."
                      show v14m9 with Dissolve(1)
                      pause(1)
                      cndy "Ahhh~..."
                      cndy "Hnn~..."
                      cndy "Hahhhh~... Ahhnn~..."
                      cndy "Hmm~..."
                      cndy "Nhhh~..."
                      cndy "Ahhhhh~... Ahhhhhhh~..."
                      cndy "Hnnnn~... Mnnnhh~..."
                      pause(1)
                      if cndy_hrny_cntr_ch14 >= 100:
                           scene v14370
                           play sound "audio/creak.mp3"
                           with vpunch
                           cndy "Annnhhhh~!" (multiple=2)
                           z "?!" (multiple=2)
                           if came_from_gallery == 0:
                               $ cndy_lst += 3
                           show screen button_lst with dissolve
                           play sound "audio/stats.wav"
                           hide screen button_lst with dissolve
                           $ cndy_hrny_cntr_ch14 = 0
                           $ edged_cndy = 0
                           pause(1)
                           jump ch14_after_edging_cndy
                      else:
                           scene v14327 with Dissolve(1)
                           z "Okay, that's enough. Don't want to overdo it now, do we?"
                           scene v14328 with Dissolve(1)
                           pause(1)
                           hide v14m8
                           jump ch14_menu_cndy

                   label ch14_cntxcndy:
                      call hide_all_ch14 from _call_hide_all_ch14_7
                      $ cndy_hrny_cntr_ch14 += 8
                      pause(1)
#                      Centoria make out is a side button. +9 horny per section (She can't cum from this)
                      scene v14345 with Dissolve(1)
                      z "Centoria."
                      cnt "Hm?"
                      z "Do you know how to kiss?"
                      scene v14346 with dissolve
                      cnt "How to kiss?"
                      cnt "I..."
                      scene v14347 with dissolve
                      cnt "Well, the princess and I practiced it a few times..."
                      scene v14348 with dissolve
                      z "Wait what?!"
                      scene v14346 with dissolve
                      cnt "What?"
                      scene v14345 with dissolve
                      z "..."
                      z "Verrry interesting..."
                      z "Well, in that case..."
                      z "I want you to kiss Candy."
                      scene v14348 with dissolve
                      cnt "..."
                      scene v14350 with dissolve
                      cnt "C-Candy?"
                      scene v14349 with dissolve
                      z "Yup. Easy enough, right?"
                      cnt "..."
                      scene v14348 with dissolve
                      cnt "O-Oka-"
                      scene v14349 with dissolve
                      z "Aggressively."
                      z "Passionately."
                      cnt "..." #Blushes.
                      z "Can you do that?"
                      scene v14350 with dissolve
                      cnt "I..."
                      cnt "I can..."
                      scene v14349 with dissolve
                      z "Show me."
                      cnt "..."
                      pause(1)
                      #Gets close to candy.
                      scene v14351 with Dissolve(1)
                      cnt "..." (multiple=2)
                      cndy "..." (multiple=2) #Both blushing af
                      scene v14352 with dissolve
                      cnt "Do you know how to kiss?"
                      scene v14351 with dissolve
                      cndy "..."
                      scene v14353 with dissolve
                      cndy "A bit..."
                      scene v14354 with Dissolve(1)
                      cnt "Well... I'll guide you, okay?"
                      scene v14355 with dissolve
                      cnt "Let's start with something simple at first, okay?"
                      scene v14356 with dissolve
                      cndy "Okay..."
                      scene v14355 with dissolve
                      cnt "Close your eyes..."
                      scene v14357 with dissolve
                      cndy "..." #Closes her eyes and her mouth is in a kiss position.
                      scene v14358 with Dissolve(1)
                      pause(1)
                      play audio "audio/kiss.mp3"
                      scene v14359 with Dissolve(1)
                      cnt "Hmm..." #Kisses her.
                      pause(2)
                      scene v14360 with Dissolve(1)
                      cnt "..." #Breaks the kiss.
                      scene v14361 with Dissolve(1)
                      cndy "..."
                      #cnt Takes Candy's hand.
                      scene v14362 with Dissolve(1)
                      cnt "Hmmm~..." (multiple=2) #Kisses her again.
                      cndy "Nmmm~..." (multiple=2)
                      play audio "audio/kiss.mp3"
                      scene v14363 with Dissolve(1)
                      cndy "Hmmmm~..." (multiple=2)
                      cnt "Mmmmm~..." (multiple=2)
                      #They start making out.
                      scene v14364 with Dissolve(1)
                      cndy "Ahhhnn~..."
                      play sound "audio/Cloth_rustle.wav"
                      scene v14365 with Dissolve(1)
                      cnt "Okay... That's enough..."
                      scene v14366 with dissolve
                      cndy "..."
                      scene v14367 with dissolve
                      pause(1.5)
                      hide v14m8
                      jump ch14_menu_cndy

                   #At 20 hornyness: Candy begs Z to put it inside her.
                   #At 30 hornyness: Candy cums.
                   #At 27+ hornyness: Candy change counter colour Z can stop and win.

                   #If Z wins, Torr rewards him by having sex with him in front of Candy in the next round.
                   #If he loses, Torr Does something else.
                   label gave_up_ch14:
                      if cndy_hrny_cntr_ch14 < 90:
                           $ gave_up_edging_cndy = 1

                   label ch14_after_edging_cndy:
                      $ dummy += 1
                      call hide_all_ch14 from _call_hide_all_ch14_8
                      if gave_up_edging_cndy == 1:
                           scene black with Dissolve(1)
                           z "(I think I failed at totally edging her...)"
                           pause(1)
                      else:
                           if cndy_hrny_cntr_ch14 >= 90:
                               $ edged_cndy = 1
                               scene black with Dissolve(1)
                               z "(I think I edged her quite well...)"
                               if came_from_gallery == 0:
                                   $ cndy_lst += 5
                               show screen button_lst with dissolve
                               play sound "audio/stats.wav"
                               hide screen button_lst with dissolve
                               pause(1)
                           else:
                               play sound "audio/Falling2.mp3"
                               scene v14374
                               with vpunch
                               z "Are you okay, there?"
                               scene v14373 with dissolve
                               cndy "Yeah... I guess I came a little too hard..."
                               scene v14374 with dissolve
                               z "..."
                               z "(I guess I failed at edging her...)"
                               pause(1)
                   if cnt_helping_edge_cndy == 0:
                      scene v14345 with Dissolve(1)
                      z "Now, Centoria..."
                      z "(Let's not push her too much, I don't think she's ready for something like sex just yet...)"
                      menu:
                           "Tell Centoria to kiss you.":
                               z "Do you know how to kiss?"
                               scene v14346 with dissolve
                               cnt "How to kiss?"
                               cnt "I..."
                               scene v14347 with dissolve
                               cnt "Well, the princess and I practiced it a few times..."
                               scene v14348 with dissolve
                               z "Wait what?!"
                               scene v14346 with dissolve
                               cnt "What?"
                               scene v14345 with dissolve
                               z "..."
                               z "Verrry interesting..."
                               z "Well, in that case..."
                               z "I want you to kiss me."
                               scene v14348 with dissolve
                               cnt "..."
                               scene v14350 with dissolve
                               cnt "O-Okay..."
                               cnt "Do you know how to kiss?"
                               scene v14349 with dissolve
                               z "I've done it a couple of times."
                               scene v14375 with Dissolve(1)
                               #Comes closer to him.
                               z "..."
                               scene v14376 with dissolve
                               cnt "D-Do you want to..."
                               cnt "Y-You know..."
                               scene v14377 with Dissolve(1)
                               cnt "..."
                               #Holds her hands.
                               scene v14378 with dissolve
                               z "Relax..."
                               scene v14379 with dissolve
                               cnt "..."
                               scene v14380 with dissolve
                               cnt "Yeah..."
                               #He kisses her slowly.
                               scene v14381 with Dissolve(1)
                               pause(1)
                               scene v14382 with Dissolve(1)
                               pause(1)
                               scene v14383 with Dissolve(1)
                               pause(1)
                               play audio "audio/kiss.mp3"
                               scene v14384 with Dissolve(1)
                               cnt "Hmm..."
                               scene v14385 with Dissolve(1)
                               #They go back for another kiss.
                               cnt "Mmmm~..."
                               play audio "audio/kiss.mp3"
                               scene v14386 with Dissolve(1)
                               cnt "Mnnnn~..."
                               #Candy and Torr are watching.
                               scene v14387 with Dissolve(1)
                               pause(2)
                               scene v14388 with Dissolve(1)
                               cndy "They're really going at it, huh..."
                               scene v14389 with dissolve
                               tr "..."
                               scene v14390 with Dissolve(1)
                               cnt "Hanh~..." #The kiss breaks.
                               scene v14391 with dissolve
                               z "That was nice..."
                               scene v14392 with dissolve
                               cnt "It was..." #Smiles shyly...
                               if came_from_gallery == 0:
                                   $ cnt_lst += 3
                               show screen button_lst with dissolve
                               play sound "audio/stats.wav"
                               hide screen button_lst with dissolve
                               scene v14393 with dissolve
                               pause(1)
                           "Tell Centoria to strip for you.":
                               z "I want you to take off your clothes."
                               scene v14346 with dissolve
                               cnt "All of it?"
                               scene v14345 with dissolve
                               z "Yeah."
                               cnt "..."
                               scene v14347 with dissolve
                               cnt "I guess the other two have done it already, so..."
                               scene v14345 with dissolve
                               cnt "..."
                               #Strips.
                               scene v14394 with Dissolve(1)
                               pause(1.5)
                               play audio "audio/cloth.mp3"
                               scene v14395 with Dissolve(1)
                               pause(1.5)
                               scene v14396 with Dissolve(1)
                               pause(1.5)
                               play sound "audio/Zip.mp3"
                               scene v14397 with Dissolve(1)
                               pause(1.5)
                               play sound "audio/Cloth_rustle.wav"
                               scene v14398 with Dissolve(1)
                               pause(1.5)
                               scene v14399 with Dissolve(1)
                               pause(1.5)
                               z "..."
                               z "Damn..."
                               scene v14400 with Dissolve(1)
                               z "You really have a great figure, Centoria..."
                               scene v14401 with dissolve
                               cnt "Thank y-you..."
                               if came_from_gallery == 0:
                                   $ cnt_lst += 3
                               show screen button_lst with dissolve
                               play sound "audio/stats.wav"
                               hide screen button_lst with dissolve
                               scene v14402 with dissolve
                               cnt "?!"
                               scene v14403 with Dissolve(1)
                               tr "Hmmm..." #Comes to see her boobs.
                               scene v14404 with dissolve
                               tr "..." #Compares it to hers.
                               scene v14405 with dissolve
                               tr "Next round!"
                               scene v14406 with dissolve
                               z "..."
                               pause(1)
                label round_5_of_r_p_s:
                   scene r_p_s_expln with Dissolve(1)
                   z "Rock..."
                   z "Paper..."
                   z "Scissors!"
                   play sound "audio/whoosh.mp3"
                   scene v14217 with dissolve
                   pause(1)
                   tr "Ahahahahahah! I win again!"
                   if edged_cndy == 1:  #if Z was able to edge candy.
                      scene v14407 with Dissolve(1)
                      tr "Hehehehe..." #Evil smile.
                      play sound "audio/sliding door.mp3"
                      scene v14408 with dissolve
                      tr "Where is that thing you got from Stephanie..." #Looks in the wardrobe.
                      tr "..."
                      play sound "audio/pick up 2.mp3"
                      scene v14409 with Dissolve(1)
                      tr "There we go!" #Gets a vibrator.
                      play audio "audio/Cloth_rustle.wav"
                      scene v14410 with Dissolve(1)
                      tr "Candy!"
                      tr "Sit on the chair and don't move until I cum."
                      scene v14411 with dissolve
                      tr "I'm also gonna use this on you..."
                      tr "But let's set it to the lowest speed..."
                      scene v14412 with Dissolve(1)
                      cndy "What are you..."
                      scene v14413
                      play sound "audio/falling2.mp3"
                      play audio "audio/creak.mp3"
                      with hpunch
                      tr "Just sit down." (multiple=2) #Pushes her down.
                      cndy "Ahh!" (multiple=2)
                      scene v14414 with dissolve
                      tr "Don't move, okay?"
                      cndy "..."
                      scene v14415 with dissolve
                      tr "Let's see..."
                      play background_s "audio/vibrator_loop (loud).mp3" volume 0.6 fadeout 1.0 fadein 1.0 loop
                      show v14m16 with dissolve
                      pause(1)
                      tr "There we go..."
                      cndy "..."
                      pause(1)
                      #Gets the vibrator to work.
                      play background_s "audio/vibrator_loop (loud).mp3" volume 0.3 fadeout 1.0 fadein 1.0 loop
                      scene v14416 with Dissolve(1)
                      cndy "Ahhh~..." #Places it.
                      show v14m17 with Dissolve(1)
                      pause(1)
                      cndy "Wait... This it too slow..."
                      cndy "Hnnn~... Ahh~..."
                      cndy "At least turn it up a bit..."
                      cndy "Hnnn~..."
                      cndy "Torr..."
                      cndy "Ahhhh~... I'll get you for this..."
                      tr "Yeah, yeah. We'll see about that."
                      pause(1)
                      scene v14417 with Dissolve(1)
                      tr "Now..."
                      tr "[mc_name]..."
                      tr "I want you to fuck me..."
                      scene v14418 with dissolve
                      z "..."
                      z "That was very straight forwar-"
                      scene v14419 with dissolve
                      tr "In front of Candy while she can only watch."
                      scene v14420 with Dissolve(1)
                      tr "The vibrator is too weak to make her cum too..."
                      scene v14421 with dissolve
                      z "..."
                      play sound "audio/Cloth_rustle.wav"
                      scene v14422 with Dissolve(1)
                      tr "Take me now..."
                      scene v14423 with dissolve
                      z "..."
                      scene v14424 with dissolve
                      z "Don't mind if I do."
                      cnt "..." #Shocked.
                      scene v14425 with dissolve
                      tr "Come on... Put it ins-"
                      show v14m18 with dissolve
                      $ renpy.pause(0.8, hard=True)
                      play sound "audio/creak.mp3"
                      stop background_s
                      tr "Ohhhh~!{w=1}{nw}" with hpunch
                      scene v14426 with dissolve
                      pause(1)
                      play background_s "audio/vibrator_loop (loud).mp3" volume 0.3 fadeout 1.0 fadein 1.0 loop
                      show v14m19 with Dissolve(1)
                      tr "Fuck~... I missed this..."
                      cndy "..."
                      tr "Ahhh~... It feels so fucking good, you know..."
                      cndy "Hahh~..."
                      tr "Ahhh~... I..."
                      tr "Fucccckkkk~... I think I'm getting close already..."
                      cndy "Hmmm~..."
                      tr "It's hitting all the good spots..."
                      cndy "Ahhh~..."
                      cnt "..." #Covering her eyes.
                      cndy "Come on... Just... Ahhh~... Make it vibrate faster... Just a bit faster..."
                      tr "No..."
                      tr "Ahhh~... Fuhckkk~..."
                      cndy "Please..."
                      z "(Torr is just being mean here...)"
                      tr "Oh gods... I'm~... Ahhhh~..."
                      tr "I'm gonna cum already..."
                      cndy "Nhhhnn~... I wanna cum to..."
                      z "Wait... I'm still not quite there yet..."
                      tr "Too late~... Ahhh~..."
                      scene v14427
                      play sound "audio/creak.mp3"
                      stop background_s
                      with hpunch
                      tr "Ohhh~... Ahhhh~..." #Cums.
                      scene v14428 with Dissolve(1)
                      cndy "..." (multiple=2)
                      tr "..." (multiple=2)
                      if came_from_gallery == 0:
                          $ tr_lst += 6
                          $ cndy_lst += 2
                      show screen button_lst with dissolve
                      play sound "audio/stats.wav"
                      hide screen button_lst with dissolve
                      pause(1)
                      #Collapses.
                   else:
                      scene v14429 with Dissolve(1)
                      tr "[mc_name] and Candy..."
                      tr "I want you two to go outside. You can't go back for five minutes."
                      scene v14430 with dissolve
                      tr "Oh, and you will be naked."
                      scene v14431 with dissolve
                      pause(1)
                      scene v14432 with Dissolve(1)
                      z "..." (multiple=2)
                      cndy "..." (multiple=2) #Both annoyed.
                      pause(1)
                      play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
                      scene v14433 with Dissolve(1)
                      #Outside.
                      z "..."
                      scene v14434 with Dissolve(1)
                      z "This fucking girl gets really imaginative sometimes, doesn't she..."
                      scene v14435 with dissolve
                      cndy "Yeah..."
                      scene v14436 with Dissolve(1)
                      cndy "..." #Shy.
                      z "Don't worry... I don't think anyone is gonna pass through here... And if they do, we can just hide..."
                      cndy "..."
                      show v14m20 with Dissolve(1)
                      pause(1)
                      #Looks horny af
                      z "..."
                      z "(Is she...)"
                      z "(Is she horny right now?)"
                      z "..."
                      z "(Right... Knowing her... This girl is probably kinda into being humiliated like that...)"
                      z "(And the last challenge is probably not helping...)"
                      z "..."
                      pause(1)
                      menu:
                           "Just wait out the five minutes.":
                               scene v14438 with Dissolve(1)
                               z "(It's probably a bad idea to try anything while we're out here...)"
                           "Get closer to Candy.":
                               pause(1)
                               #Gets closer.
                               scene v14439 with Dissolve(1)
                               cndy "!!!" #His dick is rubbing against her
                               scene v14440 with dissolve
                               z "Candy..."
                               scene v14441 with dissolve
                               cndy "Hm..."
                               scene v14440 with dissolve
                               z "You're horny, aren't you?"
                               scene v14441 with dissolve
                               cndy "..."
                               scene v14442 with dissolve
                               cndy "N-Nooooo..."
                               scene v14443 with dissolve
                               z "You're really bad at lying..."
                               scene v14444 with dissolve
                               cndy "..."
                               scene v14445 with dissolve
                               z "Let me just..."
                               play sound "audio/Falling2.mp3"
                               scene v14446 with hpunch
                               cndy "Mnnnn~..."
                               scene v14447 with Dissolve(1)
                               z "..."
                               scene v14448 with dissolve
                               cndy "Hmmm~..."
                               scene v14449 with dissolve
                               cndy "Ohhh~... Gods..."
                               scene v14450 with dissolve
                               cndy "MMNNN~!"
                               scene v14451 with dissolve
                               cndy "Mmmmmmnnn~..."
                               scene v14453 with Dissolve(1)
                               z "Damn... You're wet as fuck."
                               scene v14452 with dissolve
                               cndy "I can't help it, okay?"
                               scene v14453 with dissolve
                               z "I'm not complaining here..."
                               #Starts touching her.
                               scene v14454 with dissolve
                               cndy "Wait... What if..."
                               cndy "What if someone sees us..."
                               scene v14456 with Dissolve(1)
                               z "We'll just run for it..."
                               scene v14457 with Dissolve(1)
                               cndy "Hmmm~... Kinda..."
                               scene v14458 with dissolve
                               cndy "It's kinda exciting doing this... Ahhh~..."
                               scene v14459 with dissolve
                               z "Heh... Candy you're full of these kinky fantasies, aren't you?"
                               cndy "Ahhh~... I'm not... Hahhhh~..."
                               play sound "audio/Falling2.mp3"
                               scene v14460 with vpunch
                               cndy "!?"
                               scene v14462 with dissolve
                               cndy "[mc_name]..."
                               cndy "I..."
                               cndy "Can you..."
                               cndy "Can you put it inside for a bit..."
                               scene v14461 with dissolve
                               z "Thought you'd never ask..."
                               z "Sure that's the best idea, though?"
                               z "It'd be really difficult to run for it if someone comes through here."
                               scene v14462 with dissolve
                               cndy "I don't..."
                               cndy "I don't really care right now..."
                               cndy "I just want you inside me... Please..."
                               scene v14463 with dissolve
                               z "..."
                               scene v14462 with dissolve
                               cndy "Please... I want your dick to distroy me right here and now..."
                               cndy "Fuck me like a cheap whore in front of everyone..."
                               cndy "They might as well know me for the hopeluss little slut I am..."
                               scene v14461 with dissolve
                               z "Fuck..."
                               #Gets ready to put it inside.
                               z "You know you can't expect me to hold back when you ask like that, you little minx..."
                               scene v14462 with dissolve
                               cndy "Do it..."
                               play sound "audio/Cloth_rustle.wav"
                               scene v14464 with Dissolve(1)
                               pause(1)
                               #Is about to put it inside.
                               stfny "Mom! Have you seen my belt?"
                               scene v14465
                               play sound "audio/RecordScratch (thanks senpai).ogg"
                               stop music
                               with vpunch
                               z "?!" (multiple=2)
                               cndy "!!!" (multiple=2)
                               pause(1)
                               scene v14466 with Dissolve(1)
                               stfny "..."
                               scene v14467 with dissolve
                               stfny "Mom?"
                               scene v14468 with dissolve
                               stfny "{size=-10}Mom!{/size}"
                               pause(1)
                               scene v14469 with Dissolve(1)
                               hlna "What's wrong?"
                               scene v14471 with Dissolve(1)
                               stfny "My belt... I can't find it."
                               scene v14470 with dissolve
                               hlna "Did you look in your room?"
                               show v14m21 with Dissolve(1)
                               cndy "Hmmm~..."
                               z "{size=-10}Keep it down...{/size}"
                               hlna "Well, if it's not there, I can't see where else it could be, honey."
                               stfny "Your room, maybe?"
                               cndy "Mnn~..."
                               hlna "What? Why would it be in my room?"
                               stfny "You sometimes wash my clothes, right?"
                               hlna "Yeah? But I haven't touched your belt."
                               cndy "Ahhhmm~... Hmmm~..."
                               z "{size=-10}We're totally gonna get caught if you keep moaning like this.{/size}"
                               stfny "I always find the most random things in your room, though."
                               scene v14470 with Dissolve(1)
                               hlna "Well, you can go look there if it makes you happy."
                               play sound "audio/creak.mp3"
                               scene v14472 with dissolve
                               cndy "Hmmmmm~..."
                               scene v14473 with Dissolve(1)
                               z "..."
                               scene v14474 with Dissolve(1)
                               cndy "[mc_name]... I can't keep my voice down..." (multiple=2)
                               stfny "{size=-10}See? There's probably even rats or something in there!{/size}" (multiple=2)
                               scene v14475 with dissolve
                               cndy "Maybe we should sneak back? They're gonna catch us if we keep going..." (multiple=2)
                               hlna "{size=-10}I haven't seen a single rat in the village in years, Stephanie.{/size}" (multiple=2)
                               scene v14476 with dissolve
                               cndy "Or maybe we can just go find another spot... I kinda still wanna keep going..." (multiple=2)
                               stfny "{size=-10}Racoons then?{/size}" (multiple=2)
                               play sound "audio/Cloth_rustle.wav"
                               scene v14477 with dissolve
                               cndy "Maybe we cou-" (multiple=2)
                               hlna "{size=-10}No, honey. We don't have those either.{/size}" (multiple=2)
                               scene v14478
                               play audio "audio/cloth.mp3"
                               with vpunch
                               cndy "Hmmmm?!"
                               play music "audio/Calm s02.mp3" volume 0.15 fadeout 1.0 fadein 1.0 loop
                               scene v14479 with dissolve
                               cndy "..."
                               pause(1)
                               show v14m22 with Dissolve(0.8)
                               $ renpy.pause(2, hard=True)
                               cndy "HMM~!!!{w=2}{nw}"
                               scene v14480 with dissolve
                               pause(1)
                               show v14m23 with Dissolve(1)
                               pause(1)
                               cndy "Hmmmmnn~... Nnmmmm~..."
                               hlna "{size=-10}No, if you use that it'll ruin the colour of your clothes.{/size}"
                               cndy "Mnnnn~... Ahhhmmmm~..."
                               stfny "{size=-10}No, no. Venus said to put three drops of it into a full bucket of water.{/size}"
                               cndy "Mnnn~... Mmmmm~... Mnnnnn~..."
                               hlna "{size=-10}Only if you're washing white clothes.{/size}"
                               hlna "{size=-10}You should certainly use it for white clothes actually.{/size}"
                               cndy "Hanhhh~... Hmmm~..."
                               stfny "{size=-10}No... The one Gabbie makes is for white stuff. Venus's potion is for washing coloured clothes, mom.{/size}"
                               hlna "{size=-10}Nope. Gabbie's is for removing oil spots, honey. And you should put it on your clothes before you wash them.{/size}"
                               cndy "Ahhmmm~... Hmmm~..."
                               z "(I guess they're too busy talking about washing clothes to come this way.)"
                               cndy "Ahhh~... Mnnn~..."
                               z "(Sorry, Steph. Looks like you're gonna have to wash your belt again. It's now full of Candy's drool.)"
                               cndy "Ahhhnnn~... Hnnn~... Mnnn~..."
                               z "(Fuck... I'm close...)"
                               cndy "Hmmmnnn~... I'mmmm~... Mmhhhmmm~..."
                               cndy "Cummmmnnn~... I'mmnnn~... Cummmnnn~..."
                               z "(Me too... Fuck...)"
                               pause(1)
                               scene v14482
                               play audio "audio/creak.mp3"
                               play sound "audio/magic 7.mp3"
                               stop music fadeout 1.0
                               with hpunch
                               cndy "Ahhhhnn~..." (multiple=2)
                               z "Ughh...~" (multiple=2)
                               scene v14483 with Dissolve(1)
                               z "..."
                               if came_from_gallery == 0:
                                   $ cndy_lst += 7
                               show screen button_lst with dissolve
                               play sound "audio/stats.wav"
                               hide screen button_lst with dissolve
                               scene v14484 with Dissolve(1)
                               stfny "Tell me this wasn't a fucking racoon!"
                               play audio "audio/creak.mp3"
                               scene v14485 with Dissolve(1)
                               stfny "..."
                               scene v14486 with dissolve
                               stfny "Hm?"
                               scene v14487 with Dissolve(1)
                               stfny "It's my belt! It was totally in your room!"
                               scene v14488 with dissolve
                               stfny "But there's something poured all over it!"
                               scene v14489 with Dissolve(1)
                               stfny "Moooom! What did you do to my belt!"
                               play sound "audio/whoosh.mp3"
                               scene v14490 with dissolve
                               hlna "?"
                               pause(1)
                               scene black with Dissolve(1)
                               stop background_s fadeout 1.0
                               stop background_s2 fadeout 1.0
                               stop music fadeout 1.0
                               stop sound fadeout 1.0
                               pause(1)
                               play music "audio/Calm s02.mp3" volume 0.15 fadeout 1.0 fadein 1.0 loop
                               scene v14491 with Dissolve(1)
                               tr "The fuck have you two been doing?"
                               scene v14492 with dissolve
                               z "..."
                               scene v14493 with Dissolve(1)
                               tr "And what the fuck happened to her?"
                               scene v14494 with dissolve
                               z "Nothing... We just lost track of time..."
                               z "And Candy sprained her ankle so she couldn't walk and I offered to carry her."
                               scene v14492 with Dissolve(1)
                               tr "..."
                   scene black with Dissolve(1)
                   pause(1)
                   #Fade out a bit.
                   #Z tells Centoria to do something:
                   scene v14495 with Dissolve(1)
                   z "Okay, Centoria..."
                   z "What shall I make you do..."
                   z "(I can either push her a bit more now, or just back it up a bit...)"
                   pause(1)
                   menu:
                      "Ask to play with her ears.":
                           z "So..."
                           z "Can I touch your ears?"
                           scene v14498 with dissolve
                           cnt "My ears?"
                           scene v14499 with dissolve
                           z "Yeah?"
                           scene v14500 with dissolve
                           cnt "I mean..."
                           cnt "Sure."
                           scene v14501 with dissolve
                           z "Okay... I'll come closer..."
                           play audio "audio/Cloth_rustle.wav"
                           scene v14502 with Dissolve(1)
                           cnt "!"
                           scene v14503 with dissolve
                           cnt "..."
                           scene v14504 with dissolve
                           cnt "Eh..."
                           scene v14505 with dissolve
                           cnt "Ahh~..."
                           scene v14506 with dissolve
                           cnt "Ahhhaahnn~..."
                           scene v14507 with dissolve
                           cnt "Hmmm~..."
                           scene v14508 with dissolve
                           cnt "Ahh~..."
                           scene v14509 with dissolve
                           cnt "Ohh~... Ohhhhh~..."
                           scene v14510 with dissolve
                           cnt "Hannhhh~..."
                           scene v14511 with dissolve
                           tr "Hey! Elf ears are very sensitive! Don't push it!"
                           scene v14512 with dissolve
                           tr "?!"
                           scene v14513 with Dissolve(1)
                           tr "Ahhh~..."
                           scene v14514 with dissolve
                           tr "Anhhh~..." (multiple=2)
                           cnt "Ohhh~..." (multiple=2)
                           scene v14515 with dissolve
                           tr "Ahhhhh~..." (multiple=2)
                           cnt "Hanhh~..." (multiple=2)
                           scene v14516 with Dissolve(1)
                           tr "Hahh~..." (multiple=2)
                           cnt "Hnnn~..." (multiple=2)
                           if came_from_gallery == 0:
                               $ tr_lst += 2
                               $ cnt_lst += 2
                           show screen button_lst with dissolve
                           play sound "audio/stats.wav"
                           hide screen button_lst with dissolve
                           scene v14517 with dissolve
                           tr "..." (multiple=2)
                           cnt "..." (multiple=2)
                           scene v14518 with dissolve
                           tr "?!" (multiple=2)
                           cnt "!" (multiple=2)
                           scene v14519 with dissolve
                           tr "..." (multiple=2)
                           cnt "..." (multiple=2)
                           scene v14520 with dissolve
                           tr "Can we have the next round now?"
                           scene v14521 with dissolve
                           z "Sure."
                      "Make her do something sexual.":
                           z "Hmmm... How do I put this..."
                           z "I want you to seduce me."
                           scene v14496 with dissolve
                           cnt "Seduce you?"
                           scene v14497 with dissolve
                           z "Yes. Use your princess-like charm to seduce me as much as you can."
                           scene v14499 with dissolve
                           cnt "..."
                           scene v14500 with dissolve
                           cnt "Okay, I'll try my best."
                           #Stands up
                           scene v14501 with dissolve
                           cnt "..."
                           scene v14522 with dissolve
                           cnt "Get down on the floor."
                           scene v14523 with dissolve
                           z "..."
                           play audio "audio/Cloth_rustle.wav"
                           scene v14524 with Dissolve(1)
                           z "Okay."
                           pause(1)
                           scene v14525 with Dissolve(1)
                           cnt "..."
                           scene v14526 with Dissolve(1)
                           pause(1)
                           scene v14527 with Dissolve(1)
                           pause(1)
                           scene v14528 with Dissolve(1)
                           cnt "You should really consider yourself lucky."
                           scene v14529 with Dissolve(1)
                           pause(1)
                           play sound "audio/cloth.mp3"
                           scene v14530 with Dissolve(1)
                           cnt "Having a royal princess do such a thing for you..."
                           play audio "audio/Cloth_rustle.wav"
                           scene v14531 with Dissolve(1)
                           z "(Damn... This girl's whole vibe just changed...)"
                           #Takes off more of her clothes.
                           play sound "audio/Zip.mp3"
                           scene v14532 with Dissolve(1)
                           pause(1)
                           play sound "audio/whoosh.mp3"
                           scene v14533 with Dissolve(1)
                           cnt "Most men would kill for the chance."
                           play audio "audio/Cloth_rustle.wav"
                           scene v14534 with Dissolve(1)
                           pause(1)
                           scene v14535 with Dissolve(1)
                           cnt "{i}Giggles.{/i}"
                           scene v14536 with Dissolve(1)
                           cnt "Wars have been fought over princesses, you know."
                           scene v14537 with Dissolve(1)
                           cnt "Rich men would spend fortunes to spend one night with a princess."
                           play audio "audio/Cloth_rustle.wav"
                           scene v14538 with Dissolve(1)
                           cnt "And yet here you are getting the privilege for free."
                           #Sits on him.
                           scene v14539 with Dissolve(1)
                           cnt "This fair skin knows not the touch of a man."
                           #Makes him touch her waist.
                           scene v14540 with dissolve
                           cnt "Only the touch of my fair handmaidens. Only at my behest."
                           cnt "Do you feel how smooth it is?"
                           scene v14541 with dissolve
                           z "Yeah..."
                           z "(Fuck me, I'm getting really horny here...)"
                           scene v14542 with Dissolve(1)
                           cnt "Ahh~..." (multiple=2)
                           #Puts his hand on her boobs.
                           z "(Fuck...)" (multiple=2)
                           scene v14543 with dissolve
                           z "..."
                           scene v14544 with dissolve
                           cnt "Normally, if you would put your hand there, it would come right off."
                           cnt "Not today, though."
                           #Leans to whisper in his ear.
                           scene v14545 with Dissolve(1)
                           cnt "Today... I don't want to be treated like a princess."
                           scene v14546 with Dissolve(1)
                           cnt "Today, I want to let go."
                           scene v14547 with Dissolve(1)
                           pause(1)
                           scene v14548 with dissolve
                           pause(1.5)
                           #Positions his dick so that it's almost penetrating her.
                           scene v14549 with Dissolve(1)
                           cnt "I want to know what it feels like..."
                           #Wiggles her ass around so that his dick also swings because it's touching her.
                           scene v14550 with Dissolve(1)
                           cnt "I want to be treated like a whore."
                           scene v14551 with Dissolve(1)
                           cnt "I want you to deflower me right here and now..."
                           show v14m24 with Dissolve(1)
                           cnt "I'm tired of virtue."
                           cnt "I want some pleasure."
                           cnt "I want you to try all my holes."
                           cnt "I want them all defiled and filled with seed."
                           cnt "And after you're done using me like a common slut, I want you to tell me which hole you liked the best."
                           cnt "Then you can breed it again and again..."
                           cnt "Until my brain goes numb..."
                           cnt "Until I can't walk properly without cum driping down my legs..."
                           cnt "Until anyone who sees me walking around naked after you're done with me, would mistake me for any other whore."
                           play audio "audio/Cloth_rustle.wav"
                           scene v14552 with Dissolve(1)
                           z "Fuck... You asked for it-"
                           #Z wants to push it inside her.
                           play sound "audio/falling2.mp3"
                           scene v14553 with hpunch
                           cnt "Uh, uh. You don't get to do that, I'm afraid."
                           #Holds his head while her hand is slightly touching his dick.
                           play audio "audio/creak.mp3"
                           scene v14554 with Dissolve(1)
                           cnt "Your time with the princess is over."
                           scene v14555 with Dissolve(1)
                           cnt "You had your chance to take me, and you missed it."
                           scene v14556 with dissolve
                           z "..."
                           if came_from_gallery == 0:
                               $ cnt_lst += 4
                           show screen button_lst with dissolve
                           play sound "audio/stats.wav"
                           hide screen button_lst with dissolve
                           #Stands up.
                           scene v14557 with dissolve
                           cnt "{i}Sighs.{/i}"
                           scene v14558 with dissolve
                           cnt "Was that okay?"
                           scene v14559 with dissolve
                           z "..."
                           z "Damn! That was fucking amazing!"
                           z "You're really good at being the princess, Centoria."
                           scene v14560 with dissolve
                           cnt "{i}Giggles.{/i} Thanks..." #Sly smile.
                           scene v14561 with dissolve
                           z "Heh... You're back to normal."
                           cnt "..."
                           pause(1)
                label round_6_of_r_p_s:
                   scene r_p_s_expln with Dissolve(1)
                   z "Rock..."
                   z "Paper..."
                   z "Scissors!"
                   play sound "audio/whoosh.mp3"
                   scene v14213 with dissolve
                   pause(1)
                   z "Oh... Looks like I won this one."
                   scene v14562 with Dissolve(1)
                   z "..."
                   play audio "audio/creak.mp3"
                   scene v14563 with Dissolve(1)
                   z "Uhh... Guys?"
                   scene v14564 with dissolve
                   tr "..." (multiple=2)
                   cndy "..." (multiple=2)
                   scene v14565
                   play sound "audio/Slap2.mp3"
                   play audio "audio/Falling2.mp3"
                   with vpunch
                   z "?!"
                   scene v14566 with Dissolve(1)
                   pause(1)
                   play audio "audio/kiss.mp3"
                   scene v14567 with dissolve
                   tr "Hmmm~..." (multiple=2)
                   cndy "Ah!" (multiple=2)
                   scene v14568 with Dissolve(1)
                   tr "Hmmmnnn~..."
                   play sound "audio/Cloth_rustle.wav"
                   scene v14569 with Dissolve(1)
                   tr "Mmnmmm~..." (multiple=2)
                   cndy "Ghhhmmm~..." (multiple=2)
                   play sound "audio/creak.mp3"
                   scene v14570 with Dissolve(1)
                   cnt "..."
                   scene v14571 with Dissolve(1)
                   cnt "?!"
                   pause(1)
                   play audio "audio/Falling2.mp3"
                   scene v14572 with hpunch
                   tr "?!" (multiple=2)
                   cndy "!!!" (multiple=2)
                   scene v14573 with dissolve
                   pause(1)
                   scene v14574 with dissolve
                   pause(1)
                   scene v14575 with dissolve
                   tr "..." (multiple=2)
                   cndy "..." (multiple=2)
                   scene v14576 with dissolve
                   tr "{i}Grins.{/i}" (multiple=2)
                   cndy "{i}Grins.{/i}" (multiple=2)
                   scene v14577
                   play sound "audio/whoosh.mp3"
                   with hpunch
                   z "Guys! Guys!"
                   scene v14578 with dissolve
                   z "Play nice, will you?"
                   z "There is plenty of me for everyone here."
                   tr "..." (multiple=2)
                   cndy "..." (multiple=2)
                   #Z asks them to play nice
                   scene v14579 with dissolve
                   tr "I get the dick!"
                   scene v14580 with dissolve
                   cndy "Wait! That's not fair!"
                   scene v14581 with dissolve
                   tr "I got it first! Pick something else!"
                   scene v14582 with dissolve
                   cndy "..."
                   scene v14583 with dissolve
                   cnt "I get his mouth."
                   scene v14584 with dissolve
                   cndy "..." (multiple=2)
                   tr "..." (multiple=2)
                   scene v14585 with dissolve
                   z "..."
                   scene v14586 with dissolve
                   cnt "What?"
                   scene v14587 with dissolve
                   cndy "Ughhh!"
                   scene v14588 with dissolve
                   pause(1)
                   scene v14589 with Dissolve(1)
                   z "..."
                   scene v14590 with Dissolve(1)
                   cnt "..."
                   scene v14591 with dissolve
                   cnt "Should I-"
                   scene v14592 with Dissolve(1)
                   tr "..."
                   scene v14593 with Dissolve(1)
                   tr "Fuck~..."
                   scene v14594 with Dissolve(1)
                   tr "Oh gods..."
                   play sound "audio/falling2.mp3"
                   scene v14595 with vpunch
                   tr "Ahhhhhh~!"
                   scene v14596
                   play audio "audio/kiss.mp3"
                   with hpunch
                   tr "Hmmmmnn~..."
                   scene v14597 with Dissolve(1)
                   tr "Mnnnn~..."
                   scene v14598 with dissolve
                   cnt "Hey! That's not fair!"
                   scene v14599 with Dissolve(1)
                   tr "Well, you didn't do anything so-"
                   play sound "audio/Cloth_rustle.wav"
                   scene v14600 with dissolve
                   cnt "Humpf!" (multiple=2)
                   tr "?!" (multiple=2)
                   play audio "audio/kiss.mp3"
                   scene v14601 with Dissolve(1)
                   cnt "Hmmm~..."
                   play sound "audio/Cloth_rustle.wav"
                   scene v14602 with Dissolve(1)
                   tr "Hmm..."
                   play sound "audio/Cloth_rustle.wav"
                   scene v14603 with Dissolve(1)
                   tr "Ahhh~..."
                   scene v14604 with Dissolve(1)
                   tr "Ohhhh~..." (multiple=2)
                   cndy "Eh?!" (multiple=2)
                   show v14m25 with Dissolve(1)
                   pause(1.5)
                   tr "Ahhhh~..." (multiple=2)
                   cndy "Hahh~..." (multiple=2)
                   cnt "Mhhhnnn~..." (multiple=2)
                   cndy "Ahh~..." (multiple=2)
                   tr "Annhh~..." (multiple=2)
                   cnt "Mmmmnnn~..." (multiple=2)
                   cnt "Mhmmmmnnn~..." (multiple=2)
                   cndy "Hnnn~..." (multiple=2)
                   tr "Ohhhh~... Fuccckkk~..." (multiple=2)
                   cndy "Ahhnnn~..." (multiple=2)
                   tr "Ahhh~... Faster... Faster..." (multiple=2)
                   cndy "Ahhhhhh~... Lucky you..." (multiple=2)
                   pause(1.5)
                   show v14m26 with Dissolve(1)
                   pause(1.5)
                   tr "Ohhhh~... Fuck... This is so good~..." (multiple=2)
                   cnt "Hmmmn~..." (multiple=2)
                   tr "I... I'm close... Ahhhh~..." (multiple=2)
                   cndy "Ahhh~..." (multiple=2)
                   tr "Ohhhh~... Gods... Ahhhhhaaa~..." (multiple=2)
                   cndy "Hnnn~..." (multiple=2)
                   tr "Fuckkkk~... I came already~..." (multiple=2)
                   cnt "Hmmmnnnhh~..." (multiple=2)
                   tr "I can't stop... I wanna cum again..." (multiple=2)
                   cndy "Ahhhh~..." (multiple=2)
                   cndy "Ahhhhh~... I also want to..." (multiple=2)
                   tr "Ohhh~... Fuhhhcckkkk~..." (multiple=2)
                   cndy "Ahhhh~... I want..." (multiple=2)
                   cnt "Mhhhnnn~..." (multiple=2)
                   pause(1.5)
                   play sound "audio/Cloth_rustle.wav"
                   scene v14605 with Dissolve(1)
                   cndy "I want..." (multiple=2)
                   tr "?!" (multiple=2)
                   scene v14606
                   play sound "audio/whoosh.mp3"
                   play audio "audio/Falling2.mp3"
                   with vpunch
                   tr "Ahhh!"
                   scene v14607 with Dissolve(1)
                   cndy "Hmmm~..."
                   play audio "audio/Falling2.mp3"
                   scene v14608 with vpunch
                   cndy "Ohhhhhh~!"
                   play sound "audio/kiss.mp3"
                   scene v14609 with hpunch
                   cnt "Hmmmn~?!"
                   scene v14610 with Dissolve(1)
                   cndy "Ahhhh~..." (multiple=2)
                   cnt "Hmmnn~..." (multiple=2)
                   pause(1)
                   show v14m27 with Dissolve(1)
                   pause(1.5)
                   cndy "Gods~... This is so intense~..." (multiple=2)
                   cnt "Hmmm~..." (multiple=2)
                   cndy "[mc_name]~... You're so hard right now~..." (multiple=2)
                   cnt "Mnnn~..." (multiple=2)
                   cndy "I think I'm close already~..." (multiple=2)
                   tr "..." (multiple=2)
                   cndy "Ahhhh~... I want to do this every day..." (multiple=2)
                   cnt "Mnn~" (multiple=2)
                   cndy "Oh, gods~... I think... Ahhh~... Ahhhhhh~..." (multiple=2)
                   tr "..." (multiple=2)
                   cndy "I think I'm gonna~... Ahhh~... Hnnn~..." (multiple=2)
                   tr "..." (multiple=2)
                   cndy "Yeah... I'm totally cumming... Ahhh~... Ahhhhhhnnn~..." (multiple=2)
                   tr "Wh-What..." (multiple=2)
                   z "(I think I'm really close...)"
                   pause(1.5)
                   scene v14611
                   play sound "audio/whoosh.mp3"
                   play audio "audio/Falling2.mp3"
                   with vpunch
                   z "?!" (multiple=2)
                   tr "Okay! Enough! You came already!" (multiple=2)
                   play audio "audio/Falling2.mp3"
                   scene v14612 with vpunch
                   z "(Damn... I was so close...)"
                   cndy "When did we say the limit was cumming?!"
                   tr "I don't care! I'm the one who gets the dick!"
                   scene v14613 with dissolve
                   z "Guys! We agreed you'd play nice!"
                   scene v14614 with Dissolve(1)
                   z "Look at Centoria! She's-"
                   scene v14615 with Dissolve(1)
                   z "..."
                   scene v14616 with Dissolve(1)
                   z "Centoria?"
                   scene v14617 with Dissolve(1)
                   cnt "..."
                   scene v14618 with Dissolve(1)
                   z "(Is she gonna...)"
                   pause(1)
                   show v14m28 with Dissolve(1)
                   pause(1)
                   z "(She's actually doing it...)"
                   z "(Not even saying anything... She's just staring at me...)"
                   z "(Fuck... Something about this girl always makes me horny...)"
                   z "(Compared to the others... She just feels...)"
                   z "..."
                   z "(...untouchable?)"
                   z "(Yet here she is stroking my dick...)"
                   pause(1)
                   scene v14619 with Dissolve(1)
                   cnt "..."
                   scene v14620 with Dissolve(1)
                   cnt "Hmmmnn~..."
                   play audio "audio/kiss.mp3"
                   scene v14621 with Dissolve(1)
                   cnt "{i}Kisses it.{/i}"
                   play audio "audio/kiss.mp3"
                   scene v14622 with Dissolve(1)
                   cnt "{i}Continues kissing it.{/i}"
                   pause(1)
                   show v14m29 with Dissolve(1)
                   pause(1)
                   cnt "Ahhhh~..."
                   z "(Oh gods... She totally lost it...)"
                   z "(I can't believe she just randomly started doing this...)"
                   cnt "Ahhhh~... Hnnnhhh~..."
                   cnt "Hmmnnn~... Ahhnnn~..."
                   z "(Fuck... I might actually cum from just this...)"
                   pause(1)
                   scene v14623 with Dissolve(1)
                   cnt "Ahhhh~... It'th thooooo ha'ad..."
                   z "{i}Gulps.{/i}"
                   play audio "audio/kiss.mp3"
                   scene v14624 with Dissolve(1)
                   cnt "Mmmnn~... {i}Kisses the tip.{/i}"
                   scene v14625 with Dissolve(1)
                   cnt "Ghhhmmnn~..." (multiple=2)
                   z "Fuckk..." (multiple=2)
                   pause(1)
                   show v14m30 with Dissolve(1)
                   pause(1)
                   cnt "Ghhhmmmkk~..."
                   z "Oh, fuck me..."
                   cnt "Hmmmmnnn~..."
                   z "(This girl's got some skills...)"
                   cnt "Ghhhmmmnn~..."
                   z "(Holy fuck how did she learn how to do that...)"
                   cnt "Khhgggmmnn~..."
                   z "(She's almost taking the whole thing...)"
                   cnt "Ghhhhhkkkknn~..."
                   cnt "Hmmmmnnnn~..."
                   z "Centoria... I'm gonna..."
                   z "I'm close as fuck..."
                   cnt "Mnnn~..."
                   pause(1)
                   scene v14625 with Dissolve(1)
                   cnt "Hmmmn~..."
                   z "Eh?! Why'd you stop?!"
                   play sound "audio/Cloth_rustle.wav"
                   scene v14626 with Dissolve(1)
                   cnt "..."
                   play sound "audio/Cloth_rustle.wav"
                   scene v14627 with Dissolve(1)
                   pause(1)
                   scene v14628 with Dissolve(1)
                   z "..."
                   play sound "audio/creak.mp3"
                   scene v14629 with Dissolve(1)
                   z "(Gods... Is she really going to put it in?)"
                   scene v14630 with Dissolve(1)
                   cnt "Hmmmnn~..."
                   scene v14631 with Dissolve(1)
                   cnt "..."
                   z "(Gods... This is really happening...)"
                   play sound "audio/creak.mp3"
                   scene v14632 with Dissolve(1)
                   cnt "Hnnn~..." (multiple=2)
                   z "Fuuccckkk..." (multiple=2)
                   z "(The tip is almost in...)"
                   scene v14633 with Dissolve(1)
                   cnt "..."
                   scene v14634 with Dissolve(1)
                   tr "..." (multiple=2)
                   cndy "..." (multiple=2)
                   scene v14635 with Dissolve(1)
                   cnt "..."
                   scene v14636 with Dissolve(1)
                   cnt "?!"
                   scene v14637 with Dissolve(1)
                   cnt "..."
                   play sound "audio/Cloth_rustle.wav"
                   scene v14638 with Dissolve(1)
                   cndy "Don't worry, it won't hurt."
                   scene v14639 with dissolve
                   tr "Just slide it in slowly, okay?"
                   scene v14640 with Dissolve(1)
                   z "(Damn... I wasn't expecting them to-)"
                   scene v14641
                   play sound "audio/RecordScratch (thanks senpai).ogg"
                   stop music
                   with hpunch
                   stfny "{size=-10}[mc_name]!{/size}"
                   pause(1)
                   play sound "audio/Door slam.mp3"
                   scene v14642 with PushMove(0.1, mode="pushleft")
                   with hpunch
                   pause(1)
                   play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
                   scene v14643 with dissolve
                   stfny "..."
                   scene v14644 with Dissolve(1)
                   stfny "..."
                   scene v14645 with dissolve
                   stfny "Why the fuck are you guys-"
                   scene v14646 with dissolve
                   stfny "Never mind! I don't want to know! If you run across [mc_name] tell him Hailey needs to talk to him about tomorrow's mission."
                   stfny "Also, Torr. Anabelle wants to talk to you, I think."
                   scene v14647 with dissolve
                   pause(1)
                   scene v14648 with Dissolve(1)
                   z "Fuck me, that was close..."
                   scene v14649 with dissolve
                   cnt "Yeah..."
                   scene v14648 with dissolve
                   z "I guess Torr and I need to go, huh..."
                   scene v14650 with dissolve
                   z "Well, that was a ton of fun, guys... Let's do it again soon."
                   if came_from_gallery == 0:
                       $ cnt_lst += 5
                       $ cndy_lst += 5
                       $ tr_lst += 5
                   show screen button_lst with dissolve
                   play sound "audio/stats.wav"
                   hide screen button_lst with dissolve
                   scene v14651 with dissolve
                   pause(1)
    if came_from_gallery == 1:
        $ came_from_gallery = 0
    $ renpy.end_replay()
#6)    Arrival in Brethren:
#    -Upon arrival, rest of mission explanation is told by Helena (should hint that the monster is a succubus, who is living in the underground city.)
    scene black with Dissolve(2)
    pause(1)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(2)
    play background_s "audio/rain.mp3" volume 0.8 fadeout 1.0 fadein 1.0 loop
    scene v14652 with Dissolve(2)
    pause(1)
    scene v14653 with Dissolve(1)
    z "..."
    play music "audio/Requiem in D.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
    pause(0.75)
    show v14m1 with Dissolve(2)
    pause(0.75)
    hlna "If the letter is to be taken at face value, this has been going on for years."
    hlna "I've heard rumours about men mysteriously dying there."
    hlna "So you three have to be very careful. We might be dealing with anything here..."
    hlna "But according to the letter. It's a monster that has been feeding off the town's men for the last few years."
    hlna "According to the woman who sent this, it killed her only son last week. Her husband too a few years ago."
    hlna "The mission objectives are simple: find out what it is that killed these men, and rid the town of it. By any means necessary."
    hlna "Hailey. You'll be the leader of the mission. I'm sure you'll be up to the task."
    scene v14654 with dissolve
    hly "[mc_name]! Come on! Don't fall behind!"
    scene v14655 with Dissolve(1)
    pause(1)
    scene v14656 with Dissolve(1)
    pause(0.5)
    scene v14657 with Dissolve(1)
    pause(2)
    stop music fadeout 3.0
    scene v14658 with Dissolve(1)
    hly "Sure is way colder than in the ninja village, huh..."
    scene v14659 with dissolve
    z "Yeah... There's a weird chill in the air."
    scene v14660 with dissolve
    Character("Old Man") "You there!" #Has a pitchfor
    scene v14662 with Dissolve(1)
    Character("Old Man") "What are you three doing out here at this hour?"
    scene v14661 with dissolve
    z "Pordon the lateness of the hour, sir. We mean no harm."
    Character("Old Man") "..."
    z "We're ninjas here to look into a matter o-"
    scene v14663 with dissolve
    Character("Old Man") "Ninjas?!"
    Character("Old Man") "What would ninjas be doing here?!"
    Character("Old Man") "Don't tell me you've come to kill the succubus!"
    scene v14661 with dissolve
    z "The succubus?"
    z "What are you-"
    scene v14662 with dissolve
    Character("Old Man") "You can't! It'd upset the goddess!"
    Character("Old Man") "You need to leave! Now!"
    scene v14661 with dissolve
    z "Hey, calm down-"
    scene v14664
    play sound "audio/sword draw.mp3"
    with hpunch
    #Holds the pitch fork in an attacking position.
    Character("Old Man") "Not another step into the village, you hear?!"
    z "..."
    scene v14665 with dissolve
    z "Hey..."
    play sound "audio/Effect3.mp3"
    scene v14666 with Dissolve(1)
    play music "audio/Requiem in D.mp3" volume 0.5 fadeout 5.0 fadein 5.0 loop
    #Change in vibe
    z "Do you really think it's a good idea to threaten a ninja with a farming tool?"
    scene v14667 with Dissolve(1)
    z "..."
    scene v14668 with Dissolve(1)
    Character("Old Man") "..." #Scared.
    play sound "audio/Cloth_rustle.wav"
    scene v14669 with dissolve
    z "As I said. I mean neither you nor the town's people any harm."
    scene v14670 with dissolve
    z "Calm yourself and explain what you mean, will you?" #Pushes down the pitchfork for the man.
    scene v14671 with dissolve
    Character("Old Man") "You..."
    scene v14672 with Dissolve(1)
    Character("Old Man") "It's you..."
    Character("Old Man") "You're the reason for all of this... It's all because of you..."
    scene v14673 with dissolve
    z "What are you..."
    scene v14674
    play sound "audio/slash.mp3"
    play audio "audio/sword draw.mp3"
    stop music fadeout 1.0
    with vpunch
    Character("Old Man") "Curse you, demon!" #about to attack
    play audio "audio/Cloth_rustle.wav"
    scene v14675 with dissolve
    "Aron!"
    scene v14676 with Dissolve(1)
    Character("Young Man") "What do you think you're doing?!"
    scene v14677 with dissolve
    Character("Woman") "Go home, Aron. You probably had too much to drink."
    scene v14678 with dissolve
    Character("Woman") "Again..."
    scene v14679 with dissolve
    Character("Aron") "..."
    scene v14680 with dissolve
    Character("Aron") "Damn you, incubus..." #Leaves.
    scene v14681 with Dissolve(1)
    z "..."
    z "The fuck..."
    z "How did he know..."
    scene v14682 with dissolve
    play music "audio/Brethren.mp3" volume 0.5 fadeout 1.0 fadein 5.0 loop
    Character("Young Man") "Please don't mind him... He's always like that at night."
    scene v14683 with Dissolve(1)
    lumi "Welcome to our town. I am Lumi."
    scene v14684 with dissolve
    lumi "And this fine lady is my mother, Jacqueline."
    scene v14685 with dissolve
    jacq "And who might you three be?"
    jacq "A little over dressed, or well, armoured for tourists, aren't you?"
    scene v14686 with dissolve
    hly "Well..."
    scene v14687 with Dissolve(1)
    hly "We're not tourists, ma'am. We're ninjas."
    scene v14690 with Dissolve(1)
    jacq "Ninjas?"
    jacq "And what brings you here?"
    scene v14692 with dissolve
    hly "We've received a letter from one of the town's folk saying that her son was killed-"
    scene v14691 with dissolve
    jacq "That damned wench! She sent word to ninjas!"
    scene v14688 with Dissolve(1)
    z "?" #All three are confused.
    scene v14689 with dissolve
    z "Why? Was it a false report or something?"
    scene v14692 with Dissolve(1)
    jacq "..."
    scene v14693 with dissolve
    jacq "Yes it was."
    scene v14692 with dissolve
    z "So, what was written in the letter is not true? Is that what you're saying?"
    jacq "..."
    scene v14693 with dissolve
    jacq "It is not."
    scene v14694 with hpunch
    lumi "Mother!"
    lumi "It IS true!"
    scene v14695 with dissolve
    jacq "..."
    scene v14696 with dissolve
    jacq "No." #Turns her back.
    z "(What in the fuck is going on here...)"
    scene v14697 with Dissolve(1)
    jacq "Normally, any guest of this town would be welcomed in my home."
    jacq "Ninjas, however, are not."
    scene v14698 with dissolve
    jacq "You three should leave. Ninjas have no business here."
    scene v14699 with dissolve
    jacq "Good night."
    scene v14700 with Dissolve(1)
    #Leaves.
    z "..."
    z "What's her deal?"
    scene v14702 with Dissolve(1)
    lumi "I'm sorry about my mother's behaviour..."
    scene v14701 with dissolve
    z "Lumi, isn't it?"
    scene v14702 with dissolve
    lumi "Yes. That's me."
    scene v14701 with dissolve
    z "Any idea where we can find someone named Jane? She's the lady who wrote the letter."
    scene v14703 with dissolve
    lumi "Yeah..."
    lumi "Jane passed away just two days after her son."
    scene v14701 with dissolve
    z "What?!"
    z "Was she also killed?"
    z "Was her son even killed? Can you help us understand what's going on here?"
    scene v14702 with dissolve
    lumi "No, no... Jane wasn't killed, she was just found dead in her house after her son died... Most say she just died of grief..."
    scene v14701 with dissolve
    z "..."
    scene v14702 with dissolve
    lumi "But, yeah... Her son, Hunter... He was killed."
    lumi "I saw it with my own eyes..."
    scene v14703 with dissolve
    lumi "Well... Not exactly..."
    scene v14701 with dissolve
    z "?"
    scene v14704 with dissolve
    lumi "Listen... I'm going to talk reason to my mother. She'll let you stay in our house, I promise. You three have nowhere to stay after all, right?"
    scene v14705 with dissolve
    z "As much as I would love to say otherwise... Yeah, we don't."
    scene v14706 with dissolve
    lumi "Give me a few minutes, I'll be right back, and then we can talk inside!"
    scene v14707 with dissolve
    #Leaves
    lumi "{size=-10}Mother! Wait up!{/size}"
    pause(1)
    scene black with Dissolve(2)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(2)
    #At the mansion:
    play background_s "audio/fireplace.mp3" fadeout 1.0 fadein 1.0 loop
    scene v14708 with Dissolve(2)
    pause(1)
    play music "audio/Requiem in D.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
    scene v14709 with dissolve
    jacq "You didn't know?"
    jacq "Most of them are here for the town's brothel."
    scene v14719 with Dissolve(1)
    hly "The brothel?"
    scene v14709 with Dissolve(1)
    jacq "Indeed."
    scene v14710 with dissolve
    jacq "It was famously blessed by the gods."
    scene v14709 with dissolve
    jacq "You never heard of it?"
    #All are silent.
    scene v14718 with Dissolve(1)
    pause(1.5)
    jacq "Well... "
    jacq "Back in the day, this town was a much more popular destination, you see."
    jacq "The whole town used to live off the brothel. People from all around the continent would set off to try it for themselves."
    scene v14709 with Dissolve(1)
    jacq "The markets of the town where flourishing too. Teeming with tourists."
    jacq "We didn't have to rely on crops and breeding livestock to get by..."
    scene v14708 with dissolve
    vns "Why would people travel all the way to the brothel here? What was special about it?"
    scene v14709 with dissolve
    jacq "It was blessed by the gods, as I said."
    jacq "Those who would visit the brothel were given the gift of fertility. Even those who were previously sterile."
    jacq "Couples trying for children without luck would often come and lie together here and go home expecting some."
    scene v14708 with dissolve
    vns "Hmmm..."
    z "And? What happened after?"
    jacq "..."
    scene v14710 with dissolve
    jacq "The goddess who blessed the temple grew displeased with us, the people of the town."
    scene v14708 with dissolve
    z "Why?"
    scene v14710 with dissolve
    jacq "Why, indeed. One cannot know the minds of gods and their mood swings..."
    jacq "Athena took away our blessing and placed a curse on the brothel in its place."
    scene v14708 with dissolve
    z "Athena?!"
    scene v14709 with dissolve
    jacq "Yes."
    scene v14708 with dissolve
    hly "But didn't you say you thought we were tourists?"
    scene v14709 with dissolve
    jacq "I did, yes."
    scene v14708 with dissolve
    hly "Why would tourists visit a cursed brothel?"
    scene v14709 with dissolve
    jacq "Well, you see... The brothel's popularity might've plummeted, but it never died altogether."
    jacq "And tourists aren't affected by the curse anyhow. They just don't receive the blessing anymore."
    scene v14710 with dissolve
    jacq "Some even say that some tourists do receive the blessing every now and then."
    scene v14708 with dissolve
    z "Is it only the town's people that are affected then?"
    scene v14709 with dissolve
    jacq "Yes."
    scene v14708 with dissolve
    z "How are they affected exactly?"
    z "Does it have to do with the men who were killed?"
    jacq "..."
    scene v14709 with dissolve
    jacq "I..."
    scene v14710 with dissolve
    jacq "I shouldn't say any further."
    jacq "This is the will of the gods."
    jacq "One must not interfere with it, ninjas."
    scene v14709 with dissolve
    jacq "Your hearts may be in the right place, but please understand..."
    jacq "If you were to upset the gods even further... You may doom us all."
    play sound "audio/leather.wav"
    scene v14711 with Dissolve(1)
    jacq "You are welcome in my house... But please, heed my advice and stay away from the whole business with the curse."
    jacq "I must retire to my chamber now... Please pardon me."
    scene v14712 with dissolve
    jacq "Mercury!"
    scene v14721 with Dissolve(1)
    vns "?!"
    scene v14722 with dissolve
    vns "Did you just say..."
    scene v14713 with Dissolve(1)
    pause(1)
    scene v14714 with Dissolve(1)
    Character("Girl") "Yes?"
    scene v14715 with dissolve
    jacq "Give our guests clean changes of clothes and show them to one of the guest rooms, will you?"
    scene v14716 with Dissolve(1)
    jacq "Good night."
    play sound "audio/creaky door.mp3"
    scene v14717 with Dissolve(1)
    pause(1.5)
    #Leaves.
    scene v14723 with Dissolve(1)
    mercury "Ladies, please follow me."
    scene v14724 with dissolve
    lumi "[mc_name], come with me. We'll see if we can find something you can wear."
    play sound "audio/Cloth_rustle.wav"
    stop music fadeout 2.0
    scene v14725 with Dissolve(1)
    vns "Wait..."
    vns "Mercury?"
    scene v14726 with dissolve
    mercury "Hm?"
    mercury "Yes? That's me."
    scene v14725 with dissolve
    vns "Is that really you?"
    scene v14726 with dissolve
    mercury "I'm sorry, do we know each other?"
    scene v14725 with dissolve
    vns "You don't remember me?"
    mercury "..."
    scene v14727 with dissolve
    mercury "Wait..."
    play sound "audio/Cloth_rustle.wav"
    scene v14728
    with vpunch
    mercury "Venus?!"
    mercury "Gods! Venus?! Is that you?!"
    vns "..."
    play music "audio/Your-Heart.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
    scene v14729 with dissolve
    scene v14728 with dissolve
    #Nods.
    pause(1.5)
    scene v14730 with dissolve
    mercury "I..."
    mercury "Venus... I'm..."
    scene v14731 with dissolve
    mercury "I'm sorry... I know I couldn't meet you where we agreed back then... They kept following me..." #Starts crying.
    mercury "And I managed to run to the nearest town, and it was here, and then three men caught me and they w-"
    play sound "audio/Falling2.mp3"
    scene v14732 with hpunch
    mercury "?!"
    #Venus hugs her.
    scene v14733 with Dissolve(1)
    vns "I'm so glad you're okay..."
    play sound "audio/Cloth_rustle.wav"
    scene v14734 with Dissolve(1)
    mercury "..."
    scene v14735 with Dissolve(1)
    z "Lumi."
    lumi "Hm?"
    z "I think the girls need a moment. Let's go look for some clothes in the meantime, shall we?"
    scene v14736 with dissolve
    lumi "Oh! Yeah, of course. Follow me."
    scene v14735 with dissolve
    pause(1)
    stop music fadeout 1.0
    scene v14737 with Dissolve(1)
    $ mercury_ch14_met = 1
    #They go to a room where Lumi finds clothes for Z.
    lumi "Here we go... Those were my dad's, but I think they'll fit you."
    play sound "audio/cloth.mp3"
    scene v14738 with dissolve
    z "Thanks."
    lumi "..."
    z "..."
    pause(1)
    menu:
        "Ask Lumi for some privacy.":
            z "Ughhh... Can I have so privacy?"
            scene v14739 with dissolve
            lumi "Oh! Of course!"
            lumi "I'll be right outside if you need anything!"
            scene v14740 with dissolve
            pause(1)
        "Just change in front of him.":
            z "(Not like I'm the shy type, and he's a guy after all, even if he looks...)"
            scene v14741 with Dissolve(1)
            z "..." #Looks at how thicc he is.
            z "(..like that...)"
            play sound "audio/cloth.mp3"
            scene v14742 with Dissolve(1)
            pause(1)
            play audio "audio/Zip.mp3"
            scene v14743 with Dissolve(1)
            #Strips.
            #Lumi turns around while he does.
            pause(1)
            play sound "audio/cloth.mp3"
            scene v14744 with Dissolve(1)
            lumi "Imma change too if you don't mind."
            play sound "audio/Cloth_rustle.wav"
            scene v14745 with Dissolve(1)
            z "Sure."
            play sound "audio/cloth.mp3"
            scene v14746 with Dissolve(1)
            #Lumi looks from the side of his eyes.
            lumi "!" #Notices Z's dick
            play sound "audio/Zip.mp3"
            scene v14747 with Dissolve(1)
            lumi "..." #it's now obvious that he's looking and he's almost naked.
            z "..."
            z "(Is he looking where I think he's looking... Interesting...)"
            scene v14748 with Dissolve(1)
            lumi "Oh no..."
            scene v14749 with dissolve
            z "Hm? What's wrong?"
            scene v14750 with dissolve
            lumi "My pants... They're too tight... And..."
            scene v14749 with dissolve
            z "Hm?"
            scene v14750 with dissolve
            lumi "I can't get them down..."
            scene v14749 with dissolve
            z "..."
            scene v14750 with dissolve
            lumi "Can you like..."
            lumi "...help?"
            scene v14749 with dissolve
            z "..."
            pause(1)
            menu:
                "Help him.":
                    z "Sure."
                    z "Let's go there... I wanna sit on the bed."
                    play audio "audio/Cloth_rustle.wav"
                    scene v14752 with Dissolve(1)
                    #They go to the bed.
                    lumi "Okay... Now what?"
                    scene v14751 with dissolve
                    z "Don't worry. I have a plan."
                    scene v14753 with Dissolve(1)
                    lumi "Okay... I'm waiting..."
                    z "..."
                    pause(1)
                    menu:
                        "Try to slide down his pants gently.":
                            $ dummy += 1
                        "Spank him to loosen them.":
                            scene v14754 with dissolve
                            pause(1)
                            scene v14755
                            play sound "audio/Slap2.mp3"
                            with vpunch
                            lumi "Eeeep!"
                            scene v14756 with dissolve
                            lumi "What was that for?!"
                            scene v14757 with dissolve
                            z "To help loosen it. Trust me, I know what I'm doing, Lumi."
                            lumi "..."
                            scene v14756 with dissolve
                            lumi "O-Okay..."
                            scene v14757 with dissolve
                            z "Now, it should've loosened. Let me try to pull them down."
                    scene v14758 with Dissolve(1)
                    pause(1)
                    play sound "audio/Cloth_rustle.wav"
                    with hpunch
                    with hpunch
                    with hpunch
                    z "(Come on! Come off!)" with hpunch
                    play audio "audio/Cloth_rustle.wav"
                    with hpunch
                    with hpunch
                    with hpunch
                    play sound "audio/whoosh.mp3"
                    scene v14759 with vpunch
                    z "?!" (multiple=2)
                    lumi "Ah?!" (multiple=2)
                    play audio "audio/Falling2.mp3"
                    scene v14760 with vpunch
                    with vpunch
                    with vpunch
                    lumi "Awww..."
                    pause(1)
                    scene v14761 with Dissolve(1)
                    lumi "..."
                    scene v14762 with Dissolve(1)
                    lumi "!!!"
                    play sound "audio/Falling2.mp3"
                    scene v14763 with vpunch
                    lumi "I'm sorry!"
                    scene v14764 with dissolve
                    z "Don't worry about it. I'm mostly at fault here..."
                    scene v14765 with dissolve
                    lumi "..."
                    scene v14766 with dissolve
                    pause(1)
                    scene v14765 with dissolve
                    pause(1)
                    scene v14766 with dissolve
                    pause(1)
                    play sound "audio/Cloth_rustle.wav"
                    scene v14767 with Dissolve(1)
                    #His eyes ocilate back and forth between the two dicks.
                    lumi "It's so-"
                    play sound "audio/Knocking.mp3"
                    scene v14768 with hpunch
                    #Knocking sound
                    mercury "Lumi? Are you in there? I need your help with something!"
                    play sound "audio/Cloth_rustle.wav"
                    scene v14769 with Dissolve(1)
                    lumi "Eh?! Yeah! Of course! One second!"
                    play sound "audio/cloth.mp3"
                    scene v14770 with Dissolve(1)
                    lumi "{i}Putting on clothes.{/i}" (multiple=2)
                    z "(Did he almost...)" (multiple=2)
                    scene v14771 with Dissolve(1)
                    lumi "It'll only take a few minutes, [mc_name]..."
                    play sound "audio/creaky door.mp3"
                    scene v14770 with Dissolve(1)
                    pause(1)
                "Tell him you can't help.":
                    z "I'm sorry, Lumi... I wouldn't really know what to do..."
                    scene v14750 with dissolve
                    lumi "I get it... I'll figure it out somehow..."
                    scene v14749 with dissolve
                    pause(1)
    #Skip to Lumi telling the story:
    #Mercury isn't there!!!!
    #IT'S RAINING.
    pause(1)
    play background_s "audio/rain.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
    scene v14772 with Dissolve(1.5)
    play music "audio/Athena's theme.mp3" volume 0.3 fadeout 1.0 fadein 5.0 loop
    lumi "The monster will kill them."
    scene v14774 with Dissolve(1)
    vns "So, any villager who visits the brothel is killed by the monster?"
    scene v14773 with dissolve
    lumi "No. Only the men. Women visit it all the time and they're fine."
    scene v14775 with dissolve
    z "Why only the men?"
    scene v14776 with dissolve
    lumi "They say it's a succubus that kills them, a very powerful one, a demi-god some even say. And she only feeds off men."
    scene v14775 with dissolve
    z "Hm..."
    z "Wait... She's a demi-god, did you say?"
    scene v14776 with dissolve
    lumi "Many believe that, yeah."
    lumi "Some say she's the daughter of the goddess herself."
    scene v14775 with dissolve
    z "Athena's daughter?"
    scene v14776 with dissolve
    lumi "I guess..."
    scene v14775 with dissolve
    z "..."
    z "If Athena has a daughter, who's also a succubus..."
    z "Could that mean..."
    scene v14777 with Dissolve(1)
    hly "!"
    scene v14778 with dissolve
    hly "Are you saying..."
    scene v14779 with dissolve
    z "I don't know..."
    z "But we know about Athena and my father..."
    vns "What? I don't get it..."
    scene v14780 with dissolve
    hly "Elnor was an incubus, Venus. He and Athena were lovers for a few years."
    scene v14781 with Dissolve(1)
    vns "So?"
    scene v14782 with dissolve
    hly "So, the succubus, Athena's daughter..."
    hly "Might also be Elnor's daughter."
    scene v14783 with dissolve
    vns "Ah!"
    scene v14784 with Dissolve(1)
    vns "So your half sister?!"
    scene v14785 with dissolve
    lumi "What?!"
    lumi "You're the son of Athena?!"
    scene v14775 with dissolve
    z "Elnor. Not Athena."
    lumi "..."
    scene v14776 with dissolve
    lumi "Oh..."
    scene v14786 with Dissolve(1)
    z "Lumi."
    scene v14787 with dissolve
    z "Are you saying that the young man who was killed, Jane's son Hunter..."
    z "He visited the brothel and was-"
    scene v14788 with dissolve
    lumi "No!"
    lumi "Hunter did not visit the brothel."
    scene v14789 with dissolve
    lumi "I knew him. Best friends we were..."
    lumi "He wouldn't..."
    scene v14790 with dissolve
    hly "Maybe he did, h-"
    scene v14789 with dissolve
    lumi "No. I was there when he was killed. This was different."
    scene v14791 with dissolve
    z "You were there?!"
    scene v14792 with dissolve
    lumi "..."
    scene v14793 with dissolve
    scene v14792 with dissolve
    pause(1)
    #Nods.
    scene v14789 with dissolve
    lumi "We went to the woods nearby... Hunter and I wanted to become adventurers we went there often to hunt or just explore."
    play background_s "audio/Ambient_ninja_village_night.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v14794 with Dissolve(1)
    lumi "But that day... We heard something... A carriage or something..."
    lumi "We got closer to maybe help them, but when we spotted them, it was two men. One with gray hair wearing a creepy looking mask, the other had blond hair."
    lumi "They looked like they did not want to be seen, so we hid."
    scene v14795 with Dissolve(1)
    lumi "Then, I lost my balance... I fell..."
    lumi "So they heard us."
    scene v14796 with Dissolve(1)
    lumi "Hunter told me to run while he distracts them..."
    play background_s "audio/rain.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
    scene v14789 with Dissolve(1)
    lumi "I didn't want to leave him, but I'm a coward... So I just ran..." #Sad.
    lumi "The next day, they found his body in the woods... He had holes all over his torso... Those savages didn't even kill him properly..."
    scene v14788 with dissolve
    lumi "I told the others but they said it was probably some bandits..."
    lumi "I'm sorry, but it had nothing to do with the curse of the town..."
    lumi "Still... Hunter, like the other men, didn't deserve  to die like that..."
    lumi "So, I will help you guys in any way I can while you're here..."
    scene v14791 with dissolve
    z "..."
    stop music fadeout 4.0
    z "Thanks, Lumi. We appreciate your help."
    pause(1)
    play sound "audio/creaky door.mp3"
    scene v14797 with Dissolve(1)
    #Mercury comes to the room, she was helping the jacqline.
    mercury "Hey... I'm sorry it took a while I was just helping the madam while she retires for the night."
    mercury "Now we can talk about what you've been up to after we got separated, Venus."
    scene v14798 with dissolve
    vns "Sure, that sounds nice."
    pause(1)
    #Skip
    scene v14799 with Dissolve(1)
    play music "audio/Your-Heart.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
    mercury "And? What happened after?"
    scene v14800 with dissolve
    vns "I honestly don't remember a thing."
    scene v14801 with dissolve
    vns "I guess that's what being possessed is like."
    scene v14802 with dissolve
    mercury "Oooh, sounds spooky."
    scene v14799 with dissolve
    mercury "So, how did you get rid off it, though?"
    scene v14803 with dissolve
    vns "Well, [mc_name] managed to-"
    play sound "audio/thunder.mp3"
    scene v14804 with dissolve
    pause(0.5)
    play audio "audio/whoosh.mp3"
    scene v14805 with PushMove(0.1, mode="pushleft")
    with hpunch
    #Lightning stikes.
    mercury "Eeep!" #Jumps into z's lap.
    scene v14806 with dissolve
    z "..."
    play sound "audio/creak.mp3"
    scene v14807 with vpunch
    mercury "Ah! Sorry!"
    scene v14808 with dissolve
    vns "Whaaaat?!"
    scene v14809 with Dissolve(1)
    vns "Don't tell me you're still scared of lightning, Mercury!"
    scene v14812 with Dissolve(1)
    mercury "..."
    scene v14811 with dissolve
    mercury "No, I'm not!"
    scene v14812 with dissolve
    vns "..." (multiple=2)
    z "..." (multiple=2)
    scene v14813 with dissolve
    mercury "Maybe a bit?"
    scene v14814 with dissolve
    vns "{i}Giggles.{/i}"
    pause(1)
    scene v14815 with Dissolve(1)
    vns "{i}Continues laughing.{/i}"
    pause(2)
    #Render from the outside showing them having fun while talking while there's lightning and rain outside.
#7) Nari and Axius.
    #Irena walking around the house over hears nari and her father talking.
    scene black with Dissolve(2)
    pause(1)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(2)
    play background_s "audio/fireplace.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
    scene v14816 with Dissolve(1.5)
    pause(1)
    scene v14817 with Dissolve(1)
    axs "Again?"
    scene v14818 with dissolve
    irna "?"
    scene v14819 with Dissolve(1)
    pause(1)
    #Takes a peek.
    play music "audio/Axius's Theme.mp3" volume 0.2 fadeout 4.0 fadein 4.0 loop
    scene v14820 with Dissolve(1)
    axs "What's the matter with you?"
    scene v14821 with Dissolve(1)
    nari "It's wrong..."
    scene v14823 with dissolve
    nari "I don't want to do this anymore..."
    nari "Why would the gods want peasants murdered..."
    scene v14822 with dissolve
    axs "That's not the main goal here, Nari."
    axs "You know what we're trying to do here..."
    scene v14823 with dissolve
    nari "I know..."
    nari "But if our goal is truly pure, then why are we so sneaky about it?"
    nari "Why am I commanded to kill anyone who gets as much as a glimpse of us sneaking around in the woods like bandits?"
    axs "..."
    scene v14822 with dissolve
    axs "It is for the best if we do."
    axs "You need to overlook the death of the few for the good of the many."
    scene v14823 with dissolve
    nari "..."
    nari "I disagree."
    nari "You say we're doing this for the good of the many, don't you?"
    scene v14824 with Dissolve(1)
    nari "Why not share our plans with them, then?"
    nari "Shouldn't they rejoice to hear about it?"
    play sound "audio/whoosh (another one).mp3"
    scene v14825 with dissolve
    Character("???") "Your father wouldn't like that, my lady." (multiple=2)
    irna "?!" (multiple=2)
    scene v14826 with dissolve
    Character("???") "Not very lady-like of you to eavesdrop like this."
    scene v14827 with dissolve
    irna "Alura... Don't scare me like that..."
    scene v14828 with dissolve
    alura "What are they talking abo-" #Turns to them
    scene v14829 with dissolve
    alura "?!" #Her prespective looking at Axius.
    scene v14830 with Dissolve(1)
    nari "Why do we not simply tell them? Wouldn't that stop the unnecessary killing?"
    scene v14831 with dissolve
    axs "..."
    scene v14832 with dissolve
    nari "No answer."
    scene v14833 with dissolve
    nari "I'm not doing this anymore, Axius."
    scene v14834 with dissolve
    axs "..."
    scene v14833 with dissolve
    nari "I-"
    scene v14835 with dissolve
    axs "Either you will do it, or I will find someone who will."
    nari "..."
    scene v14836 with dissolve
    nari "What did you just-"
    scene v14837 with dissolve
    axs "I suppose I'll have to dispose of you if that were the case. You know too much after all, don't you?" #Axius is getting agressive.
    pause(1)
    play sound "audio/Magic 9.mp3"
    scene v14838 with Dissolve(1)
    nari "..." #Nari is getting ready to fight.
    play audio "audio/Cloth_rustle.wav"
    scene v14839 with Dissolve(1)
    alura "Now now, Nari... I know I let you leave the room with blue balls, but you shouldn't take it out on lord Axius, love..."
    scene v14840 with dissolve
    axs "Alura..."
    scene v14839 with dissolve
    alura "Come on, let's go back to our room. I'll make it up to you, I promise."
    alura "I'll use any part you want to do so too, so don't just stand there and come on!"
    scene v14841 with dissolve
    alura "Good night, lord Axius."
    scene v14842 with dissolve
    #Grabs his arm.
    nari "..."
    scene v14843 with Dissolve(1)
    pause(1)
    #They leave.
    scene v14844 with Dissolve(1)
    axs "..."
    scene v14845 with Dissolve(1)
    irna "..." #Worried look.
    scene v14846 with Dissolve(1)
    pause(2)
#8)    Next day:
    #Z dreams about being in the lake after sirius threw him last time.
    #Just use video from last chapter.
    scene black with Dissolve(2)
    pause(1)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(2)
    play background_s "audio/underwater.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
    show v13m36 with Dissolve(1.5)
    play music "audio/Auge's theme.mp3" volume 0.3 fadeout 1.0 fadein 5.0 loop
    z "...{w=3}{nw}"
    z "(I couldn't beat Sirius, huh...){w=5}{nw}"
    z "(This guy was crazy strong...){w=5}{nw}"
    z "...{w=3}{nw}"
    scene black with Dissolve(2)
    z "(I'm running out of breath here... I was pushed out of boundry. I already lost...)"
    scene v14847 with Dissolve(1)
    z "(Come on... End the illusion, Venus... Illusion or not... I don't want to drown...)"
    scene v14848 with Dissolve(1)
    z "..."
    scene v14849 with Dissolve(1)
    z "(Fuck! Venus!)"
    scene v14850 with Dissolve(1)
    z "!!!" #Starts to panik.
    scene v14851 with Dissolve(1)
    z "(FUCK! I'M DROWNING!)"
    scene v14852 with Dissolve(1)
    z "(WHY ISN'T THE ILLUSION ENDING! VENUS!)"
    stop background_s
    stop background_s2
    stop music
    scene v14853
    play sound "audio/creak.mp3"
    with hpunch
    z "AGGGGGGGGHGHHGHGH!"
    #Wakes up to hailey holding his nose shut.
    scene v14854
    play sound "audio/Slap2.mp3"
    with hpunch
    z "The fuck?!" (multiple=2) #Kicks her
    hly "Awww!" (multiple=2)
    play sound "audio/Falling2.mp3"
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
    scene v14855 with Dissolve(1)
    hly "Is this how you treat your mission leader?"
    hly "Imma ask Helena to deduct 10 points from you for that..."
    scene v14856 with dissolve
    z "Uhm... You might wanna fix your shirt."
    scene v14857 with dissolve
    hly "..."
    play sound "audio/Cloth_rustle.wav"
    scene v14858 with dissolve
    hly "Shit..."
    scene v14859 with dissolve
    hly "..."
    z "What the fuck were you doing?"
    play sound "audio/Cloth_rustle.wav"
    scene v14860 with Dissolve(1)
    hly "Waking you up?"
    scene v14861 with dissolve
    z "How about 'Hey [mc_name], wake up!'?"
    scene v14862 with dissolve
    hly "Pffffft... Where is the fun in that?"
    scene v14863 with dissolve
    z "..."
    scene v14864 with dissolve
    hly "Come on, I wanna talk about what we're gonna do today. Meet me outside."
    scene v14865 with dissolve
    pause(2)
    #leaves.
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.6 fadeout 1.0 fadein 1.0 loop
    scene v14866 with Dissolve(1)
    play music "audio/Brethren.mp3" volume 0.3 fadeout 1.0 fadein 5.0 loop
    hly "So, I have two things in mind to what we can do for now."
    scene v14867 with dissolve
    hly "One, investigate the dead bodies. Maybe they can tell us something about what we're dealing with here..."
    scene v14868 with dissolve
    hly "And two, investigating the tunnel to the underworld city."
    scene v14869 with dissolve
    z "Wait, wait..."
    scene v14870 with Dissolve(1)
    z "About point one, do the people here not dispose of the bodies of the deceased?"
    scene v14871 with dissolve
    hly "I've been talking to Lumi here, so..."
    scene v14872 with dissolve
    hly "They put them in coffins, apparently. Which are placed in a huge basement underneath the city hall."
    hly "Of course, I will need to be granted access to the basement, so I'm going to see the mayor."
    hly "Meanwhile, you and Venus will be investigating the tunnel."
    scene v14870 with dissolve
    z "Any clue to where we might find it?"
    scene v14874 with dissolve
    lumi "There's a door in the brothel. It's always been closed off as far as I know... And people say that it leads to the tunnel."
    scene v14870 with dissolve
    z "I see..."
    scene v14875 with dissolve
    lumi "I can't be sure, of course, as I have never seen it. You know, because I can't enter the place..."
    scene v14870 with dissolve
    z "Yeah, I understand. It's a good place to start, though."
    scene v14872 with dissolve
    hly "I recommended pretending to be customers when you get there. Access to the tunnel is forbidden so they might turn you down altogether if you waltz in there and ask to see the tunnel."
    scene v14870 with dissolve
    z "Okay, we can do that."
    z "I'm going to see if I can find Venus."
    scene v14873 with dissolve
    hly "She's probably hanging out with Mercury, so look for her in the kitchen or something."
    scene v14870 with dissolve
    z "Gotcha."
    pause(1.5)
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.3 fadeout 1.0 fadein 1.0 loop
    stop music fadeout 1.0
    scene v14876 with Dissolve(1)
    pause(1)
    play sound "audio/creaky door.mp3"
    scene v14877 with dissolve
    z "..." #Looking around the house.
    scene v14878 with Dissolve(1)
    z "Where is even the kitchen..."
    scene v14879 with dissolve
    vns "{size=-10}So I have to ask you something...{/size}"
    z "?"
    scene v14880 with Dissolve(1)
    vns "Do you like it here?"
    play sound "audio/plate.mp3"
    scene v14881 with dissolve
    play music "audio/Your-Heart.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
    mercury "Eh?"
    mercury "Where did that come from?"
    scene v14882 with dissolve
    vns "Well, you know... Being a handmaid is probably not the worst job, and you get to live with Jacqueline and her son... But..."
    vns "What do you think about coming back with me?"
    scene v14881 with dissolve
    mercury "To the ninja village?"
    mercury "But I'm not a fighter, Venus. I barely know how to defend myself."
    scene v14883 with dissolve
    vns "Being a ninja doesn't have to envolve fighting. We need all kinds of people in the village."
    scene v14885 with dissolve
    mercury "..."
    scene v14882 with dissolve
    vns "It's very safe there too, of course. We have two Keres protecting us."
    vns "And everyone is nice there."
    vns "And nymphs like us are always welcome there too. No one would bat an eye."
    $ mercury_ch14_met = 2
    mercury "..."
    scene v14886 with dissolve
    mercury "I..."
    mercury "I don't think I can anymore, Venus... I'm..."
    scene v14887 with dissolve
    vns "Why not?"
    scene v14888 with dissolve
    mercury "..."
    scene v14884 with dissolve
    mercury "Let me think about it, okay?"
    scene v14885 with dissolve
    vns "..."
    scene v14887 with dissolve
    vns "Sure..."
    scene v14888 with dissolve
    pause(1)
    z "(I think this is a good chance to interrupt.)"
    scene v14886 with dissolve
    mercury "I-"
    scene v14889 with dissolve
    z "Hey, guys."
    scene v14890 with Dissolve(1)
    vns "?"
    scene v14891 with dissolve
    vns "[mc_name]?"
    vns "Oh... I'm sorry... Is Hailey gonna tell us the plan for today?"
    scene v14890 with dissolve
    z "Actually, she already told me."
    z "You and I are going to look for the tunnel to the underworld city in the brothel."
    scene v14891 with dissolve
    vns "I see..."
    scene v14890 with dissolve
    z "Sorry to steal Venus from you, Mercury."
    scene v14892 with dissolve
    mercury "Oh, no... Please, don't worry about it." #Smile.
    scene v14893 with dissolve
    pause(1)
    scene v14894 with Dissolve(1)
    lumi "[mc_name]?"
    scene v14895 with Dissolve(1)
    lumi "I see you found Venus. Do you still want me to show you where the brothel is?"
    scene v14896 with dissolve
    z "Yep."
    scene v14897 with dissolve
    z "Ready to go, Venus?"
    play audio "audio/creak.mp3"
    scene v14898 with dissolve
    vns "Yeah. Lemme just grap a few things real quick."
    scene v14899 with Dissolve(1)
    mercury "Lumi!"
    scene v14900 with dissolve
    lumi "Yeah?"
    scene v14899 with dissolve
    mercury "Don't forget to get the potion for your mom, will you?"
    scene v14901 with dissolve
    lumi "Oh, right... Thanks for reminding me..."
    scene v14902 with dissolve
    pause(2)
    #Mercury reminds Lumi to get a potion for his mom.
    #They go to the brothel.
    stop music fadeout 1.0
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.6 fadeout 1.0 fadein 1.0 loop
    scene v14903 with Dissolve(1)
    lumi "This is it, guys."
    scene v14904 with dissolve
    lumi "As you know, I'm not allowed in. So I'll just leave you here, okay?"
    scene v14905 with dissolve
    z "Yeah. Thank you, Lumi."
    scene v14906 with dissolve
    pause(1)
    #Leaves.
    #They go in.
    play sound "audio/creaky door.mp3"
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    scene v14907 with Dissolve(1)
    pause(1)
    scene v14908 with dissolve
    play music "audio/Clair de Lune.mp3" fadeout 1.0 fadein 5.0 loop
    helda "Hello and welcome."
    helda "My name is Helda. I'm the manager of the brothel."
    helda "How can I help you?"
    scene v14909 with Dissolve(1)
    vns "We would like to..."
    vns "Well, go in?"
    scene v14910 with dissolve
    helda "..."
    scene v14909 with dissolve
    vns "Do we pay or-"
    scene v14911 with dissolve
    helda "No, dear. Not here. You pay inside when you pick what you like."
    scene v14909 with dissolve
    vns "I see."
    scene v14912 with dissolve
    helda "Are you two together then?"
    scene v14909 with dissolve
    vns "Yeah."
    scene v14913 with dissolve
    z "Eh... I think she meant as in-"
    scene v14911 with dissolve
    helda "Are you trying?"
    scene v14909 with dissolve
    vns "Trying?"
    scene v14910 with dissolve
    helda "Hm?"
    z "(Venus clearly has no idea what she's doing...)"
    pause(1)
    menu:
        "Intervene and tell Helda you're not a couple.":
            scene v14913 with dissolve
            z "Did you mean trying for a baby?"
            scene v14914 with dissolve
            z "We're not a couple. We just want to go into the brothel."
            scene v14915 with dissolve
            helda "Aaaahh... I see..."
            helda "Sorry, I misunderstood..."
            helda "Then, you two should proceed to the hall to the left. You'll find changing booths for men and women with clothes there in."
            helda "You can't bring any weapons inside of course. And the armour you're wearing is also not allowed. Change into the clothes you find in the booths."
            pause(1)
            #Skip to exploring the brothel.
        "Don't say anything.":
            helda "..."
            scene v14911 with dissolve
            helda "Well, never mind, you can take room 2. You can't bring any weapons inside of course. And the armour you're wearing is also not allowed. Change into the clothes you find in the room. There are masks there but they are optional."
            scene v14917 with Dissolve(1)
            play sound "audio/sliding door.mp3"
            pause(1)
            #Hands them a key.
            play sound "audio/keys.mp3"
            scene v14918 with Dissolve(1)
            helda "Here is the key."
            scene v14919 with Dissolve(1)
            helda "Enjoy your stay."
            scene v14920 with dissolve
            pause(1)
            # They have to change in front of each other.
            # There are candles in the room.
            scene v14921 with Dissolve(2)
            pause(2)
            play sound "audio/Cloth_rustle.wav"
            scene v14922 with Dissolve(1)
            pause(1)
            play sound "audio/Cloth_rustle.wav"
            scene v14923 with Dissolve(1)
            pause(1)
            scene v14924 with Dissolve(1)
            vns "Smells nice in here..."
            scene v14925 with dissolve
            z "I think it's the scented candles."
            scene v14926 with dissolve
            vns "I think..."
            vns "I think it's making me slightly lightheaded..."
            scene v14925 with dissolve
            z "Yeah... I get what you mean..."
            z "(A bit horny too for some reason?)"
            scene v14927 with dissolve
            vns "Wait, where am I supposed to change..."
            scene v14925 with dissolve
            z "Venus... I think..."
            z "I think when she asked if we were together, she meant if we're a couple."
            vns "..."
            scene v14926 with dissolve
            vns "Ohhh..."
            vns "Sorry about that..."
            scene v14925 with dissolve
            z "Don't worry about it..."
            vns "..."
            play sound "audio/keys.mp3"
            scene v14928 with Dissolve(1)
            pause(1)
            play sound "audio/Cloth_rustle.wav"
            scene v14929 with Dissolve(1)
            #Starts taking off her clothes.
            z "..."
            play audio "audio/cloth.mp3"
            scene v14930 with Dissolve(1)
            pause(1)
            play sound "audio/Cloth_rustle.wav"
            scene v14931 with Dissolve(1)
            pause(1)
            play sound "audio/leather.wav"
            scene v14932 with Dissolve(1)
            z "(She's not gonna ask me to turn around or anything?)"
            scene v14933 with Dissolve(1)
            pause(1)
            play sound "audio/Cloth_rustle.wav"
            scene v14934 with Dissolve(1)
            z "..."
            play sound "audio/leather.wav"
            scene v14935 with Dissolve(1)
            z "I guess I'll change too..."
            play audio "audio/cloth.mp3"
            scene v14936 with Dissolve(1)
            vns "It's so hot in here, huh..."
            play sound "audio/Zip.mp3"
            scene v14937 with Dissolve(1)
            z "Yeah..."
            scene v14938 with Dissolve(1)
            vns "..." #Admires him
            scene v14942 with Dissolve(1)
            #Close up to her face looking at him.
            z "..."
            z "(Damn... I'm somehow kinda embarrassed now... She's staring so intently...)"
            scene v14943 with dissolve
            pause(1)
            scene v14939 with Dissolve(1)
            vns "D-Did you put on some muscle?"
            scene v14940 with dissolve
            z "I guess so? A few other people mentioned that..."
            scene v14941 with Dissolve(1)
            vns "Hmmm..."
            scene v14944 with Dissolve(1)
            vns "I mean, you were always quite fit, but now you look more..."
            scene v14946 with Dissolve(1)
            pause(1)
            scene v14944 with dissolve
            vns "Appealing..."
            scene v14945 with dissolve
            z "(Appealing?)"
            play audio "audio/cloth.mp3"
            scene v14947 with Dissolve(1)
            vns "Damn... Your abs are rock hard..."
            scene v14948 with dissolve
            z "(That's not the only thing that's rock hard right now...)"
            z "(Also... She's so close...)"
            scene v14947 with dissolve
            vns "No wonder I lost against you in the tournament... Look at you... You look like you can lift me with one arm..."
            scene v14949 with dissolve
            z "{i}Pokes her.{/i} (Shit...)"
            scene v14950 with Dissolve(1)
            z "(Could it be that the candle's scent is actually making us horny? Like an aphrodisiac?)"
            scene v14952 with Dissolve(1)
            vns "..." #Looks at his dick.
            scene v14951 with dissolve
            vns "I-It's been a while since I've seen it..."
            scene v14952 with dissolve
            vns "..."
            scene v14953 with dissolve
            vns "[mc_name]... Why are you so hard?"
            scene v14952 with dissolve
            z "I think it's the scented candles... They're..."
            scene v14953 with dissolve
            vns "Yeah... I get you, I get you... I can feel it too..."
            vns "I guess that's to be expected... We're in a brothel after all..."
            scene v14952 with dissolve
            vns "..."
            play sound "audio/Cloth_rustle.wav"
            scene v14954 with Dissolve(1)
            vns "We really can't let this get to us, right? We're trained ninjas and we have a clear objective after all..."
            scene v14955 with Dissolve(1)
            z "Right..."
            vns "..."
            scene v14956 with dissolve
            vns "Do we know where we're supposed to find the entracne to the tunnel?"
            scene v14955 with dissolve
            z "It's just rumoured to be somewhere in the brothel."
            scene v14957 with dissolve
            vns "Right..."
            scene v14955 with dissolve
            z "..."
            play sound "audio/Cloth_rustle.wav"
            scene v14958 with dissolve
            z "Also is this what I'm supposed to wear?"
            z "It's way too small..."
            scene v14959 with dissolve
            vns "..."
            scene v14960 with Dissolve(1)
            helda "{i}From behind the curtain.{/i} Everything is to your liking, I hope?"
            z "Well, actually... There's a slight proble-"
            play sound "audio/Cloth_rustle.wav"
            scene v14961 with dissolve
            #Waltzes in.
            helda "Yes? What's the problem?"
            scene v14962 with Dissolve(1)
            pause(1)
            scene v14963 with dissolve
            helda "!"
            scene v14964 with dissolve
            #Observes that the underwear ain't fitting him.
            helda "Ahhh... I see we have a size problem on our hands..."
            scene v14965 with dissolve
            helda "Well, it's not per say on my hands..."
            scene v14966 with dissolve
            helda "I wish it were though..." #Winks at z.
            scene v14967 with dissolve
            helda "Maybe we can arrange that, handsome. If you're not spent after your time inside, pass by the front desk." #Seductively said.
            scene v14968
            play sound "audio/whoosh.mp3"
            with hpunch
            vns "Errr... Excuse me... I'm with him, remember?"
            scene v14969 with dissolve
            z "(Was that jealousy there?)"
            play sound "audio/Cloth_rustle.wav"
            scene v14970 with dissolve
            helda "Oh! I'm sorry, ma'am I must've gotten overexcited there..."
            helda "You've got yourself a real steed to ride there, huh."
            scene v14971 with dissolve
            vns "..."
            scene v14972 with dissolve
            helda "Now I'm wondering why you need to come to our establishment to begin with... Having a monster like that shoot some seed inside you, no way you wouldn't get pregn-"
            scene v14973
            play sound "audio/whoosh.mp3"
            with hpunch
            vns "Okay! We get it! Some privacy now, please?!"
            scene v14974 with dissolve
            helda "Of course, of course."
            scene v14975 with dissolve
            helda "I'll be right back with something to better accommodate your member, sir."
            play sound "audio/Cloth_rustle.wav"
            scene v14976 with dissolve
            pause(1)
            #Leaves.
            vns "..."
            label G55:
                $ persistent.g_55_unlock = 1
            scene v14977 with dissolve
            vns "Sheesh... What's wrong with her?"
            scene v14978 with dissolve
            z "Dunno..."
            z "..."
            vns "..."
            z "(Awkward silence...)"
            z "So, how is Margot coming along in the lab?"
            z "(Speaking of which I forgot to visit Margot in the ninja village...)"
            scene v14980 with Dissolve(1)
            vns "Oh. That girl with the glasses."
            vns "She's kinda helpful but she mostly keeps getting called by the older lady, Gabbie's mom to run errands for her."
            vns "And I don't know why, but I don't like Fransiska..."
            scene v14979 with dissolve
            z "Yeah... I don't either..."
            vns "..."
            scene v14980 with dissolve
            vns "Margot seems to be kinda crazy too, right?"
            scene v14979 with dissolve
            z "Yup."
            scene v14981 with dissolve
            vns "She wanted to make me a boob enlargement potion at one point..."
            vns "I told her I was already content with their size..."
            scene v14982 with dissolve
            vns "And then she said I'd never be able to give a good boob job with them."
            vns "Like I care about such things..."
            scene v14983 with dissolve
            vns "..." #Looks at his dick.
            scene v14984 with dissolve
            vns "..." #Her eyes go back and forth between his dick and her boobs.
            scene v14985 with dissolve
            vns "..."
            scene v14986 with dissolve
            vns "I..."
            vns "I don't care about such things, you know..."
            scene v14985 with dissolve
            z "Right..."
            scene v14986 with dissolve
            vns "But I mean... My boobs are obviously big enough for a boobjob, though..."
            scene v14982 with dissolve
            vns "Right?"
            scene v14985 with dissolve
            z "..."
            z "Probably..."
            scene v14982 with dissolve
            vns "Probably?"
            scene v14985 with dissolve
            z "How would I know?"
            vns "..."
            play sound "audio/Cloth_rustle.wav"
            scene v14987 with Dissolve(1)
            #Comes closer while standing. Her boobs are really close.
            vns "See?"
            scene v14988 with dissolve
            z "..."
            scene v14987 with dissolve
            vns "They are, right?"
            scene v14988 with dissolve
            z "..."
            scene v14989 with dissolve
            z "I'm not sure..."
            play sound "audio/Cloth_rustle.wav"
            scene v14990 with dissolve
            vns "Look!" #Places his hands on her boobs.
            scene v14991 with dissolve
            z "..."
            scene v14992 with dissolve
            #Squeezes.
            vns "Ahhhnnn~..."
            scene v14993 with dissolve
            z "Oh, sorry..."
            scene v14994 with dissolve
            vns "No, no. I didn't say it was bad..."
            vns "You can continue measuring if you want..."
            scene v14993 with dissolve
            z "Right... Measuring..."
            z "Turn around, will you?"
            scene v14994 with dissolve
            vns "O-Okay..."
            scene v14995 with Dissolve(1)
            pause(1)
            scene v14996 with dissolve
            z "Let's see..."
            scene v14997 with Dissolve(1)
            vns "..."
            scene v14998 with Dissolve(1)
            vns "Ahnn~..."
            show v14m32 with Dissolve(1)
            #Plays with her boobs from behind animation.
            vns "Hmnnn~... Ahhnn~..."
            z "(Does she just want me to play around with her boobs?)"
            vns "Ahhh~... Hnn~..."
            z "Every thing okay, Venus?"
            vns "Nunggg~... Yeah... Why?"
            z "You're just moaning kinda..."
            vns "Well, I can't help it when you're manhandling my boobs like that, can I?"
            vns "Nhhnn~... Speaking of which... Are you..."
            vns "Are you done measuring?"
            z "Not just yet..."
            vns "Ahhn~... Okay, take your time..."
            z "(Heh... This girl is just horny...)"
            z "I like the shape, you know..."
            vns "Ahhh~... Really?"
            vns "Aren't they too small?"
            z "Not really. I like boobs in all shapes and sizes."
            vns "Ah~... I see..."
            show v14m33 with Dissolve(1)
            #Starts pulling her nipples.
            vns "Ohhh~... Ahhhnnn~..."
            vns "What are you-"
            z "Your nipples are rock hard..."
            vns "I told you... I can't help it..."
            vns "Ahhhnn~... Fuck..."
            vns "What do my nipples have to do with boobjobs anyway?"
            z "Well, I'm evaluating your boobs in general for how well they can do in a boobjob."
            vns "Nhhhnnn~... But my nipples ar-"
            z "They are a part of your boobs, aren't they?"
            vns "Ahhh~... Fiiiinneee~..."
            z "..."
            z "Your nipples are really nice and perky, Venus..."
            vns "Ahhh~..."
            z "Sensitive too, it seems. Which is even better..."
            vns "Th-Thanks... Hahhh~..."
            scene v141000 with Dissolve(1)
            vns "Are we do-"
            scene v141001
            play audio "audio/kiss.mp3"
            with hpunch
            #Places his figer in her mouth.
            vns "Mmmm?!"
            scene v141002 with dissolve
            vns "Hmm~..." #Sucks on his finger.
            scene v141003 with dissolve
            z "You know, playing with your boobs made me quite horny..."
            scene v141004 with dissolve
            vns "..." #Looks down...
            scene v141005 with Dissolve(1)
            #Moves his dick between her thighs.
            pause(1)
            scene v141006 with Dissolve(1)
            vns "Ahhh~..." #Opens her mouth with her tongue sticking out.
            scene v141007 with dissolve
            vns "Choke me."
            scene v141008 with dissolve
            z "..."
            scene v141009 with dissolve
            z "Wha-"
            scene v141012 with Dissolve(1)
            vns "Choke me while you do it..."
            scene v141010 with dissolve
            z "..."
            scene v141011 with dissolve
            z "Damn, girl... You didn't strike me as the kinky type..."
            scene v141012 with dissolve
            vns "But slide it between my thighs or something, okay? Don't put it inside..."
            scene v141013 with dissolve
            z "Okay, Venus..."
            scene v141014 with dissolve
            vns "..."
            scene v141015 with dissolve
            vns "And treat me like one of the cheep whores here while you do it..." #Horny face...
            scene v141014 with dissolve
            z "..."
            menu:
                "Chokehold her and be rough with her like she asked.":
                    $ vns_kinky += 1
                    scene v141016
                    play sound "audio/Cloth_rustle.wav"
                    with vpunch
                    vns "Ghhhhnnn~!!"
                    scene v141017 with dissolve
                    vns "Ughhh~..."
                    pause(1)
                    vns "I cahhhnntthhhh~..."
                    pause(1)
                    vns "Breattthhh~..."
                    pause(1)
                    scene v141018 with dissolve
                    vns "Ahhhnnn~... Hahhhh~..."
                    scene v141019 with dissolve
                    vns "Hnnnnm~..."
                    z "(Let's not push it...)"
                    play sound "audio/Falling2.mp3"
                    scene v141020 with vpunch
                    vns "Hahhh~!"
                    scene v141021
                    play sound "audio/Cloth_rustle.wav"
                    with hpunch
                    vns "Eh?!"
                    scene v141022 with dissolve
                    vns "Ahhh~!"
                    pause(1)
                    show v14m34 with Dissolve(1)
                    pause(1)
                    vns "Ahhhh~... Fuhccckkk~..."
                    vns "Ah~... I'm~..."
                    vns "Lighhhttt~... Headed~..."
                    vns "I cahhnt... Ahhhhnn~... Thiiink~..."
                    z "Fuck... I just want to slide it in..."
                    vns "In~... Ahhhh~..."
                    vns "Inshiiidddeeee~... Hmmnnn~..."
                    vns "Nooo... Nooot insiideee~... Ahhh~..."
                    vns "Ahhhh~..."
                    vns "Harderrr~... C-Chohhhke me~..."
                    z "That's probably as hard as I can go without breaking your neck..."
                    vns "Ahhh~... Hard~... I wahnnnaaa~... Harddd~..."
                    z "Fuck... I can just fuck you hard if you want..."
                    vns "Ahhhhhh~... Harddd~..."
                    vns "Buhht~... Nohht inshhiiide~..."
                    z "Fine, fine... Then this is as good as it's going to get..."
                    vns "Ahhhh~... I~... Ahhh~..."
                    z "Venus... I'm close..."
                    vns "I~... I cahhhmme~..."
                    vns "Twiiissshh~... Alreadyyy~... Ahhh~..."
                    z "Shit..."
                "Make out with her and be nice to her instead.":
                    $ vns_kinky -= 1
                    scene v141023 with dissolve
                    pause(1)
                    scene v141024 with dissolve
                    vns "..."
                    scene v141025 with dissolve
                    vns "?!"
                    play audio "audio/kiss.mp3"
                    scene v141026 with Dissolve(1)
                    vns "Mhhhnnnn~?!"
                    scene v141027 with Dissolve(1)
                    vns "Mmmmm~..."
                    scene v141028
                    play sound "audio/Cloth_rustle.wav"
                    with hpunch
                    vns "Eh?!"
                    pause(1)
                    show v14m35 with Dissolve(1)
                    pause(1)
                    vns "Hmmmnnhhhh~... Fuhmmm~..."
                    vns "Ahnn~... I'mhhmm~..."
                    vns "Lighmmmhhttt~... Headmmnn~..."
                    vns "I cahhnt... Mnnnhhhhnn~... Thiiinknmm~..."
                    z "(Fuck... I just want to slide it in...)"
                    vns "Immmnnn~... Mamnnhhhh~..."
                    vns "Hmmnnn~..."
                    vns "Nmmmnnhh~... Ahhh~..."
                    vns "Nhhhmmm~..."
                    vns "Ahhh~... Hahhmnn~... I wahnnmm~... Hardddhhmm~..."
                    vns "Ahhmmmnnn~..."
                    vns "Nmmmmhhh~..."
                    vns "Ahhhh~... Immnn~... Ahhh~..."
                    z "Ahh... Venus... I'm close..."
                    vns "I~... I cahhhmme~..."
                    vns "Twiiissshhmnnn~... Alreadyyy~... Ahhh~..."
                    pause(1)
            z "I'm gonna cum..." #During the animation.
            vns "Hnnnhhh~... Cuuhhhmmm~..."
            pause(1)
            scene v141029 with Dissolve(1)
            z "Fuck... I'm cumming..." #Still render.
            scene v141030
            play sound "audio/Cloth_rustle.wav"
            with hpunch
            helda "Here we are!" #Waltzes with the clothes in while they're doing it.
            scene v141031 with Dissolve(1)
            helda "..."
            if came_from_gallery == 0:
                $ vns_lst += 5
            show screen button_lst with dissolve
            play sound "audio/stats.wav"
            hide screen button_lst with dissolve
            z "?!" (multiple=2)
            vns "?!" (multiple=2)
            if came_from_gallery == 1:
                $ came_from_gallery = 0
            $ renpy.end_replay()
            scene v141032 with Dissolve(1)
            helda "Damn... You sure cum a lot, don't you..."
            scene v141033
            play sound "audio/Cloth_rustle.wav"
            with hpunch
            vns "Fuck! Don't you know what knocking is?!"
            scene v141034 with dissolve
            helda "Technically, I can't knock because there's no doo-"
            scene v141035 with dissolve
            z "You know what she means!"
            scene v141036 with dissolve
            helda "Yeah... Sorry about that! I'll just leave the clothes here..."
            helda "But... You really don't need to do it here... There are plenty of better roo-"
            scene v141037
            play sound "audio/Slap2.mp3"
            with hpunch
            vns "Just fuck off!" #Pushes her.
            scene v141038 with dissolve
            helda "Okay! Bye!"
            play audio "audio/Cloth_rustle.wav"
            scene v141039 with dissolve
            z "..."
            scene v141040 with dissolve
            vns "..."
            scene v141041 with dissolve
            vns "We should get back to our objective..."
            scene v141040 with dissolve
            z "Right..."
            scene v141042 with dissolve
            z "Let's see if you can give me a boobjo-" (multiple=2)
            vns "Let's see if we can find the entrance t-"  (multiple=2)
            scene v141043
            play sound "audio/Cloth_rustle.wav"
            with hpunch
            vns "Wait what?"
            scene v141044 with dissolve
            z "What?"
            scene v141043 with dissolve
            vns "What?"
            scene v141044 with dissolve
            z "..."
            scene v141043 with dissolve
            vns "What did you just say?"
            scene v141044 with dissolve
            z "Let's see if we can find the entrance to the tunnel..."
            scene v141045
            play sound "audio/Cloth_rustle.wav"
            with vpunch
            vns "No you didn't!"
            scene v141046 with dissolve
            z "I totally did!"
            vns "..."
            scene v141045 with dissolve
            vns "You did n-"
            scene v141046 with dissolve
            z "Anyway, I'm gonna change really quick, okay?"
            scene v141045 with dissolve
            vns "Wait-"
            scene v141046 with dissolve
            z "Stop distracting me from the main objective, Venus!"
            vns "..."
            scene v141045 with dissolve
            vns "Why, you horny fuck..."
            scene v141046 with dissolve
            z "Come on, Venus. Stop fucking around and put your clothes on!"
            vns "..."
            scene v141045 with dissolve
            vns "Fuck you..." #Goes to put on her clothes.
            scene v141046 with dissolve
            pause(1)
            #They go in.
#9) Inside the brothel:
    #Girls start flirting with Z.
    scene black with Dissolve(1)
    pause(2)
    scene v141047 with Dissolve(1)
    z "..."
    z "(Wearing this is almost humiliating...)"
    scene v141048 with dissolve
    Character("Girl") "Hey there, handsome."
    #It's a bunch of girls.
    play sound "audio/Cloth_rustle.wav"
    scene v141049 with Dissolve(1)
    Character("Girl") "Want some good time?"
    play sound "audio/Cloth_rustle.wav"
    scene v141050 with Dissolve(1)
    Character("Girl 2") "He's kinda tall..." #Looks slightly like nixie.
    scene v141051 with Dissolve(1)
    Character("Girl 3") "And I like the hair..."
    scene v141052 with Dissolve(1)
    Character("Girl 3") "I'll give you a discount."
    scene v141053 with dissolve
    Character("Girl 2") "I'll give you 15 minutes for free..."
    scene v141054 with dissolve
    Character("Girl 1") "Hey! I found him first! Find other customers!"
    scene v141055 with dissolve
    Character("Girl 3") "..." (multiple=2) #Angry
    Character("Girl 2") "..." (multiple=2) #Angry
    scene v141056 with dissolve
    Character("Girl 2") "..." #Looks at z.
    scene v141057 with dissolve
    z "..." #Looks back at her.
    z "(This girl in the middle is...)"
    z "(Somehow she feels familiar...)"
    play sound "audio/creaky door.mp3"
    scene v141058 with Dissolve(1)
    Character("Girl 4") "Hey there, ladies..." #Older woman comes out of a door.
    scene v141059 with Dissolve(1)
    Character("Girl 4") "I just finished off this one young man..."
    scene v141060 with Dissolve(1)
    Character("Girl 4") "He came like a fountain as soon as I started touching him and then passed out..."
    scene v141061 with Dissolve(1)
    Character("Girls") "{i}Laughing.{/i}"
    #They laugh.
    scene v141062 with Dissolve(1)
    Character("Girl 4") "Oh! What have you got there..."
    Character("Girl 4") "Did the girls offer you their services already? Don't let them fool you with their young looks. I'm the most experienced in pleasing men here..."
    play sound "audio/Cloth_rustle.wav"
    scene v141063 with Dissolve(1)
    Character("Girl 4") "You can even call me mommy..." #Whispers in his ear.
    scene v141064 with Dissolve(1)
    z "..." #Surprised look.
    scene v141065 with dissolve
    Character("Girl 4") "Actually... You look familiar... Have I served you before?"
    scene v141066 with dissolve
    z "Huh? No. I've never be-"
    play sound "audio/Door big.mp3"
    scene v141067 with dissolve
    vns "What the fuck are these clothes..."
    scene v141068 with Dissolve(1)
    vns "They barely cover anything!"
    play audio "audio/Cloth_rustle.wav"
    scene v141069 with Dissolve(1)
    Character("Girl 1") "Ooooh... Who do we have here..."
    play sound "audio/Cloth_rustle.wav"
    scene v141070 with Dissolve(1)
    Character("Girl 3") "Look at that hair... Is the colour natural?"
    scene v141071 with dissolve
    vns "No... I actually dye it..."
    scene v141072 with dissolve
    Character("Girl 1") "Ahhh... Her voice is so cute!"
    Character("Girl 1") "Want to go somewhere more private, baby?"
    scene v141073 with dissolve
    Character("Girl 3") "Don't listen to her! I'll go down on you for 30 minutes straight until your brain melts."
    scene v141074 with dissolve
    Character("Girl 3") "Look..." #Pulls out her tongue which is very long.
    scene v141075 with dissolve
    vns "..."
    play audio "audio/Cloth_rustle.wav"
    scene v141076 with Dissolve(1)
    vns "Th-Thanks, ladies... But I already have my partner..." #Grabs z's arm.
    scene v141077 with Dissolve(1)
    pause(1)
    #All four are looking at them
    scene v141078 with dissolve
    pause(1)
    scene v141079 with dissolve
    Character("Girls") "Awwww..."
    scene v141080 with dissolve
    Character("Girl 4") "Well... Back to work, girls."
    scene v141081 with Dissolve(1)
    z "..."
    scene v141082 with Dissolve(1)
    z "Well... Let's look around, shall we?"
    scene v141083 with dissolve
    vns "Yeah..." #Older girl is looking at z.
    scene v141084 with Dissolve(1)
    z "..."
    play sound "audio/creaky door.mp3"
    scene v141085 with Dissolve(1)
    pause(1)
    scene v141086 with Dissolve(1)
    Character("Girl 2") "..."
    scene v141087 with dissolve
    pause(1)
    play sound "audio/Door close.mp3"
    scene v141088 with dissolve
    pause(1)
    scene v141089 with Dissolve(1)
    #Z looks at girl 2.
    #She's also looking at him.
    #Notices he's looking at her and looks away.
    z "Hmmmm..."
    vns "What's up?"
    scene v141090 with dissolve
    z "That one girl..."
    scene v141091 with dissolve
    z "She's..."
    scene v141092 with dissolve
    vns "?"
    z "..."
    scene v141090 with dissolve
    z "Nevermind..."
    scene v141091 with dissolve
    z "Wanna split up?"
    scene v141092 with dissolve
    vns "Sure."
    vns "Meet back here in an hour if we don't find anything?"
    scene v141091 with dissolve
    z "Yeah... Sounds good."
    scene v141092 with dissolve
    pause(1.5)
    #Z walks around for a bit.
    #Reaches a huge painting hung on a dead end.
    #Is about to go back.
    scene v141093 with Dissolve(1)
    stop music fadeout 3.0
    pause(1.5)
    scene v141094 with Dissolve(1)
    z "(Not much to see here, I guess...)"
    pause(1)
    "{size=-20}It's right there in front of you.{/size}"
    scene v141095 with dissolve
    play music "audio/Auge's theme.mp3" volume 0.2 fadeout 1.0 fadein 5.0 loop
    z "?!"
    scene v141096 with dissolve
    z "What?!"
    scene v141097 with dissolve
    z "Hello?"
    #Looks around.
    z "..."
    z "(Am I hearing things...)"
    z "..." #Looks at the painting.
    scene v141098 with Dissolve(1)
    z "(But now that I think about it... This painting looks almost as if...)"
    #Moves it, there's a door behind it.
    play sound "audio/creaky door.mp3"
    scene v141099 with Dissolve(1)
    z "..."
    z "(That's it...)"
    play sound "audio/creaky door.mp3"
    scene v141100 with Dissolve(1)
    pause(1)
    stop music fadeout 2.0
    play background_s "audio/cave.mp3" volume 0.6 fadeout 1.0 fadein 4.0 loop
    scene v141101 with Dissolve(1)
    z "..."
    z "(I can't see a thing...)"
    z "(Good thing I learnt how to use fire magic.)"
    play sound "audio/match.mp3"
    scene v141102 with Dissolve(1)
    z "..."
    #Goes in.
    #It's a tunnel.
    #The end of the tunnel is blocked by rubble.
    scene v141103 with Dissolve(1)
    pause(1)
    z "(It's blocked...)"
    "{size=-20}Who's there?{/size}"
    scene v141104 with Dissolve(1)
    #Z hears whispers from a door to the side.
    "{size=-20}Brother? Is that you?{/size}"
    z "?"
    z "(It's coming from that door...)"
    scene v141105 with Dissolve(1)
    "{size=-10}Have you come for me?{/size}"
    "{size=-10}You haven't visited in years.{/size}" #Goes to the door.
    "{size=-10}No it can't be you...{/size}"
    "{size=-10}Could it-{/size}"
    #Z goes through the door and it suddenly stops whispering.
    play sound "audio/creaky door 2.mp3"
    scene v141106 with Dissolve(1)
    z "..."
    play sound "audio/match.mp3"
    scene v141107 with Dissolve(1)
    z "Hello?"
    z "..."
    z "Who's there?!"
    z "..."
    scene v141108 with Dissolve(1)
    z "(Fuck... This is kinda creepy...)"
    z "YOU-"
    "Elnor?!" #It shouts
    scene v141109 with Dissolve(1)
    "Is that you?"
    scene v141110 with Dissolve(1)
    z "What th-"
    "I had thought you died long ago..."
    "What brings you here, brother?"
    z "..."
    z "I'm not Elnor..."
    "..."
    "You're not?"
    z "He was my father."
    "Elnor's son?"
    "The one he had with that goddess?"
    z "I suppose."
    "..."
    "What's your name?"
    z "..."
    play music "audio/Zycris's theme s02 1.mp3" volume 0.4 fadeout 1.0 fadein 5.0 loop
    stop background_s fadeout 3.0
    z "[mc_name]."
    "..."
    z "What about yours?"
    "I am Atropos."
    "Daughter of Nyx."
    z "Daughter of Nyx?"
    z "That means-"
    "Yes. Elnor was my half brother."
    "And you are my nephew."
    z "..."
    z "Are you trapped in here?"
    "Oh no. Here is where I belong."
    "I am one of the three fates, nephew. I must be sealed in stone. Lest the balance of your world fall to chaos."
    z "I'm not sure I fol-"
    "Why have you come, Nephew? Do you seek the city underground? I fear it's been destroyed long ago."
    z "No, no. I'm looking for a succubus."
    z "You see, the town above you is cursed... It's-"
    "Oh, yes. I know of this."
    z "You do?"
    z "Wait! Do you know where the monster is, then?!"
    z "Maybe you can help me, I susp-"
    "I cannot help you in that regard, nephew. For I do not know where the monster you seek is."
    z "..."
    "However... Maybe I can tell you something that you might find helpful."
    z "Hm?"
    "The curse. The monster. It wasn't here before."
    "I know when it was placed. And who placed it and why."
    "Would that be of help, dear nephew?"
    z "I've heard rumours about that already..."
    "But I know exactly what happened. No rumours. No half truths."
    z "..."
    z "Go on..."
    scene v141111 with Dissolve(1)
    "It was Athena who placed the curse. My brother's concubine herself."
    z "Yeah... I know it's Athena..."
    z "Again..."
    z "..."
    z "So I can expect her not to like it if I should interfere with her curse, I presume?"
    scene v141112 with Dissolve(1)
    "I would think as much, yes. She's no longer the forgiving kind, Athena... Not after what my brother's done..."
    z "..."
    z "What was it that happened between my father and Athena, Atropos?"
    "..."
    scene v141113 with Dissolve(1)
    "He had a child with another goddess while Athena was still his concubine, dear nephew."
    z "Wait! Wh-"
    "It is, sure enough, common amongst his kind to have more than one concubine. Many more, truth be said."
    "Athena however, is a goddess. A very proud one at that. She would not forgive him for lying with another woman and having a child with her."
    z "You can't mean..."
    scene v141114 with Dissolve(1)
    "Yes. It's you. You're his child from Demeter."
    scene v141115 with Dissolve(1)
    z "But I thought he was only involved with Athena after I was born. Long after!"
    "Falsehood, dear nephew."
    "Long before you were born..."
    #Take to story mod.
    scene v141116 with Dissolve(1)
    "Your father wanted to build a city. A city for his kind."
    "He was highly regarded by his kind. And he was smug enough to name himself king of the succubi and the incubi."
    z "..."
    scene v141117 with Dissolve(1)
    "Naturally, the mighty son of Nyx supported by the goddess of the night herself, very few dared challenge his claim to the title."
    scene v141118 with Dissolve(1)
    "He visited every town he could find and branded it with the mark of his race."
    z "The mark of his race?"
    "Lust, nephew."
    "You see, Elnor believed that lust existed in all creatures. But his race was the best at controlling it. Channeling it, if you will."
    "To prove his point, that lust was not a thing to be hidden, but displayed with pride, he founded a brothel in every town he could."
    z "A brothel?"
    "Indeed. Like the one you're within as we speak."
    z "This brothel was founded by my father?"
    "So it was. Connected to his city too."
    "Many of them were connected to the city akin to this one."
    "So had his kind ventured outside the city when needed."
    z "I see..."
    z "But that doesn't explain why Athena cursed this town..."
    "Ah, but it does..."
    scene v141119 with Dissolve(1)
    "You see. Athena came first to this town when she was a young goddess."
    "If tales are to be believed, no more than twenty summers she was when her father commanded her to gather worshipers of her own, lest she be discarded from mount Olympus."
    "And thus, she went from one town to the next. Bestowing blesssings on any who would worship her."
    "Until she happened on this one."
    "Elnor and his brothel in this town, went against the goddess's morals, you see."
    scene v141120 with Dissolve(1)
    "But they say the goddess in her yearning for affection and recognition was charmed by the incubus."
    "And a very charming man was my brother indeed."
    z "..."
    scene v141121 with Dissolve(1)
    "And so, Athena would bless this brothel and all who visited it with potency for nearly a decade."
    "Those sterile would visit the brothel with their beloved, or at times without them, mate here, and come back with children growing in the bellies of the women."
    z "..."
    z "And they had a child?"
    "No. Athena never had any children with my brother."
    z "Are you sure."
    "Quite sure, dear nephew."
    z "So when my father cheated on Athena, she..."
    scene v141122 with Dissolve(1)
    "Indeed... In her rage, she saw fit to curse the place where the two had met."
    z "..."
    z "And she placed a succubus here to do her bidding... I though she wanted my race destroyed..."
    scene v141110 with Dissolve(1)
    "Nephew..."
    "If you are to defy the goddess, I would advise caution..."
    z "..."
    z "I know..."
    z "Thank you for your help, Atropos."
    "I hope our paths cross again, dear nephew."
    "Take care."
    pause(1)
    stop music fadeout 4.0
    scene black with Dissolve(2)
    pause(2)
    #Goes back to meeting point, Venus isn't there.
    scene v141123 with Dissolve(1)
    play music "audio/Clair de Lune.mp3" fadeout 1.0 fadein 4.0 loop
    z "(Oh... I guess Venus is still looking around...)"
    z "..."
    pause(1)
    menu:
        "Go to the front counter to get Helda's offer.":
            scene v141124 with dissolve
            z "..."
            scene v141125 with dissolve
            pause(1)
            scene v141126 with Dissolve(1)
            z "Hey..."
            scene v141127 with dissolve
            helda "Everything is to your liking I hope?"
            scene v141126 with dissolve
            z "Yeah..."
            z "I actually came to talk to you about that offer..."
            scene v141128 with dissolve
            helda "Ooooh... I was hoping you'd say that..."
            scene v141129 with dissolve
            z "So wanna go to-"
            play sound "audio/open book.mp3"
            scene v141130 with dissolve
            helda "Hold on, I need to grab one of those..."
            scene v141131 with Dissolve(1)
            helda "Let's go somewhere more private, shall we?"
            play sound "audio/Cloth_rustle.wav"
            scene v141132 with Dissolve(1)
            z "..."
            play sound "audio/open book.mp3"
            scene v141133 with Dissolve(1)
            helda "?!"
            scene v141134 with dissolve
            helda "Hmmm..."
            scene v141135 with Dissolve(1)
            pause(1)
            label G56:
                $ persistent.g_56_unlock = 1
            scene v141136 with Dissolve(1)
            pause(1)
            play sound "audio/Cloth_rustle.wav"
            scene v141137 with Dissolve(1)
            pause(1)
            play audio "audio/cloth.mp3"
            scene v141138 with Dissolve(1)
            pause(1)
            play sound "audio/Cloth_rustle.wav"
            scene v141139 with Dissolve(1)
            pause(1)
            scene v141140 with Dissolve(1)
            helda "Ahh... It's even more impressive up close..."
            play sound "audio/Cloth_rustle.wav"
            scene v141141 with Dissolve(1)
            z "Let me help you wi-"
            play sound "audio/Falling2.mp3"
            play audio "audio/leather.wav"
            scene v141142 with hpunch
            z "?!"
            scene v141143 with Dissolve(1)
            helda "Don't worry, I know what I'm doing..."
            scene v141144 with Dissolve(1)
            z "..."
            play sound "audio/Cloth_rustle.wav"
            scene v141145 with Dissolve(1)
            pause(1)
            play audio "audio/cloth.mp3"
            scene v141146 with Dissolve(1)
            z "Damn... That's a nice body..."
            scene v141147 with Dissolve(1)
            helda "..."
            play audio "audio/kiss.mp3"
            scene v141148 with Dissolve(1)
            helda "Hmm~..."
            scene v141149 with Dissolve(1)
            helda "Ahhhnn~..."
            scene v141150 with Dissolve(1)
            helda "Ghhhmmmn~..."
            scene v141151 with Dissolve(1)
            helda "Guuuhhhmmm~..."
            scene v141152 with Dissolve(1)
            helda "Hmmnnnggg~..."
            scene v141153 with Dissolve(1)
            z "Fuckk..."
            scene v141154 with Dissolve(1)
            helda "Nnmmm~..."
            scene v141155 with Dissolve(1)
            helda "Hugggkkkmmnn~..."
            scene v141156 with Dissolve(1)
            helda "Shhhhhhlummmn~..."
            scene v141157 with Dissolve(1)
            helda "Ahhhnn~..."
            play audio "audio/kiss.mp3"
            scene v141158 with Dissolve(1)
            helda "{i}Kisses the tip.{/i}"
            scene v141159 with Dissolve(1)
            helda "Ahhh~... Hahh~..."
            scene v141160 with Dissolve(1)
            helda "{i}Giggles.{/i} That was quite difficult..."
            scene v141161 with Dissolve(1)
            helda "But now it's nice and wet."
            play sound "audio/Rip.mp3"
            scene v141162 with Dissolve(1)
            helda "Hold still."
            scene v141163 with Dissolve(1)
            helda "Hmm..."
            play sound "audio/pop.ogg"
            scene v141164 with Dissolve(1)
            helda "Puckk~!"
            scene v141165 with Dissolve(1)
            helda "Hmmnn~..."
            scene v141166 with Dissolve(1)
            helda "Uhhhnn~..."
            scene v141167 with Dissolve(1)
            helda "Guhhhmmmnnnn~..."
            scene v141168 with Dissolve(1)
            helda "Nghhhhmm~..."
            scene v141169 with Dissolve(1)
            helda "Fuhhckkk~... I'm out of breath..."
            play sound "audio/Cloth_rustle.wav"
            scene v141170 with dissolve
            helda "Sorry about the glasses..."
            scene v141171 with dissolve
            z "Fuck... That was an interesting way to put on a condom..."
            play sound "audio/Cloth_rustle.wav"
            scene v141172 with Dissolve(1)
            helda "..."
            play sound "audio/whoosh.mp3"
            scene v141173 with dissolve
            helda "It only gets more interesting from here."
            scene v141174 with dissolve
            pause(1)
            scene v141175 with Dissolve(1)
            helda "Now..."
            scene v141176 with Dissolve(1)
            pause(1)
            play audio "audio/leather.wav"
            scene v141177 with Dissolve(1)
            z "?!"
            play sound "audio/Falling2.mp3"
            scene v141178 with vpunch
            helda "Ahhhh~..."
            scene v141179 with dissolve
            helda "..."
            play sound "audio/Cloth_rustle.wav"
            scene v141180 with dissolve
            z "?"
            play sound "audio/whoosh.mp3"
            scene v141181 with hpunch
            z "Eh?"
            play audio "audio/kiss.mp3"
            scene v141182 with dissolve
            z "Hm?!"
            pause(1)
            show v14m37 with Dissolve(1)
            pause(1)
            helda "Ahhh~... Fuck~..."
            helda "Ah~... Can't say we've~... Ahhhhnn~..."
            helda "Ahhh~... We've ever had a customer like you..."
            helda "Didn't you already cum on my face... Ahhhh~... Like half an hour ago..."
            z "That was a while ago, though."
            helda "Ahhhhhh~... Fuckkk~..."
            helda "Most men would not be able to get so hard after..."
            helda "Did you take a potion or something... Ohhh, fuckk~..."
            z "Nope."
            helda "Ahhh~... Just natural talent, huh..."
            helda "Fuhccckk~... I wonder what it'd feel like if it was raw..."
            helda "Shhhhiiit~... I'm not even... Ahhh~..."
            helda "I'm not even taking the whole thing..."
            helda "Ahhh~... Fuckk me~... I'm cumming..."
            helda "Ohhh~... Fuck... Ahhhh~..."
            helda "The white haired girl is so fucking lucky..."
            helda "Ahhh~... Ohhh~..."
            helda "She can get this whenever she fucking wants..."
            helda "Fuckkk~... Where is she by the way... Why... Ahhh~..."
            helda "Why are you even fuckinnggg~... Ahhh~..."
            z "Don't worry, she's busy..."
            helda "Ahhhh~... Fuck... I'm cumming again..."
            helda "Oh gods... Ahhh~..."
            helda "I'm cumming... I'm..."
            pause(1)
            play audio "audio/leather.wav"
            scene v141183 with vpunch
            helda "Ohhhh~..."
            play sound "audio/Falling2.mp3"
            scene v141184 with Dissolve(1)
            helda "Fucckkk~... That was nice..."
            helda "I can't even feel my legs..."
            scene v141185 with dissolve
            z "So..."
            play sound "audio/open book.mp3"
            scene v141186 with dissolve
            z "Ready for round two?"
            scene v141187 with dissolve
            helda "..."
            pause(1)
            show v14m38 with Dissolve(1)
            pause(1)
            helda "Ohhhh~... Wait... I'm cumming... I'm cumming..."
            helda "Fuuhcckk~... I've lost count how many times I came..."
            helda "I really can't feel half of my body..."
            helda "Ahhh~... How am I supposed to finish my shift at the counter now... Ahhh~..."
            z "Probably ask someone to fill in for you?"
            helda "Fuckkk~... I don't know if that's..."
            helda "Ahhh~... I don't... Ahhh~..."
            helda "Fuccckkk~... I can't stop cumming~..."
            z "I'm actually also getting there..."
            helda "Ahhhhhhh~..."
            helda "How long have we been at this..."
            z "I think 40 minutes or so..."
            helda "Ahhh~... Really~?"
            z "Fuck... Venus..."
            helda "Fuck... I'm gonna cum again..."
            z "Me too actually... Me too..."
            z "Fuckkk..."
            pause(1)
            play audio "audio/leather.wav"
            scene v141188 with vpunch
            helda "Ahhhhhnnn~..."
            scene v141189 with Dissolve(1)
            helda "Godsss~..."
            play sound "audio/Falling2.mp3"
            scene v141190 with Dissolve(1)
            helda "{i}Collapses to the floor.{/i} That was the best..."
            scene v141191 with Dissolve(1)
            z "Fuck me... I hope Venus isn't looking for me..."
            z "Bye, Helda. That was fun."
            helda "Byeee~..."
            if came_from_gallery == 1:
                $ came_from_gallery = 0
            $ renpy.end_replay()
        "Just wait for Venus.":
            scene v141124 with dissolve
            z "(Might as well just wait...)"
            pause(1)
            #Nothing happens.
            #Skip to them going back.
#10) Going back from brothel:
    scene black with Dissolve(1)
    pause(1)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(2)
    play background_s2 "audio/Ambient_ninja_village_night.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v141192 with Dissolve(1)
    z "So she turned it into a curse."
    play music "audio/Brethren.mp3" volume 0.5 fadeout 1.0 fadein 5.0 loop
    scene v141193 with Dissolve(1)
    vns "What they told us was right?"
    scene v141194 with dissolve
    z "Yup."
    scene v141195 with dissolve
    vns "So the monster that haunts this place is acting on Athena's behist?"
    scene v141196 with dissolve
    z "Exactly."
    scene v141197 with Dissolve(1)
    vns "That complicates things, doesn't it..."
    z "I guess so."
    vns "You don't seem very concerned about all this."
    scene v141198 with Dissolve(1)
    z "Well, I've been in a similar situation, Venus."
    vns "?"
    vns "Oh, Right! The town of the faceless god!"
    scene v141199 with Dissolve(1)
    z "Yep."
    vns "..."
    vns "Well... We need to tell Hailey about this and see what she thinks before we can act in any way."
    scene v141200 with Dissolve(1)
    z "I know."
    lumi "..."
    z "One more thing, Venus..."
    z "One of the girls in the brothel... I think she might be-"
    scene v141201 with Dissolve(1)
    lumi "Oh! Here we are!"
    scene v141202 with dissolve
    z "The alchemist's shop?"
    scene v141203 with Dissolve(1)
    lumi "Yeah. I need to get a potion for my mom."
    scene v141204 with dissolve
    pause(1)
    #They go in.
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    play background_s "audio/fireplace.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
    scene v141205 with Dissolve(1)
    pause(1)
    play sound "audio/creaky door.mp3"
    scene v141206 with dissolve
    lumi "Good evening."
    scene v141207 with Dissolve(1)
    play music "audio/Alchemy.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
    Character("Alchemist") "Good evening, Lumi." #IT'S ATS'S CHARACTER
    Character("Alchemist") "You have some friends with you, I see."
    scene v141208 with dissolve
    lumi "Yeah. This is [mc_name] and Venus. They are ninjas investigating the killings."
    scene v141207 with dissolve
    Character("Alchemist") "Oh... I see..."
    Character("Alchemist") "Usual I assume?"
    scene v141208 with dissolve
    lumi "Yes, please."
    scene v141209 with Dissolve(1)
    play sound "audio/open drawer.mp3"
    pause(1)
    Character("Alchemist") "It's not here..."
    scene v141210 with dissolve
    Character("Alchemist") "LUMINA! CAN YOU GET ME THE DRAFT FOR JACQUELINE?!"
    scene v141211 with dissolve
    Character("Alchemist's assistant") "{size=-10}OKAY!{/size}"
    scene v141212 with dissolve
    Character("Alchemist") "How is the madam doing, by the way?"
    scene v141213 with dissolve
    lumi "She's doing well, actually. Thanks for asking, Tenebra"
    scene v141212 with dissolve
    Tenebra "Well be sure to send my regards, okay?"
    scene v141214 with Dissolve(1)
    z "Wait... Tenebra?"
    z "I've heard about you... Gabbie said you were the best transformation potion maker. Even better than Fransiska herself."
    scene v141215 with dissolve
    Tenebra "Hah! Fransiska... That woman has a lot of guts calling that abomination she makes a transformation potion."
    scene v141216 with dissolve
    Tenebra "I'm flattered to hear that you've heard about me, though."
    Tenebra "If you need potions don't hesitate to ask. I'll give you a good discount and the first bottle even free of charge, how does that sound?"
    scene v141217 with dissolve
    z "Sounds actually really nice. Thank you. But I'm not sure I need any potions."
    scene v141218 with dissolve
    Tenebra "Well, I'm always here if you change your mind."
    scene v141219 with Dissolve(1)
    #Her sister shows up with the potion.
    Character("Alchemist's assistant") "Here you go, sis. This is from today's batch."
    scene v141220 with dissolve
    Tenebra "Thanks, honey."
    play sound "audio/plate.mp3"
    scene v141221 with Dissolve(1)
    Tenebra "Here, Lumi. This is for you."
    play audio "audio/coin.mp3"
    scene v141222 with dissolve
    #Pays her.
    lumi "Thank you."
    Tenebra "You're quite welcome. Have a good night's sleep, okay?"
    lumi "Okay! Bye!"
    play sound "audio/creaky door.mp3"
    stop background_s fadeout 1.0
    play background_s2 "audio/Ambient_ninja_village_night.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    stop music fadeout 1.0
    scene v141223 with Dissolve(1)
    pause(1)
    #They leave.
    #They are walking away.
    scene v141224 with Dissolve(1)
    z "By the way, Lumi..." #Lumi is BEHIND HIM!!!!!
    #A hooded figure is going into the alchemis's store after them.
    scene v141225 with Dissolve(1)
    z "What kind of potion does your mom t-" #Turns to look at lumi.
    scene v141226 with dissolve
    play sound "audio/Horror.mp3"
    z "...{w=1.5}{nw}" #Spots the hooded figure, which seems to be looking back at him.
    scene v141227 with dissolve
    z "?!"
    play music "audio/Town of the faceless god.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    #They pause for a sec.
    scene v141228 with dissolve
    #The hooded figure runs away.
    z "Hey! Wait!"
    #Runs after it.
    #It goes into an alley and disappears.
    z "..."
    scene v141229 with Dissolve(1)
    z "Hey!"
    scene v141230 with Dissolve(1)
    z "..."
    scene v141231 with dissolve
    #Venus follows z.
    vns "Who was that?!"
    scene v141232 with dissolve
    vns "And why did they run from us..."
    scene v141233 with dissolve
    z "I don't know..."
    z "..."
    z "Let's just go back... I don't think they'll show themselves again..."
    scene v141234 with dissolve
    vns "But what if it was the killer trying to kill the alchemist or something?"
    scene v141233 with dissolve
    z "No. The killer only kills men, remember?"
    scene v141232 with dissolve
    vns "Right..."
    scene v141233 with dissolve
    pause(1)
#11) Home meeting:
    #They talk about what they discovered
    # Z thinks the succubus is probably buying the same potion Irena was using to look like a human and suses her to be the succubus responsible for all of it.
    #(Z suspects that it's a transformation potion since it's the alchemist's known speciality to make jaq look so young, which it partly is but it's mostly for Mercury.)
    #Z also suspects the girl in the brothel to be a succubus who's potentially responsible for the deaths but still feels like it's not her. But she's still the main suspect.
    #He mentions seeing someone being sth from the alchemist.
    #Hailey also has observations from the corpses she could get her hands on. She says they were slain.
    #Z thinks succubi wouldn't butcher their victims, Hailey mentions that this one might be doing this after killing them in other ways to cover up the fact that she's a succubus.
    #Z says that's a good point and remember that just because someone is a succubus doesn't mean that they are restricted to one certain way of killing people.
    #Hailey mentions that Hunter had holes all over his body. Z remembers Nari but doesn't say anything.
    #Z is silent looking at the floor.
    scene black with Dissolve(2)
    pause(1)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(2)
    play background_s "audio/fireplace.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
    scene v141235 with Dissolve(1)
    play music "audio/Brethren.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
    hly "Yeah. They actually wanted money for that... Can you believe this?"
    scene v141236 with dissolve
    vns "What? Why?"
    scene v141238 with dissolve
    #He remembers the succubus girl from the brothel.
    hly "They said that's how they're able to keep the crypt clean. They need to pay the crypt keeper after all..."
    scene v141086 with Dissolve(1)
    vns "Oh..."
    #He remembers the hooded figure from the alchemist.
    vns "I guess it kinda makes sense then..."
    vns "So how did it go?"
    scene v141226 with Dissolve(1)
    #Remembers Atropos.
    hly "Well... It was weird..."
    vns "Weird how?"
    hly "The corpses... They were all slain... They had big wounds on their bodies..."
    vns "Oh?"
    scene v141110 with Dissolve(1)
    vns "Wait... How is that weird?"
    hly "We thought it was a succubus killing these people, right?"
    hly "Would a succubus kill people by slashing them?"
    vns "I dunno..."
    scene v141237 with Dissolve(1)
    hly "..."
    vns "..."
    scene v141239 with dissolve
    pause(1)
    #Both looking at Z who's not paying attention.
    scene v141240 with dissolve
    z "..." #Notices.
    scene v141241 with dissolve
    z "What?"
    play audio "audio/Cloth_rustle.wav"
    scene v141242 with Dissolve(1)
    hly "Are you still with us?"
    scene v141243 with dissolve
    z "Yeah... Sorry. You were saying?"
    scene v141244 with dissolve
    hly "Do succubi kill people by slashing them?"
    scene v141243 with dissolve
    z "I don't think so?"
    z "I'm not really sure..."
    scene v141244 with dissolve
    hly "Well, you should know best..."
    scene v141243 with dissolve
    z "I haven't exactly met many succubi, Hailey..."
    scene v141245 with dissolve
    hly "Right..."
    hly "Well, the weirdest corpse was by far Hunter's though..."
    scene v141243 with dissolve
    z "Hm?"
    scene v141244 with dissolve
    hly "It had literal holes in it. Holes going all the way through his body."
    scene v141243 with dissolve
    z "What?"
    scene v141244 with dissolve
    hly "Yeah..."
    scene v141246 with dissolve
    vns "I thought he was supposed to have been killed by bandits..."
    scene v141247 with dissolve
    hly "Yeah... I know... That's why it's weird..."
    scene v12980 with Dissolve(1)
    #Remembers Nari
    hly "Something really weird is going on here... I don't kno-"
    scene v141243 with dissolve
    z "Wait..."
    hly "..."
    z "Hear me out..."
    z "One of Axius's minions... He had an ability that could do what was done to hunter."
    scene v141244 with dissolve
    hly "Oh?"
    scene v141243 with dissolve
    z "And..."
    z "So you know how Lumi got a potion for his mom from the alchemist?"
    scene v141248 with dissolve
    vns "Yeah?"
    scene v141243 with dissolve
    z "What is Tenebra known for?"
    scene v141248 with dissolve
    vns "Transformation potions?"
    scene v141243 with dissolve
    z "Exactly..."
    z "So Lumi was probably getting one too..."
    scene v141248 with dissolve
    vns "What, why?"
    scene v141243 with dissolve
    z "Well... Didn't you notice how young his mom looks?"
    scene v141249 with dissolve
    vns "Yeah. I did actually..." (multiple=2)
    hly "Yeah..." (multiple=2)
    scene v141243 with dissolve
    z "What if... She's using transformation potions to look like that?"
    hly "..."
    scene v141245 with dissolve
    hly "Ooooh..."
    hly "And here I was going to ask her what she uses for her skin care..."
    scene v141243 with dissolve
    z "And I think..."
    z "I think Jacqueline isn't Tenebra's only customer."
    z "Remember the hooded girl who ran from us?"
    scene v141248 with dissolve
    vns "Yeah?"
    scene v141243 with dissolve
    z "What if she's also a customer? She just didn't want to be seen buying transformation potions."
    scene v141248 with dissolve
    vns "Why not?"
    scene v141243 with dissolve
    z "Why indeed..."
    z "Well... My theory is..."
    z "One of the prostitutes... The blond one... She's a succubus."
    scene v141250
    play sound "audio/creak.mp3"
    with hpunch
    vns "What?!" (multiple=2)
    hly "Wait, what?!" (multiple=2)
    scene v141251 with dissolve
    vns "Why didn't you say so earlier?! We were literally there! And how do you even know?!"
    scene v141252 with dissolve
    z "Well, I don't know for sure, Venus... That's why I didn't say anything..."
    vns "..."
    z "It's incubus instinct... I could feel it... But we can't very well condemn someone as the murdering monster based on instinct, can we?"
    vns "..."
    play audio "audio/Cloth_rustle.wav"
    scene v141253 with dissolve
    vns "Yeah... I see your point..."
    scene v141254 with dissolve
    z "But the girl in the brothel doesn't look like a succubus, right?"
    scene v141255 with dissolve
    vns "Yeah..."
    scene v141256 with dissolve
    vns "Transformation potions!"
    scene v141254 with dissolve
    z "Exactly."
    z "Irena told me lots of succubi do this. It's not really uncommon."
    z "The main issue with the theory here is obviously the way the men died..."
    z "You said they had wounds on their bodies, right?"
    scene v141257 with dissolve
    hly "Yep."
    hly "Well, it could be that who ever kills them does it after killing them to cover up the way they actually died?"
    scene v141254 with dissolve
    z "Actually... Could be, yeah..."
    z "..."
    z "I say we go back to the alchemist tomorrow and ask her to help us."
    z "If she confirms the girl in the brothel buys transformation potions from her, we have a main suspect."
    z "Even if it's not her doing the killings, maybe she knows something."
    scene v141257 with dissolve
    hly "Okay... Let's do that."
    scene v141258 with dissolve
    vns "Guys... I promised Mercury to hang out together tomorrow..."
    scene v141259 with dissolve
    vns "Is it okay if you two do that without me?"
    scene v141260 with dissolve
    hly "Sure... Go ahead..." (multiple=2)
    z "Yeah. I don't mind." (multiple=2)
    scene v141261 with dissolve
    vns "Thanks..."
    play sound "audio/creak.mp3"
    scene v141262 with dissolve
    hly "Well, I guess we have our plan for tomorrow..."
    play sound "audio/creak.mp3"
    scene v141263 with Dissolve(1)
    hly "We should go to sleep. I think everyone else is asleep already."
    scene v141264 with dissolve
    z "Yeah... Good night, guys."
    scene v141265 with dissolve
    vns "Night..." (multiple=2)
    vns "Good night." (multiple=2)
    scene v141266 with dissolve
    pause(1)
#12) Sirius and Artemis incounter:
    scene black with Dissolve(2)
    pause(1)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(2)
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
    scene v141267 with Dissolve(1)
    play music "audio/Sirius's theme.mp3" volume 0.4 fadeout 1.0 fadein 5.0 loop
    Character("Girl") "So the goddess didn't shoot?"
    scene v141268 with dissolve
    tresha "No..."
    scene v141267 with dissolve
    Character("Girl") "A man comes spying on her bathing and leaves unharmed?"
    Character("Girl") "Quite unusual, no?"
    scene v141269 with dissolve
    tresha "Well... He wasn't just any man..."
    tresha "He looks very different... But I think I know who it was..."
    scene v141267 with dissolve
    Character("Girl") "Who?"
    scene v141270 with Dissolve(1)
    artemis "Sirius..."
    scene v141271 with dissolve
    srs "..."
    srs "How have you been, Arti?"
    scene v141272 with Dissolve(1)
    artemis "..."
    scene v141273 with Dissolve(1)
    pause(1)
    scene v141274 with Dissolve(1)
    pause(1)
    #Looks at his torn arm and eye
    scene v141275 with Dissolve(1)
    artemis "No."
    scene v141276 with dissolve
    artemis "I refuse to believe it."
    artemis "You're not Sirius."
    scene v141284 with dissolve
    pause(1)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    scene v141277 with Dissolve(1.5)
    #Artemis remembers how sirius, a mortal, managed to take down the last pheonix (was sirius's friend) when it went crazy thanks to athena playing arti.
    play background_s "audio/fire_in_kitchen.mp3" volume 0.6 fadeout 1.0 fadein 1.0 loop
    srs "Get back inside."
    scene v141278 with dissolve
    artemis "But-"
    srs "I'll deal with it."
    artemis "..."
    artemis "You'll deal with it?"
    artemis "Wait... It's my mess up... I'll fix it someh-"
    srs "Arti."
    srs "Go inside the temple."
    artemis "But Sirius!"
    artemis "It's a pheonix! Even gods can barely fight them."
    srs "..."
    scene v141279 with dissolve
    srs "Do as I say, Arti."
    scene v141280 with Dissolve(1)
    artemis "..."
    play sound "audio/explosion (slow mo).mp3"
    pause(0.5)
    scene v141281 with Dissolve(1)
    #Skip to a shot of the pheonix falling from the sky.
    artemis "..." #Looking at it falling shocked.
    scene v141282 with Dissolve(1)
    pause(1.5)
    scene v141283 with Dissolve(1)
    pause(1.5)
    #Fade to current artemis.
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
    scene v141285 with Dissolve(1)
    artemis "Sirius is dead. He died at the eclipse."
    artemis "I let him die. He wouldn't have lost if it weren't for my eclipse."
    scene v141286 with dissolve
    artemis "I might as well have killed him myself."
    scene v141284 with dissolve
    artemis "..."
    scene v141286 with dissolve
    artemis "You..."
    scene v141287 with Dissolve(1)
    srs "Arti..." #Approaches her.
    scene v141288 with dissolve
    artemis "..."
    scene v141289 with dissolve
    artemis "No..."
    artemis "Stay the fuck back!"
    scene v141290 with dissolve
    artemis "Sirius is dead! I killed him!"
    scene v141291
    play sound "audio/Cloth_rustle.wav"
    with hpunch
    srs "..." #Hugs her.
    play sound "audio/Cloth_rustle.wav"
    scene v141292 with dissolve
    artemis "No..."
    scene v141293 with dissolve
    artemis "{i}Breaks down crying.{/i}"
    artemis "I'm sorry..."
    artemis "I'm so fucking sorry..."
    artemis "It's all my fault..."
    artemis "It's all my fault, it's all my fa-..."
    srs "Shhh..."
    srs "Stop."
    artemis "{i}Continues crying.{/i}"
    stop music fadeout 3.0
    pause(1.5)
    #Skip to after:
    scene v141294 with Dissolve(1)
    artemis "That's not possible."
    artemis "You'll die."
    scene v141295 with dissolve
    artemis "Ichor will be as good as poison in your veins."
    artemis "Perhaps being feared by the gods made you actually forget?"
    scene v141294 with dissolve
    artemis "You aren't a god, Sirius."
    artemis "Mortals can't withstand the power of ichor."
    scene v141296 with dissolve
    srs "Is that a fact, now?"
    scene v141297 with dissolve
    artemis "..."
    scene v141298 with dissolve
    artemis "The boy..."
    scene v141300 with dissolve
    play music "audio/Zycris's theme.mp3" volume 0.3 fadeout 1.0 fadein 6.0 loop
    artemis "You..."
    artemis "You've met him?"
    artemis "It's true then?"
    artemis "He has it?"
    scene v141299 with dissolve
    srs "Yes."
    srs "And so did his father before him."
    srs "I spilled it myself."
    artemis "..."
    scene v141300 with dissolve
    artemis "How..."
    scene v141299 with dissolve
    artemis "..." #Looks at srs again.
    scene v141301 with dissolve
    artemis "Look... It doesn't matter."
    artemis "It'll kill you. You've no idea how many mortals tried."
    artemis "It kills them all."
    scene v141302 with dissolve
    srs "You won't talk me out of this, Arti."
    artemis "..."
    scene v141301 with dissolve
    artemis "Well, maybe not."
    artemis "But I won't lead you to it either."
    scene v141302 with dissolve
    srs "..."
    srs "I see..."
    #Gets up.
    srs "Was really good to see you again."
    scene v141303 with dissolve
    srs "Goodbye, Arti."
    scene v141304 with dissolve
    pause(1.5)
    #Starts to leave
    play sound "audio/rustle 2.mp3"
    scene v141305 with Dissolve(1)
    artemis "Wait!"
    scene v141306 with dissolve
    srs "..."
    scene v141308 with dissolve
    artemis "Why?"
    artemis "What are you hoping the ichor will give you that you don't already have?"
    artemis "What do you plan to do with it?"
    scene v141306 with dissolve
    srs "..."
    scene v141307 with dissolve
    srs "If I tell you..."
    srs "Will you tell me where I can find it?"
    scene v141309 with dissolve
    artemis "You're such an idiot still..."
    artemis "Can't you tell I already decided to tell you?"
    scene v141310 with dissolve
    srs "..."
    scene v141311 with Dissolve(1)
    srs "I..."
    srs "That boy..."
    srs "[mc_name]..."
    srs "He could heal."
    srs "If his arm were to be cut off, he could regrow it in less than a minute."
    artemis "..." #Surprised
    scene v141312 with dissolve
    artemis "I don't believe you..."
    scene v141313 with dissolve
    artemis "Not even my father can do that..."
    scene v141311 with dissolve
    srs "It's true."
    srs "I saw it with my own eyes."
    artemis "..."
    scene v141312 with dissolve
    artemis "So you think if you drink the ichor..."
    artemis "You can get your arm and eye back."
    artemis "Is that it?"
    scene v141311 with dissolve
    srs "..."
    srs "Yes."
    scene v141312 with dissolve
    artemis "And then..."
    artemis "You'll kill them?"
    scene v141314 with Dissolve(1)
    artemis "My sister. My uncle."
    artemis "My twin brother too?"
    scene v141315 with dissolve
    srs "..."
    artemis "..."
    scene v141316 with Dissolve(1)
    artemis "Sirius." #Stands.
    artemis "If you can best me, I'll tell you where you'll find ichor."
    scene v141317 with dissolve
    srs "You just said you'd tell me-"
    play audio "audio/cloth.mp3"
    scene v141318 with Dissolve(1)
    artemis "I lied." #Grabs her bow.
    play sound "audio/Magic 9.mp3"
    scene v141319 with Dissolve(1)
    srs "..."
    pause(1)
    #Sirius wins./ Artemis is thrown on the ground.
    #It's at the end of rainbows.
    #Later, Sirius is interrupted before he actually reaches the ichor cause he's called by Anabelle and yumi who are in trouble fighting Athena, so he fights athena without it.
    #Artemis tells Sirius that she wouldn't help him kill her twin. He'll have to do that himself.
#13) Dream and next morning:
    #At night, Z dreams about Helena where all her koniochi friends die    to protect a black belt man. He's the man in the dream.
    scene black with Dissolve(2)
    pause(1)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    play background_s "audio/cave.mp3" fadeout 1.0 fadein 1.0 loop
    pause(2)
    scene v141320 with Dissolve(1)
    z "..."
    z "(What...)"
    scene v141321 with Dissolve(1)
    z "What the..."
    z "Who-"
    play sound "audio/whoosh.mp3"
    scene v141322 with hpunch
    hlna "Wait! We'll open a window for you to attack it!"
    scene v141323 with dissolve
    z "What?! What do you mean we?!"
    #More koniochi show up.
    play sound "audio/sword draw.mp3"
    play music "audio/Auge's theme.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
    scene v141324 with Dissolve(1)
    z "Wait! Don't rush at it! We don't know what it even is or what it can do!"
    hlna "Go!"
    play sound "audio/whoosh cinematic.mp3"
    scene v141325 with hpunch
    z "Wait! No!"
    #They dissapear in the darkness. Z follows.
    #All are corpses except for helena.
    #Z goes to her.
    scene v141326 with Dissolve(1)
    z "Helena?"
    scene v141327 with Dissolve(1)
    z "..."
    z "Gods... Why did you..."
    z "We should've attacked together..."
    hlna "No..."
    hlna "Kuniochi are there to shield you..."
    hlna "Only a man like you could kill this thing..."
    hlna "It'd make no sense for you to throw your life away like us."
    hlna "You're our only hope..."
    scene v141328 with Dissolve(1)
    z "..."
    scene v141329 with dissolve
    z "?"
    hlna "Kill it..."
    play sound "audio/Magic 9.mp3"
    scene v141330 with Dissolve(1)
    z "..."
    play sound "audio/explosion2 (loud).mp3"
    play audio "audio/Magic 8.mp3"
    stop background_s fadeout 4.0
    stop background_s2 fadeout 4.0
    scene v141331 with vpunch
    z "Ughh!"
    scene v141332 with Dissolve(1)
    z "..."
    scene v141333 with dissolve
    pause(1.5)
    scene v141334 with Dissolve(1)
    z "Huh?"
    scene v141335 with Dissolve(1)
    z "Who-"
    play sound "audio/Cloth_rustle.wav"
    scene v141336 with Dissolve(1)
    athna "Ughh..."
    #Sth from behind attacks him. Z attacks back.
    #It's athena (HAS LONG HAIR). She's knocked down bleeding from her nose. Light is back.
    play audio "audio/Magic 9.mp3"
    scene v141337 with Dissolve(1)
    "Disgraceful."
    "How can you be an Olympian if demi-gods can throw you around like this..."
    scene v141338 with dissolve
    athna "Wait! Father-"
    play audio "audio/Magic 9.mp3"
    scene v141339 with dissolve
    pause(1)
    scene v141340 with dissolve
    athna "..."
    play background_s "audio/fire_in_kitchen.mp3" volume 0.6 fadeout 1.0 fadein 1.0 loop
    scene v141341 with Dissolve(1)
    pause(2)
    play sound "audio/pick up 2.mp3"
    scene v141342 with dissolve
    pause(1)
    scene v141343 with Dissolve(1)
    athna "..."
    scene v141344 with Dissolve(1)
    athna "AAAAAHHHH!{w=1}{nw}"
    scene v141345
    play sound "audio/metal hit.mp3"
    stop background_s
    stop background_s2
    stop music
    with vpunch
    #Leaves.
    #Z is shocked to see this.
    #Crying Athena (has short hair now) is smithing her shield from her own hair.
    #She bangs her shield with a hammer to shape it, Z wakes up to hailey banging a pot lid with a spoon or sth to wake him up.
    z "!!!"
    pause(1)
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
    z "..."
    z "Hailey, for fuck's sake..."
    scene v141346 with dissolve
    hly "What? I'm just trying to wake you up."
    scene v141347 with dissolve
    z "Just wake me up fucking normally, will you?"
    hly "..."
    scene v141348 with dissolve
    hly "I'll think about it."
    scene v141347 with dissolve
    z "..."
    z "Give me a few minutes to put on my shirt..."
    scene v141346 with dissolve
    hly "Okay... I'm gonna go get dressed too."
    scene v141347 with dissolve
    pause(1)
    #She's opening up.
    scene v141349 with Dissolve(1.5)
    pause(1)
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.7 fadeout 1.0 fadein 1.0 loop
    scene v141350 with dissolve
    z "Good morning."
    play music "audio/Brethren.mp3" volume 0.3 fadeout 1.0 fadein 5.0 loop
    scene v141351 with Dissolve(1)
    Tenebra "Oh. You're back, huh?"
    Tenebra "I'm not open yet though, I'm afraid. Give me 30 minutes and you can buy whatever you want."
    scene v141352 with dissolve
    z "Well... No, that's not why I'm here."
    scene v141353 with dissolve
    Tenebra "Pardon?"
    scene v141354 with dissolve
    z "Say..."
    z "I need to know if someone's been buying transformation potions from you."
    scene v141355 with dissolve
    Tenebra "Well, obviously a lot of people do. It's my speciality after all. You said so yourself yesterday remember?"
    scene v141354 with dissolve
    z "Yeah, I know. But I need more details."
    scene v141356 with dissolve
    Tenebra "Meaning?"
    scene v141354 with dissolve
    z "Who exactly has been buying them."
    Tenebra "..."
    scene v141355 with dissolve
    Tenebra "I'm sorry. Can't help you there."
    scene v141354 with dissolve
    z "What? Why not?"
    scene v141356 with dissolve
    Tenebra "I won't sell my customers. Most people who do need a transformation potion for whatever reason wouldn't want everyone knowing they use it, would they? I'm sure you can understand?"
    scene v141354 with dissolve
    z "Yeah. I do. But this is different. This is about the killings."
    z "We think the monster who killed all these men is using a transformation potion, which you are probably providing, to blend in with the people of the town."
    Tenebra "..."
    scene v141356 with dissolve
    Tenebra "I understand."
    scene v141354 with dissolve
    z "So, you'll hel-"
    Tenebra "And I stand by my previous statement. I shan't sell my customers."
    scene v141354 with dissolve
    z "Even if one is a murdering monster?"
    scene v141356 with dissolve
    Tenebra "Even if, and that's a big if, you're right. Then yes. Even if one is a murdering monster."
    Tenebra "It's called sticking to your principles. I'm sure a ninja like you will understand."
    scene v141354 with dissolve
    z "No. I actually don't understand."
    scene v141356 with dissolve
    Tenebra "I'm afraid I made my decision."
    Tenebra "Your patronage is still very welcome in my shop. And the discount still stands. But that's all you're getting from me."
    scene v141354 with dissolve
    z "..."
    z "If you help us here, you can save dozens of people."
    z "We won't tell a single soul who your customers are and what they buy, I promise. We just need it to find who the monster is and rid this town of it."
    Tenebra "..."
    scene v141356 with dissolve
    Tenebra "I'm sorry. I cannot help you, ninja."
    Tenebra "Good luck with your investigation."
    play sound "audio/creaky door.mp3"
    scene v141358 with Dissolve(1)
    pause(1)
    #Goes inside.
    scene v141359 with Dissolve(1)
    hly "..."
    z "That didn't go as planned..."
    scene v141360 with dissolve
    hly "Yeah..."
    scene v141361 with dissolve
    hly "Any suggestions?"
    scene v141359 with dissolve
    z "..."
    z "One..."
    pause(2)
    #Skip to brothel.
#14) Brothel second visit:
    #They go in.
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene v141362 with Dissolve(1)
    play music "audio/Clair de Lune.mp3" fadeout 1.0 fadein 4.0 loop
    helda "Hello and wel-"
    scene v141363 with dissolve
    helda "Oh! You're back!"
    helda "With a new partner no less!"
    scene v141364 with dissolve
    pause(1)
    scene v141365 with Dissolve(1)
    hly "..."
    scene v141366 with dissolve
    helda "I would've suggested buying some of the girls' services but you seem doing well getting them yourself, huh..."
    helda "We offer special treatment for second timers here, would you be interested?"
    scene v141367 with Dissolve(1)
    z "Uhhh... Does it envolve going to the main lobby?"
    scene v141368 with dissolve
    helda "Of course! It's part of the experience."
    scene v141367 with dissolve
    z "Then sure..."
    scene v141368 with dissolve
    helda "Splendid!"
    scene v141367 with dissolve
    pause(1)
    #Skip
    #Z is in a hot spring.
    play background_s "audio/water.mp3" fadeout 1.0 fadein 1.0 loop
    scene v141369 with Dissolve(1)
    z "Ahhh..."
    scene v141370 with dissolve
    z "(Damn... This is nice...)"
    play sound "audio/Cloth_rustle.wav"
    scene v141371 with Dissolve(1)
    hly "Oh this place is amazing!"
    scene v141372 with Dissolve(1)
    z "I know, right?"
    scene v141373 with dissolve
    hly "But we can't stay here... We need to focus on the obj-"
    scene v141374 with dissolve
    z "{size=-10}Shhh... There's someone behind you...{/size}"
    scene v141375 with dissolve
    hly "..."
    scene v141376 with dissolve
    z "I have an idea."
    hly "Hm?"
    z "Get in the water, I'll explain."
    scene v141377 with dissolve
    hly "Okay."
    scene v141378 with Dissolve(1)
    pause(1.5)
    play sound "audio/leather.wav" volume 0.4
    scene v141379 with Dissolve(1)
    pause(1.5)
    play sound "audio/cloth.mp3"
    scene v141380 with Dissolve(1)
    pause(1.5)
    play sound "audio/Cloth_rustle.wav"
    scene v141381 with Dissolve(1)
    pause(1.5)
    scene v141382 with Dissolve(1)
    pause(1.5)
    play sound "audio/pick up 2.mp3"
    scene v141383 with Dissolve(1)
    #Strips in front of him.
    z "..."
    hly "..."
    scene v141384 with dissolve
    #Notices he's looking.
    hly "Dude... You're supposed to look away..."
    scene v141385 with dissolve
    z "Sorry... You should've warned me."
    play sound "audio/creak.mp3"
    scene v141386 with Dissolve(1)
    hly "..." #Sus.
    if came_from_gallery == 0:
        $ hly_lst += 2
    show screen button_lst with dissolve
    play sound "audio/stats.wav"
    hide screen button_lst with dissolve
    play sound "audio/splash.mp3"
    scene v141387 with Dissolve(1)
    z "..."
    #Goes in.
    z "So..."
    z "They said we could ask for girls to join us."
    z "We can ask for the succubus girl. Once she comes here, one of us, well... Stays with her. While the other says the want to go to the bathroom or something and sneaks into her room while she's here."
    scene v141388 with dissolve
    hly "Ooooh... That could work, yeah."
    scene v141389 with dissolve
    hly "We don't know where her room is though."
    scene v141387 with dissolve
    z "Well, the one who tries to sneak into it will have to figure it out somehow."
    hly "..."
    scene v141389 with dissolve
    hly "Okay... So... Who stays with her?"
    scene v141387 with dissolve
    z "Well..."
    scene v141391 with dissolve
    hly "Are they gonna... With her... You know..."
    scene v141390 with dissolve
    z "I mean... It's a brothel, after all..."
    hly "..." #Embarrassed.
    scene v141391 with dissolve
    hly "Well... Just so you know, I'm not into girls..."
    scene v141390 with dissolve
    z "Well as it so happens, I am."
    scene v141392 with dissolve
    hly "I noticed..."
    hly "So, you stay with her while I sneak there?"
    scene v141390 with dissolve
    z "Sounds like a plan."
    scene v141392 with dissolve
    hly "Okay..."
    scene v141390 with dissolve
    z "I'll go ask for her."
    pause(1)
    play sound "audio/splash.mp3"
    scene v141393 with Dissolve(1)
    z "Hi."
    scene v141394 with dissolve
    Character("Girl") "Can I help you, sir?"
    scene v141393 with dissolve
    z "Yeah... Yesterday I saw this blond girl who works here with short hair and blue eyes... I didn't get her name."
    scene v141394 with dissolve
    Character("Girl") "Oh, you mean Babylon?"
    scene v141393 with dissolve
    z "Yeah. I guess so. Can I ask for her."
    scene v141394 with dissolve
    Character("Girl") "Of course. I'll go check if she's not busy."
    scene v141393 with dissolve
    z "Oh, and... Can you give us some privacy if she's available."
    scene v141394 with dissolve
    Character("Girl") "Certainly."
    play sound "audio/Cloth_rustle.wav"
    scene v141395 with Dissolve(1)
    pause(1)
    #Leaves.
    scene v141396 with Dissolve(1)
    z "Now, Hailey."
    play sound "audio/splash.mp3"
    scene v141397 with Dissolve(1)
    hly "Gotcha."
    play audio "audio/cloth.mp3"
    scene v141398 with Dissolve(1)
    hly "I'll make it as quick as I can."
    play sound "audio/Cloth_rustle.wav"
    scene v141399 with Dissolve(1)
    pause(1)
    scene v141400 with Dissolve(1)
    z "(Okay... Nothing to do but wait.)"
    #She also leaves.
    pause(2)
    play sound "audio/splash.mp3"
    scene v141401 with Dissolve(2)
    pause(1.5)
    play sound "audio/Cloth_rustle.wav"
    scene v141402 with Dissolve(1)
    #Babylon comes to Z. She's wearing revealing swimming clothes.
    Character("Babylon") "Hey, sir. I heard you asked for me perso-"
    scene v141403 with dissolve
    Character("Babylon") "..." #Notices it's Z
    scene v141404 with dissolve
    z "..."
    scene v141405 with dissolve
    z "(I think she knows I know what she is...)"
    z "(But until I can prove it I don't wanna raise suspicion. Especially since Hailey is trying to sneak into her room.)"
    z "(Let's play this as nicely as I can.)"
    z "(Imma play dumb...)"
    scene v141406 with dissolve
    z "Aren't you a bit too shy to be in this kind of..."
    z "...business?"
    scene v141408 with dissolve
    Character("Babylon") "..."
    scene v141407 with dissolve
    Character("Babylon") "You..."
    Character("Babylon") "Aren't you..."
    scene v141408 with dissolve
    z "Hm?"
    z "Yeah?"
    Character("Babylon") "..."
    scene v141409 with dissolve
    Character("Babylon") "N-No... It's nothing..."
    scene v141410 with dissolve
    Character("Babylon") "{i}Sighs.{/i}"
    scene v141411 with dissolve
    Character("Babylon") "I'm sorry sir... I wanted to say that I'm very flattered to hear that you asked for me personally."
    Character("Babylon") "My name is Babylon. It'll be my pleasure to keep you entertained today."
    scene v141412 with dissolve
    z "Nice to meet you, Babylon. My name is [mc_name]."
    scene v141413 with dissolve
    Character("Babylon") "May I come in?"
    scene v141414 with dissolve
    z "Of course."
    z "(Okay looks like she dropped her gaurd.)"
    pause(1)
    #Comes close to Z almost touching him.
    play sound "audio/splash.mp3"
    scene v141415 with Dissolve(1)
    Character("Babylon") "I thought you had a partner already? The girl I saw you with yeste-"
    scene v141416 with dissolve
    z "I'd rather not talk about that. Is that okay? (let's not let her poke around...)"
    scene v141415 with dissolve
    Character("Babylon") "Oh, I'm sorry... Of course."
    play sound "audio/Cloth_rustle.wav"
    scene v141417 with Dissolve(1)
    Character("Babylon") "Don't worry... I can help you not think about that at all..." #Gets closer.
    scene v141418 with dissolve
    pause(1)
    menu:
        "'Distract' her with sexual stuff.":
            z "(It is a brothel, after all. Only one thing can be expected if a customer asked for one of the girls...)"
            play sound "audio/Cloth_rustle.wav"
            label G57:
                $ persistent.g_57_unlock = 1
            scene v141422 with Dissolve(1)
            Character("Babylon") "Hahhn~..."
            play audio "audio/Cloth_rustle.wav"
            scene v141423 with Dissolve(1)
            Character("Babylon") "Ahhnn~..."
            pause(1)
            show v14m39 with Dissolve(1)
            pause(1)
            Character("Babylon") "Ahh~..."
            Character("Babylon") "So rough... Ahhhhhnn~..."
            Character("Babylon") "Ahhhh~... "
            Character("Babylon") "Girl boobs are... Ahhh~... Sensitive you know..."
            Character("Babylon") "Ahhhhhnnn~... Ohhh~..."
            Character("Babylon") "I forgot to bring a condom..."
            Character("Babylon") "Fuckkk~... I don't want to go get one... Ahhh~..."
            Character("Babylon") "Ohhh~... Just pull out, okay?"
            play audio "audio/kiss.mp3"
            scene v141424 with Dissolve(1)
            Character("Babylon") "Hmnnn~..."
            scene v141425 with Dissolve(1)
            Character("Babylon") "Nhhhmmm~..."
            scene v141426 with Dissolve(1)
            Character("Babylon") "Hahhhh~..."
            play sound "audio/splash.mp3"
            scene v141427 with vpunch
            Character("Babylon") "?!"
            scene v141428 with dissolve
            Character("Babylon") "Don't cum inside, okay?"
            scene v141429 with dissolve
            z "I won't."
            scene v141430 with dissolve
            Character("Babylon") "..."
            show v14m40 with Dissolve(1)
            $ renpy.pause(2, hard=True)
            show v14m41 with Dissolve(1)
            pause(1)
            Character("Babylon") "Ahhhn~... Ahhhhhh~... Ahhhhhhh~..."
            Character("Babylon") "Fuhhcck~..."
            Character("Babylon") "Ahhhnnnn~... It's sooo deeehhpp~..."
            Character("Babylon") "Ah~... Ohhhh~... Hahhh~..."
            Character("Babylon") "Aren't you... Ahhhh~..."
            Character("Babylon") "You're not getting... Ahhh~... Tired?"
            z "I'm good, don't worry..."
            Character("Babylon") "But... Ahhh~... I'm heavy..."
            z "Not really."
            Character("Babylon") "Ohhhh~... I've never tried this position before..."
            Character("Babylon") "I really... Ahhhh~... Really like it..."
            Character("Babylon") "Fuuhcck~... You're really good at this..."
            Character("Babylon") "I think I'm..."
            Character("Babylon") "Ahhhnnn~... Ahhhhhh~... I'm cumming..."
            Character("Babylon") "I'm cumming... I'm fuckkk~..."
            pause(1)
            scene v141431
            play sound "audio/magic 7.mp3"
            with vpunch
            Character("Babylon") "OOOOHHHH~!"
            pause(1)
            play sound "audio/splash.mp3"
            scene v141432 with Dissolve(1)
            Character("Babylon") "Fuhhhhhcckk~..."
            scene v141433 with Dissolve(1)
            Character("Babylon") "Gods... Even my arms are numb..."
            scene v141434 with Dissolve(1)
            Character("Babylon") "That was so g-"
            play audio "audio/creak.mp3"
            scene v141435 with dissolve
            Character("Babylon") "?!"
            play sound "audio/splash.mp3"
            scene v141436 with dissolve
            Character("Babylon") "Ooooohhh~... Holy fuckkk~..."
            pause(1)
            show v14m42 with Dissolve(1)
            pause(1)
            Character("Babylon") "Ahhhh~... Ahhhnnn~..."
            Character("Babylon") "Fuucckkk~..."
            Character("Babylon") "You're still... You can stillll~... Ahhhh~..."
            Character("Babylon") "Annnhhhh~... Fucckkkk~... How much stamina do you have..."
            Character("Babylon") "Haannnhhh~... Ahhh~..."
            Character("Babylon") "Gods... Ahhh~... Ohhhh~..."
            Character("Babylon") "Hnnnn~... Ahhhnn~..."
            Character("Babylon") "Hahhhhhh~... I'm close..."
            Character("Babylon") "[mc_name]... I'm gonna..."
            Character("Babylon") "Ahhhnnn~... I'm gonna cum again..."
            z "I'm about to cum too..."
            Character("Babylon") "Ahhhhh~..."
            play audio "audio/Cloth_rustle.wav"
            scene v141437 with Dissolve(1)
            hly "Okay, I'm back."
            scene v141438 with Dissolve(1)
            hly "What the-"
            if came_from_gallery == 1:
                $ came_from_gallery = 0
            $ renpy.end_replay()
            play sound "audio/splash.mp3"
            scene v141439 with hpunch
            Character("Babylon") "Ah! I'm sorry!"
            play audio "audio/Cloth_rustle.wav"
            scene v141440 with Dissolve(1)
            z "Wait! It's okay!"
            scene v141441 with dissolve
            hly "..."
            z "(Fuck... I was so close...)"
            scene v141442 with Dissolve(1)
            hly "..."
            z "Heeyyyy..."
            scene v141445 with dissolve
            hly "Hey."
            scene v141443 with dissolve
            z "(She's totally looking at my dick...)"
            if came_from_gallery == 0:
                $ hly_lst += 2
            show screen button_lst with dissolve
            play sound "audio/stats.wav"
            hide screen button_lst with dissolve
            z "(This is a bit awkward.)"
            z "(Let's get some conversation going.)"
            #She tells him since it's his first time with one of the girls, it'll be free.
        "Just distract her by chatting with her.":
            scene v141419 with dissolve
            z "Yeah... Honestly, it would be nice to have a chat with you."
            play sound "audio/Cloth_rustle.wav"
            scene v141420 with dissolve
            Character("Babylon") "Oh..."
            Character("Babylon") "Sure. Is there something you'd like to tell me about?"
            Character("Babylon") "Helda said you were a ninja, right? Tell me about your adventurers..."
            scene v141421 with dissolve
            z "Well... Yeah... How about the time when..."
            pause(1.5)
            scene black with Dissolve(2)
            #Skip to hailey coming back.
    #Hailey could only snatch steal a key from one of the girls. She says they all sleep in a common dorm.
    scene v141442 with Dissolve(1)
    z "So... How did it go?" #Both wearing towels only
    scene v141444 with dissolve
    hly "Well... All the girls sleep in one room... And it's always locked."
    hly "And that one pale girl stayed in the room the whole time, so I couldn't get in..."
    scene v141442 with dissolve
    z "Shit... So that didn't go anywhere..."
    scene v141444 with dissolve
    hly "Well, but I did manage to snatch the key from one of the girls."
    scene v141442 with dissolve
    z "..."
    z "Where is their room?"
    scene v141446 with Dissolve(1.5)
    pause(1.5)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    #Skip to them going there.
    scene v141447 with dissolve
    hly "She's probably still in there... So what's the plan?"
    scene v141448 with dissolve
    z "Well, I can also ask for he-"
    play sound "audio/creaky door.mp3"
    scene v141449 with dissolve
    #She leaves the room.
    hly "!" (multiple=2)
    z "!" (multiple=2)
    scene v141450 with dissolve
    pause(1)
    scene v141451 with dissolve
    pause(1)
    #She locks the door behind her.
    play sound "audio/door_lock.mp3"
    scene v141452 with Dissolve(1)
    z "There's our chance."
    play sound "audio/creaky door.mp3"
    scene v141453 with dissolve
    pause(1)
    play audio "audio/Door close.mp3"
    scene v141454 with dissolve
    pause(1.5)
    scene v141455 with Dissolve(1.5)
    pause(1.5)
    scene v141456 with Dissolve(1)
    #They go in.
    hly "..."
    scene v141457 with dissolve
    hly "So, transformation potions, right?"
    scene v141458 with dissolve
    z "Yeah. Or anything of that sort."
    scene v141459 with dissolve
    pause(1)
    scene v141460 with Dissolve(1)
    z "This one is weirdly empty..."
    pause(1)
    scene v141461 with dissolve
    #They look around for a bit.
    hly "[mc_name]..."
    hly "Look at this."
    scene v141462 with dissolve
    pause(1)
    #Goes to her.
    play sound "audio/pick up 2.mp3"
    scene v141463 with Dissolve(1)
    z "..."
    z "It looks exactly like the bottle Lumi got for his mom yesterday."
    scene v141464 with dissolve
    hly "So that means..."
    scene v141465 with dissolve
    Character("Girl") "{size=-20}I don't know! Maybe I left it inside?{/size}"
    z "?!" (multiple=2)
    hly "!!!" (multiple=2)
    scene v141466
    play sound "audio/whoosh.mp3"
    with hpunch
    #Throws them on the floor.
    hly "Hide!" (multiple=2)
    Character("Girl 2") "{size=-20}Okay, fine. I'll open it for you.{/size}" (multiple=2)
    scene v141467 with dissolve
    play sound "audio/keys.mp3"
    pause(1.5)
    #The girls go in.
    play sound "audio/creaky door.mp3"
    scene v141468 with dissolve
    Character("Girl 2") "Be quick about it please... Helda said I needed to be in the lobby like 5 minutes ago."
    scene v141470 with Dissolve(1)
    Character("Girl 1") "No, it's okay. You can leave it unlocked. I'm staying here anyway. My shift is over."
    scene v141469 with dissolve
    Character("Girl 2") "What? Why did you even go out, then?"
    scene v141470 with dissolve
    Character("Girl 1") "Forgot something in one of the rooms."
    scene v141471 with Dissolve(1)
    Character("Girl 2") "Oh. Okay then. See ya later."
    Character("Girl 1") "Thanks! I'll look around."
    #Z and Hailey are hiding in a locker if possible.
    #Her boobs are in his face.
    scene v141472 with Dissolve(1)
    z "{size=-10}Fuck... She's staying?{/size}"
    scene v141473 with dissolve
    hly "{size=-10}This place is extremely crammed...{/size}"
    hly "{size=-10}Also can you not breathe on my boobs... They are sensitive...{/size}"
    scene v141474 with dissolve
    z "{size=-10}Well, I'm sorry but I can't not breathe, Hailey.{/size}"
    z "..."
    menu:
        "Try to use your quick movement magic to get the two of you out of here.":
            z "{size=-10}I think I have a way to get us out of here...{/size}"
            z "{size=-10}Hold on tight, okay?{/size}"
            scene v141473 with dissolve
            hly "{size=-10}Okay...{/size}"
            play sound "audio/Magic 9.mp3"
            scene v141475 with Dissolve(1)
            hly "?!"
            play audio "audio/whoosh cinematic.mp3"
            scene v141476 with Dissolve(1)
            pause(1)
            scene v141477 with Dissolve(1)
            pause(2)
            #Ends the scene.
        "Just wait until the girl leaves.":
            label G58:
                $ persistent.g_58_unlock = 1
            scene v141473 with dissolve
            hly "{size=-10}Uhmmm...{/size}"
            hly "{size=-10}[mc_name]?{/size}"
            scene v141474 with dissolve
            z "{size=-10}Yeah?{/size}"
            scene v141473 with dissolve
            hly "{size=-10}Are you...{/size}"
            scene v141478 with Dissolve(1)
            hly "{size=-10}I can feel your...{/size}"
            hly "{size=-10}Did your towel fall too?{/size}"
            z "{size=-10}I think so, yeah...{/size}"
            pause(1)
            z "(Fuck... This is making me really fucking horny...)"
            show v14m43 with Dissolve(1)
            pause(1)
            z "{size=-10}Stop moving... You're gonna get us busted...{/size}"
            hly "{size=-10}I'm not moving...{/size}"
            hly "{size=-10}Not intentionally...{/size}"
            z "..."
            z "(My dick...)"
            z "(She's rubbing it with her thighs...)"
            z "(Fuck... This is basically a thighjob...)"
            hly "{size=-10}[mc_name]...{/size}"
            hly "{size=-10}What are we doing...{/size}"
            z "{size=-10}I don't know...{/size}"
            z "{size=-10}But I can't really stop...{/size}"
            hly "..."
            hly "{size=-10}I can't either...{/size}"
            z "{size=-10}Fuck it...{/size}"
            pause(1)
            play audio "audio/kiss.mp3"
            show v14m44 with Dissolve(1)
            pause(1)
            hly "{size=-10}Ahhh~... My boob...{/size}"
            hly "{size=-10}I told you... It's sensitive...{/size}"
            hly "{size=-10}Ahhh~... Oh gods...{/size}"
            hly "{size=-10}Fuhhcckkk~... You're pulling my nipples so hard...{/size}"
            hly "{size=-10}Ahhhhhh~.. I'm...{/size}"
            hly "{size=-10}FuccckkK~... I'm losing it... I...{/size}"
            pause(1)
            scene v141479 with Dissolve(1)
            hly "{size=-10}Hahhh~...{/size}"
            scene v141480 with Dissolve(1)
            z "..."
            play audio "audio/kiss.mp3"
            scene v141481 with Dissolve(1)
            hly "{size=-10}Hmmmnnn~...{/size}"
            pause(1)
            show v14m45 with Dissolve(1)
            pause(1)
            hly "{size=-10}Mmnnnn~...{/size}"
            hly "{size=-10}Fuhhmmmmnn~...{/size}"
            hly "{size=-10}Nuhhhmmmnnn~...{/size}"
            hly "{size=-10}Ahhmmmnnnnnn~... Hnnnmmm~...{/size}"
            hly "{size=-10}Fuhhmmmnn~... Imnn~...{/size}"
            hly "{size=-10}Ghhhmmmnnnn~...{/size}"
            hly "{size=-10}Ahhnnnmm~... Hmmnn~...{/size}"
            hly "{size=-10}Mnnnnhh~...{/size}"
            hly "{size=-10}Nmmmhhh~...{/size}"
            hly "{size=-10}Ahhhmmnnn~... Waiihhmmnn~...{/size}"
            hly "{size=-10}Waaaiihhttttmmnn~...{/size}"
            pause(1)
            scene v141482 with Dissolve(1)
            hly "{size=-10}Hannhh~...{/size}"
            scene v141483 with dissolve
            z "{size=-10}Are you okay?{/size}"
            scene v141484 with dissolve
            hly "..."
            scene v141485 with dissolve
            hly "{size=-10}If we continue...{/size}"
            scene v141484 with dissolve
            z "..."
            scene v141483 with dissolve
            z "{size=-10}How about... I just put the tip in?{/size}"
            scene v141484 with dissolve
            hly "..."
            scene v141486 with dissolve
            hly "{size=-10}The tip?{/size}"
            scene v141487 with dissolve
            hly "{size=-10}How big is it?{/size}"
            hly "{size=-10}I don't know if I'm ready for...{/size}"
            hly "{size=-10}You know...{/size}"
            scene v141488 with dissolve
            z "{size=-10}It's not too big...{/size}"
            scene v141484 with dissolve
            hly "..."
            scene v141487 with dissolve
            hly "{size=-10}Just the tip, yeah?{/size}"
            scene v141488 with dissolve
            z "{size=-10}Just the tip...{/size}"
            scene v141484 with dissolve
            hly "..."
            scene v141489 with Dissolve(1)
            hly "..."
            pause(1)
            show v14m46 with Dissolve(1)
            $ renpy.pause(6, hard=True)
            hly "{size=-10}Ahhhhnnn~...{/size}{w=3}{nw}"
            $ renpy.pause(1.5, hard=True)
            show v14m47 with Dissolve(1)
            pause(1)
            hly "{size=-10}Ahhh~... Fuckkk~...{/size}"
            hly "{size=-10}Ohhhh~... Insertion really is something else...{/size}"
            hly "{size=-10}Hooolyy fuckkk~... This is~...{/size}"
            hly "{size=-10}Ahhhnnn~...{/size}"
            hly "{size=-10}Ahhhnnn~... [mc_name]~...{/size}"
            hly "{size=-10}It's so biggg... Did I take...{/size}"
            hly "{size=-10}Ahhhh~... Did I take the whole thing?{/size}"
            z "{size=-10}Nope. Not even close... It's barely the whole tip...{/size}"
            hly "{size=-10}Fuccckk~... You're totally...{/size}"
            hly "{size=-10}You're fuckinggg~... Ahhh~... You're fucking full of shit...{/size}"
            z "{size=-10}I'm not...{/size}"
            hly "{size=-10}Ohhh~... Fuck... This is fucking amazing~... Ahhhhhh~...{/size}"
            z "{size=-10}You're kinda loud...{/size}"
            hly "{size=-10}Ahhhhnnn~... I can't help it, mmmkayyy~?{/size}"
            z "{size=-10}Well... I have a solution for that...{/size}"
            pause(1)
            play audio "audio/kiss.mp3"
            show v14m48 with Dissolve(1)
            pause(1)
            hly "{size=-10}Hnnnnmmmmm~... Ahhmnnnnn~...{/size}"
            hly "{size=-10}Funnnhhmmmmnn~...{/size}"
            z "(She's still kinda loud actually...)"
            hly "{size=-10}Nhhhhhmmmnnn~...{/size}"
            z "(Well, as long as the girl can't hear us, I guess we're good...)"
            hly "{size=-10}Mmnnmmmnn~...{/size}"
            hly "{size=-10}Ahhhmmnnn~...{/size}"
            hly "{size=-10}Hhhmmmmmnnnn~...{/size}"
            hly "{size=-10}Ahhnnnmm~... Hmmnn~...{/size}"
            play sound "audio/creak.mp3"
            Character("Girl 1") "Fucking rats again..."
            scene v141490 with hpunch
            z "!!!" (multiple=2)
            hly "{size=-10}Mnnnnhh?!{/size}" (multiple=2)
            play audio "audio/Magic 9.mp3"
            scene v141491 with Dissolve(1)
            z "..."
            play sound "audio/whoosh cinematic.mp3"
            play audio "audio/creaky door.mp3"
            scene v141492 with Dissolve(1)
            Character("Girl 1") "..."
            scene v141493 with dissolve
            Character("Girl 1") "Ughhh... I need to talk to Helda about this..."
            pause(2)
            if came_from_gallery == 1:
                $ came_from_gallery = 0
            $ renpy.end_replay()
            scene v141494 with Dissolve(1.5)
            z "Fuck... That was close..."
            play sound "audio/Cloth_rustle.wav"
            scene v141495 with dissolve
            hly "..."
            if came_from_gallery == 0:
                $ hly_lst += 8
            show screen button_lst with dissolve
            play sound "audio/stats.wav"
            hide screen button_lst with dissolve
            scene v141496 with dissolve
            z "..."
            z "Are you okay?"
            scene v141498 with dissolve
            hly "Yeah..."
            hly "You said just the tip!"
            scene v141497 with dissolve
            z "It totally was just the tip!"
            scene v141499 with dissolve
            hly "No it wasn't!"
            scene v141500 with dissolve
            z "It was!"
            hly "..."
            scene v141498 with dissolve
            hly "Did you..."
            hly "You know..."
            scene v141497 with dissolve
            z "Hm?"
            scene v141498 with dissolve
            hly "Did you also..."
            hly "Finish?"
            scene v141497 with dissolve
            z "Oh..."
            z "Not just yet, no. I was close though."
            scene v141498 with dissolve
            hly "Oh... So you didn't..."
            hly "You know, shoot anything inside?"
            scene v141497 with dissolve
            z "Nope. Don't worry."
            scene v141498 with dissolve
            hly "Fuck... Thank the gods..."
            hly "Believe it or not, I'm probably not the best mom material."
            scene v141497 with dissolve
            z "You seem to be great big sister material, so why not mom?"
            hly "..."
            scene v141498 with dissolve
            hly "Well..."
            scene v141499 with hpunch
            hly "Tamara!"
            hly "Don't fucking say a word about this to her, okay?!"
            hly "I have an example to set here!"
            scene v141500 with dissolve
            pause(1)
            if tmra_lst >= 6: #if had sex with tamara or did anything w her:
                z "{size=-20}Yeah... That ship has already-{/size}"
                scene v141499 with dissolve
                hly "What?"
                scene v141500 with dissolve
                z "Nothing!"
                hly "..."
                scene v141498 with dissolve
                hly "Anyway, we got what we came here for. Let's get out of here before someone realises something is wrong."
                scene v141497 with dissolve
                z "Yeah."
                pause(1)
            else:
                z "Yeah... Don't worry, my lips are sealed."
                hly "..."
                scene v141498 with dissolve
                hly "Thanks..."
                hly "Anyway, we got what we came here for. Let's get out of here before someone realises something is wrong."
                scene v141497 with dissolve
                z "Yeah."
                pause(1)
#15) Going back again:
    #Right outside the brothel.
    scene black with Dissolve(2)
    pause(1)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    play background_s2 "audio/Ambient_ninja_village_night.mp3" volume 0.6 fadeout 1.0 fadein 1.0 loop
    pause(2)
    scene v141501 with Dissolve(1.5)
    hly "It was amazing, by the way. How you got us out of there... How do you move so quickly?"
    scene v141502 with Dissolve(1)
    z "I'm not exactly sure to be honest with you. It's mostly instinctive when I need to get out of a bad situation."
    scene v141503 with Dissolve(1)
    hly "So you c-"
    #They notice someone wearing a hood again.
    play sound "audio/Cloth_rustle.wav"
    scene v141504 with Dissolve(1)
    z "Wait."
    scene v141505 with dissolve
    z "See that girl?"
    scene v141506 with Dissolve(1)
    hly "?"
    hly "Yeah?"
    scene v141507 with Dissolve(1)
    hly "She looks oddly suspicious..."
    z "I think it's the same girl who ran from us yesterday by the alchemist's shop."
    scene v141508 with Dissolve(1)
    z "Hey, you!"
    scene v141509 with Dissolve(1)
    Character("Girl") "..."
    z "Can I ask y-"
    play music "audio/Town of the faceless god.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v141510 with dissolve
    pause(1)
    #Runs
    scene v141511 with dissolve
    z "Wait!"
    scene v141512 with vpunch
    z "Heiley! Go!"
    scene v141514 with dissolve
    hly "Got it!"
    scene v141515 with dissolve
    pause(2)
    scene v141516 with Dissolve(2)
    pause(1)
    scene v141517 with dissolve
    #Z chases her.
    #Z loses her.
    Character("Girl") "..."
    play sound "audio/whoosh.mp3"
    scene v141518 with PushMove(0.1, mode="pushup")
    hly "AAAAHH!{w=1}{nw}"
    play audio "audio/Falling2.mp3"
    scene v141519 with vpunch
    "Ughhh..."
    #Hailey attacks her from above.
    scene v141520 with Dissolve(1)
    z "We got you this time."
    scene v141521 with dissolve
    stop music fadeout 4.0
    z "..."
    scene v141522 with dissolve
    z "Wait... That's..."
    z "LUMI?!" (multiple=2) with hpunch
    hly "Lumi!" (multiple=2)
    z "What the fuck are you doing dressed like that?!"
    lumi "..."
    scene v141523 with dissolve
    lumi "I c-can explai-"
    scene v141524 with Dissolve(1)
    vns "What's going on there!" #Venus heard the noise and comes runing.
    scene v141525 with Dissolve(1)
    mercury "Wait up, Venus!" #Runs after her.
    scene v141526 with dissolve
    vns "Mercury! I told you not to follow me! It's dangerous it could be the killer!"
    scene v141527 with dissolve
    z "Relax, guys. It's just Lumi."
    scene v141528 with dissolve
    vns "..." (multiple=2) #A hooded figure is subtly in the background!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    mercury "..." (multiple=2)
    scene v141529 with dissolve
    vns "Lumi? Why are you dressed like that?"
    scene v141530 with Dissolve(1)
    lumi "I..."
    scene v141531 with dissolve
    lumi "Well..."
    scene v141532 with dissolve
    z "..."
    play music "audio/Brethren.mp3" volume 0.3 fadeout 1.0 fadein 5.0 loop
    z "You were sneaking into the brothel."
    z "..."
    z "You dress as a girl so that the monster doesn't kill you."
    z "Right?"
    lumi "..."
    z "Lumi..."
    z "Shit... How long have you been doing this..."
    scene v141531 with dissolve
    lumi "Look, it's not easy for a guy like me to find a partner, okay?!"
    scene v141532 with dissolve
    z "..."
    scene v141533 with Dissolve(1)
    z "Guys. No one can know about this."
    z "Get me?"
    scene v141534 with dissolve
    hly "Yeah."
    scene v141535 with Dissolve(1)
    vns "Yes." (multiple=2)
    mercury "Of course." (multiple=2)
    scene v141532 with Dissolve(1)
    z "If the monster knew, it's gonna kill him."
    z "Lumi, get up."
    z "Take off that dress. I'll give you my shirt, okay?"
    scene v141530 with dissolve
    lumi "Yeah..."
    scene v141532 with dissolve
    pause(2)
    #They go home.
    scene v141536 with Dissolve(1.5)
    jacq "Lumi?"
    jacq "Where have you been?"
    jacq "What are you wearing? What happened to your clothes?"
    scene v141537 with dissolve
    lumi "..."
    scene v141539 with Dissolve(1)
    lumi "They..."
    scene v141540 with dissolve
    lumi "They got torn on my way back, so [mc_name] gave me his shirt to cover myself."
    scene v141538 with dissolve
    jacq "..."
    jacq "And where have you been exactly?"
    lumi "..."
    scene v141540 with dissolve
    lumi "I-"
    play sound "audio/Cloth_rustle.wav"
    scene v141541 with dissolve
    z "I asked him to show us around the town."
    scene v141542 with Dissolve(1)
    jacq "..."
    scene v141543 with dissolve
    jacq "So, you're helping them, huh? I told you to stay away from that business."
    scene v141544 with dissolve
    z "(Shit... I hope I didn't make it worse...)"
    lumi "..."
    scene v141545 with dissolve
    jacq "I'll let you ninjas stay this one last night in my house. But tomorrow you'll find another place to stay if you're going to be staying in Brethren."
    jacq "And you will not ask my son for any more help. Or talk to him at all for that matter."
    jacq "Is that clear."
    scene v141546 with Dissolve(1)
    lumi "Bu-" #Z stops him
    play sound "audio/Cloth_rustle.wav"
    scene v141547 with dissolve
    lumi "?"
    scene v141548 with dissolve
    z "Quite clear."
    scene v141549 with dissolve
    jacq "..."
    scene v141550 with dissolve
    #Leaves.
    z "..."
    scene v141551 with Dissolve(1)
    lumi "I'm sorry... I-"
    scene v141552 with dissolve
    z "Don't worry about it. She's right. You shouldn't endanger yourself."
    scene v141551 with dissolve
    lumi "But..."
    scene v141552 with dissolve
    z "You've done enough for us already. Let us take it from here, okay?"
    z "We will find who ever is killing people here, I promise."
    lumi "..."
    scene v141553 with dissolve
    lumi "Okay..."
    scene v141552 with dissolve
    pause(1)
#16) Last dream:
#     Z dreams about making the shield again. He is Hephaestus looking at Athena.
    scene black with Dissolve(2)
    pause(1)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(2)
    play background_s "audio/fireplace.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
    scene v141554 with Dissolve(2)
    play music "audio/Auge's theme.mp3" volume 0.3 fadeout 1.0 fadein 5.0 loop
    athna "Mirror."
    scene v141555 with dissolve
    athna "I'll call it Mirror."
    scene v141554 with dissolve
    athna "What do you think, Hephaestus?"
    scene v141556 with dissolve
    Character("Hephaestus", color = "ff9d1c") "A good strong name, little sister."
    Character("Hephaestus", color = "ff9d1c") "Do you think you can win with this?"
    athna "..."
    scene v141555 with dissolve
    athna "I have to..."
    scene v141556 with dissolve
    athna "..."
    scene v141554 with dissolve
    athna "Do YOU think I can win with it?"
    scene v141556 with dissolve
    Character("Hephaestus", color = "ff9d1c") "..."
    Character("Hephaestus", color = "ff9d1c") "You've been my most dedicated apprentice."
    scene v141554 with dissolve
    athna "Have been?"
    scene v141556 with dissolve
    Character("Hephaestus", color = "ff9d1c") "I have nothing more to teach you, little sister."
    Character("Hephaestus", color = "ff9d1c") "I believe in your skills to craft."
    Character("Hephaestus", color = "ff9d1c") "Now go prove yourself."
    athna "..."
    #Athena wins for the first time.
    #She defeats Theseus.
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    scene v141557 with Dissolve(1)
    pause(1.5)
    scene v141558 with Dissolve(1)
    athna "..."
    scene v141559 with dissolve
    athna "I..."
    athna "I did it..."
    scene v141560 with dissolve
    athna "Father! Did you see? I did it!"
    play sound "audio/Magic 9.mp3"
    scene v141561 with dissolve
    Character("Zeus", color = "fff64f") "Not good enough."
    scene v141562 with Dissolve(1)
    athna "..." #Mortified look.
    scene v141563 with dissolve
    Character("Zeus", color = "fff64f") "YOU are not good enough, Athena."
    scene v141564 with dissolve
    athna "But..."
    scene v141563 with dissolve
    Character("Zeus", color = "fff64f") "How can you be an Olympian with no worshipers? Hm?"
    Character("Zeus", color = "fff64f") "Does a single mortal even know you exist, daughter?"
    scene v141565 with dissolve
    athna "..."
    Character("Zeus", color = "fff64f") "I am sending you down to them."
    Character("Zeus", color = "fff64f") "The mortals."
    scene v141566 with dissolve
    Character("Zeus", color = "fff64f") "Prove yourself to me, daughter."
    Character("Zeus", color = "fff64f") "Prove you are the daughter of Zeus."
    Character("Zeus", color = "fff64f") "I want the mortals to build statues in your honour."
    Character("Zeus", color = "fff64f") "I want every man, woman, and child to know your name."
    Character("Zeus", color = "fff64f") "Only then, will I let you return."
    scene v141567 with dissolve
    athna "But..."
    scene v141568 with hpunch
    Character("Zeus", color = "fff64f") "Now begone."
    play sound "audio/whoosh cinematic.mp3"
    scene v141569 with Dissolve(1.5)
    athna "Wait! Fath-{w=1}{nw}"
    stop music fadeout 4.0
    scene white with Dissolve(2)
    pause(1)
    show v14m36 with Dissolve(1)
    $ renpy.pause(1.7, hard=True)
    play sound "audio/Falling2.mp3"
    scene v141570 with vpunch
    #Falls to earth where Z is supposed to go to find mercury and lumi.
    #Is dying there on the floor. Also happens during his fight with athena before night falls. When he gets up and fights.
    pause(1)
    z "(I...)"
    z "(I can't move...)"
    z "(Every single part of my body hurts... What happened to me...)"
    play background_s "audio/heartbeat.mp3" volume 0.6 fadeout 1.0 fadein 1.0 loop
    scene v141571 with Dissolve(1)
    #Hailey screams.
    hly "[mc_name]!"
    z "Hailey..."
    scene v141572 with Dissolve(1)
    z "(I'm sorry... I think I'm going to die...)"
    scene v141573 with Dissolve(1)
    hly "[mc_name]!!!"
    hly "WAKE UP!"
    scene v141574
    stop background_s
    stop background_s2
    stop music
    stop sound
    play sound "audio/creak.mp3"
    with vpunch
    z "!!!" #Wakes up.

#17) Lumi is missing:
#    The next day Hailey wakes Z up telling him that Lumi's gone missing, they look around everywhere for him also in the forest where the succubus leaves corpses. They split up to potentially find him.
    scene v141575 with Dissolve(1)
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
    z "Hailey! Not agai-"
    play sound "audio/creak.mp3"
    scene v141576 with dissolve
    hly "Get up! Quickly!"
    scene v141577 with Dissolve(1)
    hly "Lumi! He's gone missing!"
    scene v141578 with dissolve
    play music "audio/Zycris's theme s02 1.mp3" volume 0.3 fadeout 1.0 fadein 5.0 loop
    z "..."
    z "What?!"
    play sound "audio/creak.mp3"
    scene v141579 with Dissolve(1)
    hly "Everyone is looking for him outside!"
    hly "He's no where to be found in the house! His mother and the villagers are looking around the town."
    hly "We need to find him before he gets killed!"
    scene v141580 with dissolve
    z "Fuck! I'll be right behind you!"
    pause(1)
    #They go out, venus is there.
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.6 fadeout 1.0 fadein 1.0 loop
    scene v141581 with Dissolve(1)
    hly "Venus!"
    scene v141582 with dissolve
    vns "?"
    scene v141583 with dissolve
    hly "Anything?" #hailey asks venus
    scene v141584 with Dissolve(1)
    vns "No! And now I can't find Mercury either!"
    scene v141585 with dissolve
    z "What?!"
    scene v141586 with dissolve
    vns "We split up to look for Lumi and now they're both gone!"
    scene v141585 with dissolve
    z "Fuck..."
    scene v141587 with Dissolve(1)
    jacq "This is all your fault!"
    scene v141588 with dissolve
    z "?!"
    scene v141590 with Dissolve(1)
    jacq "Why did you have to come poke around in something you don't understand!"
    jacq "And now my son has to pay for helping you!"
    scene v141589 with dissolve
    z "..."
    z "Jacqueline..."
    z "We will do all we can to find your son."
    z "But..."
    z "Just because the curse has failed to affect you so far, doesn't mean you should do nothing to stop it."
    z "The curse is wrong and evil. Like the one who put it there."
    scene v141590 with dissolve
    jacq "It was put there by the gods, you-"
    scene v141589 with dissolve
    z "Where is it written that gods can't be evil?"
    scene v141591 with dissolve
    jacq "Don't speak about what you don't understand, you little brat!"
    scene v141589 with dissolve
    z "You-"
    play sound "audio/Cloth_rustle.wav"
    scene v141592 with Dissolve(1)
    hly "Don't waste your time on her. We have a boy to find."
    scene v141593 with dissolve
    z "..."
    scene v141594 with Dissolve(1)
    z "Yeah. Let's go."
    scene v141595 with Dissolve(1)
    pause(1.5)
    scene v141596 with Dissolve(1)
    z "Hailey, you look inside the town. Venus and I will search the nearby woods."
    scene v141597 with dissolve
    hly "The woods? You think Lumi could've been taken there?"
    scene v141596 with dissolve
    z "Yeah. I think so."
    scene v141597 with dissolve
    hly "Why? That's not where the dead men where found."
    scene v141596 with dissolve
    z "It's a hunch."
    hly "..."
    scene v141598 with dissolve
    hly "Okay. Go!"
    scene v141599 with dissolve
    z "Venus!"
    scene v141600 with dissolve
    vns "Yeah! Let's go!"
    scene v141601 with Dissolve(1.5)
    #They go to the forest.
    vns "Lumi!" (multiple=2)
    z "Lumi!" (multiple=2)
    scene v141602 with dissolve
    vns "Should we split up?" #Kinda far.
    scene v141603 with Dissolve(1)
    z "Okay! Let's meet up back here in say... Three hours if we don't find anything."
    scene v141604 with dissolve
    vns "Okay!"
    scene v141605 with dissolve
    pause(1)
    #vns leaves.
    scene v141606 with Dissolve(1)
    z "..."
    scene v141607 with dissolve
    pause(1)
    scene v141608 with Dissolve(1)
    pause(1)
    #Some time passes.
    #It's getting darker but still day.
    scene v141609 with Dissolve(1)
    pause(1)
    scene v141610 with Dissolve(1)
    z "Lumi!"
    z "If you can hear me, say something!"
    scene v141611 with dissolve
    pause(1)
    scene v141612 with Dissolve(1)
    z "..." #Looks right or left.
    scene v141613 with dissolve
    z "(Wait...)"
    z "(I know this place.)"
    z "..." #Goes further.
    z "(I was here last night...)"
    scene v141614 with dissolve
    z "(In my dream...)"
    z "(How is this possible...)"
    z "(Is it a sleep nymph ag-)"
    play sound "audio/rustle 2.mp3"
    "Hmmm..."
    scene v141615 with dissolve
    z "?!"
    scene v141616 with dissolve
    pause(1)
    #Lumi is tied up.
    play background_s2 "audio/Ambient_ninja_village_night.mp3" volume 0.4 fadeout 3.0 fadein 3.0 loop
    scene v141617 with Dissolve(1)
    z "..."
    stop music fadeout 4.0
    scene v141618 with Dissolve(1)
    z "Lumi!"
    scene v141619 with Dissolve(1)
    lumi "..." #Knocked out.
    play audio "audio/cloth.mp3"
    scene v141620 with dissolve
    z "Hey! Are you okay?!" (multiple=2)
    lumi "Ahhh..." (multiple=2)
    scene v141621 with dissolve
    lumi "[mc_name]..."
    scene v141622 with dissolve
    lumi "..."
    scene v141623 with vpunch
    lumi "[mc_name]! It's her! Oh gods! She's a monster! She was like a sister to me!"
    scene v141624 with dissolve
    z "What?!"
    z "What are you talking about?! Calm dow-"
    scene v141623 with dissolve
    lumi "MERCURY! She's the monster!"
    play music "audio/Town of the faceless god.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v141624 with dissolve
    z "..."
    z "What the fuck are you-"
    play sound "audio/rustle 2.mp3"
    scene v141625 with Dissolve(1)
    mercury "For what it's worth, Lumi... I am sorry."
    scene v141626 with dissolve
    mercury "I really don't want to do this... You and Jacqueline are like family to me."
    scene v141627 with Dissolve(1)
    z "..." #Shocked.
    z "Mercury..."
    play audio "audio/sword draw.mp3"
    scene v141628 with Dissolve(1)
    #Draws his sword.
    z "You have exactly five seconds to explain what the fuck is going on, or else..."
    scene v141629 with dissolve
    mercury "Or else what?"
    scene v141630 with dissolve
    z "Or else I'll take your head right off." #Fighting pose.
    z "You don't have to worry about Venus finding you, I'll make sure she never learns about what happens to you."
    scene v141631 with dissolve
    mercury "A bit too late for that, wouldn't you say?"
    scene v141632 with Dissolve(1)
    z "..."
    scene v141633 with Dissolve(1)
    #Looks to the side. Venus is there...
    vns "Mercury..."
    scene v141634 with dissolve
    vns "No..."
    scene v141635 with dissolve
    vns "No, no, no, no..."
    scene v141636 with dissolve
    vns "This is not happening..."
    scene v141637 with Dissolve(1)
    vns "Hey..."
    vns "This is just a joke, right?"
    scene v141638 with dissolve
    pause(1)
    scene v141639 with Dissolve(1)
    mercury "..."
    scene v141640 with dissolve
    mercury "I wish it were, Venus..."
    scene v141639 with dissolve
    mercury "..."
    scene v141641 with dissolve
    mercury "I'm sorry..."
    mercury "I have to do this. It's not up to me."
    scene v141642 with Dissolve(1)
    vns "You have to?" (multiple=2)
    z "(She's getting too close...)" (multiple=2)
    vns "Why?"
    scene v141643 with dissolve
    mercury "..."
    scene v141644 with dissolve
    mercury "It's the will of the gods."
    scene v141642 with dissolve
    vns "The gods?"
    vns "Fuck the gods! Why do you car-"
    scene v141644 with dissolve
    mercury "No, Venus."
    mercury "It doesn't work like that, I'm afraid."
    scene v141645 with dissolve
    mercury "I literally can't disobey the goddess."
    mercury "I wouldn't even be alive if it weren't for her."
    mercury "All I have... All I am now, I owe to Athena."
    scene v141643 with dissolve
    vns "..."
    scene v141644 with dissolve
    mercury "I never told you this..."
    mercury "After we got separated, you see..."
    scene v141645 with dissolve
    mercury "I did manage to get away from those men back then, but..."
    mercury "I was starving, I wouldn't have made it all the way to my village."
    mercury "I almost gave up. I was sure I was going to die."
    scene v141644 with dissolve
    mercury "And then I saw her."
    scene v141646 with Dissolve(1)
    mercury "Athena."
    mercury "She told me she would spare me my wretched fate."
    mercury "She asked for but one thing in return. That I serve her. The people of this town had sinned, you see."
    mercury "And I was to put their sins to an end."
    scene v141642 with Dissolve(1)
    vns "How did they sin?"
    scene v141644 with dissolve
    mercury "Lust, Venus. Lust."
    mercury "Do you remember how our lives were ruined?"
    mercury "It was only because of the lust of that man!"
    mercury "He tried to rape me, Venus! All those men who followed us too! They all wanted the same thing!"
    mercury "And to enable people to pursue their lust in a brothel?! Do you not see the problem?!"
    $ mercury_ch14_met = 3
    scene v141647 with dissolve
    z "How about tourists? Why are they allowed to visit the brothel, then?"
    scene v141648 with dissolve
    mercury "The rules aren't up to me, [mc_name]."
    scene v141650 with Dissolve(1)
    mercury "It's up to the goddess. We mortals cannot hope to comprehend the minds of the gods."
    scene v141649 with dissolve
    mercury "..."
    scene v141650 with dissolve
    mercury "What the goddess wills shall be."
    play audio "audio/sword draw.mp3"
    scene v141651 with Dissolve(1)
    z "Not while I can stand and fight."
    scene v141652 with hpunch
    vns "[mc_name]! Wait!"
    play sound "audio/Magic 9.mp3"
    scene v141653 with Dissolve(1)
    mercury "Heh... You really think you can stop me, [mc_name]?"
    #Are going to fight.
    scene v141654 with Dissolve(1)
    z "..."
    z "(She's a fury, but her form seems to be actually complete... She's way stronger than the one from the town of the faceless god.)"
    play sound "audio/Magic 9.mp3"
    scene v141655 with Dissolve(1.5)
    z "(Clearly a formidable opponent... But I think I can take her...)"
    scene v141656 with Dissolve(1)
    mercury "..."
    scene v141657 with dissolve
    mercury "What the..."
    mercury "What are you..."
    scene v141658 with Dissolve(1)
    z "..."
    vns "[mc_name]! Do-"
    scene v141659 with Dissolve(1)
    z "I'm sorry, Venus..."
    scene v141660 with dissolve
    z "Don't worry... I won't let her suffer."
    scene v141661 with dissolve
    mercury "..."
    z "..."
    play background_s "audio/heartbeat.mp3" fadeout 1.0 fadein 1.0 loop
    scene v141662 with Dissolve(1)
    z "(What the...)"
    z "(I can sense something... Something horrifyingly strong...)"
    z "(Is it Mercury?)"
    z "(No... It's...)"
    z "(I know this presence... It's-)"
    play sound "audio/Magic 9.mp3"
    stop background_s fadeout 1.0
    stop music fadeout 1.0
    scene v141663 with Dissolve(1.5)
    #Athena lands.
    z "?!"
    play sound "audio/whoosh cinematic.mp3"
    scene v141664 with Dissolve(1.5)
    scene v141665 with Dissolve(1.5)
    pause(2)
    scene v141666 with Dissolve(1.5)
    z "..." (multiple=2)
    vns "..." (multiple=2)
    play music "audio/Athena's theme.mp3" volume 0.3 fadeout 1.0 fadein 5.0 loop
    scene v141667 with Dissolve(1)
    athna "You again..."
    athna "Quite nostalgic, is it not..."
    athna "...[mc_name]?"
    scene v141668 with dissolve
    z "You bothered to remember my name, huh..."
    if against_athena >= 11:
        scene v141669 with dissolve
        athna "You think there are enough people who disobeyed me and lived to tell the tale for me to forget you?"
    else:
        scene v141669 with dissolve
        athna "You think us gods proud and ignorant, do you?"
        athna "A man like you who knows when to listen. A loyal, smart and strong man like you is worth remembering, incubus."
    scene v141670 with dissolve
    z "..."
    scene v141671 with dissolve
    athna "Not to mention. I know your father all too well."
    athna "He was quite daring for a mortal, I'll give him that."
    scene v141672 with dissolve
    z "..."
    scene v141673 with Dissolve(1.5)
    z "(This is...)"
    z "(She's at full strength this time... I can tell...)"
    z "(Ichor runs through her veins... Real one... I can feel it...)"
    scene v141671 with Dissolve(1)
    athna "I think you and I both know you are stronger than my fury."
    scene v141674 with Dissolve(1)
    mercury "He..."
    mercury "He is stronger than me?"
    scene v141675 with Dissolve(1)
    athna "The fact that you can't even tell says quite a lot, Mercury."
    scene v141676 with dissolve
    athna "[mc_name]."
    if against_athena >= 11:
        scene v141677 with dissolve
        athna "I will only say this once."
        athna "Leave this town now and never turn back..."
        athna "...or face your doom."
    else:
        scene v141677 with dissolve
        athna "I trust you're smarter than to pick a fight with me."
        scene v141678 with dissolve
        z "..."
        scene v141677 with dissolve
        athna "Of course you are."
        athna "Take your friends and leave."
    scene v141678 with dissolve
    z "..."
    scene v141679 with Dissolve(1)
    vns "[mc_name]..."
    vns "What do we do..."
    scene v141680 with dissolve
    z "..."
    scene v141681 with dissolve
    z "Athena."
    scene v141682 with Dissolve(1)
    athna "..."
    z "Why exactly did you place the curse?"
    scene v141683 with dissolve
    athna "Heh... You're very bold, you know."
    scene v141684 with dissolve
    athna "Do you think it unfair?"
    athna "Do you know what happened in this brothel before I cursed it?"
    scene v141682 with dissolve
    z "..."
    scene v141685 with Dissolve(1)
    athna "Of course not. No one weeps for dead whores after all."
    scene v141686 with dissolve
    athna "Before I even set foot in this village, half a dozen women died while working in that damned place."
    athna "Want to know how they died?"
    athna "One was slashed down with a sword during a fight. Two men got into a fight after drinking a lot more than they should've."
    athna "An accident. So no one cared that much. The girl had no family of note either."
    athna "Four died when a plague struck these lands. They laid with sick men who did not say they were sick."
    athna "One was beaten to death by one of your own kind. She refused to lie with him and he took it as an insult. He was a high general of your father. Rejection wasn't a humiliation he was willing to bear."
    athna "What can you expect from a place like that, after all."
    athna "Lust is but a sin like all others. I only regret not cursing it earlier."
    scene v141687 with dissolve
    z "Why curse it? Why not burn it down?"
    z "And why does the curse only apply to the town's folk and only the men?"
    scene v141688 with dissolve
    athna "Father give me strength... Never had a goddess to explain herself to a mortal for 5 minutes straigt."
    athna "The brothel is one of this towns main income sources. Without it the people would start starving in mere weeks."
    athna "If I forbade the women from going to the brothel, who will be working in it then?"
    athna "This town worships me. You think I'd let my own people starve to death?"
    scene v141689 with dissolve
    z "..."
    scene v141690 with Dissolve(1)
    athna "I care about my worshipers, believe it or not, [mc_name]."
    scene v141691 with dissolve
    athna "Do you think it easy? Being the daughter of the great Zeus?"
    athna "All my brothers were granted titles as Olympians, at least the true born ones. Only I had to earn it."
    scene v141690 with dissolve
    athna "Do you think it's easy to take care of hundreds of towns and villages who worship you?"
    athna "Do you think you can protect them without them being afraid of what you're protecting them from?"
    scene v141692 with Dissolve(1)
    athna "It's easy to be an ignorant prick like your father. Manipulating everyone with charm and desire to think you can lead them."
    scene v141693 with Dissolve(1)
    athna "Under your father's rule, his kind massacred hundreds of people, [mc_name]. Raping, killing, stealing... You name it, they did it."
    athna "I trust you met a few examples of your own kind like that?"
    #Remembers axius.
    scene v141698 with Dissolve(1)
    z "..."
    scene v141694 with Dissolve(1)
    athna "The underworld city had to go. So do the men of this town who visit the brothel."
    athna "Otherwise, this town would not be kept in order. And if we didn't bury the underworld city the world would've been a much more horrid place."
    athna "Sacrifice will always be needed for the greater good. A sad truth that not even gods can escape."
    z "..."
    scene v141690 with Dissolve(1)
    athna "So? What shall it be?"
    scene v141695 with Dissolve(1)
    vns "[mc_name]..."
    vns "I'm scared..."
    vns "I don't want to fight Mercury..."
    vns "And Athena is..."
    scene v141697 with dissolve
    vns "She is going to kill us..."
    vns "Let's just..."
    vns "...leave..."
    scene v141699 with Dissolve(1)
    z "..."
    scene v141703 with Dissolve(1)
    with Pause(1)
    show screen ch14_btn_leave
    if against_athena <= 9:
        show screen ch14_btn_negotiate
    show screen ch14_btn_fight
    call screen pixel
    label ch14_negotiate:
        call hide_all_ch14 from _call_hide_all_ch14_9
        $ against_athena -= 1
        scene v141699 with Dissolve(1)
        pause(1)
        scene v141708 with Dissolve(1)
        z "Let the boy go."
        athna "..."
        z "Let him go and my friends and I will leave with not further interference."
        z "How does that sound?"
        scene v141709 with dissolve
        athna "You want the same deal as last time?"
        athna "Bold, aren't you?"
        athna "Very bold."
        athna "Bolder than even your father, perhaps..."
        athna "You really have proven to be much more than your father's son."
        athna "So be it."
        scene v141711 with dissolve
        mercury "But he knows who I am now."
        scene v141712 with dissolve
        athna "Get a memory potion from the alchemist, then."
        scene v141711 with dissolve
        mercury "I understand..."
        scene v141709 with dissolve
        athna "Satisfied?"
        scene v141710 with dissolve
        z "Yes."
        athna "Hm..." #Smurks.
        pause(2)
        scene v141715 with Dissolve(1)
        z "Nothing else we could've done..."
        scene v141716 with Dissolve(1)
        hly "Yeah... I guess not..."
        scene v141717 with Dissolve(1)
        vns "..."
        scene v141718 with Dissolve(1)
        pause(1)
        scene v141719 with Dissolve(1)
        pause(2)
        #Renders of them leaving the town with Venus sad. She stops to look at the place for a bit and then continues walking.
        jump after_athna_ch14
    label ch14_leave:
        call hide_all_ch14 from _call_hide_all_ch14_10
        $ against_athena -= 2
        scene v141705 with Dissolve(1)
        pause(1)
        scene v141713 with Dissolve(1)
        z "Let's go, Venus."
        vns "..."
        scene v141714 with dissolve
        z "There's nothing we can do here."
        scene v141709 with Dissolve(1)
        athna "Heh..." #Smurks.
        athna "You really have proven to be much more than your father's son."
        athna "You may not be as strong, but you're much more reasonable."
        athna "Go with peace, [mc_name]."
        athna "I hope the three fates favour you."
        scene v141710 with dissolve
        z "..."
        pause(2)
        scene v141715 with Dissolve(1)
        z "Nothing else we could've done..."
        scene v141716 with Dissolve(1)
        hly "Yeah... I guess not..."
        scene v141717 with Dissolve(1)
        vns "..."
        scene v141718 with Dissolve(1)
        pause(1)
        scene v141719 with Dissolve(1)
        pause(2)
        #Renders of them leaving the town with Venus sad. She stops to look at the place for a bit and then continues walking.
        jump after_athna_ch14
    label ch14_fight:
        call hide_all_ch14 from _call_hide_all_ch14_11
        $ against_athena += 3
        scene v141707 with Dissolve(1)
        pause(1)
        scene v141720 with Dissolve(1)
        z "So..."
        z "According to you..."
        z "Who decides which sacrifices are needed and which are not?"
        z "I can see the appeal of killing all of my kind in your mind."
        z "I say a great sacrifices we could do is to rid the world of your kind as well, Athena."
        z "You know..."
        play sound "audio/sword draw.mp3"
        stop music fadeout 1.0
        scene v141721 with Dissolve(1)
        z "Gods." #Draws his sword scary looking.
        scene v141722 with Dissolve(1)
        vns "[mc_name]..."
        scene v141723 with Dissolve(1)
        athna "..."
        scene v141724 with dissolve
        athna "Are you mad..."
        athna "Are you out of your damned mind?"
        athna "This is not a mortal form, you stupid fool."
        scene v141725 with dissolve
        athna "I am at my full strength here."
        athna "Is your mortal brain filled with rot?"
        athna "You shall pay for drawing your weapon in my presence you impu-"
        play sound "audio/whoosh cinematic.mp3"
        scene v141726 with Dissolve(1)
        pause(1)
        play audio "audio/slash.mp3"
        scene v141727 with hpunch
        pause(1)
        play music "audio/Zycris's theme s02 1.mp3" volume 0.4 fadeout 1.0 fadein 5.0 loop
        scene v141728 with Dissolve(1)
        #Attacks her.
        #She dodges.
        z "Quick, aren't you?"
        scene v141729 with dissolve
        pause(1)
        scene v141730 with dissolve
        mercury "Athena!"
        play background_s "audio/electricity.mp3" volume 0.6 fadeout 1.0 fadein 1.0 loop
        scene v141731 with dissolve
        vns "D-Don't move!"
        scene v141732 with Dissolve(1)
        mercury "..."
        scene v141733 with dissolve
        vns "I'm serious! Don't move, Mercury!"
        scene v141732 with dissolve
        mercury "Or what?"
        vns "..."
        scene v141733 with dissolve
        vns "Or I'll attack you."
        scene v141732 with dissolve
        mercury "..."
        scene v141734 with dissolve
        mercury "You wouldn't-{w=1.5}{nw}" #Moves
        play sound "audio/electric-shock.mp3"
        play audio "audio/thunder.mp3"
        scene v141735 with vpunch
        pause(0.5)
        scene v141736 with Dissolve(1)
        vns "..."
        #Strikes next to her.
        scene v141737 with Dissolve(1)
        mercury "..." #Terrified.
        scene v141738 with hpunch
        vns "DON'T FUCKING MOVE, OKAY?!"
        scene v141739 with Dissolve(1)
        mercury "..." #Scared.
        pause(1)
        stop background_s fadeout 1.0
        #Back to Z and athena
        #Attacks her again. She blocks with the sheild.
        #Z gets injured.
        #He pauses for a second.
        scene v141740 with Dissolve(1)
        pause(0.5)
        play sound "audio/Swordplay/s1.mp3"
        scene v141741 with hpunch
        pause(0.5)
        play audio "audio/Swordplay/s2.mp3"
        scene v141742 with hpunch
        pause(0.5)
        scene v141743 with dissolve
        pause(1)
        play sound "audio/sword cut 2.mp3"
        scene v141744 with vpunch
        z "UGHHH!"
        # I'm here S <-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
        scene v141745 with Dissolve(1)
        z "..."
        play sound "audio/Healing.mp3"
        scene v141746 with Dissolve(1)
        pause(1)
        scene v141747 with Dissolve(1)
        z "Mirror..."
        z "I'll call it Mirror."
        play audio "audio/Magic 9.mp3"
        scene v141748 with Dissolve(1)
        z "What do you think, Hephaestus?"
        scene v141749 with dissolve
        pause(1)
        scene v141750 with Dissolve(1)
        athna "..." #Shocked.
        scene v141751 with dissolve
        z "So that's why it's called Mirror..."
        z "That's how you won in the arena."
        z "That's how you defeated Sirius..."
        scene v141752 with dissolve
        athna "How did you-"
        scene v141753
        play sound "audio/Swordplay/Long.mp3"
        with hpunch
        pause(0.5)
        play audio "audio/sword cut 2.mp3"
        scene v141754 with vpunch
        pause(0.75)
        scene v141755 with Dissolve(1)
        z "..."
        play sound "audio/whoosh cinematic.mp3"
        scene v141756
        play audio "audio/Punch2.mp3"
        with hpunch
        pause(0.5)
        play sound "audio/Falling2.mp3"
        scene v141757 with vpunch
        z "Ughhh..."
        pause(0.5)
        play sound "audio/Punch3.mp3"
        play audio "audio/splat.mp3"
        scene v141758 with vpunch
        athna "AHHHH!"
        scene v141759 with Dissolve(1)
        athna "..."
        play sound "audio/charge_n_hit.mp3"
        $ renpy.pause(1.5, hard=True)
        scene v141760 with Dissolve(1)
        athna "?!{w=1}{nw}"
        scene v141761 with hpunch
        pause(0.5)
        play audio "audio/sword cut 2.mp3"
        scene v141762 with vpunch
        z "Fuccckkk!"
        scene v141763 with Dissolve(1)
        z "..."
        #Attacks her again.
        #Injured but heals.
        #Cycle of the same.
        z "(She's not attacking...)"
        z "(Is she not strong enough to attack?)"
        z "(Or is she planning on killing me using her shield's effect?)"
        z "(She's extremely good at blocking with it. Her reaction time is crazy.)"
        z "(And since the shield will reflect whatever attack hits it back on the attacker...)"
        z "(...She's basically invincible.)"
        play sound "audio/Healing.mp3"
        scene v141764 with dissolve
        z "(Could Anabelle take her?)"
        z "(Could Seira?)"
        z "..."
        z "(No.)"
        z "(If it weren't for my healing, I would've been long dead.)"
        z "(If I lose here, Venus and Hailey are as good as dead.)"
        z "(Somehow I have to win...)"
        z "(I need to be faster...)"
        z "(Much faster...)"
        scene v141766 with dissolve
        z "(Fast enough to actually slash her before she's able to block with the shield.)"
        z "(I'm not at full strength for some reason...)"
        z "(Why can't I move as fast as I could when fighting before...)"
        z "(Now that I think about it...)"
        z "(I haven't really managed to master any of my strongest abilities...)"
        z "(I don't fully understand them...)"
        z "(Did I just pick the wrong fight for the first time...)"
        scene v141765 with dissolve
        athna "I see you have a talent not even the mighty Elnor had..."
        athna "But you are nowhere near as strong as he was."
        athna "I've seen dark creatures with your talent before."
        athna "Never seen it in one of your kind, though."
        athna "No matter... I shall bring you down all the same."
        scene v141766 with dissolve
        z "..."
        z "(Her shield...)"
        z "(It's damaged...)"
        play sound "audio/rustle 2.mp3"
        scene v141767 with dissolve
        z "(I don't think I did that. I think it was already damaged before our fight.)"
        z "(But it just means, it's possible to break it.)"
        play audio "audio/Magic 9.mp3"
        scene v141768 with Dissolve(1)
        z "(I just need to hit it hard enough...)"
        z "(Again and again...)"
        play sound "audio/Magic 9.mp3"
        scene v141769 with Dissolve(1)
        z "(Until I break it.)"
        play sound "audio/Swordplay/Long.mp3"
        scene v141770 with hpunch
        pause(0.5)
        play audio "audio/splat.mp3"
        scene v141771 with vpunch
        z "Uggh!"
        play sound "audio/Falling2.mp3"
        scene v141772 with vpunch
        z "(Fuck... My sword arm...)"
        scene v141773 with dissolve
        z "(Where is my sword...)"
        play sound "audio/Swordplay/s8.mp3"
        play audio "audio/splat.mp3"
        scene v141774 with vpunch
        z "{i}Gasps.{/i}"
        play sound "audio/Swordplay/s3.mp3"
        scene v141775 with Dissolve(1)
        pause(1)
        play sound "audio/Swordplay/s8.mp3"
        play audio "audio/splat.mp3"
        scene v141776 with hpunch
        z "UGHHHH!"
        scene v141777 with Dissolve(1)
        #Cycle of attacking and blocking.
        z "..." #Really injured.
        athna "What's wrong?"
        athna "Can't move any more?"
        scene v141778 with Dissolve(1)
        athna "Can't heal any more?"
        play sound "audio/Swordplay/s2.mp3"
        play audio "audio/Falling2 (loud).mp3"
        scene v141779 with vpunch
        #Thrusts him with her spear lifting him up.
        #Throws him down.
        z "Ugghh..."
        play background_s "audio/heartbeat.mp3" volume 0.6 fadeout 1.0 fadein 1.0 loop
        scene v141780 with Dissolve(1)
        stop music fadeout 5.0
        z "{i}Heavily breathing.{/i}"
        z "..."
        z "(What the...)"
        scene v141781 with Dissolve(1)
        z "(It's the same...)"
        z "(In my dream...)"
        scene v141782 with Dissolve(1)
        z "(I was here...)"
        z "..."
        scene v141783 with Dissolve(1)
        z "(Dying...)"
        z "(Am I going to die here...)"
        play music "audio/Requiem in D.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
        scene v141784 with Dissolve(1)
        z "..." #A blurry woman appears.
        z "(Who...)"
        play audio "audio/Magic 9.mp3"
        scene v141785 with Dissolve(1)
        "Get up and fight, boy."
        z "(I know this voice...)"
        stop music fadeout 1.0
        scene v141786 with Dissolve(1)
        stop background_s fadeout 1.0
        scene v141787 with Dissolve(1)
        z "..."
        scene v141788 with Dissolve(1)
        athna "..."
        #Night falls suddenly.
        play sound "audio/Effect4.mp3"
        scene v141789 with Dissolve(1)
        play music "audio/Zycris's theme 4.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
        athna "?!"
        z "..."
        z "(I feel...)"
        z "(...strong.)"
        play sound "audio/Swordplay/Draw.mp3"
        scene v141790 with Dissolve(1)
        z "..."
        #Gets up completely healed.
        scene v141791 with Dissolve(1)
        athna "..." #Confused.
        scene v141792 with dissolve
        athna "What do you think you're going to achi-"
        play sound "audio/Effect4.mp3"
        pause(0.5)
        scene v141793 with Dissolve(0.25)
        pause(0.25)
        play audio "audio/Swordplay/s9.mp3"
        scene v141794 with hpunch
        athna "!" #Breaks her spear.
        scene v141795 with Dissolve(1)
        athna "..."
        scene v141796 with dissolve
        athna "My spear?!"
        play sound "audio/whoosh.mp3"
        scene v141797 with hpunch
        pause(0.5)
        scene v141798 with dissolve
        pause(1)
        scene v141799 with dissolve
        play sound "audio/Effect4.mp3"
        pause(0.5)
        scene v141800 with dissolve
        athna "..."
        scene v141801 with dissolve
        athna "Eh?"
        play audio "audio/whoosh cinematic.mp3"
        scene v141802 with dissolve
        athna "?!{w=0.5}{nw}"
        play sound "audio/Swordplay/s8.mp3"
        scene v141803 with vpunch
        pause(0.5)
        scene v141804 with dissolve
        z "..."
        scene v141805 with Dissolve(1)
        athna "..."
        scene v141806 with Dissolve(1)
        z "(My blade actually reached her...)"
        z "(Be it a strand of her hair...)"
        play sound "audio/Swordplay/s8.mp3"
        scene v141807 with vpunch
        athna "!"
        scene v141808 with Dissolve(1)
        z "(And a scratch on her armour.)"
        #In the same attack combo, cuts her hair and then even manages to evade the shield and scratch her armour
        play sound "audio/Swordplay/s5.mp3"
        play audio "audio/splat.mp3"
        scene v141809 with vpunch
        z "UGHHH!"  #Is cut in turn.
        scene v141810 with dissolve
        z "..."
        scene v141811 with Dissolve(1)
        z "(Even though I didn't touch her shield, my attack still got reflected back on me?!)"
        z "(Does her armour have the same effect as her shield? Or does attacking her in general cause this...)"
        z "..."
        z "(Only one way to find out...)"
        play sound "audio/Effect4.mp3"
        pause(0.5)
        scene v141812 with Dissolve(0.25)
        pause(0.5)
        scene v141813 with dissolve
        pause(0.5)
        play audio "audio/Effect4.mp3"
        pause(0.5)
        scene v141814 with Dissolve(0.25)
        pause(0.5)
        play sound "audio/slash2.mp3"
        play audio "audio/whoosh cinematic.mp3"
        scene v141815 with hpunch
        pause(0.5)
        scene v141816 with dissolve
        play sound "audio/Effect4.mp3"
        pause(0.5)
        scene v141817 with Dissolve(0.25)
        pause(1)
        scene v141818 with Dissolve(1)
        athna "..."
        play sound "audio/Effect4.mp3"
        pause(0.5)
        scene v141819 with Dissolve(0.25)
        z "(I got you now...)"
        play audio "audio/Effect4.mp3"
        pause(0.5)
        scene v141820 with Dissolve(0.25)
        pause(1)
        play sound "audio/Magic 9.mp3"
        scene v141821 with Dissolve(1)
        athna "..."
        play audio "audio/Effect4.mp3"
        pause(0.5)
        scene v141822 with Dissolve(0.25)
        pause(0.5)
        play sound "audio/whoosh cinematic.mp3"
        scene v141823 with Dissolve(0.25)
        pause(0.5)
        play audio "audio/Punch3.mp3"
        play sound "audio/Swordplay/s8.mp3"
        scene v141824 with hpunch
        athna "AHH!"
        scene v141825 with Dissolve(1)
        #Throwing her shield away.
        athna "...{w=0.5}{nw}"
        #Is gonna finish her off.
        play sound "audio/Swordplay/s8.mp3"
        play audio "audio/splat.mp3"
        stop music
        scene v141826 with hpunch
        z "UGHHHH!" #Mercury attacks him from behind blinding him.
        play sound "audio/Falling2 (loud).mp3"
        scene v141827 with dissolve
        #Athena crawls to her shield.
        play music "audio/Zycris's theme 2.mp3" volume 0.8 fadeout 1.0 fadein 4.0 loop
        z "(Fuck! My eyes!)"
        z "(Was that Mercury?! I thought Venus was supposed to stop her from attacking...)"
        scene v141828 with Dissolve(1)
        athna "..."
        play audio "audio/rustle 2.mp3"
        scene v141829 with Dissolve(1)
        pause(1)
        scene v141830 with Dissolve(1)
        z "(Fuck... She's gonna attack again...)"
        z "(I can barely see a thing... My eyes aren't healing fast enough...)"
        scene v141831 with dissolve
        pause(0.5)
        play sound "audio/thunder (load af).mp3"
        play audio "audio/thunder.mp3"
        scene v141832 with vpunch
        z "Ughhh!"
        pause(1)
        scene v141833 with Dissolve(1)
        z "..."
        play sound "audio/Falling2 (loud).mp3"
        play audio "audio/rustle 2.mp3"
        scene v141834 with vpunch
        #Blurry and bloody Z's vision sees mercury is about to attack again.
        #A flash.
        #Mercury is stunned. She was struck by venus's lighting.
        vns "..."
        scene v141835 with Dissolve(1)
        #Mercury falls on the floor dead.
        #Athena who was her shield sees this.
        #Venus is crying.
        z "..." #Looks at athena with wrath in her eyes.
        scene v141836 with Dissolve(1)
        #Athena's pov.
        athna "..." #Charges lightning to attack athena.
        scene v141837 with dissolve
        pause(1)
        athna "..." #Z is also running at athena.
        scene v141838 with Dissolve(1)
        vns "..."
        play audio "audio/rustle 2.mp3"
        scene v141839 with dissolve
        pause(0.5)
        play sound "audio/Falling2 (loud).mp3"
        scene v141840 with vpunch
        vns "{i}Sobbing.{/i}"
        pause(1)
        play background_s "audio/electricity.mp3" volume 0.6 fadeout 1.0 fadein 1.0 loop
        scene v141841 with Dissolve(1)
        vns "..."
        play sound "audio/Effect4.mp3"
        scene v141842 with Dissolve(1)
        athna "..."
        play sound "audio/Magic 4.mp3" volume 0.4
        scene v141843 with Dissolve(1)
        pause(1)
        scene v141844 with Dissolve(1)
        z "(We can do it...)"
        z "(If I put everything I have into this shot... We can break her shield...)"
        z "(I don't care what happens to us if we do, I don't think Venus cares either at this point...)"
        stop sound fadeout 1.0
        stop background_s fadeout 1.0
        play sound "audio/charge_n_hit.mp3"
        scene v141845 with Dissolve(1.5)
        scene white with Dissolve(1.5)
        pause(1)
        play audio "audio/thunder.mp3"
        pause(2)
        scene v141846 with Dissolve(1.5)
        pause(2)
        #Beams up to the sky quickly.
        #Venus strikes but there's nothing there.
        scene v141847 with Dissolve(1)
        z "..."
        scene v141848 with hpunch
        vns "WHERE IS SHE?!" #Furios
        scene v141849 with Dissolve(1)
        vns "Where is she, [mc_name]?!"
        scene v141850 with dissolve
        z "She's gone. I think she ran away, Venus..."
        scene v141851 with Dissolve(1)
        z "We didn't get her... I'm sorry..."
        scene v141852 with dissolve
        vns "..."
        scene v141853 with dissolve
        vns "{i}Breaks down crying.{/i}"
        vns "Mercury... {i}She says while crying.{/i}"
        scene v141854 with Dissolve(1.5)
        vns "I'm sorry... I'm sorry... {i}Continues crying.{/i}"
        pause(2)
        $ mercury_ch14_met = -1
        #Goes to hug venus. Show them from mercury's dead body.
        #Render from above of the battlefield.
        jump after_athna_ch14
    label after_athna_ch14:
        $ dummy += 1
        scene black with Dissolve(2)
        pause(1)
        stop background_s fadeout 3.0
        stop background_s2 fadeout 3.0
        stop music fadeout 3.0
        stop sound fadeout 3.0
        pause(4)
#18) Ending clips:
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.7 fadeout 1.0 fadein 1.0 loop
    scene v141855 with Dissolve(2)
    pause(1.5)
    play sound "audio/splash.mp3"
    scene v141856 with Dissolve(1)
    gbrla "Shouldn't Stephanie's mission be back by now?"
    scene v141857 with dissolve
    s "Yeah... Helena seems to be worried about that one..."
    scene v141858 with dissolve
    gbrla "But they would've sent a letter if something wrong happened, right?"
    scene v141857 with dissolve
    s "I-"
    scene v141859 with Dissolve(1)
    Character("Familiar voice", color = "c44f00") "Gabbie?"
    scene v141860 with Dissolve(1)
    gbrla "..."
    scene v141861 with dissolve
    gbrla "Jenny?!"
    pause(2)
    scene black
    stop background_s
    stop background_s2
    stop music
    stop sound
    pause(3)
#    -Jamie and Jenny show up in the village at the end of the chapter, since Fran informed Jamie she's gonna tell the ninjas everything. He argues with her that she shouldn't.
#    -Jamie loses most of his money due to Z uncovering the stuff in Esyl. Jenny (can break up with him or not? but) comes go to live in the ninja village (with or without him)
#    -Give them roles in the village.
    #Chapter end.
#18) After credits scene:
    play background_s2 "audio/Ambient_ninja_village_night.mp3"
    scene v141862 with Dissolve(1)
    play music "audio/Axius's Theme.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    pause(1)
    scene v141863 with Dissolve(1)
    cndy "..."
    scene v141864 with Dissolve(1)
    alura "Come out, come out, cutie..."
    alura "I don't bite, you know..."
    scene v141865 with Dissolve(1)
    cndy "..."
    play sound "audio/rustle 2.mp3"
    scene v141866 with dissolve
    cnt "..."
    scene v141867 with Dissolve(1)
    pause(1)
    scene v141868 with Dissolve(1)
    cndy "{size=-10}Centoria!{/size}"
    cndy "{size=-10}Hey!{/size}"
    scene v141869 with Dissolve(1)
    cndy "..."
    scene v141870 with Dissolve(1)
    cndy "..."
    scene v141871 with dissolve
    alura "There you are, cutie.{w=1.5}{nw}"
    scene black
    pause(2)
    play background_s "audio/fire_in_kitchen.mp3" volume 0.6 fadeout 1.0 fadein 1.0 loop
    scene v141872 with Dissolve(1)
    stfny "Fuck..."
    scene v141873 with dissolve
    irna "Nari! Wait! Don't kill her!"
    scene v141874 with Dissolve(1)
    irna "Haven't you realised what she is?"
    scene v141875 with dissolve
    nari "..."
    pause(2)
    play sound "audio/Magic 9.mp3"
    stop background_s
    scene v141876 with Dissolve(1)
    stfny "?!"
    scene v141877 with Dissolve(1)
    pause(1)
    scene v141878 with Dissolve(1)
    stfny "..."
    scene v141879 with Dissolve(1)
    irna "..."
    scene v141880 with Dissolve(1)
    scene v141881 with Dissolve(1)
    pause(2)

    #    Candy, Centoria, Yumi, and Stephanie run into Nari on their mission.
    #    Nari wins against Stephanie and Yumi, while his gf totally distroys Centoria and Candy. Before Nari is about to kill Stephanie, Irena realises who Steph is and stops him by asking him if he can tell who she is.
    #    Nari After pausing for a while tells his gf to let go of Centoria and Candy so they can withdraw.
    #    #Chapter end.

    scene black with fade
    stop music fadeout 1.0
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop sound fadeout 1.0
    pause(1.0)
    jump season2_chapter_3