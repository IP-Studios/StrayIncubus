label season2_chapter_3:
    $ chapter = 15
    define jamie = Character("Jamie", color = "09EC8C")
    define vollstahl = Character("Vollstahl", color = "94BD21")
    define klyn = Character("Klyn", color = "55AAE7")
    define jillia = Character("Jillia", color = "B955E7")
    define illya = Character("Illya", color = "9B3DF7")
    define Dohkong = Character("Dohkong", color = "F36526")
    define plgbln = Character("Pale Goblin", color = "26F39E")
    define scrs = Character("Sorceress", color = "F3A626")
    define crpr = Character("Crown Prince", color = "FADA5E")
    define y_r_u_g_counter = 0 #Move to top of script
    #Title: Of Goblins and Elves.

    image v15m1 = Movie(size = (1920,1080), channel="movie", play="2.3/videos/v15m1.webm", loop=True)
    image v15m2 = Movie(size = (1920,1080), channel="movie", play="2.3/videos/v15m2.webm", loop=True)
    image v15m3 = Movie(size = (1920,1080), channel="movie", play="2.3/videos/v15m3.webm", loop=True)
    image v15m4 = Movie(size = (1920,1080), channel="movie", play="2.3/videos/v15m4.webm", loop=True)
    image v15m5 = Movie(size = (1920,1080), channel="movie", play="2.3/videos/v15m5.webm", loop=True)
    image v15m6 = Movie(size = (1920,1080), channel="movie", play="2.3/videos/v15m6.webm", loop=True)
    image v15m7 = Movie(size = (1920,1080), channel="movie", play="2.3/videos/v15m7.webm", loop=True)
    default persistent.g_59_unlock = 0
    default persistent.g_60_unlock = 0
    default persistent.g_61_unlock = 0
    default persistent.g_62_unlock = 0
    default persistent.g_63_unlock = 0
#1) Alchemist's hut in the ninja village:
    pause(1.5)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    play background_s2 "audio/Ambient_ninja_village_night.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v151 with Dissolve(1.5)
    cndy "..."
    scene v152 with Dissolve(1.5)
    cndy "Is she gonna be okay?"
    scene v153 with Dissolve(1)
    gbrla "Yeah... She's just unconscious."
    #Torr waltzes in.
    scene v155 with Dissolve(1.5)
    tr "Centoria!!!"
    scene v154 with Dissolve(1)
    cndy "?!" (multiple=2)
    gbrla "?!" (multiple=2)
    scene v156 with Pause(1)
    scene v157 with Dissolve(1)
    cndy "Torr?! When did you get ba-"
    scene v158 with Dissolve(1)
    tr "Like 5 minutes ago!"
    scene v159 with Dissolve(1)
    tr "What happened to Centoria?!"
    scene v160 with Dissolve(1)
    gbrla "She's fine. Don't worry, Torr."
    scene v161
    tr "..."
    scene v162
    gbrla "..."
    scene v163
    tr "I heard Yumi and Stephanie got injured too?"
    scene v164
    ymi "I'm okay, don't worry." #Comes in.
    scene v165
    gbrla "I told Stephanie not to move too much for a day or two, but she seems fine too."
    scene v166
    cndy "How did your mission go? Anyone injured?"
    scene v167
    tr "Well, no... Thanks to Anabelle..."
    scene v168
    tr "It was a handful of goblins kidnapping the women. They tried to attack us when we went to rescue the missing girls. They were no match for us though. Anabelle killed seven of them herself. I killed two and the midget didn't kill anyone."
    scene v166
    cndy "I see... That's good."
    scene v167
    tr "Did [mc_name] return yet?"
    scene v166
    cndy "Not yet..."
    hly "{size=-10}Are you sure you're up to it?{/size}"
    scene v169
    cndy "?" (multiple=2)
    tr "?!" (multiple=2)
    scene v170
    vns "I'm fine, Hailey. I have stuff to do here..." #Venus and hailey go in.
    scene v171
    gbrla "Venus?"
    scene v172
    vns "I'm told a few people are injured?"
    scene v171
    gbrla "Yeah... One of Stephanie's arms is swollen... I'm not sure if it's broken or not..."
    scene v173
    vns "..."
    scene v172
    vns "Where is she?"
    scene v171
    gbrla "She's in the lab."
    scene v174
    vns "I'll go take a look."
    scene v176
    hly "Venus... Wait..."
    #She leaves.
    gbrla "..."
    scene v177
    gbrla "Is she okay?"
    scene v178
    hly "..."
    #Skip

#2) Zycris is going to his room.
    scene v179 with Pause(1.0)
    scene v180
    z "..." #It's dark.
    scene v181
    scene v182
    scene v183
    #Sits down, looks sad.
    scene v188
    s "Darling? Are you in here?" #Comes from the outside.
    scene v187
    z "..."
    z "Seira..."
    z "I..."
    scene v189
    s "..."
    scene v190
    s "Are you okay?"
    scene v191
    z "..."
    scene v192
    z "I don't..."
    z "...know."
    scene v193
    s "..."
    scene v194
    s "What happened?"
    # if fought twice: against_athena = 14
    # if fought then left: against_athena = 9
    # if left then left: against_athena = 7
    # if left then fought: against_athena = 12
    # if left then negotiated: against_athena = 8
    scene v193
    z "I did what I thought was right..."
    scene v192
    s "..."
    if against_athena == 14:
        scene v193
        z "I fought Athena."
        z "That's twice now."
        z "I almost won, Seira..."
        z "I almost won."
        z "Athena's..."
        z "Well, minion, I suppose. She interfered before I could finish Athena off..."
        z "And Venus had to kill her."
        scene v194
        s "You almost finished Athena off?!"
        scene v193
        z "Yeah..."
        z "I think..."
        z "But Seira..."
        z "Athena's minion..."
        scene v192
        z "She was Venus's dear childhood friend..."
        z "And Venus had to kill her to protect me..."
        scene v191
        s "..."
        scene v193
        z "She didn't want to fight, actually..."
        hide v15m1
        show v15m1 with Dissolve(1.0)
        z "Venus..."
        z "She just wanted us to back off."
        z "But... What Athena was doing... What she's doing everyday to those people..."
        z "What she did in the town of the faceless god."
        z "It's wrong."
        z "I couldn't let that stand."
        scene v223
        s "..."
        s "You know there's no going back from decisions like these, I trust?"
        scene v224
        z "Yeah..."
        s "..."
    elif against_athena == 12: #if fought once and left or the other way round
        scene v193
        z "I fought Athena this time."
        z "I actually..."
        z "I..."
        z "I liked it..."
        z "I almost won, Seira..."
        z "I almost won."
        z "Athena's..."
        z "Well, minion, I suppose. She interfered before I could finish Athena off..."
        z "And Venus had to kill her."
        scene v194
        s "You almost finished Athena off?!"
        scene v193
        z "Yeah..."
        z "I think..."
        z "But Seira..."
        z "Athena's minion..."
        scene v192
        z "She was Venus's dear childhood friend..."
        z "And Venus had to kill her to protect me..."
        scene v191
        s "..."
        scene v193
        z "She didn't want to fight, actually..."
        z "Venus..."
        hide v15m1
        show v15m1 with dissolve(1.0)
        z "She just wanted us to back off."
        z "But... What Athena was doing... What she's doing everyday to those people..."
        z "What she did in the town of the faceless god."
        z "It's wrong."
        z "I couldn't let that stand."
        scene v223
        s "..."
        s "You know there's no going back from decisions like these, I trust?"
        scene v224
        z "Yeah..."
        s "..."
    elif against_athena == 9 or against_athena == 7:
        scene v192
        z "I left a boy to die..."
        z "I had a choice between letting him die and trying to fight Athena."
        z "And she had a fury there too..."
        z "Venus was there too... She asked me to back off from the fight."
        z "So I did..."
        z "The fury..."
        z "She was Venus's childhood friend... We would've had to kill her too..."
        scene v223
        s "..."
        s "So you just left..."
        scene v224
        z "Yeah..."
        s "..."
    else:
        scene v193
        z "I made a deal with her..."
        z "Athena."
        z "I made her spare a boy's life in exchange for me not interfering with her curse over the town."
        hide v15m1
        show v15m1 with dissolve(1.0)
        z "So even though this one person has been spared, the rest of them will still suffer."
        z "I had a choice between walking away and trying to fight Athena."
        z "And she had a fury there too..."
        z "Venus was there too... She asked me to back off from the fight."
        z "So I did..."
        z "The fury..."
        z "She was Venus's childhood friend... We would've had to kill her too..."
        scene v223
        s "..."
        s "So you just left..."
        scene v224
        z "I made Athena spare one boy. But yeah... We left."
        s "..."
        scene v225
        s "Want to talk more about it?" #Gets close to him.
        scene v226
        z "..."
        scene v227
        z "No..."
        scene v228
        s "..."
        #Grabs his face.
        scene v229
        s "Look..."
        scene v230
        s "I can't make these decisions for you..."
        scene v231
        s "And I already told you there's no such thing as a right or a wrong choice in situations like these."
        #cuddling saying this
        s "Just know this, baby."
        s "I will always be at your back. Whatever you decide."
        s "And I will always be proud of you. Whatever you become."
        z "..."
        z "Thank you, Seira..."
        s "Anytime [mc_name]."
        s "Now. You've got a big job ahead of you. Get some rest."
        z "Goodnight Seira. I love you."
        s "Goodnight, darling. I love you too."
        #seira gives him a kiss on the forehead then leaves

#3) Meeting: 	
    #-If fought athena, all the ninja celebrate Z's coming back asking about his fight with her. Helena is caught eavesdropping on them looking conflicted (she believes that they actually have a chance against athena and is now willing to defy her.)
    #-If didn't fight athena, Helena may not defy athena later on.
    #Stephanie's mission returns with no casualties. She's frustrated saying they just let them go.
    #Anabelle reports that several cities have been abandoned after being attacked by bandits.	
    scene v195
    stfny "We were totally helpless... I couldn't even lay a finger on him."
    stfny "He was crazy strong."
    scene v196
    hly "Stronger than your mom?"
    scene v197
    stfny "Yeah... I think so..."
    stfny "I would say he's even stronger than Seira..."
    scene v198
    stfny "His long ranged attack is ridiculous. My shield barely held against it for five second."
    scene v196
    hly "How on earth did you all make it out of the fight, then?"
    scene v199
    stfny "..."
    scene v195
    stfny "They just..."
    stfny "Let us go..."
    scene v196
    hlna "..."
    scene v196
    hly "Why would they let you go?"
    scene v197
    stfny "I don't know..."
    scene v202
    stfny "A girl interfered... Axius's daughter, I think... She said something to him about me b-"
    scene v203
    hlna "Look. It doesn't matter how exactly you all made it out alive. The important thing is that you all did."
    scene v204
    scene v205
    a "Next time, we may not be so lucky, Helena."
    a "We have four new missions already, and the last batch of ninjas just got home. A few of them are too injured to take a new mission. And almost all of them are still too tired to take one."
    a "So... Do we accept these missions? Or do we turn them down?"
    scene v206
    hlna "..."
    scene v207
    z "I can take a mission if needed. I'm not really tired."
    if against_athena >= 12:
        scene v211
        hly "You fought Athena herself, [mc_name]... You should really get some rest..."
        scene v213
        hlna "..." #Focus a bit on her.
        scene v209
        a "Is it true you almost defeated her, [mc_name]?"
        scene v210
        z "..."
        scene v209
        z "Probably... If it weren't for her fury..."
        z "I might've..."
        scene v210
        a "..."
    else:
        scene v211
        hly "You faced Athena herself, [mc_name]... You should really get some rest..."
        scene v210
        a "..."
    scene v216
    a "Something is going on..."
    a "Something big..."
    a "On our way to our mission, we traveled through three villages. All three were abandoned recently."
    scene v215
    a "It's almost as if someone is behind all this chaos..."
    #Cut to axius.


#4) Athena and Axius:
    #After the meeting, Axius is sitting infront of a chess board.
    #He's contacted by athena using an orb.
    scene v218
    scene v219
    scene v220
    scene v222
    athna "I hear you have been busy..."
    athna "A dozen villages abandoned. Three burnt to the ground."
    athna "What is the meaning of this, incubus?"
    scene v221
    axs "You told me the ninja villages were our enemies, didn't you?"
    scene v222
    athna "What of it?"
    scene v221
    axs "Attacking them directly is not the way to go..."
    axs "This is."
    athna "..."
    scene v222
    athna "You..."
    scene v221
    axs "They are too strong to attack directly."
    axs "But... If we exhaust them first."
    axs "If the ninjas don't get the chance to sit down after one mission because they get sent on another right away..."
    scene v220
    athna "..."
    #Checkmate move on the chess board after spreading the pieces away from the king. - this needs animating
    scene v221
    axs "That's how we'll beat them."
    scene v220
    athna "..."
    #Cut.

#5) Z meets Jenny in the ninja village:
    #Looks like he didn't get enough sleep.
    scene v236
    z "..." #Going to check on the wounded.
    scene v237
    cndy "[mc_name]?"
    scene v238
    z "..."
    z "Hey, Candy."
    z "How are you?"
    scene v239
    cndy "I'm okay, thanks for asking..."
    scene v240
    z "No injuries or anything from your last mission?"
    scene v239
    cndy "No. I'm fine."
    scene v240
    z "I see..."
    cndy "..."
    scene v241
    cndy "Are you okay? You look..."
    scene v240
    z "Hm?"
    scene v242
    Character("Voice from behind", color = "c44f00") "Like you didn't get enough sleep."
    scene v243
    z "I actually didn't sleep very well..."
    z "..."
    z "Who-" #Turns around.
    scene v244
    z "..."
    scene v246
    z "......"
    scene v247
    z "........."
    scene v245
    z "I guess I'm still dreaming."
    scene v248
    jnfr "No you're not, you dummy!"
    scene v249
    z "..."
    scene v250
    z "What?!"
    scene v251
    z "Jenny?! The fuck are you doing here?!"
    scene v253
    jnfr "Wow... That's quite the warm welcome..."
    scene v251
    z "No! I didn't mean..."
    scene v252
    z "It's just... Does Jamie have business with the ninja village or something?"
    z "But if so, why are you wearing a white belt? Did you both join the ninja village?"
    scene v254
    z "Or did you two brea-"
    scene v255
    jnfr "No, not exactly..."
    scene v250
    z "..."
    scene v252
    z "Are you maybe here to issue a mission?"
    scene v256
    jnfr "I guess you can say that, yeah..."
    scene v255
    jnfr "But I also wanted to help, and Helena told me I should join up if I want to help so I did. She said I could still leave any time I want, but I don't see that happening any time soon..."
    scene v254
    z "What's-"
    scene v257
    tmra "Apparently, her betrothed has been trading with bandits and he doesn't feel safe trading with them anymore."
    scene v258
    tmra "And he thinks if they learn he cut ties with them, they might try to kill him or something."
    scene v259
    tmra "I just had to listen to what he had to say. For their safety, they'll stay here for the time being until the bandit issue has been settled."
    scene v260
    jnfr "..."
    scene v261
    jnfr "Hey, cutie."
    jnfr "Tamara, right?"
    scene v262
    tmra "Yeah... Hey..."
    scene v263
    z "I see..."
    scene v264
    jnfr "Jamie has always been secretive about who he does business with, so I don't know too much about it... I just know that he and my mom were dealing with fishy people..."
    scene v265
    z "So they're both potentially asking for protection from the same people..."
    scene v266
    tmra "Yeah... I think that might be the case too."
    tmra "Sadly, both of them refuse to share all the details, so we can't really be sure."
    scene v269
    gbrla "Jenny!"
    scene v270
    gbrla "Oh hey, [mc_name]!"
    scene v271
    z "Hi there, Gabbie."
    scene v272
    gbrla "Can I borrow Jenny for a few minutes? She's helping us with treating the injured."
    scene v274
    z "Oh?"
    scene v273
    jnfr "Yeah... I'm not really good at it, but it's the least I can do to be useful around here. Seeing how you guys are protecting us, giving us food and a place to stay, and all of that..."
    scene v275
    #They leave.
    scene v276
    scene v277
    tmra "..."
    scene v278
    tmra "What are you looking at?"
    scene v279
    z "Nice to see you too, Tamara."
    #Leaves.
    scene v280
    cndy "I kinda wanna eat something..."
    scene v281
    z "I could use something to eat too..."
    scene v282
    z "Wanna go grab something?"
    scene v283
    cndy "Sure..."

#6) Eating scene:
    #Skip to them at the foody place
    scene v291
    z "What was she like?" #Walking towards the foody place
    scene v292
    cndy "Well, I don't really remember much..."
    cndy "She somehow got Centoria first."
    scene v293
    cndy "Even though Centoria had three clones."
    scene v294
    cndy "She was somehow able to tell which one was the real Centoria, and then-"
    cnt "And then she approached me. Really quickly. She's probably more or less as fast as you."
    scene v296
    z "Oh. Hey, Centoria."
    scene v297
    cnt "Hey, [mc_name]. Hey, Candy."
    if invited_misty >= 1:
        scene v299
        cnt "What do you guys wanna eat? We have roasted birds, potato chips, and turtle soup."
        scene v301
        z "Turtle soup?"
        scene v302
        misty "It's my own recipe. You haven't tried it so far?"
        scene v303
        z "I don't believe so..."
        scene v304
        misty "You should really try it."
        scene v305
        z "..."
        z "By the way, how are you doing, Misty?"
        scene v304
        misty "I'm doing just fine, thanks, [mc_name]."
        scene v307
        misty "How about you? I heard your last mission was crazy."
        scene v306
        z "Ehh... I'm okay... It's Venus I'm most worried about..."
        scene v307
        misty "Yeah... I heard about that too..."
        z "..."
        scene v308
        cndy "Can I have the potato chips?"
        scene v309
        misty "Sure."
        pause(1)
        menu:
            "Get the turtle soup.":
                scene v311
                z "I want to try the turtle soup, actually."
                scene v313
                misty "Oh? Okay, you got it!"
                $ misty_aff += 2
                scene v314
            "Get something else.":
                scene v311
                z "I'll have the same, please."
                scene v312
                misty "Sure!"
        #Skip a bit.
        #Centoria and misty are sitting down with them.
        scene v324
        misty "Why?"
        scene v327
        cnt "I think her ability doesn't work unless she whispers it in your ear?"
        scene v315
        cndy "Yeah. Something similar happened to me."
        cndy "I was hiding behind a tree. I don't know how she was able to spot me, but she whispered to me too..."
        cndy "And then..."
        scene v316
        cndy "..."
        scene v317
        cndy "I just remember waking up like 30 minutes after."
        cndy "I must've lost consciousness..."
        scene v316
        z "..."
        scene v318
        z "Do you remember what she said to you?"
        scene v319
        cndy "..."
        scene v317
        cndy "No..."
        cndy "I just remember it being..."
        cndy "Hmmm..."
        scene v320
        cnt "Soothing?"
        scene v323
        cnt "Like my mother singing me a lullaby before going to bed."
        scene v332
        cndy "Yeah..."
        scene v333
        cnt "I actually..."
        cnt "I do actually remember my mother singing to me now..."
        scene v329
        cnt "When I was young..."
        cnt "I didn't remember anything from my parents before, but now..."
        cnt "Which makes sense because my mother died giving birth to me and my father never stuck around long enough for even that..."
        scene v332
        z "..."
        scene v324
        misty "I'm sorry..."
        scene v328
        cnt "Thanks, Misty..."
        scene v329
        cnt "I remember it though..."
        cnt "My mother's face..."
        cnt "But it's weird, because she's not..."
        scene v336
        z "..."
        z "Not what?"
        scene v333
        cnt "Well, I think it's just the magic... I'm just confused..."
        scene v337
        tr "You started eating without me?!"
        scene v338
        z "Oh. Hey, Torr."
        z "How are you do-"
        scene v339
        tr "Na-uh!"
        scene v340
        tr "How are YOU doing?"
        scene v341
        z "..."
        z "I'm fine, Torr. Thanks."
        scene v343
        tr "..."
        scene v342
        tr "Can I get some food?"
        misty "I'll get you some right away."
        #Sits down.
    else:
        #if didn't invite misty, there's a spider in the bg.
        scene v299
        cnt "What do you guys wanna eat? We have roasted skeevers or potato chips?"
        scene v300
        cndy "Can I have the potato chips?"
        scene v301
        z "Me too please..."
        scene v299
        cnt "Sure."
        #Skip a bit.
        #Centoria is sitting down with them.
        scene v325
        z "Why?"
        scene v326
        cnt "I think her ability doesn't work unless she whispers it in your ear?"
        cndy "Yeah. Something similar happened to me."
        cndy "I was hiding behind a tree. I don't know how she was able to spot me, but she whispered to me too..."
        cndy "And then..."
        cndy "..."
        cndy "I just remember waking up like 30 minutes after."
        cndy "I must've lost consciousness..."
        z "..."
        z "Do you remember what she said to you?"
        cndy "..."
        cndy "No..."
        cndy "I just remember it being..."
        cndy "Hmmm..."
        cnt "Soothing?"
        cnt "Like my mother singing me a lullaby before going to bed."
        cndy "Yeah..."
        cnt "I actually..."
        cnt "I do actually remember my mother singing to me now..."
        cnt "When I was young..."
        cnt "I didn't remember anything from my parents before, but now..."
        cnt "Which makes sense because my mother died giving birth to me and my father never stuck around long enough for even that..."
        z "..."
        cnt "I remember it though..."
        cnt "My mother's face..."
        cnt "But it's weird, because she's not..."
        z "..."
        z "Not what?"
        cnt "Well, I think it's just the magic... I'm just confused..."
        scene v337
        tr "You started eating without me?!"
        scene v338
        z "Oh. Hey, Torr."
        z "How are you do-"
        scene v339
        tr "Na-uh!"
        scene v340
        tr "How are YOU doing?"
        scene v341
        z "..."
        z "I'm fine, Torr. Thanks."
        scene v343
        tr "..."
        scene v342
        tr "Can I get some food?"
        cnt "Yeah. Give me a second."
        #Sits down.
    scene v344
    z "Goblins?"
    scene v345
    tr "Yeah."
    tr "Like eight... No, nine of them."
    scene v344
    z "They decided to raid the village on their own?"
    scene v345
    tr "Well, not raid... More like kidnap women who they catch alone in the woods nearby."
    scene v344
    z "I see..."
    z "There were some goblins venturing all the way north when I joined the ninja village..."
    z "But those were mostly sent by Axius when he was looking for me, I think..."
    z "Is it normal for them to do things like this often?"
    scene v346
    a "No. It's not." #It's annie and yumi with the cat.
    scene v347
    z "Oh hey, guys! How long have you been standing there."
    #Yumi and the cat sit next to torr who doesn't look happy about the cat.
    a "Goblins hardly venture into human territory. But we've been receiving several reports about them doing so in the last couple of days."
    z "..."
    z "What could that mean?"
    a "I'm not sure... But something is up..."
    a "Increased bandit activity is also being reported and we're being flooded with missions."
    a "Aren't goblins typically found near elf villages?"
    scene v350
    tr "Yeah. We have a goblin village close to us."
    scene v351
    cnt "Us too. There has been a conflict between my city and the nearby goblins for decades now."
    scene v352
    a "..."
    a "By the way, Centoria..."
    a "There has been a letter from your city."
    scene v353
    cnt "Eh?!"
    scene v354
    a "From the crowned prince himself."
    a "It involves you too, [mc_name]."
    z "?"
    #Skip to yumi, centoria and z being briefed by helena.
    scene v356
    z "They asked for me?"
    scene v355
    hlna "Personally, yes."
    hlna "For Centoria too of course. And another high ranking ninja. As they said, it's of the highest importance to them."
    hlna "So I picked Yumi as she and Hailey are the least injured of the higher ranking ninjas. And I need Hailey for another mission."
    scene v357
    z "I understand Centoria and a high ranking ninja but why me?"
    scene v358
    hlna "Well, you've apparently become something of a celebrity around the continent."
    hlna "The demi-god ninja."
    scene v359
    hlna "Of course, the title did not originally belong to you. It's an old title that people have been hearing for years. That's probably why it took off again so quickly."
    scene v360
    z "An old title?"
    scene v361
    ymi "My brother. That's what people used to call him. He was the first demi-god ninja."
    scene v362
    z "Sirius?"
    scene v359
    hlna "And since Sirius is not active as a ninja any more, you seem to have inherited the title from him."
    hlna "I must admit, you have done really well yourself of course."
    scene v367
    z "..."
    scene v366
    hlna "Well, back to your mission..."
    hlna "The princess, Illya the Third. It's gonna be her birth week in two days. She needs a body guard while traveling around as a part of the celebration."
    hlna "She apparently wants to visit villages around the city walls as well. Which is probably going to be very dangerous, even more so considering that the local goblins have been repeatedly attacking the elven city recently."
    scene v360
    z "I see..."
    z "That does sound dangerous..."
    #need a scene of z looking confused here in same pose as the rest
    z "Wait, did you say birth week?"
    scene v363
    cnt "It's an elven tradition to celebrate not the day on which you were born, but the whole week."
    scene v364
    z "I see..."
    scene v363
    cnt "Oh, and this is a major event, since the princess will turn twenty. It means she..."
    scene v364
    z "Hm?"
    scene v363
    cnt "It means she can make a major change to the elven way of life."
    cnt "It's supposed to teach her responsibility. She's expected to one day rule the city, after all."
    scene v364
    z "Hmmm..."
    scene v368
    hlna "Normally, seeing how many other missions we have, I'd not prioritise a mission like this."
    scene v366
    hlna "However, our alliance with the elves is paramount. I'll have to humour them on this."
    hlna "You'll leave tomorrow at dawn. The mission leader will be Yumi. The objective is simple; protect the princess at all costs."
    hlna "But... I would still try to limit the loss of goblin lives as much as I could."
    scene v367
    z "Yeah... Understood."
    scene v368
    hlna "We'll discuss your points from both missions after you return."

#7) Torr sparing with Anabelle:
    #Z is walking around.
    #Hears sparing sounds.
    scene v369
    scene v370
    z "?"
    scene v371
    #Goes to it.
    scene v372
    z "..."
    scene v373
    z "(Is that...)"
    scene v374
    scene v375
    a "Good. Always minimise the area your opponent can hit."
    scene v376
    a "Grip your sword more tightly."
    scene v377
    tr "..."
    scene v378
    a "Yeah. That's it."
    scene v379
    a "Here I come."
    scene v380
    scene v381
    scene v382
    scene v384
    scene v385
    scene v386
    scene v387
    scene v388
    scene v389
    scene v390
    #Anabelle beats her easily. But Torr blocks a few times.
    #Z can tell when torr makes a mistake.
    scene v391
    scene v392
    scene v393
    scene v394
    scene v395
    scene v396
    scene v397
    z "(No! Don't rush!)"
    #Torr's sword flies next to Z's foot when she falls.
    scene v398
    scene v399
    scene v400
    scene v401
    a "[mc_name]? How long have you been standing there?"
    z "Just a minute or two."
    scene v402
    z "Did Torr ask you to train her?"
    a "Yeah... Actually..."
    scene v403
    tr "I asked both her and Seira. But Seira is busy today, so only Anabelle is teaching me right now."
    scene v404
    z "Hmmm..."
    scene v405
    scene v406
    scene v407
    #Picks up the sword.
    a "..."
    tr "..."
    scene v408
    z "Let's see what you learnt."
    scene v409
    scene v410
    tr "I don't think I can beat you just yet, [mc_name]."
    z "We're just practicing. It doesn't matter who wins."
    scene v411
    tr "Okay, good point..."
    scene v412
    scene v413
    scene v414
    scene v415
    scene v416
    scene v417
    scene v418
    scene v419
    scene v420
    scene v421
    scene v422
    scene v423
    scene v424
    scene v425
    scene v426
    scene v427
    scene v428
    #Beats Torr again.
    tr "Oh..."
    scene v429
    z "Well, it was much better than what happened the first time we tried that..."
    scene v430
    tr "Heh..." #Smiles.
    scene v431
    a "Can I have that for a minute?"
    scene v432
    tr "Sure."
    tr "I need to go talk to my team about tomorrow's mission anyway."
    scene v433
    tr "Thanks for your help, Anabelle."
    scene v434
    a "Any time, honey."
    scene v435
    z "Your team?"
    z "You're the mission leader?"
    scene v436
    tr "Yep."
    tr "First time I'm the mission leader. Hehehehe..."
    scene v437
    z "Your team is..."
    scene v439
    tr "Candy and Gabbie."
    scene v438
    z "Oh, Gabbie is going on a mission?"
    scene v440
    tr "Yeah... We needed a medic on the team, so it was supposed to be Venus. But Helena said she doesn't want to give her missions just yet."
    scene v438
    z "Yeah... I see."
    scene v440
    tr "See you, guys."
    a "Bye."
    scene v441
    z "..."
    z "She's grown a lot more mature, hasn't she?"
    scene v442
    z "I'm really prou-"
    scene v443
    #Hits her head against sth.
    tr "Awww!"
    scene v444
    tr "..."
    scene v445
    scene v446
    #Leaves.
    scene v447
    z "..."
    scene v448
    z "Wanna give it a go?"
    scene v449
    a "Sure..."
    scene v450
    a "..."
    scene v451
    scene v452
    a "You know..."
    a "I've been..."
    scene v453
    a "...meaning to talk to you."
    scene v454
    a "It's just we never got a chance to properly talk... With Sirius, and then the mission, and..."
    scene v455
    z "Yeah... I get you."
    a "..."
    scene v456
    a "About what happened in..."
    a "In Kalytro..."
    scene v457
    a "After you fought Nari and we barely made it out alive..."
    scene v455
    z "..."
    z "Yeah..."
    scene v458
    z "Listen-" (multiple=2)
    a "So I w-" (multiple=2)
    scene v455
    z "..." (multiple=2)
    a "..." (multiple=2)
    z "You go first."
    a "..."
    scene v456
    a "Okay..."
    a "I just wanted to say..."
    scene v457
    a "Should we just pretend it never..."
    scene v458
    a "You know..."
    scene v459
    z "..."
    z "I guess that's probably for the best..."
    z "(I really can't see myself being with this girl...)"
    z "(She's totally out of my league...)"
    z "(Right?)"
    scene v457
    a "It was just a tiny mistake... I don't want things between us to be awkward forever..."
    z "(And her saying it was a mistake just proves that...)"
    scene v455
    z "I get you. Yeah."
    scene v457
    a "So..."
    a "We forget about it?"
    scene v455
    z "Sure."
    scene v457
    a "And swear to never do it again?"
    scene v455
    z "Yeah."
    scene v457
    a "You know, so... Like not even other stuff..."
    scene v455
    z "Of course, that goes without saying..."
    z "You're like an older sister to me... It's just..."
    scene v457
    a "Wrong."
    scene v455
    z "Exactly."
    z "Honestly, you're totally right."
    z "We absolutely can't do this again... Any of it..."
    scene v457
    a "Oh, I'm so glad you understand... You are really mature, you know..."
    a "And I just didn't want things to be awkward between us. I really think of you as my little brother and I didn't want to lose that, you know?"
    scene v455
    z "Of course. I didn't want to lose what we have either."
    z "And I have a huge amount of respect for you, Annie. I really think of you as my older sister."
    scene v457
    a "Ohhh... Thanks..."
    a "So let's just forget about it and never mention it in any way at all?"
    scene v455
    z "Sounds good."
    z "Nothing of any sort regarding it. May it die in our memories and be done with it."
    scene v457
    a "Exactly."
    scene v455
    z "Right?"
    scene v457
    a "Yeah..."
    scene v455
    z "Yup..."
    scene v457
    a "Hmmm..."
    z "..."
    a "..."
    z "..."
    a "..."
    scene v458
    a "Sooo... Ready to spar?"
    scene v459
    z "Yup. Let's do it!"
    scene v460
    a "..."
    scene v461
    scene v462
    scene v463
    scene v464
    scene v465
    scene v466
    #looks at him while he's about to attack.
    #Suddenly blushes and loses her focus, so he beats her easily.
    scene v467
    z "Eh?! Are you okay?"
    scene v468
    z "Sorry! I think I swung a bit too hard?!"
    scene v469
    a "No, no... It's not..."
    scene v471
    a "Listen, I think I might've overestimated my stamina... I think I should take a break after all."
    scene v470
    z "I see."
    scene v469
    a "Let's call it a day?"
    scene v470
    z "Sure."
    scene v469
    a "Sorry we had to cut it short... I'll make it up to you some other time, I promise..."
    scene v470
    z "It's okay, you don't need to worry about that."
    scene v472
    z "Here... Let me help you up."
    scene v473
    #Pulls her a bit too close to him.
    scene v474
    scene v475
    a "..." #Blushes again.
    scene v476
    a "See you around!" #Leaves.
    scene v477
    z "..."
    scene v478
    z "(So much for it not being awkward...)"

#8) Alchemist's hut:
    #Z walking towards his room
    #scene 1
    z "(Whistling)..."
    #Gabbie peeks out and grabs z - yeets him into alchemists hut - anim 1
    #scene 2
    gbrla "Heyy [mc_name]... You got a minute for us?"
    #scene 3
    z "Uhhh, sure Gab, what can I help you with?"
    #scene 4
    gbrla "Well, Margot had an experiment that she wanted to test, and thought it might be easier if we got you to help us with it."
    #Margot says the below suddenly appearing behind Z and purring in his ear - scene 5
    margot "Please [mc_name], won't you help us poor scientists with a little experiment?"
    #Z jumps - scene 6
    z "AHH"
    #scene 7
    z "Margot... Hey..."
    menu:
        "Sure, I'll help. What do you need me to do?":
            #margot and gabbie take their shirts off - scene 8
            gbrla "..." (Multiple=2)
            margot "Oh you already know, stallion" (Multiple=2)
            #scene starts - gab + margot on knees - one each side of z dick - licking - anim 2
            margot "Hmmmnnnn"
            gbrla "Mmmmffff"
            #scene 9
            margot "Oh Gods I forgot how big you are..."
            #scene 10
            margot "Are you certain I can't experiment on you? I promise it won't hurt too much."
            z "Yeah that's still not happening Margot. Get back to where you belong."
            #scene 12
            margot "Yes sir. Anything for this cock."
            #scene 13
            z "Gab? How you doing down there?"
            #scene 14
            gbrla "Mhhhhh I'm in love"
            #scene 15
            z "Glad to hear it. I think I might be too if you continue with this."
            #scene 16
            gbrla "Happily."
            #anim 2 again
            z "Let's get a bit more comfortable girls."
            #z pushes m to the ground and grabs g and places her over m's face - scene 17
            margot "Hmmmnnn..."
            #scene 18
            margot "This is exactly how I see our experiments going, [mc_name]"
            #scene 19
            z "I already told you, that's not going to happen. Let's see if you can put your mouth to better use, Gabbie, sit down."
            #scene 20
            gbrla "On her face? Are you sure?"
            #scene 21
            z "Yes I'm sure, sit down Gab."
            #scene 22
            gbrla "Oh, o-okay. Sorry Margot"
            #g sits down on ms face - scene 23
            margot "Mmmmfff Hmmmmmmm"
            #anim 3
            gbrla "AHHHMMMM Oh my Gods she's moving her tongue so much. I-It's so go-"
            #z kisses gabbie - scene 24
            $ gbrla_lst+=2
            #back to anim 3
            gbrla "Oh Gods. I think she's close."
            #scene 25
            gbrla "HMMMMMNNNN" (multiple=2)
            margot "MMMNFFF HMMMMNNNN-" (multiple=2)
            #scene 26
            z "Gabbie get up and get on all fours."
            #gabbie gets on all fours - dripping
            #scene 27
            z "How was that psycho? Good enough for you?"
            #margot slightly quivering for line below - anim 4
            margot "Oh my- You're gon- gonna have to give me a-a couple of minutes. I don't think, haa- I don't think I've ever cum that hard before."
            #scene 28
            z "Good to hear. You ready Gabbie?"
            #scene 29
            gbrla "Please. [mc_name]. Please fuck me. Please. I'm begging you."
            z "You asked for it."
            #slides his dick in completely in one go - anim 5
            #scene 30
            z "Ohhhh shit that's tight."
            #anim 6
            gbrla "HAAAA-"
            gbrla "I"
            gbrla "LOVE"
            gbrla "YOUR"
            gbrla "COCK"
            gbrla "HMMMMNN"
            gbrla "Oh Gods I'm gonna CUUUU-"
            #scene 31
            gbrla "MMMMMFFFFFF"
            $ gbrla_lst+=2
            #anim 6 again
            #z keeps going
            gbrla "Wait! [mc_name]! Please!"
            z "That's not gonna happen Gabs. You feel so fucking good."
            z "Gabbie, put your mouth to good use and help Margot out."
            gbrla "Haaa... Hmmnn"
            #z pushes gab head down into margots pussy - scene 32
            margot "OH YES!"
            #anim 7
            gbrla "Hmmmnnn MMMMFffff"
            margot "I think she's going to cum again, [mc_name]. She's licking so hard and breathing so heavily."
            margot "HMMMMmNnn"
            z "She's not the only one. Holy fuck"
            #scene 33
            margot "Where are you gonna finish stallion? Inside sweet Gabbie? Inside little old me? Or maybe you want to paint both of us?"
            menu:
                "Cum inside Gabbie":
                    #scene 34
                    z "Gods Gabbie I'm cumming"
                    #fills her up - scene 35
                    gbrla "HMMMMMNNNN"
                    margot "AHHHHHHH"
                    #margot crawls round to mc - scene 36
                    #scene 37
                    margot "Holy shit Gabbie he filled you to the brim."
                    gbrla "mmmnnnn haaa-"
                    $ gbrla_lst+=2
                "Cum inside Margot":
                    z "Shit I'm gonna cum. Margot get over here!"
                    #margot moves out from under gabbie - z inserts himself and fills her up
                    #scene 38
                    margot "AHHHHHH"
                    margot "Holy shit there's so much."
                    #scene 39
                    #she grabs some that is leaking out and eats it
                    #scene 40
                    margot "And it tastes amazing, Gods."
                "Cover them both":
                    z "Get on your knees both of you"
                    #scene 41
                    #gab and margot kneel before z and start kissing his tip
                    #scene 42
                    #z cums on their faces
                    #scene 43
                    z "Holy shit that was amazing. You are both... Amazing"
                    $ gbrla_lst+=2
                    $ gbrla_aff+=2
            #scene 44
            margot "Thank you for that stud. Hope we can do this again soon."
            #scene 45
            z "You know, for once Margot, I agree with you."
            #scene 46
            gbrla "Haaaa... Cock... So good..."
        "I'm kinda busy right now, sorry guys.":
            $ dummy+=1
            #scene 47
            margot "Really? Ok I guess we'll see you another time."
            #scene 48
            gbrla "Bye [mc_name]"
            #scene 49
            z "See you soon girls."


#9) Scene with Jenny:
    #Helena is showing Jenny and Jamie the bath.
    #Z is passing by.
    scene v561
    hlna "We didn't really have any men around here for such a long time that there are no rules against men and women using it at the same time."
    hlna "I guess now we should have some put in effec-"
    scene v562
    z "Hey."
    scene v564
    hlna "Oh, Hey there, [mc_name]."
    hlna "I was showing Jenny and her betrothed around."
    scene v563
    z "Wouldn't that have been more convenient during the day?"
    scene v564
    hlna "Yeah. But I had lots to attend to earlier. And I didn't have anyone available to do it. So I thought why not do it myself."
    hlna "And I had nothing else to do for the rest of the evening..."
    scene v563
    z "I see..."
    scene v566
    jnfr "You guys have such a wonderful place here..."
    scene v567
    jamie "A bigger room would've been nice..."
    scene v568
    jamie "Aww..." #Jenny hits him.
    scene v569
    jnfr "He's just in shock after everything that happened."
    scene v570
    z "..."
    scene v571
    z "What happened?"
    scene v572
    jnfr "..." #Looking at jamie
    scene v573
    jamie "I..."
    jamie "I was just dealing with the wrong people... And I was too deep in it..."
    scene v574
    z "What people? What did you-"
    scene v575
    jamie "Look... If we're going to talk about this, at least get me a drink."
    scene v576
    z "..."
    menu:
        "Invite him and Jenny to drink in the bath.":
            scene v576
            z "There is wine in the bathing room..."
            scene v577
            jnfr "Ohhh... I'm dying for a warm bath."
            scene v580
            jamie "..."
            z "So? What do you say? Shall we?"
            scene v581
            jamie "I suppose why not."
            scene v582
            jnfr "Hold on... I'm not going to be the only girl with two guys..." #Sus.
            scene v583
            z "Then Helena why don't you join us?"
            scene v584
            hlna "Eh?"
            scene v585
            z "You said you had nothing to do, right?"
            scene v586
            hlna "Yeah..."
            scene v587
            jnfr "So it's settled then?"
            scene v588
            z "Yup. Let's go."
            scene v589
            jnfr "You guys go on ahead. I'll get something from my room and be right behind you."
            scene v590
            #Skip.
            scene v591
            hlna "Ahhhh... This is so good..."
            scene v592
            jamie "Yeah... It's not bad at all..."
            scene v593
            jamie "Wasn't expecting something so luxurious here..."
            scene v594
            jnfr "Sorry to keep you guys waiting."
            scene v595
            z "No worries."
            scene v597
            z "I'll get the wine."
            scene v596
            jnfr "I'll help."
            scene v598
            z "Hmmm... This sho-"
            scene v599
            scene v600
            jnfr "Pssst."
            scene v601
            z "?"
            #Hands him cards.
            scene v602
            z "What's this?"
            scene v607
            jnfr "Something to spice things up."
            scene v602
            z "..."
            #Looks at them.
            scene v603
            scene v604
            z "Where did you get this..."
            scene v605
            jnfr "Esyl, I think..."
            jnfr "This fat guy with a weird mustache was selling them..."
            scene v606
            z "..."
            scene v607
            jnfr "So? Shall we?"
            scene v606
            z "Sure..."
            scene v608
            z "So..."
            z "Instead of just drinking..."
            scene v609
            #Shows them the cards.
            z "Jenny and I have an idea on how to make this more interesting."
            scene v610
            jamie "Interesting?"
            scene v611
            hlna "What are those cards?"
            scene v612
            jnfr "They are game cards I got from Esyl."
            scene v611
            hlna "What kind of game? I'm not usually good at games..."
            scene v612
            jnfr "It's just a drinking game. And don't worry, it doesn't involve skills at playing or anything like that."
            scene v613
            hlna "Drinking game?"
            scene v614
            hlna "Those games where you'll ultimately get drunk?"
            scene v615
            jnfr "Pretty much."
            scene v616
            hlna "I don't know if I should be getting drunk... I have to protect the village if anything happens..."
            scene v608
            z "You've been stressed over the village's safety for a while now, Helena. Even you have to let go a little sometimes."
            z "I single handedly dealt with the attacker the last time. And I'm pretty sure at least Anabelle and Seira are even more capable than me."
            z "In the unlikely scenario where something should happen while you and I are here, those two will manage."
            scene v619
            hlna "..."
            scene v620
            hlna "I suppose you have a point."
            hlna "So? How does one play?"
            scene v617
            jnfr "Okay, so..."
            scene v618
            jnfr "We're supposed to play in pairs. Since Jamie and I are betrothed, it makes sense that we should be a pair."
            scene v619
            z "I guess you and I are a pair then, Helena."
            scene v620
            hlna "Okay, sure."
            scene v617
            jnfr "Great!"
            scene v618
            jnfr "I'll start to show you guys how it's done."
            #Physically explains how it's done.
            scene v621
            jnfr "You draw a card..."
            jnfr "You read whatever is written on it."
            scene v622 with Dissolve(1)
            scene v623 with Dissolve(1)
            scene v624
            jnfr "For example this card says: Slap a player from the opposing team on any part on the body you want."
            jnfr "Well... I'm supposed to do what's on the card and slap one of you guys. But I don't want to."
            jnfr "So... If I don't do what's written I have to drink."
            scene v625
            #drinks.
            scene v624
            jnfr "And... Well, once someone can't drink any more... They're out. They lose, basically."
            jnfr "Easy enough, right?"
            scene v620
            hlna "Yeah."
            scene v617
            jnfr "Okay, let's play clockwise."
            jnfr "Helena, you're up."
            scene v626
            scene v627
            #Draws a card.
            hlna "..."
            scene v628
            hlna "Your partner must take off their top."
            scene v629
            hlna "..."
            z "But I'm not wearing a top..."
            scene v630
            jnfr "Well that means she drinks."
            scene v631
            hlna "Ah..."
            scene v632
            scene v633
            #Drinks.
            #Jamie draws.
            scene v634
            scene v635
            jamie "Drink twice."
            scene v636
            jamie "Oh... That's not great..."
            scene v637
            scene v638
            #Drinks twice.
            scene v637 #you are here
            jnfr "Seems like you could get used to this Jamie?"
            scene v639
            jamie "Hmmmm..."
            z "Okay, I'm up."
            scene v640
            #Draws.
            scene v641
            z "Arm wrestle a member of the opposing team. If you lose, drink twice. If you win, kiss the other."
            scene v643
            jamie "Eh?"
            jamie "I'm guessing you're going to arm wrestle me."
            scene v644
            z "No, Imma wrestle Jenny and kiss you..."
            z "Of course I'm gonna wrestle you, dude..."
            scene v645
            jamie "..."
            #They arm wrestle.
            scene v646
            jamie "You're quite jacked, huh..."
            jamie "I guess you need to be if you're going to be a ninja."
            scene v647
            z "We do get quite a bit of physical exercise, so yeah..."
            scene v648
            scene v649
            jamie "Heh... But in arm wrestling, technique is more important than muscle."
            scene v650
            z "Is it now?"
            scene v649
            jamie "Of course! I'll show you how I'll beat you with my technique."
            scene v650
            z "You do a lot of arm wrestling in your day?"
            scene v652
            jamie "..."
            scene v651
            jamie "Well, no. But I-"
            scene v653
            jamie "Oh, this is just a foolish trick to try to annoy me before we start, you sneaky bastard!"
            scene v650
            z "Not really..."
            scene v649
            jamie "Let's let our arms talk for us, shall we?"
            scene v650
            z "Sure."
            scene v656
            scene v655
            #Z wins in a second.
            scene v654
            jamie "Wait! No! I wasn't ready!"
            jamie "Someone should count down from three!"
            scene v657
            jnfr "I'll do it."
            jnfr "Three..."
            scene v651
            jnfr "Two..."
            scene v652
            jnfr "One..."
            scene v656
            jnfr "Go!"
            scene v655
            #Z wins in a second.
            scene v654
            jamie "Ah!"
            jamie "Wait! I thought it'd be three, two, one, zero!"
            scene v650
            z "Dude..."
            scene v658
            jnfr "Come on, Jamie... It's just a game..."
            scene v659
            jamie "No, no, dear. This guy is just using my unpreparedness."
            jamie "You know how sneaky those ninjas are."
            scene v650
            z "Jenny, can you count down from three to zero?"
            scene v658
            jnfr "Yeah, fine..."
            scene v650
            z "When we hear zero, we both start. Sounds good?"
            scene v653
            jamie "Heh... You should've taken the win you got while you could."
            jamie "Deal!"
            scene v650
            z "Let's go, Jenny."
            scene v658
            jnfr "Three..."
            scene v651
            jnfr "Two..."
            scene v652
            jnfr "One..."
            jnfr "Zero!"
            #Jamie manages to hold Z for a second.
            scene v656
            jamie "See?! It's working! Now I can turn this ar-"
            scene v655
            #Z totally destroys him.
            jamie "..."
            jamie "No... Wai-"
            scene v660
            z "Shhhhhhhh..."
            scene v661
            z "Excuse me, I have a kiss to claim."
            scene v662
            jamie "..."
            scene v663
            z "..."
            scene v664
            z "Ready?" #To jenny.
            scene v665
            jnfr "Y-Yeah..."
            scene v666
            z "(Jamie is kinda looking...)"
            z "(And so is Helena.)"
            z "(Guess I should...)"
            scene v667
            menu:
                "(...go all out with a strong kiss.)":
                    scene v668 #YOU FINISHED HERE 03/07/25
                    jnfr "Hmm..."
                    jnfr "Hmmmnnn~?"
                    jnfr "Ahhhnn~..."
                    jnfr "Hanhhh~..."
                    $ jnfr_lst += 1
                    $ jxj -= 3
                "(...give her a nice PG-13 kiss.)":
                    scene v668
                    jnfr "Hmm..."
                    jnfr "Nnm..."
            z "Okay... It's your turn, Jenny."
            jnfr "Right..."
            jnfr "If there's someone shorter than you on the opposing team, they drink. And for every member taller than you, you drink once."
            jnfr "Hmmm... So Helena is slightly shorter than I am..."
            jnfr "And you're way taller, [mc_name]..."
            z "So both you and Helena drink."
            jnfr "Damn... You haven't drunk a single time so far..."
            z "What can I say, I'm just good."
            jnfr "Hmmm..." #Sus.
            jnfr "Cheers."
            hlna "Cheers!"
            #They drink.
            #need helena with a card in her hand here - no scene for it
            hlna "The opposing team drinks."
            #scene of jenny looking annoyed
            jnfr "Damn..."
            #2 scenes - one of of jamie drinking and one of jenny drinking
            #They drink.
            #scene of jamie pulling a card
            jamie "The opposing team drinks twice, but you have to be blindfolded for the rest of the game."
            #scene of jamie looking confused
            jamie "Eh?"
            jamie "Wh-"
            jnfr "Do it Jamie. [mc_name] hasn't drunk the whole game. We'll totally end up losing unless he gets to drink."
            jamie "..."
            jamie "Okay, good point... Must be why he managed to beat me in arm wrestling."
            z "Ahuh..."
            jamie "Okay... I can't see anything." #Puts on a blindfold.
            z "Guess we have to drink, Helena."
            hlna "..."
            z "Okay, let's see."
            z "Slap a player from the opposing team on any part of the body you want."
            z "Oh, same card as the one we started with."
            jnfr "I guess some of them have replicas."
            z "Hmmm..."
            z "I'll slap..."
            menu:
                "Use the card to spank Jenny.":
                    z "Jenny."
                    jnfr "Hmmmm..."
                    jnfr "I wonder where you'll do it..."
                    z "Me too..."
                    jamie "..."
                    #Bends over and gives him her ass.
                    z "..."
                    hlna "..." #Surprised.
                    jnfr "Awwww~!!!"
                    jnfr "Ahh~..."
                    jamie "Jenny?! Are you okay?"
                    jnfr "Yeah... It..."
                    jnfr "It wasn't bad, don't worry..."
                    jamie "Hmmm..."
                "Use the card to slap Jamie.":
                    z "Jamie."
                    jamie "Ugh..."
                    jamie "Let's get it ov-"
                    #slaps him
                    jamie "Offghh!"
                    jamie "Awwww..."
                    jamie "Did you have to do it so hard..."
                    jnfr "It's just a game, Jamie... Man up."
                    jamie "Humpf..."
                "Drink.":
                    z "I'll just skip this one."
                    jnfr "Boooo..."
                    z "Yeah, yeah."
            #scene of jenny holding a card
            jnfr "Okay, my turn."
            #jenny reading the card
            jnfr "All players on the opposite team must take off their tops."
            hlna "Oh..."
            jnfr "You can drink instead if you're not comfortable with it..."
            hlna "Hmmm..."
            hlna "No I'm okay... I've had plenty to drink already. I don't want to lose too early."
            #Takes off her bra.
            jnfr "..."
            z "(Interesting...)"
            jnfr "I guess since [mc_name] isn't wearing a top, I guess I have to drink."
            hlna "Suck on on whichever body part of your partner's that you want. If you do so, the other team drinks."
            hlna "..."
            z "Eh... It-"
            #Approaches him.
            jnfr "..."
            #Kneels.
            z "Helena?"
            #Grabs his hand.
            #Sucks on his thumb seductively.
            hlna "..." #Gets up.
            hlna "{i}Clears her throat.{/i} Who's next?"
            jamie "Me..."
            jamie "Oh... How am I supposed to rea-"
            jnfr "I'll do it." #Takes it from him.
            jnfr "Your partner must take off their top."
            jnfr "Oh no, oh no... Whatever am I to do..."
            jamie "What are yo-"
            #Takes off her top.
            jnfr "I'm not losing."
            jamie "You could've just drunk..."
            jnfr "I could've, but then we would've lost in a few rounds."
            jamie "Hmmm... I guess it's just a game..."
            z "Eh? Wait, we can't see your..."
            jnfr "Hm? Did you say something, Mr.Pervert?"
            z "But..."
            z "..."
            z "Fine... My turn."
            z "Play 'fuck, marry and kill'. The one you kill drinks."
            z "Okay..."
            label y_r_u_g:
            menu:
                "Fuck Jenny and marry Helena.":
                    z "I'd fuck Jenny... Marry Helena... And kill Jamie."
                    jnfr "Oooh, how romantic..." #Sus.
                    z "I must admit I'm more into doing one than the other two."
                    jnfr "..."
                    $ jnfr_lst += 1
                    jamie "I'm guessing it's killing me?"
                    z "Heh... Sure..."
                "Fuck Helena and marry Jenny.":
                    z "I'd fuck Helena... Marry Jenny... And kill Jamie."
                    hlna "..."
                    jnfr "That was a romantic proposal..."
                    z "More romantic than the one you currently have, I imagine..."
                    jnfr "..."
                    jamie "Hey... I can be very romantic, you know..."
                    jnfr "Of course you can, dearest..."
                "More options." if y_r_u_g_counter == 0:
                    #Why are you geh meme.
                    $ y_r_u_g_counter = 1
                    jump y_r_u_g
            jnfr "Okay, let's see."
            jnfr "Give a lap dance to someone from the opposing team. They must drink after."
            jnfr "Easy."
            jamie "Wait, you're really going to do this?!"
            jnfr "Oh, don't worry, Jamie. [mc_name] is like a little brother to me."
            jamie "Hmmm..."

            #Gives Z a lap dance.
            #He gets an erection.
            $ jnfr_lst += 1
            hlna "..."
            jnfr "I can see I did well..."
            z "I guess so..."
            #Z drinks.
            hlna "Okay..."
            hlna "Pick two people you'd have a threesome with. Anyone not picked must drink."
            hlna "..."
            hlna "Well... I guess [mc_name]..."
            hlna "And Jenny..."
            jnfr "Ooooh... That sounds interesting..."
            jamie "Your loss..."
            #Drinks.
            scene v783
            jnfr "I'll get it for you, dear."
            jnfr "Take one drink for every player you've had sex with."
            scene v784
            jamie "Oh..."
            scene v785
            #Doesn't drink.			
            #IF THEY FUCKED, THEY BOTH DRINK.
            label they_fucked:
                jnfr "..." #Looks at Z.
                hlna "..."
                hlna "Wha..."
                jamie "Hm? What?"
                hlna "..."
                hlna "No, it's nothing..."
                #renders 794 through 797 need recreating - grey box at bottom of screen?
            #If they didn't fuck, no one drinks.			
            z "Okay, my turn."
            z "You and your partner each take a piece of clothing off each other. If you don't, you both drink."
            z "..." #Looks at helena.
            z "We can both drink if you prefer no-"
            hlna "No, no. Let's do it."
            z "..."
            z "I'm not saying no to that."
            #Hlna takes off Z's pants and admires his dick for a bit.
            jnfr "See something you like, Helena?"
            hlna "?!"
            hlna "That's not..."
            hlna "..."
            hlna "Who's next..."
            jnfr "That'd be me..." #Stands up to grab a card
            jnfr "Oh..." #Falls on Z. Her boobs are in his face.
            jnfr "Sorry... I think I'm a bit tipsy..."
            z "We can st-"
            jnfr "Na-uh. I'm fine. We can continue. I'm not gonna lose."
            z "Sure..."
            jnfr "Kiss any member of the opposing team. If you do, they must drink."
            jamie "..."
            jnfr "Well..."
            #Goes to Z.
            jnfr "By the way, Jamie. I'm only doing this so we can win."
            jnfr "[mc_name] is literally like a little bro-"
            jnfr "Hmmmn~..." #Z starts kissing her.
            jnfr "Hmmmnnnn~... Uhmmnn~..." #They make out.
            jnfr "Hmnn~..." #They break the kiss.
            $ jnfr_lst += 1
            jnfr "..."
            jnfr "Now, drink."
            z "Yeah, yeah."
            #Drinks.
            menu:
                "Tell Jenny she can also do the same to Helena.":
                    z "Wait."
                    z "You want to win, right?"
                    jnfr "Of course!"
                    z "The card didn't say you can only do this to one member of the other team, did it?"
                    jnfr "..."
                    #Checks the card.
                    jnfr "I guess not..."
                    jnfr "..." #looks at Helena.
                    hlna "..."
                    #Goes to her.
                    jnfr "I've..."
                    jnfr "I've never... You know... With a girl..."
                    hlna "I haven't either..."
                    jnfr "..."
                    jnfr "Hmnn~..." #Kisses her a bit.
                    jnfr "Ahhnmm~..." #Makes out with helena.
                    jnfr "Mnnn~..."
                    jnfr "..."
                    jnfr "Fuck... That's totally different..."
                    jnfr "Girls are much softer, aren't they..."
                    hlna "Y-Yeah..."
                    jnfr "Okay, now drink."
                    #Hlna drinks.					
                "Don't remind her.":
                    z "..."
            hlna "Okay..."
            hlna "All players on the opposite team must take off their tops."
            hlna "Again, huh..."
            jnfr "Well... I guess I had it coming..."
            #Takes off her towel.
            z "(Nice...)"
            jnfr "..." #Catches him looking and smiles at him.
            jnfr "Jamie is topless, so you drink, Helena."
            #She drinks.
            jnfr "Okay, here's your card, Jamie."
            jnfr "..."
            jnfr "Oh..."
            jamie "What?"
            jnfr "Joker card: Your partner must give oral sex to a member of the opposing team and that person drinks thrice. If you refuse, you drink five times."
            jamie "What?!"
            jnfr "..."
            jnfr "Well..."
            jnfr "Yeah... I forgot to mention the cards tend to get spicier the deeper you go into the draw."
            jamie "But..."
            jamie "Fuck... I've already drunk quite a bit... I'm dizzy... I don't think I can take much more drinking..."
            jamie "..."
            jamie "Do it."
            jnfr "..."
            #Smiles seductively.
            jnfr "But, are you sur-"
            jamie "Yeah... It's just a game after all, right?"
            jnfr "Of course."
            z "(Damn... Is this really about to happen...)"
            z "(Is it because he's quite drunk that he agreed to this?)"
            jnfr "Oh... Darling, don't worry... This doesn't mean anything..."
            jamie "Yeah..."
            jnfr "..."
            jnfr "Wanna move to the edge?"
            z "Sure."
            jnfr "..." #kneels next to his dick.
            hlna "..."
            jnfr "Muaahhh~..." #Kisses it.
            jnfr "Hmmmnn~..."
            jnfr "Ghhhnnnmm~..." #Starts sucking.
            jamie "Can you be a bit more quiet about it?"
            jnfr "Hmmggkkknnn~..."
            jnfr "Can't help it... It's quite hard to take it in my mouth..."
            jamie "Ehhh..."
            jnfr "Ghhhmmmnnn~..."
            jnfr "Gahhhhmmmnnnn~... Mnnhhh~..."
            z "Ohhhh..."
            jamie "..."
            jamie "How long do you have to do this..."
            jnfr "Hmmn~..."
            z "Ehhh... I don't think she can talk right now..."
            z "But to answer your question... I think until I finish?"
            jamie "Ughh..."
            jnfr "Hmnnn~... Uhhhmmnn~..."
            z "Oh shit... Not that fast, Jenny... I'm..."
            z "Ohhh fuck..."
            #Cums.
            jnfr "Ughhhmmm~!!!"
            jnfr "Ahhhhnnn~..."
            $ jnfr_lst += 2
            jamie "..."
            jamie "Is it over?"
            z "Yeah..."
            jamie "Ugh..."
            z "Okay, my turn."
            z "You decide. You can make two members of each team kiss or drink."
            jnfr "Wait, I'm gonna go clean this mess up."
            z "..."
            menu:
                "Stop Jenny and make her kiss Jamie like this.":
                    z "Wait."
                    jnfr "Hm?"
                    z "Kiss Jamie."
                    jnfr "Hu-"
                    z "Like this." #Whispers.
                    jnfr "..."
                    jnfr "......"
                    jnfr "........."
                    jnfr "Heh..."
                    jnfr "Dear..." #Goes to Jamie.
                    jamie "?"
                    jnfr "Muuuahhh!" (multiple=2) #Kisses him
                    jamie "Hmmm?!" (multiple=2)
                    jnfr "Hehehehehe..."
                "Let her clean up and make them drink after.":
                    z "Okay, you two should drink after you're done."
                    jnfr "Yeah."
            z "(What about our team...)"
            menu:
                "Kiss Helena.":
                    z "Say..."
                    z "Let's just kiss?"
                    hlna "..."
                    hlna "Y-Yeah..."
                    hlna "..."
                    z "Here I come..."
                    hlna "..."
                    hlna "Hmmmn~..."
                    hlna "Mmmm~..."
                    hlna "Hahhnn~..."
                    z "Are you okay?"
                    hlna "Yeah..."
                    hlna "I just feel hot after doing that..."
                    hlna "This game is making me feel young again, heh..."
                "You both drink.":
                    z "Let's just both drink, Helena."
                    hlna "..."
                    hlna "Sure..."
                    #Both drink.
            jnfr "Okay..."
            jnfr "Joker card-"
            jamie "Oh, shit! Not again..."
            jamie "This game was a bad idea, after all..." #Takes off blindfold.
            jnfr "Stop acting like a child, Jamie... It's just a game..."
            jamie "I don't want to watch my wife being fucked, thank you very much."
            jnfr "I'm not even your wife, yet! And it's not like there's even any cards for that!"
            jnfr "Look... This says..."
            jnfr "Joker card: pick a member of your team and a member of the opposing team to carry you. The one who can carry you the longest gets to have sex with you while the other has to watch."
            jnfr "..."
            jamie "..."
            jnfr "If you don't, then you and your partner drink 10 times."
            jamie "Come the fuck on!"
            jnfr "Oh..."
            jnfr "I guess I was wrong..."
            jnfr "I mean, we can drink ten times... We'll lose, but there's no way you can carry me longer than [mc_name]..."
            jamie "..."
            jamie "You know fucking what..."
            jamie "Do you really think I can't carry you more than that blond elf?"
            z "Not an elf... And you're also blond..."
            jamie "No, no. This is fucking personal now. You get to kiss my wife and even get your dick sucked by her. I won't let this stand."
            jamie "Jenny. Come over here. I'm gonna show you I can carry you way longer than that twat!"
            jamie "Sure he's a bit more jacked than me, so what?!"
            jamie "Let's do this!"
            z "Are you sure y-"
            jamie "Very."
            jnfr "..."
            jnfr "Okay... Let's do it..." #Smiles.
            jnfr "Try your best, dear."
            jamie "I will."
            jamie "Helena. You count."
            hlna "Sure."
            #Carries her.
            hlna "One..."
            hlna "Two..."
            hlna "Three..."
            hlna "Four..."
            hlna "Five..."
            hlna "Six..."
            hlna "Seven..."
            hlna "Eight..."
            hlna "Nine..."
            hlna "Ten..."
            hlna "Eleven..."
            hlna "Twel-"
            #They fall.
            jamie "Ughh!" (multiple=2)
            jnfr "Eeep!" (multiple=2)
            jamie "Twelve, huh..."
            hlna "Actually, it wasn't twe-"
            z "Nah. Let him have the twelve."
            z "Jenny."
            jnfr "Yeah."
            #Carries her.
            hlna "One..."
            hlna "Two..."
            hlna "Three..."
            hlna "Four..."
            hlna "Five..."
            hlna "Six..."
            hlna "Seven..."
            hlna "Eight..."
            hlna "Nine..."
            hlna "Ten..."
            hlna "Eleven..."
            hlna "Twelve..."
            hlna "Thirteen..."
            z "Okay, let's put you-"
            jnfr "Heyyyy... Come on, you can do better than that."
            z "..."
            hlna "Sixteen..."
            z "Do you want me to totally destroy him or something?"
            jnfr "He's always this cocky guy who thinks he's better than everyone, so yeah. I'd like to see that."
            jnfr "At least every once in a while."
            z "..."
            z "You do realise that I'm literally about to fuck you right in front of him, right?"
            z "Isn't that a good enough lesson in humility?"
            jnfr "Maybe it won-" (multiple=2)
            hlna "Thirty three..." (multiple=2)
            jamie "Okay, okay... I lost..."
            jnfr "..."
            jnfr "You actually admit you lost?"
            jamie "Yeah, so what?"
            jnfr "..."
            jamie "Please... Let's stop the game now..."
            jnfr "..."
            jnfr "What happened with your business?"
            jamie "What?"
            jnfr "Why did you suddenly get scared that the people you deal with will come after you?"
            jnfr "Tell me that at least."
            jamie "..."
            jamie "Let me sleep on it..."
            jamie "I promise I'll tell you everything when I'm ready..."
            jnfr "..."
            jnfr "Fine."
            jnfr "I think Jamie and I had enough to drink anyway."
            jnfr "Let's call it a day?"
            z "Ehhh..."
            jnfr "I'll make it up to you, I promise..." #Smol font.
            z "I'll take you up on that, okay?"
            jnfr "Yep."
            #They leave.
            hlna "Gods... Were you two really going to..."
            hlna "You know..."
            z "We-"
            hlna "No, no. I don't want to know..."
            hlna "Well, I should probably sleep early tonight anyhow."
            hlna "You're traveling tomorrow, so you should do the same."
            #Wants to get up but falls on Z.
            z "Are you okay?"
            hlna "..."
            z "I'd say sober up a bit first, maybe?"
            hlna "Ehh... But-"
            z "How about I help you loosen up your muscles?"
            hlna "Loosen them up, you say?"
            z "Yeah. Seira and I do it to each other all the time."
            z "I mean, we used to... It's been a while actually..."
            hlna "How do you mean loosen them up?"
            z "Okay, I'll show you."
            #Messages her shoulders.
            hlna "Ehhh... You're a bit ro-"
            hlna "..."
            hlna "Ooooohhh~..."
            hlna "That feels..."
            hlna "Greaaat..."
            z "See? I told you."
            #z starts messaging further and further down
            hlna "Hmmmnnn..."
            #z grabs helena's tits
            hlna "Haaa~"
            #helena sobers up
            hlna "Wait, [mc_name]!"
            z "Helena? What's wrong?"
            hlna "I think we should stop this. I mean, you're not even half my age!"
            z "Does that matter? If you're enjoying it, you're enjoying it."
            hlna "It matters to me..."
            #helena gets out of the bath and gets dressed
            hlna "Goodnight, [mc_name]. This was surprisingly enjoyable."
            z "(What was that about?)"
            #skip to helena in her room - white orb
            "Helena."
            "You must remember your promise."
            "Do not let them sway you."
            #fade to nari scene
        "Drop the subject.":
            scene v578
            z "Well. I should get going anyway."
            z "I'll leave you guys to your tour."
            scene v579
            $ dummy += 2
            jnfr "Good night."
            z "Night..."
            
    #) Nari dreams about his sister giving him his necklace and a big wave:
    #woman that looks like nari says below
    Character("???") "Take this, I'll see you soon."
    #younger nari
    nari "Thanks sis. Safe travels."
    #fades out to next scene
    #He remembers someone saying Nari
    "Nari..." #just on a white screen
    #Auge appears and tells him that's not really his name.
    auge "Strange. Remembering something that isn't truly yours..."
    auge "Especially something as important as a name."
    #He asks Auge who she is and asks if she's the one giving him dreams.
    nari "Who are you? Are you the one making me see these things?"
    #She says she's there to help him remember.
    auge "I'm here to help you remember."
    nari "Remember what?"
    #Auge says "Remember..." and shows him a ship.
    auge "Remember... Zephyr..."
    #I'm here R <-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
    #fades to next scene



#10) Axius and the team that attacked Stephanie's team:
    scene v479 with Pause(1)
    scene v480 with Pause(1)
    scene v481 with Pause(1)
    scene v482 with Pause(1)
    scene v483 with Pause(1)
    scene v485 with Pause(1)
    axs "..."
    scene v486 with dissolve
    axs "Are they dead?"
    scene v488 with dissolve
    nari "..."
    scene v487 with dissolve
    axs "Are they?"
    scene v489 with dissolve
    nari "No."
    scene v488 with dissolve
    axs "..."
    scene v490 with dissolve
    axs "You had very simple instructions, Nari."
    axs "Get me the town's alchemist."
    axs "And kill anyone who interferes."
    nari "..."
    scene v491 with dissolve
    nari "I did bring you the alchemist."
    scene v492 with dissolve
    axs "Yes. But you didn't kill a single ninja."
    axs "Were they stronger than you and your team?"
    nari "..."
    axs "Grown weak, have you? Four kunoichi can beat your team now?"
    scene v493 with dissolve
    nari "..."
    scene v495 with dissolve
    axs "Perhaps next time Alura should lead the missions?"
    scene v494 with dissolve
    nari "No."
    nari "Alura works for me, not you Axius."
    scene v496 with dissolve
    axs "Most of the work she does for you seems to be in the bedroom these days."
    scene v497 with dissolve
    nari "How dare you..."
    nari "Say that again."
    scene v496 with dissolve
    axs "..."
    alura "..." #Scared.
    scene v497 with dissolve
    nari "Go on."
    scene v498 with dissolve
    irna "..."
    scene v499 with dissolve
    scene v500 with dissolve
    axs "You're dismissed."
    scene v501 with dissolve
    axs "All of you."
    scene v502 with Pause(1)
    scene v503 with Pause(1)
    scene v504 with Pause(1)
    axs "Nari..."
    axs "Do not fail me again."
    axs "Or it'll be the last time you do."
    scene v505 with Pause(1)
    scene v506 with Pause(1)
    scene v507 with Pause(1)
    scene v508 with Pause(1)
    scene v509 with dissolve
    #They leave.
    #Irna is walking back to her room (ALONE!)
    #Opens the door and wants to change.
    irna "*{i}Sighs.{/i}"
    scene v510 with Pause(1)
    scene v511 with Pause(1)
    nari "Why did you stop me?"
    scene v512 with dissolve
    irna "EEEP?!"
    scene v513 with dissolve
    irna "..."
    scene v514 with dissolve
    irna "What are you doing here, Nari?"
    scene v515 with dissolve
    nari "..."
    nari "Irena."
    nari "Why did you stop me from killing the girl?"
    nari "What is that you know?"
    scene v517 with dissolve
    irna "..."
    scene v516 with dissolve
    irna "I..."
    scene v517 with Pause(1)
    scene v516 with dissolve
    irna "It's just..."
    scene v517 with Pause(1)
    scene v516 with dissolve
    irna "It's how incubi are, Nari."
    scene v518 with dissolve
    irna "My father isn't special in this regard, really."
    scene v519 with dissolve
    nari "..."
    scene v521 with dissolve
    nari "Expl-"
    scene v520 with dissolve
    irna "Go and ask Nixie about it."
    irna "She's the same as that girl."
    irna "There's others too, I'm sure..."
    irna "The only difference Nixie was from the rest of them is that her mother was a succubus and thus my father found her useful."
    scene v521 with dissolve
    nari "..."
    scene v522 with dissolve
    nari "You mean..."
    nari "How many bast-"
    scene v523 with dissolve
    irna "Probably dozens of them out there."
    nari "..."
    scene v521 with dissolve
    nari "How could you tell that girl was one of them?"
    scene v520 with dissolve
    irna "I can always tell..."
    irna "Can't say I like the fact that I do. But I can tell."
    scene v523 with dissolve
    nari "..."
    irna "You..."
    nari "Hm?"
    scene v520 with dissolve
    irna "You could've just ignored me and killed them all."
    irna "Why didn't you?"
    scene v521 with dissolve
    nari "..."
    nari "Do you think it's right?"
    nari "What we're doing..."
    scene v524 with dissolve
    irna "..."
    nari "..."
    scene v525 with dissolve
    nari "Good night, my lady." #Leaves.
    scene v526 with dissolve
    irna "Nari."
    scene v527 with dissolve
    nari "?"
    scene v526 with dissolve
    irna "Do you..."
    scene v527 with Pause(1)
    scene v526 with dissolve
    irna "Do you remember anything now?"
    irna "From your past?"
    scene v527 with dissolve
    nari "..."
    nari "A bit..."
    nari "Sometimes... In my dreams... I can see little shards of it..."
    nari "I've been dreaming quite often lately..."
    nari "..."
    nari "Irena..."
    nari "Does your father have sleep nymphs under his command?"
    scene v528 with dissolve
    irna "Sleep nymphs?"
    irna "Not that I know of..."
    scene v529 with dissolve
    nari "I see..."
    #Leaves.
    scene v530 with dissolve
    irna "..."
    irna "(If Nari turns on my father...)"
    irna "(And with [mc_name]'s help...)"
    scene v531 with dissolve
    irna "(Maybe...)"
    irna "(Just maybe...)"

#11) Arrival at elven city:
    #Tourny is already beginning when they arrive.
    #It is a jousting competition at first.
    scene v532 with pause(1.0)
    scene v533 with dissolve
    z "..."
    scene v534 with dissolve
    z "This is interesting..."
    z "What are they doing with those sticks?"
    scene v535 with dissolve
    cnt "It's jousting."
    z "Hm?"
    cnt "The two people on horseback will try to knock their opponent off using the lance."
    cnt "Whoever falls loses."
    z "..."
    z "I see."
    cnt "Oh! It's Ser Klyn!"
    z "Hm?"
    z "The guy on the white horse?"
    cnt "That's him, yeah."
    cnt "He's never lost a single tourney."
    cnt "He's the commander of the royal guards."
    cnt "Or well, he was when I was last here."
    z "I see..."
    z "And the guy in the full armour?"
    cnt "..."
    cnt "I actually don't know him... I don't think..."
    ymi "He's rather small, isn't he?"
    z "Yeah..."
    Character("Announcer") "And for the final round of our jousting tournament..."
    Character("Announcer") "We have..."
    Character("Announcer") "Ser Klyn!"
    Character("Announcer") "Versus!"
    Character("Announcer") "Ser Vollstahl!"
    Character("Announcer") "May the stronger fighter win!"
    #They begin.
    #Vollstahl wins it.
    cnt "Eh?!"
    z "..."
    z "That was surprising..."
    ymi "I thought Klyn had never lost before."
    z "You know what they say, first time for everything."
    cnt "I guess..."
    illya "Centoryyyy!"
    cnt "Illya?!"
    #The princess hugs centoria similar to how torr's family hugged her.
    vollstahl "My lady... That'sh no way for a prinshesh to behave."
    illya "*Pouting* Grr..."
    illya "At least let me greet my friends."
    cnt "Illya your hair! What happened?"
    illya "Ah, of course, we are supposed to be clones after all."
    illya "Let's just say I fancied a change. Lot's of things to talk about after all."
    illya "Ahem."
    illya "You must be [mc_name], right?"
    z "Yes. And you must be Princess Illya."
    illya "I am. Nice to finally meet you, [mc_name]."
    z "Nice to meet you too, Princess."
    illya "No need to Princess me every five minutes. Illya will do."
    z "Gotcha."
    illya "Hi, there. I'm Illya." #Goes to yumi.
    ymi "Hi, Prin-"
    illya "Ah-uh. Illya."
    ymi "..."
    ymi "Hey, Illya. My name's Yumi."
    illya "Nice to meet you."
    illya "Ooooh, you guys look really scary with all of those weapons and armour and stuff."
    illya "Oh, speaking of lots of armour..."
    illya "This is Vollstahl. The commander of the royal guard."
    cnt "Oh? I thought it was Ser Klyn?"
    klyn "Not since this guy showed up a few months back."
    klyn "I have yet to best him once."
    vollstahl "Sher Klyn ish too humble. I'm shure he beshted me onshe or twishe at least while shparring."
    cnt "Nice to meet you, ser."
    vollstahl "You two, young Shentoria. The prinshesh told ush lotsh about you."
    vollstahl "Shall we ischcort your gueshtsh to the cashtle, my lady?"
    illya "Yeah. My dad must be waiting."
    #They go to the castle.

#12) Elven castle:
    #The castle is majestic.
    ymi "Gods... Look at that..."
    cnt "Yeah... The castle has always been a marvel."
    z "Damn..."
    #Z notices goblins working and cleaning around the castle.
    z "Aren't those..."
    cnt "Hm?"
    z "They're goblins, aren't they?"
    cnt "Yeah?"
    z "I thought the elves and the goblins were trying to kill each other?"
    illya "Not all of them."
    illya "That's exactly why I need you guys."
    illya "Many goblins work here in our city. They are even granted residence in our city. I made sure of that."
    z "These goblins live in the city with the elves?"
    illya "Gabro and Lishten? They live with us in the castle."
    z "..."
    z "I don't want to sound like an asshole, but are they able to fit in?"
    illya "Aside from having difficulty learning our language, they fit in just fine."
    illya "I've been teaching the ones who work in the castle the common tongue myself."
    vollstahl "You are shometimesh too ricklesh, my lady."
    illya "Nonsense. Don't listen to Vollstahl."
    illya "Goblins are a bit different than us, sure. But they aren't mindless monsters, [mc_name]."
    illya "I'd imagine you wouldn't want people to assume the same about you just because you're an incubus, correct?"
    z "No... I mean, yes..."
    z "I just thought..."
    z "..."
    illya "..." #Smiling.
    z "Princess..."
    z "What did you mean when you said that's why you needed us?"
    illya "..."
    illya "I..."
    #Intercepted by Vollstahl telling them they're about to meet the crowned prince.
    vollstahl "I'm shorry prinshesh, but your father ish waiting."
    illya "Thank you Vollstahl. Apologies Centoria, [mc_name]. My father does not like to be kept waiting."
    #The royal guard whom Z works with are all bald dark skinned topless women with nipple piercings.
    crpr "My beautiful daughter, I'm so glad you could make it."
    #illya and z bowing to father
    illya "Father, thank you for seeing us today."
    #Z asks why the guards have no weapons, the prince makes them demonstrate their powerful af magic saying that elves are specialists in magic.
    z "Your Highness, how come your guards have no weapons?"
    crpr "Oh? I'm sorry, I didn't explain, my guards are all proficient in magic, physical weapons are useless to them."
    crpr "See that dummy over there?"
    z "Yes?"
    crpr "Guards."
    #illya steps back and casts magic
    z "Illya?"
    z "What are you doing?"
    #anim showing off the magic
    z "What the..."
    z "Wow... That's pretty cool."
    #The prince brags about how he provided well paying jobs for the goblins and helped civilise them. Gives some credits to illya.
    crpr "I'm very proud of our attempts to integrate our societies. Myself and my daughter have been working for this to benefit both the elves and the goblins."
    #The prince says he'll also lend them a dozen of his personal guard when they leave to the nearby villages and says he doesn't understand why his daughter wants to visit these peasants.
    crpr "My daughter insists on visiting the nearby villages, I have no idea why. However, I trust her judgement. I will lend you a dozen of my personal guard to accompany you."
    illya "Thank you, Father."
    #Z (with centoria) gets a mission to protect the princess of Centoria's village of some sort. Her father specifies that he's not to be further than 1 meter away outside of the city and can be instructed to be up to 20
    crpr "[mc_name], as my daughter's birthweek celebrations, she will be visiting the outskirts of the city. I want you to protect her."
    z "Of course, Your Highness."
    crpr "As of tomorrow morning, you are not to be further than 1 meter away from her outside of the city."
    z "And inside the city?"
    crpr "Inside the city, you may be up to 20 metres from her."
    z "Yes, Your Highness."
    #A magic bond is formed by a sorceress working in the castle.
    crpr "I have asked the sorceress to create a bond between you two. She will be able to communicate with you through this bond."
    illya "Father that is not necessary."
    crpr "Unfortunately daughter, this is non-negotiable."
    z "It's fine Princess, it can't hurt."
    crpr "Excellent, I'm glad you understand."
    #Sorceress enters
    scrs "Your highness."
    crpr "Sorceress, please create the bond."
    #The sorceress creates the bond.
    scrs "Could you two hold out your hands, please?"
    #mc looks at illya's face
    z "(...)"
    z "(She's so...)"
    z "(She's beautiful...)"
    #illya shy and looking at mc
    scrs "It is done."
    scrs "Uhhhh..."
    scrs "Are you two planning on staring at each other much longer?"
    z "..." (multiple=2)
    illya "..." (multiple=2)
    scrs "Alright, now look at your hands."
    scrs "The symbol you see before you is one of two people being bonded."
    scrs "It is done, Crown Prince "
    crpr "Thank you, sorceress. You may take your leave."
    #The sorceress leaves.
    #centoria and yumi return to the castle
    cnt "Greetings, Your Majesty."
    cnt "Is everything OK?"
    crpr "The bonding process was successful."
    crpr "Now, [mc_name], the goblins recently attacked the elf city. You must keep my daughter safe."
    cnt "No harm will come to her Your Highness. You have our word"
    crpr "Thank you Centoria. I shall see you when you return."
    #The sorceress who works for the prince is a hooded figure who never shows any part of her skin (She's a goblin!)
    #The prince tells them that local goblins recently attacked the elf city a few times and the princess insists on visiting the outskirts of the city as a part of her birthweek celebrations like she always does. A body guard is needed for the princess.
    #z, illya and centoria leave - sorceress waiting outside for them
    scrs "Your plan will not succeed Princess."
    illya "Sorceress? What do you mean?"
    #The sorceress turns illya, centoria and yumi into snowmen.
    #finger snap sound
    scrs "[mc_name], elves and goblins can never be integrated. You must make a choice."
    z "What? Why would the Crown Prince's sorceress say that?"
    scrs "It will be obvious soon, Incubus. But that is not for me to reveal."
    z "..."
    z "And why are you only telling me this?"
    scrs "Because they will only interfere with the plan."
    z "What plan?"
    scrs "I shall see you soon, Incubus."
    scrs "Sleep well, child."
    z "..."
    z "You too?"
    #sorceress leaves - turns illya back
    illya "Sorceress?"
    illya "What in the worlds did she mean?"
    z "I have no idea, Illya."
    illya "[mc_name], Centoria, we should prepare. Yumi, we shall see you in the morning for the tournaments."
    #blackscreen - explain something?
    z "Goodnight Yumi, sleep well."
    illya "Goodnight Yumi. Rest well."
    cnt "Goodnight Yumi. Sleep well."

#13) Fencing tournament:
    z "So this is the fencing tournament? Impressive."
    cnt "Yeah, it's a big deal here."
    #illya appears next to them
    illya "Indeed it is. We have been hosting these tournaments annually for centuries."
    z "Tournaments?"
    illya "Yes, we host a fencing tournament, a magic tournament and a goblin tournament."
    z "A goblin tournament? How does that work?"
    illya "The goblin tournament is only open for goblins. No humans or elves may participate."
    z "I see."
    z "This is impressive."
    cnt "Yeah, the  a big deal here."
    illya "I'm glad you think so. Yumi, [mc_name], would you do me the honour of participating?"
    z "I'm not against it. How about you Yumi?"
    ymi "I'm in."
    illya "Excellent, I shall get you both signed up"
    crpr "WELCOME EVERYONE! TO THE 437TH ANNUAL FENCING TOURNAMENT!"
    crpr "OUR FIRST MATCH IS-!"
    #skips to semi-finals - yumi vs vollstahl
    crpr "THE SECOND SEMI-FINALS IS HERE. OUR REIGNING CHAMPION, SER VOLLSHTAHL! VERSUS. OUR NEWCOMER, YUMI!"
    illya "Unfortunately, Yumi does not stand a chance here [mc_name]."
    z "I wouldn't be so sure, Illya. Yumi can be quite slippery when she wants to be."
    illya "We shall see."
    #vollstahl and yumi fight - yumi gets destroyed
    crpr "AND THE WINNER IS SER VOLLSHTAHL!"
    illya "See, [mc_name]. I told you."
    z "Yeah, you were right. He's quite the fighter."
    illya "Indeed he is."
    #In the fencing tourney (no magic is allowed) Z is asked to compete by the princess.
    crpr "AND OUR FINAL MATCH IS HERE! OUR REIGNING CHAMPION, SER VOLLSHTAHL! VERSUS. POTENTIALLY HIS BIGGEST THREAT SO FAR, [mc_name]!"
    #vollstahl - still in his full armour and z fight - it's close but z loses
    crpr "LADIES AND GENTLE-ELVES! AFTER AN EXTREMELY CLOSE MATCHUP. YOUR CHAMPION, FOR THE 437TH ANNUAL FENCING TOURNAMENT IS SER VOLLSHTAHL!"
    vollstahl "Well fought [mc_name]. You are a worthy opponent."
    z "Thank you, Ser Vollstahl. You are just as impressive as the Princess said."
    #Vollstahl, the king's personal guard, wins against Z. Vollstahl is a short man, who always wears a full armour and a helmet covering all of his body. (He's actually a goblin who betrays the elves later on and joins axius).
    #Z is asked to compete by the princess. He loses to Vollstahl in the finals.
    crpr "AT OUR CLOSING CEREMONY, OUR CHAMPIONS AND RUNNER UPS WILL BE PRESENTED WITH THEIR PRIZES!"
    #z goes back to illya and centoria
    illya "You did well, [mc_name]."
    z "Not well enough. How is Yumi?"
    cnt "She's a bit banged up, but nothing serious."
    z "I'm glad. Vollstahl is extremely strong."
    illya "Yes, he is. However, the next tournament is soon, we should make a move."
    z "As you wish Illya."

#14) Magic tournament: - in the evening
    z "So this is the magic tournament?"
    illya "Yes. Here, teams shall fight until one team is no longer able to continue."
    z "So I assume that makes us a team?"
    illya "As you can't leave my side, that would be the case."
    z "In that case Princess, we should be fine with this one."
    illya "Confident?"
    z "Very. You may be Elves and strong with magic, but I am an Incubus. Magic is my forte."
    illya "Well, I shall be expecting great things from our team."
    #we watch the first matchup between elves
    crpr "AND THE WINNERS OF THE FIRST MATCH ARE THE ELVES FROM ESANKADI!"
    z "Esankadi?"
    illya "A small village in the East. They have some wonderful scenery, as you will see when we visit."
    #skip to our first match
    crpr "AND THE NEXT MATCH IS HERE! OUR NEWCOMER, [mc_name] AND THE PRINCESS ILLYA! VERSUS! THE ELVES FROM NASAKADI!"
    z "From where?"
    illya "The North. Unimportant, pay attention to their fighting style."
    z "Got it."
    #fight starts - fairly even
    #z takes a hit from an unknown magic
    illya "WATCH YOUR LEFT!"
    illya "You OK, [mc_name]? I am hoping one hit does not take you out."
    z "Fine Princess, that wasn't nearly enough to finish me off."
    illya "Wonderful. You focus on the man and leave the girl to me."
    z "As you say Princess."
    #z and illya fighting
    z "Too slow!"
    z "(How is Illya?)"
    #z looks over to see illya winning the fight against the girl
    z "(Absolutely fine... maybe I worry too much.)"
    #they fight - z and illya win
    illya "I recommend not getting up again. It is over."
    crpr "AND THE WINNERS OF THE SECOND MATCH ARE PRINCESS ILLYA AND [mc_name]! MY HOW INTERESTING THIS IS TURNING OUT TO BE!"
    z "See Princess. I told you, nothing to sweat about."
    illya "You are indeed quite strong. But do not get overconfident."
    z "..."
    illya "Did I not also tell you to call me Illya. Drop this Princess nonsense."
    z "Apologies Illya, thought it might seem inappropriate if your bodyguard called you by your first name."
    illya "I see... In that case, do not fret. We are friends first, bodyguard and Princess second."
    z "Understood."
    illya "And if anyone complains. I shall have them exiled."
    z "Exiled? Surely you can't do tha-"
    illya "I was joking, [mc_name]."
    z "Of course you were."
    illya "Shall we continue watching some more fights?"
    z "Absolutely."
    #skip to the final.
    crpr "AND THE FINAL MATCH IS HERE! THE ELVES FROM ESANKADI! VERSUS! PRINCESS ILLYA AND [mc_name!u]!"
    #shot on the elves from Esankadi
    #shot on Illya and Z
    crpr "MAY THE STRONGEST TEAM WIN!"
    #fight starts - elves shitting on illya and z
    #elves from eskandi so fast z and illya can't react - z casts shield that illya did previously
    z "Illya!"
    #illya and z both get hit and go down - z bleeding
    Character("Female Elf from Eskandi") "Where are you looking?"
    Character("Female Elf from Eskandi") "I'm up here!"
    z "ILLYA!"
    z "ILLYA! ARE YOU ALRIGHT?"
    crpr "IS IT OVER? [mc_name!u] AND THE PRINCESS ARE DOWN. SEEMINGLY FOR THE COUNT."
    illya "DON'T FOCUS ON ME [mc_name!u]. THEY ARE GOING TO WIN."
    Character("Male Elf from Eskandi") "She's right. We are going to win!"
    z "DON'T WORRY ILLYA. I'VE GOT THIS!"
    #z uses the same unknown magic from the first match - takes out one then teleports to the other and fus roh dah's the other
    Character("Female Elf from Eskandi") "What?"
    Character("Female Elf from Eskandi") "What's going on?"
    Character("Female Elf from Eskandi") "Why can he still move?"
    Character("Female Elf from Eskandi") "What..."
    z "NEVER HURT ILLYA!"
    crpr "OH MY! WHAT A TURNAROUND!"
    crpr "AFTER THAT INCREDIBLE MATCH, THE WINNERS ARE PRINCESS ILLYA AND [mc_name!u]!"
    z "(ILLYA!)"
    z "ILLYA!"
    z "Illya... Please tell me you're..."
    illya "I'm okay."
    illya "Slightly injured, but nothing serious."
    illya "The healers will have me restored in no time."
    illya "However my brave bodyguard will have to carry me there."
    illya "Hey, you're hurt. You're bleeding."
    z "Don't worry Princess, I still have plenty of strength."
    illya "Well then... I have to admit..."
    illya "THAT WAS AMAZING [mc_name!u]!"
    z "I did tell you to trust me Illya."
    illya "My apologies. I never should have doubted you."
    z "No need to apologise. We won, that's all that matters."
    illya "Indeed. However. How did you do that? Have you ever used that magic before?"
    z "No. I'm just a quick learner."
    illya "I see. I'm glad you are helping me then."
    crpr "WELL, I SHALL SEE THE VICTORS AT THE CLOSING CEREMONY."
    illya "Well, [mc_name]. As this is the last tournament of the day, we should go and get some cleaned up and get some rest."
    z "As you wish Illya, let's get Centoria then head back."
    #illya kisses z cheek

#15) Taking a bath with Illya and Centoria:
    z "Well. Illya, Centoria, I'll be waiting in the castle."
    illya "Oh no, you have had the sorceress's bond placed on you. You are not allowed to leave our side."
    z "But you are bathing? Men aren't allowed to be in the same bath as the Princess."
    #illya looks at centoria curiously
    illya "Oh? And I wonder how you found out about that rule?"
    #centoria blushing
    cnt "I... Uh..."
    #illya giggles
    illya "[mc_name]. You are my bodyguard. The rules do not apply completely the same to you as they do to the public."
    illya "And it seems Centoria is not against the idea."
    #centoria blushing again
    z "I see. I shall be waiting in the bath then."
    #z waiting in the bath - illya and centoria come in with towels wrapped around them
    z "You two are taking a bath with towels on?"
    illya "Yes. We are not allowed to be seen naked by anyone, remember?"
    z "I thought the rules didn't apply to me?"
    cnt "Illy, stop messing with him. Please."
    #illya giggles again
    illya "I'm sorry Centy, I couldn't resist. He's just so easy to tease."
    z "Well, I'm glad I can bring you some amusement."
    illya "We shall find out how much amusement you can bring me."
    #illya and centoria drop their towels
    z "Wow."
    illya "I could have you executed right now."
    z "I think I'd die happy if you killed me right now."
    #centoria rolls her eyes
    illya "You are a strange one, [mc_name]."
    z "Would you be surprised if I told you that you aren't the first to tell me that?"
    #illya rolls her eyes
    #illya and centoria get into the bath - slowly crawl towards z
    illya "So? [mc_name]? Fancy committing some more treason?"
    menu:
        "Absolutely.":
            cnt "Illy are you sure about this?"
            illya "I have never been as sure about anything Centy"
            $ cnt_lst=+1
            #z kisses illya
            illya "Hmmm. Not bad. This promises to be a fun night."
            illya "Come and have a go Centy."
            cnt "Oh Illy. If you're sure."
            z "You ready Centoria? Shall we do this again?"
            illya "AGAIN? Centy you naughty girl."
            #z kisses centoria
            cnt "I'm sorry Princess. I couldn't resist."
            illya "I'm not mad. I'm impressed."
            illya "Now, [mc_name]. You have been entertaining us. Now, it is our turn to entertain you."
            #illya pushes z back
            illya "Centy, how about you get down and show him some love?"
            cnt "It would be my pleasure Illya"
            #centoria goes down on z
            z "Ahh"
            illya "That seems to be pleasurable?"
            z "You have no idea."
            illya "I wouldn't be too sure of that if I were you."
            #z looks surprised
            z "(Well that's bound to be interesting)"
            z "I think you should join me up here Princess"
            illya "With pleasure [mc_name]."
            #z and illya start kissing - z playing with illya tits
            cnt "Mmmnnnn."
            #illya pulls away from the kiss
            illya "Mmmnff. Centy I think it's my turn."
            #centoria pulls z out of her mouth
            cnt "Of course Illy, get down here and I'll show you how to do it properly."
            #illya starts to go down - z stops her
            z "How about we get more comfortable?"
            illya "That would be much appreciated."
            #get out of bath and z lies on the edge of the bed with illya between his legs - centoria kneeled showing her what to do
            illya "So like this?"
            cnt "Yeah, exactly like that. Look at his face, see how he likes it."
            z "Haaaa... Illya this is... Amazing."
            z "Centoria how about your come up here?"
            cnt "Up there?"
            z "Yes, up here." #indicates to his face
            illya "You should Centy!"
            z "See. Even the gracious Princess agrees with me."
            #illya licks his tip
            illya "Didn't I tell you not to call me Princess?"
            z "I'm sorry Illya. You just look so royal down there."
            #centoria laughs
            cnt "Hehe. I'm inclined to agree Illy."
            #centoria climbs up - legs over z's face
            z "..."
            #z pulls her down
            cnt "EH!"
            #z starts eating her out
            cnt "AHHHH!"
            illya "Hehe. Who's looking royal now Centy?"
            #illya keeps sucking
            cnt "HMNF! WHY DID HE START LICKING MO-HAAAAA??"
            #z keeps eating her out
            illya "Hmmmnn. Do you plan on only letting Centoria up there [mc_name]?"
            #z lifts centoria off his face - centoria dripping
            cnt "I was so close. Please."
            z "Illya, your turn up here."
            illya "With pleasure." #climbs up onto z's face
            z "Centoria?"
            cnt "Mhm?"
            z "How about you climb on top of me elsewhere?"
            cnt "Wait... You mean?"
            z "I want you to ride me."
            cnt "..."
            illya "I think you should Centy."
            cnt "OK, if you're sure."
            #centoria climbs on top of z
            cnt "Please be gentle..."
            menu:
                "Let her take her time.": #centoria 
                    cnt "Haaaaaa..."
                    cnt "(Holy shit he's so big...)"
                    $ cnt_aff += 2
                    $ cnt_lst += 2
                "Pull her down.":
                    cnt "OH GODS WAIT!"
                    cnt "(He's hitting my womb...)"
                    $ cnt_lst += 2
            illya "How does it feel Centy?"
            #centoria not riding - panting
            cnt "Oh I've never felt anything like it Illy..."
            cnt "..."
            illya "Hmmmnnn~~ I can't wait to feel him for myself"
            z "(Oh Gods... If she's anywhere near as tight as Centoria then I don't know what I'll do.)"
            illya "Ahhnnn~ FUCK!"
            cnt "Such- AHHH! Such vulgar language Illy... What would your people think?"
            illya "HNNNN~ WHO CARES?! THEY WOULD AHHHH-AGREE IF THEY HAD THIS TONGUE UNDER THEM!"
            z "(Well I'm not sure I'd want to be under all of them but I'm sure she knows that.)"
            z "Mmmmfff~"
            illya "AH! He started moving his tongue faster! I think he's close!"
            cnt "Hmmmnnnn... I'm so close"
            illya "Ahnnnn! Me too Centy!"
            cnt "HNNNNN!"
            illya "HAAAAA!"
            menu:
                "Cum inside":
                    $ cnt_lst += 2
                    #illya climbs off z's face
                    #centoria climbs off z's dick
                    #cum spilling out (he's an incubus come on)
                    illya "Oh Centy you look so full."
                    cnt "Ahhn~ I don't think you would believe how full I feel."
                "Pull out":
                    $ cnt_lst += 1
                    #illya climbs off z's face
                    #centoria covered in cum (he's an incubus come on)
                    illya "Oh Centy you look so pretty."
                    cnt "Ahhn~ Thank you Illy."
            z "Holy shit that was amazing..."
            illya "Hey [mc_name]. Think you can go again?"
            z "And break even more laws? Of course I can. You fancy climbing on?"
            illya "Absolutely. I want my turn."
            z "Well then it would be my pleasure if you would get up here."
            #illya sitting on z - looking at dick
            illya "Holy shit Centy... I don't know how you took this."
            illya "I mean... How can this fit inside me?"
            illya "It's almost up to my tits!"
            cnt "Hehe. You'll manage Illy."
            z "We can go slow Illya, take your time."
            #illya starts lowering herself onto z's dick
            illya "Haa~"
            z "Holy shit you are so fucking tight."
            illya "Ahhhn~ How much is in Centy?"
            cnt "About half..."
            z "Take your time Princess we have all night."
            #illya slides down fully - very slow - anim
            illya "Hnngh~ Oh Gods I think you might be in my womb!"
            z "I'm sure you don't need me to tell you this, but take your time."
            illya "Oh? You don't think I should just impale myself? I'm surprised..." #rolls her eyes
            cnt "Hehe. He really knows how to read the room Illy."
            z "Sorry. Just trying to be helpful."
            illya "It's fine, we're just teasing... I'm going to start moving now."
            #z puts hands on her hips
            z "Go for it."
            #anim start - illya riding
            illya "Ahhhnnn~ OH GODS!"
            illya "You are hitting EVERYWHERE!"
            z "I think it's more that you are ridiculously tight!"
            cnt "It's probably a mix of both..."
            illya "Hmmmmmnn..."
            illya "Well whatever it is, I'm so fucking close."
            z "Me too!"
            cnt "Where do you want to finish, [mc_name]?"
            menu:
                "Cum inside":
                    illya "Holy shit! He's filling me up!"
                    #illya full - still on dick
                    illya "Haaa~ I've never felt like this..."
                    #illya gets off - cum dripping down thigh
                    illya "There's so much inside me."
                "Cum outside":
                    #cum all over illya
                    illya "Holy shit! It's everywhere!"
                    #z gets up - looks at his handiwork on illya
                    z "Damn you look very pretty like this Illya."
                    cnt "I can only agree..."
            illya "That was amazing. Gods..."
            z "You can say that again."
            illya "You two feel like making this a permanent fixture?"
            z "Haha. Thank you for the offer Princess, we shall certainly think about it, right Centoria?"
            cnt "If it's always like this then absolutely..."
            illya "Well, let's get cleaned up and get to bed, we have a lot of work to do still."
            z "Agreed, how about we actually use the bath as we were supposed to and then sleep."
            #skip to after they bathe - illya + centoria lying down on one bed, z on another
            cnt "Well after today, I hope this trip can only get better."
            illya "Me too. Thank you for today."
            z "Fingers crossed. Goodnight both of you."
            illya "Goodnight [mc_name]."(Multiple=2)
            cnt "Goodnight [mc_name]."(Multiple=2)
        "Not tonight":
            $ dummy += 2
            illya "Shame. Let us bathe and go to sleep then."
            #skip to after they bathe - illya and centoria lying on one bed, z on another
            illya "Big day tomorrow. Hopefully everything goes to plan."
            z "Goodnight girls. Sleep well."
            cnt "Goodnight [mc_name]."(Multiple=2)
            illya "Goodnight [mc_name]."(Multiple=2)
            #ISCH PLEASE READ THROUGH THIS SCENE IT TOOK ME SO LONG TO GET THROUGH THIS AND I AM NOT SURE ABOUT IT

    scene black with fade
    stop music fadeout 1.0
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop sound fadeout 1.0
    pause(1.0)

    $ MainMenu(confirm=False)()