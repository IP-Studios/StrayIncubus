label season2_chapter_3:
    $ chapter = 15
    define jamie = Character("Jamie", color = "f5c13d")
    define vollstahl = Character("Vollstahl", color = "f5c13d")
    define klyn = Character("Klyn", color = "f5c13d")
    define jillia = Character("Jillia", color = "f5c13d")
    define illya = Character("Illya", color = "f5c13d")
    define Dohkong = Character("Dohkong", color = "f5c13d")
    define plgbln = Character("Pale Goblin", color = "f5c13d")
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
            scene v596
            z "I'll get the wine."
            scene v597
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
            jnfr "Something to spice things up."
            scene v603
            z "..."
            #Looks at them.
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
            scene v613
            jnfr "It's just a drinking game. And don't worry, it doesn't involve skills at playing or anything like that."
            scene v613
            hlna "Drinking game?"
            hlna "Those games where you'll ultimately get drunk?"
            scene v613
            jnfr "Pretty much."
            scene v615
            hlna "I don't know if I should be getting drunk... I have to protect the village if anything happens..."
            scene v616
            z "You've been stressed over the village's safety for a while now, Helena. Even you have to let go a little sometimes."
            z "I single handedly dealt with the attacker the last time. And I'm pretty sure at least Anabelle and Seira are even more capable than me."
            z "In the unlikely scenario where something should happen while you and I are here, those two will manage."
            scene v617
            hlna "..."
            hlna "I suppose you have a point."
            hlna "So? How does one play?"
            scene v618
            jnfr "Okay, so..."
            scene v619
            jnfr "We're supposed to play in pairs. Since Jamie and I are betrothed, it makes sense that we should be a pair."
            scene v620
            z "I guess you and I are a pair then, Helena."
            scene v621
            hlna "Okay, sure."
            scene v622
            jnfr "Great!"
            scene v623
            jnfr "I'll start to show you guys how it's done."
            #Physically explains how it's done.
            scene v624
            jnfr "You draw a card..."
            jnfr "You read whatever is written on it."
            scene v625
            jnfr "For example this card says: Slap a player from the opposing team on any part on the body you want."
            jnfr "Well... I'm supposed to do what's on the card and slap one of you guys. But I don't want to."
            jnfr "So... If I don't do what's written I have to drink."
            scene v626
            #drinks.
            scene v625
            jnfr "And... Well, once someone can't drink any more... They're out. They lose, basically."
            jnfr "Easy enough, right?"
            scene v627
            hlna "Yeah."
            scene v625
            jnfr "Okay, let's play clockwise."
            jnfr "Helena, you're up."
            scene v628
            scene v629
            #Draws a card.
            hlna "..."
            scene v630
            hlna "Your partner must take off their top."
            scene v361
            hlna "..."
            z "But I'm not wearing a top..."
            scene v632
            jnfr "Well that means she drinks."
            scene v621
            hlna "Ah..."
            scene v635
            scene v633
            scene v634
            #Drinks.
            #Jamie draws.
            scene v636
            scene v637
            jamie "Drink twice."
            scene v638
            jamie "Oh... That's not great..."
            scene v639
            #Drinks twice.
            scene v460
            jamie "This wine is really good quality, I have to admit..."
            scene v642
            jnfr "See? I told you the village is not such a bad place..."
            scene v641
            jamie "Maybe you're right..."
            scene v642
            z "Okay, I'm up."
            #Draws.
            scene v643
            scene v644
            z "Arm wrestle a member of the opposing team. If you lose, drink twice. If you win, kiss the other."
            scene v645
            jamie "Eh?"
            jamie "I'm guessing you're going to arm wrestle me."
            scene v646
            z "No, Imma wrestle Jenny and kiss you..."
            z "Of course I'm gonna wrestle you, dude..."
            scene v647
            jamie "..."
            #They arm wrestle.
            scene v648
            jamie "You're quite jacked, huh..."
            jamie "I guess you need to be if you're going to be a ninja."
            scene v649
            z "We do get quite a bit of physical exercise, so yeah..."
            scene v650
            scene v651
            jamie "Heh... But in arm wrestling, technique is more important than muscle."
            scene v653
            z "Is it now?"
            scene v652
            jamie "Of course! I'll show you how I'll beat you with my technique."
            scene v653
            z "You do a lot of arm wrestling in your day?"
            scene v650
            jamie "..."
            scene v651
            jamie "Well, no. But I-"
            scene v652
            jamie "Oh, this is just a foolish trick to try to annoy me before we start, you sneaky bastard!"
            scene v653
            z "Not really..."
            scene v652
            jamie "Let's let our arms talk for us, shall we?"
            scene v653
            z "Sure."
            scene v657
            scene v659
            #Z wins in a second.
            scene v660
            jamie "Wait! No! I wasn't ready!"
            jamie "Someone should count down from three!"
            scene v654
            jnfr "I'll do it."
            jnfr "Three..."
            scene v657
            jnfr "Two..."
            jnfr "One..."
            jnfr "Go!"
            scene v659
            #Z wins in a second.
            scene v658
            jamie "Ah!"
            jamie "Wait! I thought it'd be three, two, one, zero!"
            scene v653
            z "Dude..."
            scene v650
            jnfr "Come on, Jamie... It's just a game..."
            scene v652
            jamie "No, no, dear. This guy is just using my unpreparedness."
            jamie "You know how sneaky those ninjas are."
            scene v654
            z "Jenny, can you count down from three to zero?"
            scene v626
            jnfr "Yeah, fine..."
            scene v655
            z "When we hear zero, we both start. Sounds good?"
            scene v656
            jamie "Heh... You should've taken the win you got while you could."
            jamie "Deal!"
            scene v655
            z "Let's go, Jenny."
            scene v657
            jnfr "Three..."
            jnfr "Two..."
            jnfr "One..."
            jnfr "Zero!"
            #Jamie manages to hold Z for a second.
            scene v658
            jamie "See?! It's working! Now I can turn this ar-"
            scene v659
            #Z totally destroys him.
            jamie "..."
            jamie "No! Wai-"
            scene v665
            z "Shhhhhhhh..."
            scene v666
            z "Excuse me, I have a kiss to claim."
            scene v667
            jamie "..."
            scene v668
            z "..."
            scene v669
            z "Ready?" #To jenny.
            scene v670
            jnfr "Y-Yeah..."
            scene v671
            z "(Jamie is kinda looking...)"
            z "(And so is Helena.)"
            z "(Guess I should...)"
            scene v672
            menu:
                "(...go all out with a strong kiss.)":
                    scene v673
                    scene v674
                    jnfr "Hmm..."
                    scene v675
                    jnfr "Hmmmnnn~?"
                    scene v676
                    jnfr "Ahhhnn~..."
                    scene v677
                    scene v679
                    scene v679
                    scene v680
                    jnfr "Hanhhh~..."
                    $ jnfr_lst += 1
                    $ jxj -= 3
                "(...give her a nice PG-13 kiss.)":
                    scene v673
                    jnfr "Hmm..."
                    scene v675
                    jnfr "Nnm..."
            scene v681
            z "Okay... It's your turn, Jenny."
            scene v682
            jnfr "Right..."
            jnfr "If there's someone shorter than you on the opposing team, they drink. And for every member taller than you, you drink once."
            scene v683
            jnfr "Hmmm... So Helena is slightly shorter than I am..."
            scene v684
            jnfr "And you're way taller, [mc_name]..."
            scene v685
            z "So both you and Helena drink."
            scene v686
            jnfr "Damn... You haven't drunk a single time so far..."
            scene v687
            z "What can I say, I'm just good."
            scene v688
            jnfr "Hmmm..." #Sus.
            scene v689
            jnfr "Cheers."
            scene v690
            hlna "Cheers!"
            scene v691
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
            scene v692
            jnfr "Do it Jamie. [mc_name] hasn't drunk the whole game. We'll totally end up losing unless he gets to drink."
            scene v693
            jamie "..."
            scene v694
            jamie "Okay, good point... Must be why he managed to beat me in arm wrestling."
            scene v695
            z "Ahuh..."
            scene v696
            jamie "Okay... I can't see anything." #Puts on a blindfold.
            scene v697
            z "Guess we have to drink, Helena."
            scene v698
            hlna "..."
            scene v699
            scene v700
            z "Okay, let's see."
            z "Slap a player from the opposing team on any part of the body you want."
            z "Oh, same card as the one we started with."
            scene v701
            jnfr "I guess some of them have replicas."
            scene v702
            z "Hmmm..."
            scene v703
            z "I'll slap..."
            menu:
                "Use the card to spank Jenny.":
                    z "Jenny."
                    scene v704
                    jnfr "Hmmmm..."
                    jnfr "I wonder where you'll do it..."
                    scene v705
                    z "Me too..."
                    jamie "..."
                    scene v706
                    #Bends over and gives him her ass.
                    z "..."
                    hlna "..." #Surprised.
                    scene v707
                    scene v708
                    jnfr "Awwww~!!!"
                    scene v709
                    jnfr "Ahh~..."
                    jamie "Jenny?! Are you okay?"
                    scene v710
                    jnfr "Yeah... It..."
                    scene v711
                    jnfr "It wasn't bad, don't worry..."
                    scene v712
                    jamie "Hmmm..."
                "Use the card to slap Jamie.":
                    z "Jamie."
                    scene v713
                    jamie "Ugh..."
                    jamie "Let's get it ov-"
                    scene v714
                    #Slaps him.
                    scene v716
                    scene v715
                    jamie "Offghh!"
                    jamie "Awwww..."
                    jamie "Did you have to do it so hard..."
                    scene v717
                    jnfr "It's just a game, Jamie... Man up."
                    scene v718
                    jamie "Humpf..."
                "Drink.":
                    z "I'll just skip this one."
                    scene v717
                    jnfr "Boooo..."
                    scene v718
                    z "Yeah, yeah."
            #scene of jenny holding a card
            jnfr "Okay, my turn."
            #jenny reading the card
            jnfr "All players on the opposite team must take off their tops."
            scene v719
            hlna "Oh..."
            scene v720
            jnfr "You can drink instead if you're not comfortable with it..."
            scene v721
            hlna "Hmmm..."
            scene v722
            hlna "No I'm okay... I've had plenty to drink already. I don't want to lose too early."
            scene v723
            #Takes off her bra.
            jnfr "..."
            z "(Interesting...)"
            scene v724
            jnfr "I guess since [mc_name] isn't wearing a top, I guess I have to drink."
            scene v725
            hlna "Suck on on whichever body part of your partner's that you want. If you do so, the other team drinks."
            scene v726
            hlna "..."
            z "Eh... It-"
            #Approaches him.
            jnfr "..."
            scene v727
            #Kneels.
            z "Helena?"
            scene v728
            scene v729
            scene v730
            scene v731
            scene v732
            scene v733
            scene v734
            scene v735
            #Grabs his hand.
            #Sucks on his thumb seductively.
            scene v736
            hlna "..." #Gets up.
            scene v737
            hlna "{i}Clears her throat.{/i} Who's next?"
            scene v738
            jamie "Me..."
            jamie "Oh... How am I supposed to rea-"
            scene v739
            jnfr "I'll do it." #Takes it from him.
            jnfr "Your partner must take off their top."
            scene v740
            jnfr "Oh no, oh no... Whatever am I to do..."
            scene v741
            jamie "What are yo-"
            #Takes off her top.
            scene v742
            jnfr "I'm not losing."
            scene v743
            jamie "You could've just drunk..."
            scene v742
            jnfr "I could've, but then we would've lost in a few rounds."
            scene v743
            jamie "Hmmm... I guess it's just a game..."
            scene v744
            z "Eh? Wait, we can't see your..."
            scene v745
            jnfr "Hm? Did you say something, Mr.Pervert?"
            scene v746
            z "But..."
            z "..."
            z "Fine... My turn."
            z "Play 'fuck, marry and kill'. The one you kill drinks."
            z "Okay..."
            define y_r_u_g_counter = 0 #Move to top of script
            label y_r_u_g:
            menu:
                "Fuck Jenny and marry Helena.":
                    z "I'd fuck Jenny... Marry Helena... And kill Jamie."
                    scene v747
                    jnfr "Oooh, how romantic..." #Sus.
                    scene v748
                    z "I must admit I'm more into doing one than the other two."
                    scene v749
                    jnfr "..."
                    $ jnfr_lst += 1
                    scene v752
                    jamie "I'm guessing it's killing me?"
                    scene v753
                    z "Heh... Sure..."
                "Fuck Helena and marry Jenny.":
                    z "I'd fuck Helena... Marry Jenny... And kill Jamie."
                    scene v751
                    hlna "..."
                    scene v750
                    jnfr "That was a romantic proposal..."
                    scene v749
                    z "More romantic than the one you currently have, I imagine..."
                    jnfr "..."
                    scene v752
                    jamie "Hey... I can be very romantic, you know..."
                    scene v753
                    jnfr "Of course you can, dearest..."
                "More options." if y_r_u_g_counter == 0:
                    #Why are you geh meme.
                    $ y_r_u_g_counter = 1
                    jump y_r_u_g
            scene v755
            jnfr "Okay, let's see."
            scene v756
            jnfr "Give a lap dance to someone from the opposing team. They must drink after."
            scene v757
            jnfr "Easy."
            scene v758
            jamie "Wait, you're really going to do this?!"
            scene v759
            jnfr "Oh, don't worry, Jamie. [mc_name] is like a little brother to me."
            scene v760
            jamie "Hmmm..."
            scene v761
            scene v762
            scene v763
            scene v764
            scene v765
            scene v766
            scene v767
            scene v768
            scene v769
            scene v770
            scene v771
            scene v772
            #Gives Z a lap dance.
            #He gets an erection.
            $ jnfr_lst += 1
            scene v775
            hlna "..."
            scene v773
            jnfr "I can see I did well..."
            scene v774
            z "I guess so..."
            #Z drinks.
            scene v776
            hlna "Okay..."
            hlna "Pick two people you'd have a threesome with. Anyone not picked must drink."
            scene v777
            hlna "..."
            scene v778
            hlna "Well... I guess [mc_name]..."
            scene v779
            hlna "And Jenny..."
            scene v780
            jnfr "Ooooh... That sounds interesting..."
            scene v781
            jamie "Your loss..."
            scene v782
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
                scene v786
                jnfr "..." #Looks at Z.
                scene v788
                scene v789
                scene v791
                hlna "..."
                scene v790
                hlna "Wha..."
                jamie "Hm? What?"
                scene v791
                hlna "..."
                scene v792
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
            scene v799
            scene v800
            scene v801
            #Hlna takes off Z's pants and admires his dick for a bit.
            jnfr "See something you like, Helena?"
            scene v802
            hlna "?!"
            scene v803
            hlna "That's not..."
            scene v804
            hlna "..."
            hlna "Who's next..."
            scene v801
            jnfr "That'd be me..." #Stands up to grab a card
            scene v805
            jnfr "Oh..." #Falls on Z. Her boobs are in his face.
            scene v806
            scene v807
            scene v808
            jnfr "Sorry... I think I'm a bit tipsy..."
            scene v809
            z "We can st-"
            scene v810
            jnfr "Na-uh. I'm fine. We can continue. I'm not gonna lose."
            scene v811
            z "Sure..."
            scene v812
            jnfr "Kiss any member of the opposing team. If you do, they must drink."
            scene v813
            jamie "..."
            jnfr "Well..."
            #Goes to Z.
            jnfr "By the way, Jamie. I'm only doing this so we can win."
            scene v814
            jnfr "[mc_name] is literally like a little bro-"
            scene v815
            jnfr "Hmmmn~..." #Z starts kissing her.
            scene v816
            jnfr "Hmmmnnnn~... Uhmmnn~..." #They make out.
            scene v817
            jnfr "Hmnn~..." #They break the kiss.
            scene v818
            $ jnfr_lst += 1
            jnfr "..."
            scene v819
            jnfr "Now, drink."
            scene v820
            scene v821
            z "Yeah, yeah."
            #Drinks.
            menu:
                "Tell Jenny she can also do the same to Helena.":
                    scene v823
                    z "Wait."
                    scene v824
                    z "You want to win, right?"
                    scene v825
                    jnfr "Of course!"
                    scene v826
                    z "The card didn't say you can only do this to one member of the other team, did it?"
                    scene v827
                    jnfr "..."
                    #Checks the card.
                    scene v828
                    jnfr "I guess not..."
                    scene v829
                    jnfr "..." #looks at Helena.
                    scene v830
                    hlna "..."
                    #I'm here R <-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
                    #Goes to her.
                    scene v831
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
    scene v479
    axs "..."
    scene v480
    axs "Are they dead?"
    scene v481
    nari "..."
    scene v482
    axs "Are they?"
    scene v484
    nari "No."
    scene v483
    axs "..."
    scene v486
    axs "You had very simple instructions, Nari."
    axs "Get me the town's alchemist."
    axs "And kill anyone who interferes."
    scene v488
    nari "I did bring you the alchemist."
    scene v486
    axs "Yes. But you didn't kill a single ninja."
    axs "Were they stronger than you and your team?"
    scene v487
    nari "..."
    scene v486
    axs "Grown weak, have you? Four kunoichi can beat your team now?"
    scene v487
    nari "..."
    scene v486
    axs "Perhaps next time Alura should lead the missions?"
    scene v488
    nari "No."
    nari "Alura works for me, not you Axius."
    scene v489
    axs "Most of the work she does for you seems to be in the bedroom these days."
    scene v490
    scene v491
    nari "How dare you..."
    scene v492
    nari "Say that again."
    scene v493
    axs "..."
    scene v494
    alura "..." #Scared.
    scene v495
    nari "Go on."
    scene v496
    irna "..."
    scene v497
    axs "You're dismissed."
    scene v498
    axs "All of you."
    scene v499
    axs "Nari..."
    scene v500
    scene v501
    scene v502
    axs "Do not fail me again."
    axs "Or it'll be the last time you do."
    scene v503
    scene v504
    scene v505
    scene v506
    scene v507
    scene v508
    #They leave.
    #Irna is walking back to her room (ALONE!)
    #Opens the door and wants to change.
    irna "*{i}Sighs.{/i}"
    scene v509
    nari "Why did you stop me?"
    scene v510
    irna "EEEP?!"
    scene v511
    irna "..."
    scene v512
    irna "What are you doing here, Nari?"
    scene v513
    nari "..."
    nari "Irena."
    nari "Why did you stop me from killing the girl?"
    scene v514
    nari "What is that you know?"
    scene v515
    irna "..."
    irna "I..."
    irna "It's just..."
    irna "It's how incubi are, Nari."
    irna "My father isn't special in this regard, really."
    scene v516
    nari "..."
    scene v514
    nari "Expl-"
    scene v517
    irna "Go and ask Nixie about it."
    irna "She's the same as that girl."
    irna "There's others too, I'm sure..."
    irna "The only difference Nixie was from the rest of them is that her mother was a succubus and thus my father found her useful."
    scene v518
    nari "..."
    nari "You mean..."
    nari "How many bast-"
    scene v519
    irna "Probably dozens of them out there."
    scene v520
    nari "..."
    nari "How could you tell that girl was one of them?"
    scene v519
    irna "I can always tell..."
    irna "Can't say I like the fact that I do. But I can tell."
    scene v520
    nari "..."
    scene v519
    irna "You..."
    scene v522
    nari "Hm?"
    scene v519
    irna "You could've just ignored me and killed them all."
    irna "Why didn't you?"
    scene v521
    nari "..."
    nari "Do you think it's right?"
    nari "What we're doing..."
    scene v523
    irna "..."
    nari "..."
    scene v524
    nari "Good night, my lady." #Leaves.
    scene v525
    irna "Nari."
    scene v526
    nari "?"
    scene v527
    irna "Do you..."
    irna "Do you remember anything now?"
    irna "From your past?"
    scene v528
    nari "..."
    nari "A bit..."
    nari "Sometimes... In my dreams... I can see little shards of it..."
    nari "I've been dreaming quite often lately..."
    nari "..."
    nari "Irena..."
    nari "Does your father have sleep nymphs under his command?"
    scene v529
    irna "Sleep nymphs?"
    irna "Not that I know of..."
    scene v530
    nari "I see..."
    #Leaves.
    irna "..."
    irna "(If Nari turns on my father...)"
    irna "(And with [mc_name]'s help...)"
    irna "(Maybe...)"
    irna "(Just maybe...)"

#11) Arrival at elven city:
    #Tourny is already beginning when they arrive.
    #It is a jousting competition at first.
    z "..."
    z "This is interesting..."
    z "What are they doing with those sticks?"
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
    #The princess hugs centoria similar to how torr's family hugged her.
    vollstahl "My lady... That'sh no way for a prinshesh to behave."
    illya "Sorrrryyy..."
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
    illya "I'd imagine you wouldn't want people to assume the same about you just because you're an incubus, right?"
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
    Character("Crown Prince") "My beautiful daughter, I'm so glad you could make it."
    #illya and z bowing to father
    illya "Father, thank you for seeing us today."
    #Z asks why the guards have no weapons, the prince makes them demonstrate their powerful af magic saying that elves are specialists in magic.
    z "Your Highness, how come your guards have no weapons?"
    Character("Crown Prince") "Oh? I'm sorry, I didn't explain, my guards are all proficient in magic, physical weapons are useless to them."
    Character("Crown Prince") "See that dummy over there?"
    z "Yes?"
    Character("Crown Prince") "Guards."
    #anim showing off the magic
    z "Wow... That's pretty cool."
    #The prince brags about how he provided well paying jobs for the goblins and helped civilise them. Gives some credits to illya.
    Character("Crown Prince") "I'm very proud of our attempts to integrate our societies. Myself and my daughter have been working for this to benefit both the elves and the goblins."
    #The prince says he'll also lend them a dozen of his personal guard when they leave to the nearby villages and says he doesn't understand why his daughter wants to visit these peasants.
    Character("Crown Prince") "My daughter insists on visiting the nearby villages, I have no idea why. However, I trust her judgement. I will lend you a dozen of my personal guard to accompany you."
    illya "Thank you, Father."
    #Z (with centoria) gets a mission to protect the princess of Centoria's village of some sort. Her father specifies that he's not to be further than 1 meter away outside of the city and can be instructed to be up to 20
    Character("Crown Prince") "[mc_name], as my daughter's birthweek celebrations, she will be visiting the outskirts of the city. I want you to protect her."
    z "Of course, Your Highness."
    Character("Crown Prince") "As of tomorrow morning, you are not to be further than 1 meter away from her outside of the city."
    z "And inside the city?"
    Character("Crown Prince") "Inside the city, you may be up to 20 metres from her."
    z "Yes, Your Highness."
    #A magic bond is formed by a sorceress working in the castle.
    Character("Crown Prince") "I have asked the sorceress to create a bond between you two. She will be able to communicate with you through this bond."
    illya "Father that is not necessary."
    Character("Crown Prince") "Unfortunately daughter, this is non-negotiable."
    z "It's fine Princess, it can't hurt."
    Character("Crown Prince") "Excellent, I'm glad you understand."
    #Sorceress enters
    Character("Sorceress") "Your highness."
    Character("Crown Prince") "Sorceress, please create the bond."
    #The sorceress creates the bond.
    Character("Sorceress") "It is done."
    Character("Crown Prince") "Thank you, sorceress. You may take your leave."
    #The sorceress leaves.
    Character("Crown Prince") "Now, [mc_name], the goblins recently attacked the elf city. You must keep my daughter safe."
    cnt "No harm will come to her Your Highness. You have our word"
    Character("Crown Prince") "Thank you Centoria. I shall see you when you return."
    #The sorceress who works for the prince is a hooded figure who never shows any part of her skin (She's a goblin!)
    #The prince tells them that local goblins recently attacked the elf city a few times and the princess insists on visiting the outskirts of the city as a part of her birthweek celebrations like she always does. A body guard is needed for the princess.
    #z, illya and centoria leave - sorceress waiting outside for them
    Character("Sorceress") "Your plan will not succeed Princess."
    illya "Sorceress? What do you mean?"
    #The sorceress turns illya, centoria and yumi into snowmen.
    Character("Sorceress") "[mc_name], elves and goblins can never be integrated. You must make a choice."
    #sorceress leaves - turns illya back
    illya "Sorceress?"
    illya "What in the worlds did she mean?"
    z "I have no idea, Illya."
    illya "We should prepare. We shall see you in the morning for the tournaments."
    z "Goodnight Illya. Goodnight Centoria."
    illya "Goodnight [mc_name], Yumi. Rest well."
    cnt "Goodnight [mc_name], Yumi. Sleep well."

    #z and yumi go back to their room:
    #Yumi has to apply a potion from Gabbie and Venus to heal up properly. Z has to apply it when Centoria isn't around, leading to sexual stuff.
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
    Character("Crown Prince") "WELCOME EVERYONE! TO THE 437TH ANNUAL FENCING TOURNAMENT!"
    Character("Crown Prince") "OUR FIRST MATCH IS-!"
    #skips to semi-finals - yumi vs vollstahl
    Character("Crown Prince") "THE SECOND SEMI-FINALS IS HERE. OUR REIGNING CHAMPION, SER VOLLSHTAHL! VERSUS. OUR NEWCOMER, YUMI!"
    illya "Unfortunately, Yumi does not stand a chance here [mc_name]."
    z "I wouldn't be so sure, Illya. Yumi can be quite slippery when she wants to be."
    illya "We shall see."
    #vollstahl and yumi fight - yumi gets destroyed
    Character("Crown Prince") "AND THE WINNER IS SER VOLLSHTAHL!"
    illya "See, [mc_name]. I told you."
    z "Yeah, you were right. He's quite the fighter."
    illya "Indeed he is."
    #In the fencing tourney (no magic is allowed) Z is asked to compete by the princess.
    Character("Crown Prince") "AND OUR FINAL MATCH IS HERE! OUR REIGNING CHAMPION, SER VOLLSHTAHL! VERSUS. POTENTIALLY HIS BIGGEST THREAT SO FAR, [mc_name]!"
    #vollstahl - still in his full armour and z fight - it's close but z loses
    Character ("Crown Prince") "LADIES AND GENTLE-ELVES! AFTER AN EXTREMELY CLOSE MATCHUP. YOUR CHAMPION, FOR THE 437TH ANNUAL FENCING TOURNAMENT IS SER VOLLSHTAHL!"
    vollstahl "Well fought [mc_name]. You are a worthy opponent."
    z "Thank you, Ser Vollstahl. You are just as impressive as the Princess said."
    #Vollstahl, the king's personal guard, wins against Z. Vollstahl is a short man, who always wears a full armour and a helmet covering all of his body. (He's actually a goblin who betrays the elves later on and joins axius).
    #Z is asked to compete by the princess. He loses to Vollstahl in the finals.
    Character("Crown Prince") "AT OUR CLOSING CEREMONY, OUR CHAMPIONS AND RUNNER UPS WILL BE PRESENTED WITH THEIR PRIZES!"
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
    Character("Crown Prince") "AND THE WINNERS OF THE FIRST MATCH ARE THE ELVES FROM ESANKADI!"
    z "Esankadi?"
    illya "A small village in the East. They have some wonderful scenery, as you will see when we visit."
    #skip to our first match
    Character("Crown Prince") "AND THE NEXT MATCH IS HERE! OUR NEWCOMER, [mc_name] AND THE PRINCESS ILLYA! VERSUS! THE ELVES FROM NASAKADI!"
    z "From where?"
    illya "The North. Unimportant, pay attention to their fighting style."
    z "Got it."
    #fight starts - fairly even
    #z takes a hit from an unknown magic
    z "Interesting..."
    illya "You OK, [mc_name]? I am hoping one hit does not take you out."
    z "Fine Princess, that wasn't nearly enough to finish me off."
    #they fight - z and illya win
    Character("Crown Prince") "AND THE WINNERS OF THE SECOND MATCH ARE PRINCESS ILLYA AND [mc_name]! MY HOW INTERESTING THIS IS TURNING OUT TO BE!"
    z "See Princess. I told you, nothing to sweat about."
    illya "You are indeed quite strong. But do not get confident."
    z "..."
    illya "Did I not also tell you to call me Illya. Drop this Princess nonsense."
    z "Apologies Illya, thought it might seem inappropriate if your bodyguard called you by your first name."
    illya "I see. Do not fret. We are friends first, bodyguard and Princess second."
    z "Understood."
    illya "And if anyone complains. I shall have them exiled."
    z "Exiled? Surely you can't do tha-"
    illya "I was joking, [mc_name]."
    z "Of course you were."
    illya "Shall we continue watching some more fights?"
    z "Absolutely."
    #skip to the final.
    Character("Crown Prince") "AND THE FINAL MATCH IS HERE! THE ELVES FROM ESANKADI! VERSUS! PRINCESS ILLYA AND [mc_name!u]!"
    #shot on the elves from Esankadi
    #shot on Illya and Z
    Character("Crown Prince") "MAY THE STRONGEST TEAM WIN!"
    #fight starts - elves shitting on illya and z
    #illya and z both get hit and go down - z bleeding
    z "SHIT!"
    z "ILLYA! ARE YOU ALRIGHT?"
    Character("Crown Prince") "IS IT OVER? [mc_name!u] AND THE PRINCESS ARE DOWN. SEEMINGLY FOR THE COUNT."
    illya "DON'T FOCUS ON ME [mc_name!u]. THEY ARE GOING TO WIN."
    z "DON'T WORRY ILLYA. I'VE GOT THIS!"
    #z uses the same unknown magic from the first match - takes out one then teleports to the other and fus roh dah's the other
    Character("Crown Prince") "OH MY! WHAT A TURNAROUND!"
    Character("Crown Prince") "AFTER THAT INCREDIBLE MATCH, THE WINNERS ARE PRINCESS ILLYA AND [mc_name!u]!"
    illya "THAT WAS AMAZING [mc_name!u]!"
    z "I did tell you to trust me Illya."
    illya "My apologies. I never should have doubted you."
    z "No need to apologise. We won, that's all that matters."
    illya "Indeed. However. How did you do that? Have you ever used that magic before?"
    z "No. I am just a quick learner."
    illya "I see. I'm glad you are helping me then."
    Character("Crown Prince") "WELL, I SHALL SEE THE VICTORS AT THE CLOSING CEREMONY."
    illya "Well, [mc_name]. As this is the last tournament of the day, we should go and get some cleaned up and get some rest."
    z "As you wish Illya, let's get Centoria then head back."

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
            #illya measuring z's dick against stomach
            illya "I mean... It's almost up to my tits!"
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




#16) Goblin tournament:
    #This whole thing was suggested by Illya's father. She doesn't like the idea because it establishes that the goblins are beneath the elves and that they should transform.
    #There is an event for goblins, whoever wins gets a potion that transforms them into elves.
    #Z is surprised that such a potion exists. The elves explain that them and the goblins have a common ancestry and with a powerful potion you can ascend to an elf as a goblin but the potion is very expensive.
    z "So... What is this tournament about again?"
    illya "This tournament is just for the goblins. My fathers idea, I abhore it."
    z "That doesn't sound so bad? What do you hate about it?"
    illya "My father is about to start, you'll understand once he's finished."
    Character("Crown Prince") "WELCOME BACK TO THE SECOND DAY AND THE FINAL OF OUR TOURNAMENTS!"
    Character("Crown Prince") "THIS FINAL TOURNAMENT IS MY PERSONAL FAVOURITE! THE GOBLIN TOURNAMENT!"
    z "Ok so it's his favourite tournament, I still don't see the issue?"
    illya "Let him finish..."
    Character("Crown Prince") "AS YOU KNOW, THE WINNER OF THIS TOURNAMENT WILL RECEIVE A POTION TO ASCEND!"
    Character("Crown Prince") "WITH THAT... THE TOURNAMENT SHALL BEGIN! MAY THE STRONGEST GOBLIN WIN!"
    z "What does he mean 'ascend'?"
    illya "My father, along with a surprisingly high number of elves, believe that goblins are lesser creatures."
    z "So what does this potion do?"
    illya "The potion allows the goblin who wins the tournament to transform into an elf."
    z "There's a potion that can do that?!"
    cnt "Elves and goblins share common ancestry. Allowing a potion to transform the goblins into elves. The potion is extremely expensive and takes roughly a year to brew, so only one is brewed per year."
    z "Ah. I can see why you don't like the tournament Illya."
    illya "Indeed, hopefully this shall be the last."
    #z looks puzzled - continues anyway
    z "Well let's watch and hopefully our gracious Princess will find a way to fix this."
    illya "Let's hope."
    #tournament - we see the final fight
    Character("Crown Prince") "CONGRATULATIONS TO NEMTYL! OUR NEWEST CHAMPION FOR THE TOURNAMENT!"
    #crowd cheers
    Character("Crowd") "(CHEERS)"
    Character("Crown Prince") "PLEASE COME TO THE PALACE AND COLLECT YOUR PRIZE!"
    illya "Centoria, [mc_name]. Come. We have some items we need to discuss."
    z "Of course Illya."
    #skip




#17) Illya's plan:
    #Later to Z's team alone after playing together in the tournament and bonding with them - this is back in Illya's "office"
    illya "I want us and the goblins to reach a peace agreement."
    illya "The constant fighting is not good for anyone."
    illya "Visiting the nearby villages is a lie I told to my father, so he'll hire you."
    illya "I'm the one who asked him to hire you personally. Not him."
    illya "And I'm sorry. I didn't hire you because you are a great warrior. I'm sure you're very capable. But I hired you because you are an incubus."
    z "..."
    z "What are you talking about..."
    illya "You of all people should be able to understand your race being misunderstood and hated and seen as mere monsters."
    z "..."
    illya "I want to visit the goblins around the city. I want to talk to them."
    illya "If they agree to my plan... I can finally do it and free everyone from this damned situation."
    z "..."
    z "What exactly is your plan, Illya?"
    illya "I'll make them all citizens of the elven city."
    z "You..."
    z "You want the goblins as citizens here?"
    z "You know that not all the goblins are like the ones who live here, right?"
    illya "Yeah, yeah. They'll have to adjust and so will we, I know."
    illya "I'm not an idiot. I know it'll create dozens of problems."
    illya "But I'd rather have to solve those than have the pointless conflict that we have right now."
    illya "And in a decade or two, we will have gotten used to each other."
    illya "It'll take time and effort. But we can do it."
    illya "It is the best solution."
    z "I don't think your father will agree to it, do you?"
    illya "He won't."
    illya "But..."
    illya "I've just turned twenty."
    z "..."
    z "The major change to the elven way of life."
    z "Your first decision..."
    z "This will be it..."
    illya "You know about that?"
    z "Centoria told me..."
    illya "Well, yes."
    z "..."
    z "(This girl...)"
    z "(She's very interesting...)"
    #Stares at Z
    illya "My plan is, however, very difficult. I'll need lots of help if I am to do it."
    illya "Will you guys help me?"
    z "How?"
    illya "Do your job. Protect me while I try doing all of this."
    illya "And tell noone about this."
    z "..."
    z "I assume not even your father."
    illya "Especially not my father."
    illya "Not until the foundation for the plan is laid down."
    illya "I'll tell him myself then."
    z "..."
    ymi "You know, Illya..."
    ymi "A goblin tried to rape me once."
    illya "..."
    ymi "A couple of others tried to kill me."
    ymi "I've killed a few goblins myself too."
    illya "..."
    ymi "But I've seen plenty of humans try to do the same..."
    ymi "And I've heard all my life that a woman should not come within two villages from an incubus."
    ymi "Yet here I am friends with one."
    ymi "So know this, Illya..."
    ymi "I'll go with you to where the goblins live..."
    ymi "And make sure that if any of these green shits tries to lay a finger on you, they'll be cut to shreds."
    z "..."
    illya "Centory?"
    cnt "Of course I'll be with you, Illya."
    illya "..." #Looks at Z.
    z "..."
    z "Yumi, I'd like to take charge of the expedition in goblin territory."
    ymi "Sure."
    z "Thanks."
    z "Centoria, you'll pose as the princess the whole time."
    cnt "Of course."
    z "Yumi, if you get as much as a whiff of a potential attack, grab the princess and run back to the city. Leave Centoria and I behind if you must."
    ymi "I will."
    z "Princess, you'll keep your face hidden and dress like a handmaiden to hide your identity."
    illya "Okay, b-"
    z "And I also want the two goblins I saw working outside the castle to come with us."
    illya "Eh?"
    illya "Explain."
    z "They're a sign of good faith. If the goblins see their own walking with the princess, they might get the impression that we come peacefully and that goblins and elves can cooperate."
    illya "I see, I see..."
    illya "Not a bad idea at all."
    illya "Anything else?"
    z "Yes. Carry a weapon. A knife or something you can hide in your clothes."
    illya "But I don't know how to use a knife."
    z "Trust me, princess, it's not that hard."
    z "..."
    z "Your father said he'd send some of his guards with us..."
    illya "Yeah... That's also a problem..."
    z "Actually..."
    z "You wouldn't know how to forge your father's signature, would you?"
    illya "Hm?"
    #Skip

#18) Outside the city:
    #At the gate.
    Character("Guard") "Halt!" #Stops Z's wagon.
    z "..."
    Character("Guard") "Where are you going? And what have you got inside that wagon?"
    cnt "Stand down, Edgar." #Peeks out of the wagon.
    Character("Edgar") "Princess?"
    Character("Edgar") "What are you-"
    cnt "Let us through."
    cnt "And keep it down, will you? I don't want everyone to know about this."
    Character("Edgar") "But-"
    z "Here are your orders from the prince himself. We didn't publicly announce this for the princess's safety. You understand, I trust?"
    Character("Edgar") "..." #Reads the letter.
    Character("Edgar") "This is the prince's signature..."
    z "Edgar. The prince knew you could be trusted. That's why we picked the time when you're the one stationed on the gate. So tell no one about this, yeah?"
    Character("Edgar") "The prince sai-"
    z "Not a word to anyone, get me?"
    Character("Edgar") "Y-Yes, of course, my lord."
    z "Good man."
    #Goes forward.
    #Sees goblins going inside the city with their papers being checked.
    z "What's going on there?"
    illya "These goblins work in the city, but they don't live in it."
    illya "My father specified that any goblin who is to live in the city, must either have worked in the city for 10 years, or have a job which requires they stay in the city."
    z "..." 
    #Looks at the goblins.
    #They advance.
    z "..."
    z "Are we close?"
    illya "Yes. Their biggest camp is behind that hill."
    illya "Their leader, the pale goblin they call her, apparently lives there."
    z "..."
    illya "Believe me, [mc_name]. I'm well informed. I've been asking the goblins we have in the city about this for months."
    z "I see..."
    illya "They told me I could find the pale goblin here today. She moves around from one camp to the other, you see..."
    z "That's a bit weird..."
    illya "I guess goblins have a different way of life to us. The elves also used to move around following resources like water from one season to the other."
    illya "Until they decided to settle down in one place and use tunnels to bring the water to them a few centuries ago."
    illya "Maybe it's similar for the goblins."
    z "..."
    z "Wait..."
    z "You said they told you you could find the pale goblin here {i}today{/i}?"
    illya "Yes?"
    z "You told them which exact day you planned to go there?"
    illya "Yeah. Because they told me it can change from one day to the other."
    z "..."
    z "And these goblins..."
    z "Are they the ones that enter and leave the city everyday?"
    illya "Of course. The ones who live in the city wouldn't know all of th-"
    z "Fuck! Halt!"
    illya "What?! Why?!"
    z "They know-"
    #The two goblins are killed first with spears. 
    z "!!!"
    #Someone tries throwing a spear at illya thinking she's not important but Z catches it.
    z "Yumi! Centoria! Take her and run!"
    illya "Bu-"
    ymi "Fuck! He's right! Come on!" #Pulls illya
    illya "Wai-"
    #Ymi pumps into a big woman.
    ymi "..." #Backs off to see there's actually also a minotaur.
    ymi "What the fuck..." #Terrified.
    #Wants to plant her sword into the ground.
    #A magic chain is shown on her arm just before she hits the ground.
    #Her magic doesn't work.
    ymi "..."
    ymi "What?!"
    z "(She can't use magic?!)"
    #The big woman is swinging her axe at yumi
    ymi "Fuck! Get back!" #Pushes illya away to take the hit herself.
    ymi "..." #Getting ready to take it.
    # Transformed Z blocks the big woman with his sword.
    ymi "..."
    ymi "(He stopped it?!)"
    z "Get it together, Yumi."
    ymi "..."
    ymi "Sorry about that..."
    #Throws a smoke bomb on the floor.
    #The whole place is filled with smoke and by the time it clears she, centoria, and illya ran away.
    Character("Big woman") "After them!"
    #Goblins run after them.
    #Z teleports there and blocks the way.
    Character("Big woman") "Kill him!"
    #Goblins attack him.
    #They stop mid-way and are terrified by his face.
    #He absorbs them.
    Character("Big woman") "What the..."
    z "..."
    Character("Big woman") "Do you have a death wish, boy?"
    Character("Big woman") "Why do you risk your life for them? You're not even an elf."
    z "(She can tell I'm not an elf?)"
    z "..."
    z "(She looks almost half minotaur but she's actually quite intelligent)"
    z "(That's the minotaur that attacked me when I was with Torr and Candy in the woods. I can tell.)"
    z "(I thought it served Axius... Is he involved in the goblin-elf conflict somehow?)"
    z "I can ask the same of you."
    z "Why would you fight alongside goblins?"
    z "The minatour behind you..."
    z "He once tried to kill me."
    z "On Axius's orders."
    z "Are you working for him?"
    Character("Big woman") "..."
    Character("Big woman") "Minatours... Half-breeds... Goblins... Incubi... Does it really matter which we are and who we work with?"
    Character("Big woman") "The other races look at us like demons equally. Like vermin that should be eradicated."
    Character("Big woman") "I would've hoped the attack on the incubus city would've taught you as much?"
    z "(I guess she's some kind of a half breed...)"
    z "..."
    z "So you just... Kill them? That's your solution?"
    Character("Big woman") "It's a war, boy. Hundreds will die no matter what. I'd rather most of the dead be from them than from us."
    z "The princess-"
    Character("Big woman") "Enough talking. Move, boy. I need to catch the princess before she reaches the city gates."
    Character("Big woman") "More or I'll cut you to shreds."
    z "You think you could?"
    z "Go on, then. Cut me to shreds." #Looks scary.
    #A chain appears on his arm.
    z "?!" #Loses his magic.
    z "What the-"
    #Barely dodges an axe attack from her.
    z "..."
    z "(I can't use magic?!)"
    z "(Can I even beat all of these goblins and this monster without magic?!)"
    z "(Fuck...)"
    #The goblins are closing in on him.
    Character("Big woman") "Stand back. I'll handle him. You go after the princess."
    z "(Shit... I can't both stop the goblins and fight her.)" #Looks away from her at the goblins.
    Character("Big woman") "You sure you want to be looking away from me while we fight, boy?"
    z "..."
    z "(I have to finish her off quickly and follow the goblins and the other minatour.)"
    #They fight. Z is winning with difficulty.
    #She's physically crazy strong and when Z stops her axe she just punches him a few times.
    #While fighting, more goblins show up.
    z "(Fuck... Even if I can defeat her, am I gonna have enough strength to beat all of these goblins after?)"
    #Manages to punch her making her nose bleed.
    #She pauses.
    Character("Big woman") "..."
    Character("Big woman") "You're strong."
    Character("Big woman") "Change of plans."
    Character("Big woman") "Goblins! Chain him!"
    z "Wha-"
    #Magic chains appear on all of his limbs until he can't move anymore."
    z "Fuck..." #Looks at his chains.
    #Turns to the big woman. She's punches him in the face and fade out.

#19) Goblin camp:
    #Z wakes up in the dungeons.
    z "Ughhh..."
    "He's waking up..."
    z "..."
    #Sees it's two elves. A man and a pregnant woman.
    z "Who..."
    Character("Pregnant Woman") "Are you okay?"
    z "No... My head hurts..."
    z "..."
    z "Where am I?"
    Character("Man") "The goblin's dungeon."
    Character("Man") "They threw you in about an hour ago."
    z "..."
    z "I see..."
    Character("Man") "What's your name, friend?"
    z "[mc_name]."
    Character("Man") "[mc_name]?"
    Character("Man") "Quite an unusual name for an elf, isn't it?"
    Character("Sye") "I'm Sye. And this is my wife Helle."
    z "..."
    z "I'm not an elf."
    Character("Man") "You're not?"
    z "No..."
    z "I-"
    Character("Goblin girl") "You're up, huh?"
    Character("Goblin girl") "Are you hungry? Meals are supposed to be served at noon once a day, but I can get you something to eat since you weren't here at noon."
    Character("Goblin girl") "Or maybe you already ate before you were captured?"
    z "..."
    Character("Goblin girl") "Are you okay? You were hit pretty hard on your head..."
    z "Who are you?"
    Character("Goblin girl") "Dohkong. I'm responsible for the prisoners."
    z "You speak our language?"
    Dohkong "Yes. My parents worked for years in the elven city. They've been teaching me how to speak it since I was a child."
    Dohkong "And I've always gotten plenty of practice talking to the prisoners."
    z "..."
    z "Awfully cheerful for someone in your position."
    Dohkong "Ahahahah..."
    Dohkong "I know the prisoners have it hard. I don't see any reason to make their stay here any harsher."
    Dohkong "So? I gave you my name..."
    z "..."
    z "[mc_name]."
    Dohkong "Are you hungry, [mc_name]? As I said, I could get you something to eat."
    z "I'm fine... Thank you."
    Dohkong "How did you get captured, if I may ask?"
    z "..."
    z "I was escorting the princess... And some goblins and a minotaur being led by a huge woman ambushed us."
    Dohkong "Oh? And what happened to the princess?"
    z "She got away. At least I hope so."
    Dohkong "So you stayed behind to give her a chance to escape?"
    z "..."
    Dohkong "That's quite noble. Are you a royal guard?"
    z "(She's just making casual conversation...)"
    z "(I never thought I'd have such a normal conversation with a goblin...)"
    z "(Maybe the princess had a point about them?)"
    z "I can't very well reveal such information to the enemy, can I, Dohkong?"
    Dohkong "Ahahah... So I'm your enemy? That's sad to hear."
    z "You wouldn't say that the elves and the goblins are enemies?"
    Dohkong "Sadly, the realistic answer is probably yes, they are enemies."
    z "Sadly? The goblins are the ones who have been attacking and raiding the elven city!"
    Dohkong "Did I attack or raid anyone? For the record I very much disagree with doing that."
    Dohkong "Sadly... The pale goblin has been distant lately... Listening to her new advisor, who's been advising her to attack the elves every chance they get..."
    Dohkong "But it's not really up to me. Is it up to you that the goblins born for workers inside the elven city are given potions to transform into elves?"
    z "What?"
    Dohkong "..."
    Dohkong "I guess I can't expect you to know much about that? Doesn't affect you after all, does it?"
    z "..."
    Dohkong "..."
    Dohkong "Hey... You do live in the elven city, don't you?"
    z "..."
    Dohkong "You don't? Where are you from then?"
    Dohkong "What are you doing protecting the princess?"
    z "I won't say."
    Dohkong "..."
    Dohkong "Fine, fine."
    Dohkong "I don't know how you got to work for the elves. But look... They aren't the perfect pure creatures they claim to be."
    Dohkong "I know we the goblins are sadly the last ones to talk. I know goblins all around the continent commit all kinds of ugly deeds."
    Dohkong "But..."
    Dohkong "The elven city... The land where it's built belonged to the goblins long ago."
    Dohkong "It's been more than a century since the first elves drove the goblins out of those lands, of course..."
    z "..."
    Dohkong "I'm sorry... I know you suffered a bit of head trauma before you got here... The last thing you need is to be thinking about such a complicated conflict..."
    Character("Helle") "Dohkong... I have a little stomachache... Can you get me something for that?"
    Dohkong "Sure thing. Give me a minute."
    z "..."
    z "You're pregnant..."
    Character("Helle") "Yes. I'll be giving birth in two or three weeks."
    Character("Sye") "[mc_name]... Is it true you're a member of the royal guard?"
    z "No..."
    Character("Sye") "So were you lying when you said you were protecting the princess?"
    z "Also, no... It's complicated..."
    #Explains.
    Character("Sye") "So they didn't get the princess?"
    z "I can't be sure... But I don't think they did, no."
    Character("Helle") "That's a relief..."
    Character("Sye") "..."
    Character("Sye") "So you were requested to guard the princess by the crowned prince himself, right?"
    z "Yeah."
    Character("Sye") "So you must be a very capable warrior."
    z "I can handle myself."
    Character("Sye") "I can fight as well. Helle too. We're both very good sorcerers."
    Character("Sye") "Sadly the goblins have gotten very good at using magic sealing spells to stop us elves from using our superior magic."
    Character("Sye") "But... If you can fight without magic until we manage to break the seals and aid you, we stand a chance of escaping this place."
    z "..."
    z "How do you break the seal?"
    Character("Sye") "Isn't it obvious?"
    z "..."
    z "You kill the goblin who placed it..."
    Character("Sye") "Yes. That's the safest option. But getting out the range of their seal spell would also work."
    z "I see..."
    z "It's quite risky, wouldn't you say?"
    z "Your wife is pregnant here..."
    Character("Helle") "I..."
    Character("Helle") "We don't want our child to be born and grow up in captivity, [mc_name]..."
    Character("Helle") "I'd rather take the risk..."
    z "..."
    z "Alright..."
    z "Let's plan this tomorrow..."
    z "It's already too late to try to escape now... And we'll need some sleep if we're going to do something like this."
    Character("Helle") "..." (multiple=2)
    Character("Sye") "..." (multiple=2)
    Character("Sye") "So be it."
    #Z is sleeping.
    Character("Helle") "AAAAAAH!"
    z "?!"
    Character("Helle") "Fuck! Sye! It's..."
    Character("Helle") "The baby... It's coming..."
    Character("Sye") "Gods... No, no, no... It's too early..."
    Character("Sye") "What do I do, Helle?!"
    Character("Helle") "I don't know... Fuck... Help me, Sye..."
    Character("Helle") "[mc_name]... Help..."
    z "..."
    Character("Sye") "..."
    Character("Sye") "Dohkong!"
    Character("Sye") "Dohkong! Are you there?!"
    Dohkong "Guys... What's with all th-"
    Character("Sye") "Help! Please! It's Helle! She's..."
    Dohkong "..."
    Dohkong "Oh no..."
    Character("Sye") "Please Dohkong... Help us..."
    Dohkong "I..."
    Character("Sye") "Can you deliver a baby?"
    Dohkong "Goblin babies... Not elf babies..."
    Character("Sye") "It's the same! We're not different from the goblins! Please!"
    Dohkong "..."
    Dohkong "I..."
    Character("Sye") "Dohkong!"
    Dohkong "Fuck! Okay!"
    #Opens the door.
    Dohkong "Okay, Helle... Calm down... Breathe slowly, okay?"
    Dohkong "..."
    Dohkong "It'll be okay... Don't worry..."
    Character("Helle") "The baby... Is it-"
    Dohkong "The baby will be okay... I just need you to push."
    z "..."
    Dohkong "Come on, Helle... You can do this..."
    Character("Helle") "I can't... Ahhhhhhh! I..."
    Dohkong "You got this! Go on!"
    Character("Helle") "AHHHHH! AAAAHH!"
    "{i}Baby crying.{/i}?"
    z "..."
    Dohkong "..." #Crying a bit.
    Dohkong "Eheh..."
    Dohkong "Ehehehe... Look! Helle! It's a boy! Look!"
    Character("Helle") "..." #Takes the baby
    Dohkong "Look! Sy-"
    Character("Sye") "..." #Is gonna hit her on her head.
    #Z blocks him but Dohkong still gets knocked out.
    z "The fuck do you think you're doing?!"
    Character("Sye") "The gate is open! She was distracted! Now is our chance to escape!"
    z "..."
    z "You almost killed her..."
    z "She was only distracted because she was helping your wife deliver your fucking child."
    Character("Sye") "Yes... But it was the only way."
    Character("Sye") "She is the one holding the seals on our magic."
    Character("Sye") "We had no hope of escaping while our magic was sealed."
    z "I thought the goblins who placed the seal were holding our seals."
    Character("Sye") "Of course, they'll transfer them to her. Otherwise we would be out of range for their seals the second they leave the dungeons."
    Character("Sye") "It seems knocking her out did the trick though..." #Has magic.
    Character("Sye") "Can you stand?" #Helps his wife get up.
    Character("Sye") "We have to leave now."
    z "..."
    Dohkong "..." #Wakes up.
    #Sounds the alarm.	
    Character("Sye") "?!"
    Character("Sye") "Fuck! We have to leave."
    Character("Sye") "Come on, Helle! We have to move quickly!"
    Character("Helle") "I can't... My legs... They're too weak..."
    z "..."
    z "You two go. I'll hold them off."
    z "It'll take them a while to get through me. Maybe it'll give the two of you a chance to escape."
    Character("Sye") "..."
    Character("Sye") "Thank you, [mc_name]. We won't forget this."
    #They leave.
    #Goblins enter the dungeon. Z is facing them.
    #He's tied up and brought before the pale goblin.
    #The minotaurs and his sister are behind her.
    z "..."
    z "You're the pale goblin?"
    plgbln "..."
    if succubus_incountered == 1:
        nxi "Veka korak lo tek tem nok."
    else:
        Character("Succubus") "Veka korak lo tek tem nok."
    z "?"
    if succubus_incountered == 1:
        z "Nixie?!"
        nxi "Hello again, [mc_name]."
        z "What are you doing here..."
    else:
        z "Who the fuck..."
        Character("Succubus") "Hello, [mc_name]."
        nxi "I am Nixie. A succubus at the service of lord Axius."
        z "..."
        z "So Axius is involved in this after all."
    nxi "Lord Axius asked me to provide the goblins with counsel. That's all."
    z "..."
    plgbln "Vekat kor tek tem nok, var."
    nxi "She says yes. That's what the elves call her."
    z "Did you order that attack on the princess?"
    nxi "Tek korak tok lo rak tek rak?"
    plgbln "Var."
    nxi "Yes."
    z "..."
    z "I'm assuming you knew we were coming because the information was leaked to you via the goblins working in the elven city, no?"
    nxi "Korak tek morak vekat lorkak ar mora kora tek lo nokvat kor lo vekat tora, nar?"
    plgbln "Lorat tokar vekat mora, korak."
    nxi "She says the traitors brought us the information."
    z "Traitors?"
    plgbln "Lorat! Nokta vekat kor lo vekat tora!"
    nxi "They have chosen to work for the enemy."
    z "Thinking the elves are your enemies will bring you nowhere."
    z "You must've also known from the goblins working in the city that the princess was trying to bring you peace."
    z "She'd let you all in the city and name you citizens. How's that not a good thing? How's that not better than killing each other?!"
    nxi "Veka korak tek vekat tora lora morat ar lora rakar vekat nokta lo lor vetor lo vekat tora."
    nxi "Veka korak lo tek kora ar rakar vekta."
    plgbln "Veka tek kor lora lo nar mor mora lor lorik ar lorek."
    nxi "..."
    z "What's she saying?"
    nxi "She says you're a fool who doesn't understand loyalty or dignity."
    plgbln "Nokvat lo vekat tora kor lo lorak lo kora rak lo kor lo vekat ar nar lora rakar."
    nxi "She says the goblins in the city work at the bottom of the food chain in the jobs that the elves aren't willing to take."
    plgbln "Nokvat nar korak lorak lo vekat lo tek lor."
    nxi "The goblins and the elves will never be equal in their eyes."
    z "..."
    z "So... What exactly is your plan to fix that, pale goblin?"
    nxi "Veka korak lo tek lork tek."
    plgbln "Vek korak tokar veqat nokta! Korak lok tek!"
    z "..."
    z "What did she say?"
    nxi "She says she'll kill all of them."
    nxi "Look... I know you think that just because I work for lord Axius, I must be evil."
    nxi "And I will admit... I have been plenty evil."
    nxi "But the goblins are the ones being oppressed."
    nxi "Even if the princess follows through with her promise to make the goblins citizens in the elven city. The goblins will always remain worth less than elves."
    nxi "Look at how the goblins are treated in the city. They only get the dirty and dangerous jobs that no elf wants to take."
    nxi "And believe me... I'm doing my best to avoid an all out war that wipes out the goblins or the elves..."
    "Nar korik vekat lorik lo tek! Rakar tek lo korak tora!"
    z "..."
    #The goblins start dragging him away.
    z "What are they doing?"
    nxi "They're taking you to another dungeon."
    z "..."
    nxi "..." #Maintains eye contact while he's dragged away.

#20) Dungeon visit:	
    #Z is put in another cell where he's suspended from all his limbs.
    z "..."
    z "(Fuck...)"
    z "(I can't use magic...)"
    z "(I don't think there's a way for me to escape...)"
    z "Hello!"
    z "Anyone there?!"
    z "..."
    z "(Am I just going to starve to death here...)"
    #Puts his head down.
    #Sound.
    z "?"
    #The door opens.
    nxi "How is it hanging?"
    z "Very funny..."
    nxi "I talked to the pale goblin. She'll have you transferred to the other dungeon you were in next week."
    nxi "She said she wants to keep you here for a bit as punishment for trying to escape."
    nxi "She originally wanted to keep you here forever."
    nxi "I'll talk to her again tomorrow to have you out of here sooner."
    z "..."
    z "Why would you help me exactly?"
    nxi "You're an incubus. You think I'll let one of the few survivors of my race rot in a goblin dungeon in the middle of nowhere?"
    z "..."
    z "What exactly are you trying to do here, Nixie?"
    nxi "Help the goblins beat the elves."
    z "Why?"
    nxi "Lord Axius's orders for one."
    nxi "But..."
    nxi "The goblins are not really very different from us succubi and incubi, are they?"
    z "..."
    nxi "You and I don't need to be enemies, [mc_name]..."
    nxi "I've heard quite a bit about you, you know."
    nxi "If what I've heard is true... I wouldn't even know how to kill you."
    nxi "And I don't think I want to kill you, [mc_name]."
    nxi "What I want... Most of all, it is for us to be allies."
    z "..."
    nxi "You know..."
    nxi "Irena seems to really like you."
    nxi "She hides it underneath all that bad girl attitude, but I know Irena too well for any of that to fool me."
    nxi "Aside from lord Axius, the three of us might as well be all that remains of our race, [mc_name]."
    nxi "Should we really kill each other off?"
    z "..."
    z "Why are you saying all of that exactly?"
    z "You speak of us being allies and yet here I am hanging from all my limbs."
    nxi "I'd think if you wanted to talk to me while you don't trust me yet, you might do the same."
    nxi "Especially if I were strong enough to kill you without breaking a sweat."
    z "..."
    pause(1)
    menu:
        "Tell her you're not going to kill her.":
            z "..."
            z "I'm not going to kill you, Nixie."
            nxi "..."
            $ nxi_trst += 2
            nxi "How can I trust anything you say, [mc_name]?"
            nxi "I would love to trust you, I promise..."
        "Don't promise anything.":
            z "..."
            nxi "Yeah... I thought as much..."
    nxi "Look..."
    nxi "The goblins have a lot in common with us..."
    nxi "They also suffered a great injustice at the hands of these elves."
    z "Does that justify killing innocent elves?"
    nxi "Does it matter if it justifies it?"
    nxi "That's the only way they can hurt the elves, isn't it?"
    nxi "I'm pretty sure that's all the goblins care about."
    nxi "Plus, do you actually think in a war of a goblin army against the elven army the goblins stood a chance until now?"
    z "Until now?"
    nxi "..."
    z "Wait..."
    z "You don't mean..."
    z "You want my help?"
    nxi "I don't want it..."
    nxi "I need it."
    nxi "A minotaur and a demi-god fighting with the goblins, and we might start looking like a winning side."
    nxi "The elves haven't had a war in centuries."
    nxi "Their warriors are not seasoned. Their army is not disciplined. Not a single elven soldier today has been within a mile of a battle."
    nxi "The pale goblin has been pushing for an all out attack for weeks now."
    nxi "I've convinced her to wait for the right time. And she's listening for now, but not for long."
    nxi "I told you. I don't want to massacre any of the two sides. But if we can overwhelm them quickly enough, the death toll will be minimised."
    z "You're going to attack them..."
    nxi "Eventually, yes. With or without you, I'm afraid."
    z "So if I say no to joining you, you-"
    nxi "I told you. I don't want to kill you."
    nxi "I'll just keep you here. If you'd help the elves, that's a problem for us."
    z "My friends are still in the elven city."
    nxi "..."
    nxi "I trust you know I can't do anything about that... If I send them a warning, the elves will know we're coming. And surprise on our side is something we can't throw away."
    z "..."
    nxi "I'll let you sleep on it."
    nxi "I want an answer from you soon, [mc_name]."
    z "..."

#21) Dohkong visit:	
    #Z dreams of being chained up like he is but in black void.
    #He is also naked.
    #A figure is approaching him.
    z "..."
    z "Who's there?"
    z "..."
    z "Athena?"
    #It's auge.
    z "Who..."
    z "..."
    z "I've seen you before..."
    z "In my dreams..."
    z "Who are you?"
    Character("????") "..."
    z "Are you a sleep nymph? Are you the one influencing my dreams?"
    Character("????") "..."
    z "..."
    z "Have you come to just stare at me naked?"
    z "Wel-"
    Character("????") "Tsk. Tsk. Tsk..."
    Character("????") "Quite good at putting yourself in situations like these, aren't you..."
    #Gets really close to him.
    Character("????") "You have lots to do for me..."
    Character("????") "I can't have you rotting away in a place like this..."
    Character("????") "Wouldn't you agree?"
    #It's Seria behind her.
    z "Seira?"
    s "[mc_name]..."
    #Z wakes up.
    #It's morning.
    Dohkong "..." #She's bringing him food.
    z "..."
    z "Dohkong..."
    z "Are you okay?"
    Dohkong "Yeah... It could've been much worse..."
    Dohkong "He would've killed me..."
    Dohkong "..."
    Dohkong "You stopped him didn't you?"
    z "Yeah..."
    Dohkong "Why?"
    Dohkong "Your chances of escaping would've been better if you let him finish the job."
    z "I'm not a monster Dohkong."
    Dohkong "Even if it meant you being instead of running free?"
    z "You guys can't hold me forever."
    Dohkong "..."
    Dohkong "I had hoped that Herra and Sye would've come to see me as a friend..."
    z "..."
    z "I'm sorry..."
    Dohkong "Say..."
    Dohkong "When we first met you said we were enemies, you and me, didn't you?"
    Dohkong "Is there anything I can do to make you change your mind?"
    z "..."
    z "I..."
    z "I don't think that you and I are enemies, Dohkong..."
    z "I was assigned to protect the princess from the goblins who almost killed her. So the goblins were my enemies."
    z "But I have nothing against you personally."
    z "I actually like you. That's why I saved your life, remember?"
    Dohkong "..."
    Dohkong "I see..."
    Dohkong "..."
    Dohkong "My instructions were to only free one of your hands to you can eat and only after leaving your cell."
    Dohkong "..."
    Dohkong "But..."
    #Frees all his limbs.
    z "..."
    Dohkong "I can't let the man who saved my life struggle through eating his breakfast, can I?"
    z "Thanks..."
    #Sits down and eats.
    Dohkong "I'm sorry... I know we don't cook great food..."
    z "No, no. Don't worry about it... I've had worse..."
    z "What am I eating exactly?"
    Dohkong "How do you call that creature in your language..."
    Dohkong "..."
    Dohkong "Skeever! That's it!"
    Dohkong "It's skeever stew basically..."
    z "..." #Stops eating.
    #Puts the bowl down.
    z "I see..."
    Dohkong "So will you tell me now what you're doing here?"
    Dohkong "Nixie said you're a ninja. Is it true?"
    z "Yeah."
    Dohkong "Why would you protect the princess?"
    z "I guess there's no point in not telling you... Nixie probably knows everything anyway."
    z "I was hired to protect her during her birth week."
    Dohkong "Why? Doesn't she have the royal guard for that?"
    z "The princess asked for us instead of the royal guard because she wanted to go against her father's wishes by bringing a peace agreement to the goblins."
    z "And the royal guard would've reported her plan to the crowned prince."
    Dohkong "Oh..."
    Dohkong "She really wanted to make us citizens?"
    z "Yeah..."
    Dohkong "I see..."
    z "Would you like that?"
    Dohkong "..."
    Dohkong "I don't..."
    Dohkong "No... I don't think so..."
    z "How come?"
    Dohkong "I actually do like it here..."
    Dohkong "And I don't honestly think we'll ever be treated equally in there..."
    Dohkong "I've lived in the city for years... I know the way elves look at me every time I walk around in their streets..."
    z "..."
    z "I see..."
    Dohkong "But I guess there are also elves like you..."
    Dohkong "And like Illya..."
    z "..."
    z "I'm not actually an elf, Dohkong."
    Dohkong "..."
    Dohkong "Eh?!"
    z "I'm an incubus."
    z "Same as Nixie. But, well... Male."
    Dohkong "..."
    Dohkong "Do you ever have a hard time because of it?"
    Dohkong "Being who you are?"
    z "Well, maybe a bit..."
    z "There was this one woman in the ninja village who was wary of me for a while."
    z "Ultimately though, she warmed up to me, I guess."
    Dohkong "..."
    Dohkong "Do you think that would happen if the princess's plan succeeds?"
    z "Maybe..."
    z "I can't say for sure..."
    Dohkong "..."

#22) Big woman visit:
    #Skip to him sleeping with no chains cuz Dohkong doesn't chain him anymore.
    #Woken up by the Big woman.
    z "?!"
    Character("Big woman") "No chains, huh..."
    Character("Minatour") "Dohkong is such a soft little girl."
    z "..."
    z "What do you want?"
    Character("Big woman") "You didn't get any brain damage from my punch, I hope?"
    z "Not that I've noticed."
    Character("Big woman") "You were too strong for me to hold back. I didn't think anything less than my full strength would knock you out."
    z "..."
    Character("Big woman") "So... No hard feeling?" #Wants to shake his hand.
    z "..."
    pause(1)
    menu:
        "Shake her hand.":
            z "..."
            Character("Big woman") "That's a good grip you have..."
        "Refuse.":
            Character("Big woman") "You're the serious type, I can tell..."
            Character("Big woman") "Fine..." #Takes her hand back.
    Character("Big woman") "It's been while since I've faced a man who could stand his ground againts me, kid."
    Character("Big woman") "You don't look all that big maybe, but you know how to fight, huh..."
    z "I was taught by the best."
    Character("Big woman") "I see..."
    z "The minatour doesn't seem as talkative as you..."
    z "For some reason you have a similar vibe to him..."
    z "So what exactly are you? Just naturally big? Or are you something else?"
    Character("Big woman") "..."
    Character("Big woman") "He's my little brother."
    z "..."
    Character("Big woman") "Half brother."
    Character("Big woman") "Guess it's true what they say that the womb remembers."
    Character("Big woman") "You inherit even a thing or two even from your parents previous partners."
    z "Your father wasn't a minatour? Is that what you're saying?"
    Character("Big woman") "Nah."
    Character("Big woman") "Just a lad from where my mother lived. Sold bread on a wagon."
    Character("Big woman") "Died a week after I was born. Plague took him, according to my mom at least..."
    Character("Big woman") "But he wasn't big."
    Character("Big woman") "I got that from my brother somehow. Or his father, I guess..."
    z "Your brother's father, huh..."
    z "He was-"
    Character("Big woman") "A minatour. Yup."
    z "..."
    z "(I guess Anabelle and Yumi also somehow inherited their sun powers from Helios somehow, even though he wasn't their father...)"
    z "..."
    z "What's your name?"
    jillia "Jillia."
    z "I'm-"
    jillia "We all know exactly who you are, [mc_name]..."
    z "..."
    z "And your brother... He..."
    jillia "He was too weak at birth... My mother took him to the market and wanted to sell him as meat."
    jillia "Then came a winged big man with two horns."
    z "..."
    z "Axius?"
    jillia "Aye."
    jillia "He offered to buy him."
    jillia "Alive."
    jillia "Took him away as I watched behind my mother's leg."
    jillia "Then he stopped. Turned around and looked me right in the eye."
    jillia "Then said he'd buy me for twice what he paid for my brother."
    jillia "I didn't even think my mother would consider it."
    jillia "Then she asked for three times as much."
    jillia "He nodded."
    z "..."
    jillia "He shot my brother with half a dozen potions."
    jillia "So he turned to what he is now."
    jillia "But he lived."
    jillia "Can't speak though. And as sharp as a butter knife, he is."
    z "..."
    z "So you are a slave?"
    jillia "You can call it that..."
    jillia "But if I had to a say in it, I'd still choose lord Axius."
    z "Why?"
    jillia "Because I have a place to belong to."
    jillia "It's home."
    jillia "I wouldn't want to be a stray."
    jillia "And my brother wouldn't survive without his potions."
    jillia "We need Axius more than he needs us."
    z "..."
    jillia "And you?"
    jillia "Why did you choose to fight for the ninja village?"
    jillia "Do you agree with every choice they make?"
    jillia "Do you have a say in what they do and when and why they do it?"
    jillia "Or are you there just because it's home?"
    z "..."
    jillia "Did they cut your tongue out, boy?"
    z "I..."
    jillia "You?" #Get closer.
    jillia "Speak up, boy!" #Gets very close.
    z "I wouldn't..."
    jillia "Do you need to whisper it in my ear like lovers?" #Gets close enough for him to whisper.
    z "I wouldn't move closer to my prisoner so carelessly if I were you."
    #Trips her over and gets on top of her.
    jillia "?!"
    jillia "You..."
    #Chain locks.
    jillia "..." #notices her hand has been chained to the wall.
    jillia "Ughhhh!" #Pull the chain really hard.
    z "You won't be able to br-" #He's next to the door.
    #Breaks it.
    z "?!"
    z "What the..."
    jillia "That was a close one..."
    jillia "To think you were able to push me down like that..."
    #Walks up to him. The door is within her reach.
    z "..."
    z "(Fuck... She just broke that chain like it was nothing... There's no way I can beat her...)"
    #Closes the door.
    #Throws the key outside of the dungeon.
    z "?!"
    jillia "{i}Heavily breathing.{/i}"
    z "..."
    z "(Is she...)"
    #Looks horny af.
    z "(Fuck me...)"
    z "You..."
    #Strips.
    menu:
        "Kiss her.": #this is gonna be femdom #fucklimit
            jillia "Hmmff~"
            #jillia pushes z over
            z "Agh-"
            jillia "Awwww. Look at you, so cute down there."
            #jillia undresses z
            jillia "Oh wow. You will do nicely."
            #jillia sits over z's face - facing away from his dick
            z "(Oh Gods... She's already so wet)"
            jillia "Show me what you can do with your tongue big boy."
            #jillia sits down fully - z starts eating her out
            jillia "Haaaa~~ I can tell you've had practice."
            #z grabs jillia's ass
            jillia "Ahnn~ Getting a bit bold cutie... You have to remember you aren't in charge here."
            z "Hmmm?"
            #jillia grabs z's hands - pins them above his head
            jillia "Let's see if we can find something to hold you there so I don't have to do this the whole time."
            #jillia looks around and sees some rope on the ground
            z "(What is she doing?)"
            jillia "Oh this will do perfectly... Hmnnn~" #picks up the rope and starts tying z's hands up
            #z opens his eyes and looks up at jillia then at his hands
            z "HMMMF?!"
            jillia "Oh do you have something to say? That's too bad... Haaaa~"
            #jillia finishes tying z's hands
            jillia "Maybe I'll let you speak after I cum."
            z "(Oh Gods... There's nothing I can control here...)"
            #jillia looks at z's dick
            jillia "You're so hard for me... Looking forward to part 2 of this?"
            z "MMMHMM!"
            jillia "Well you better get ready becau- HAAAA~ because I'm gonna cum!"
            jillia "OH GODS!"
            #jillia cums and gets up
            z "Wow... That was... Amazing..."
            jillia "Agreed cutie... I think it's time for your reward."
            #jillia hovers over z's dick
            jillia "You did well before sweetie but do you really deserve this?"
            z "Yes! I do!"
            jillia "Ah ah... Ask nicely dear."
            z "Please Jillia! Please sit down!"
            jillia "Well, since you asked so nicely"
            #jillia sits on z's dick
            z "OH... You're so tight!"
            jillia "Oh Gods~ You're hitting my womb!"
            #jillia starts riding
            z "Oh DAMN! You feel- Ahhh~ You feel amazing!"
            #jillia starts riding harder
            jillia "HAAAA~ I'M GOING TO CUM AGAIN!"
            z "OH GODS! ME TOO!"
            #they both cum together
            jillia "AHHHNN~~"
            z "Haaaa~~ That was fucking great!"
            jillia "I agree cutie. But we're not done yet..."
            z "Huh?"
            #jillia starts riding again
            z "Ahhhhn~~"
            z "Wait! I'm not ready again yet!"
            jillia "That's not for you to decide cutie..."
            z "Hmmmmnn~ Well I'm not going to last long then!"
            jillia "Ahhhh~ That's fine cutie... Me Nei- HAAAAA~ ME NEITHER!"
            #both cum - still inside
            z "OH GODS!" (Multiple=2)
            jillia "AHHHNN~"(Multiple=2)
            z "Oh my Gods. I don't think I can go anymore!"
            jillia "That's fine cutie..."
            jillia "Thank you for that. It was better than I ever could've imagined."
            #jillia gets up, gets dressed and unties z's hands - shackles him back up
        "Back off.":
            $ dummy += 2
            z "I'm sorry... We can't do this if I can't trust you."
            jillia "Shame. I guess I'll see you again soon."
            #jillia shackles him back up
    z "Did you really have to shackle me again?"
    jillia "That is what's necessary. Sleep well, [mc_name]. We'll see you again very soon."
    z "Goodnight Jillia."

#24) Gabbie gets kidnapped:
    #Gabbie and Venus are gathering ingerdients from the woods nearby.
    gbrla "Why not?"
    vns "Well, Seira literally trained him, didn't she?"
    vns "He's a quick learner, granted. But Seira has years of experience."
    gbrla "But he's a demi-god."
    vns "So is Seira."
    gbrla "But..."
    gbrla "Seira lost against the other demigod... Annabelle's brother."
    vns "Sirius?"
    vns "Everyone loses against Sirius, Gabbie."
    vns "And [mc_name] lost against him too, didn't he?"
    gbrla "Well, yes... But the fight lasted longer..."
    gbrla "And he got injured."
    vns "Not really enough to put [mc_name] above Seira."
    vns "Every fight has its circumstances. Every fighter is more likely to win or lose against a certain type of fighting too."
    vns "If I beat an opponent whom you lost against, that doesn't always mean that I'm stronger than you."
    gbrla "..."
    gbrla "Is that how it works?"
    vns "Yep."
    #Zoom in to Venus.
    vns "We need some mountain dale too, don't we?"
    #Turns away from gabbie.
    #Sound.
    vns "?!"
    vns "Gabbi-"
    #Nari is carrying an unconscious gabbie.
    vns "What the-"
    #Charges with lightning.
    #Nari seems worried.
    #Alura touches her head from behind.
    alura "Sleep."
    vns "..."
    #Falls on the floor.
    nari "That's not the Keres, is it?"
    alura "Nope. Both have white-ish hair, but that's not her."
    alura "Why do you ask?"
    nari "For a second there, she felt quite dangerous..."
    nari "..."
    nari "It seems we underestimated them."
    alura "..."
    nari "..." #Looks at alura.
    nari "Let's go."
    #Nari and Alura take gabbie and leave the unconscious venus there.


    scene black with fade
    stop music fadeout 1.0
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop sound fadeout 1.0
    pause(1.0)

    $ MainMenu(confirm=False)()

#NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES|NOTES


    #They specifically asked for Z after hearing about his exploits.
    #They also ask for Centoria.
    #Yumi, Zycris, and Centoria are sent.

    #The Celebration with for the princess's birthday include several tournoments in which Z competes.
    #When they get to the elf village, the tournoments have already begun.
    #In the fencing tourny (no magic is allowed) Z is asked to compete by the princess.
    #Vollstahl, the king's personal gaurd, wins againts Z. Vollstahl is a short man, who always wears an full armour and a helmet covering all of his body. (He's actually a goblin who betrays the elves later on and joins axius).
    #The winner is decided by who stops just before hitting their opponent. Vollstahl is very respectful towards Z after winning.
    #Before beating Z Vollstahl totally destroys Yumi.
    #More games where the princess competes with Z giving them more time to build a friendship.	
    #Many goblins work in the elf city in low paying jobs that the elves wouldn't do.
    #Elves have strong magic that they always use.

    #When Z leaves the city, he sees goblins going in at the gates having their work permits checked.
    #Z's party is ambushed by a bunch of goblins and two minatours, the two goblins are shockingly killed immediately. He manages to draw the goblins away from the princess and tells them to run back to the city. Z is captured though using magic sealing spells by the goblins.

    #In the dungeon, he meets elves being improsined there (one woman is pregnant with her husband).
    #The pregnant elf tells Z she's about to give birth and she doesn't want her child to grow up in captivity.
    #The guard (a goblin) is nice to the prisoners. Z is surprised she speaks his language. She says her parents worked for years in the elf city.
    #Z takes the chance to talk to her, she tells him the place where the elves built their city belonged to the goblins.
    #They were driven away according to her and many of them died while fighting the elves. Z tells her it's still not right to attack the elves killing innocents. She says she didn't make that decision.
    #She says the pale goblin has a new advisor who advised him to do the attacks.
    #Z wakes up to the elf woman giving birth. She begs the gaurd to help her deliver the baby. The gaurd hesitantly accepts. The gaurd helps her, the husband tries to kill the gaurd while she's occupied with the birth.
    #Z stops him but the gaurd is knocked out.
    #Z asks him wtf he just tried to do, the husband says they have to escape and it was the only way.
    #The guard wakes up and sounds the alarm. They are surrouned by goblins with no magic, Z fights off the goblins with his bare hands while the others escape.

    #Z is taken directly before the pale goblin. On his side is Nixie.
    #The minatour from chapter 3 and a new minatour woman is also there.
    #Z notices the old minatour.
    #Nixie translates for him.
    #Nixie tells him that even though she works for axius and she does plenty of evil. The goblins are in the right here.
    #Z tells the pale goblin that many goblins work in the elven city and have good jobs.
    #The pale goblin calls them traitors. And says they only get the jobs that are at the foot of the economy anyway.
    #Z the pale goblin what his plan is. The pale goblin tells him he'll kill all the elves.

    #&&&&&&&&MORE DETAILS&&&&&&&&&&&&
    #Nixie visits, asking him what he plans to do now.
    #She says she doesn't trust him yet, so that's why she can't risk him escaping to use his magic.
    #She says she knows from the others that she can't kill him normally cuz he'll regenerate. And she says she doesn't want to kill him.

#Dev log:
#We'll be meeting some new characters that will probably stick with us for a while. The conflict between the now more powerful Axius & the ninja village will start to to spark.
#start of next chapter Seira breaks Z out:
    #nxi "[mc_name], you kno-..."
    #s "(Huh? Who?)"
    #z "You speak of us being all-"
    #s "([mc_name]? What's going on?)"
    #nxi "I-"
    #nxi "... Goblins..."
    #z "... Equals-"
    #s "(What are they talking about?)"
    #nxi "... With or without- ..."
    #nxi "... Kill you ..."
    #s "(NO! NO WAIT!)"
    #seira wakes up - sweating (YOU DON'T HAVE TO TURN THE SETTING OFF !)
    #s "{size=+20}[mc_name!u]!{/size}"
    #seira dressed and leaves through bedroom door
    #z "..."
    #s "{size=+20}[mc_name!u]!{/size}"
    #z "{size=+20}SEIRA???{/size}"
    #s "Oh Gods I'm so happy you're alive!"
    #z "What do you mean?"
    #s "I saw you and the succubus, Nixie? She was talking about how she was going to kill you?"
    #z "Huh? Nixie never said she would kill me?"
    #z "Wait she said about not wanting to kill me? Is that what you're talking about?"
        #&&&&&&&&MORE DETAILS&&&&&&&&&&&&
    #Seira, who saw Z imprisoned in the dream, rushes to save him.
    #Seira leads the others to be able to free Zycris.

    #In the battle, Vollstahl and the sorceress desert and are not there to protect the king.
    #If Z sides with the goblins, the princess and some other elves seek refuge in the western elf village.
    #Either confront Pale goblin or Crowned prince depending on Z's choice.
    #If confronts crowned prince, Vollstahl and the sorceress are noticibly nowhere to be found.

    #seira scene for a later chapter:
    #scene v232
        #z "..."
        #scene v233
        #Their faces are very close.
        #Z goes for a kiss.
        #s "Hmmm~..."
        #scene v234
        #scene v235
        #s "Hmmmmm~"
        #if calling_s_mom == 1:
            #z "What should I do with you, Mommy?"
            #s "Why don't you come down here and find out sweetie?"
            #z goes down and starts undressing seira whilst kissing her
            #s "Mmmmf~"
            #z "Have I ever told you how nice your tits are Mommy?" #playing with them aggressively
            #s "Hnn~ You haven't baby, but-"
            #s "AHN!"
            #s "-With how hard you're playing with them now... I think I can tell."
            #z "I need to try them. Please Mommy, lie down."
            #seira lies down, holding her tits together
            #s "Like this baby?"
            #z "That's perfect Mommy. You're perfect."
            #z starts fucking seira's tits
            #z "Fuck they're so soft."
            #s "Yeah baby? You can use them as you want. Hmmm~"
            #z "Hnnng~"
            #s "You feeling good? You can finish whenever you want..."
            #z cums over seira's face and tits
            #z "AHHHNN!"
            #s "Wow... I can't believe how much you let out... Hopefully you've got some more in you?"
            #menu:
                #"For you? I could go forever.":
                    #s "Then choose a hole..."
                    #z "You mean?"
                    #s "That's right baby, any hole."
                    #z "Then..."
                    #menu:
                        #"I want your ass.":
                            #s "Oh you wanna be my first?"
                            #z "Your first? You mean?"
                            #s "Yes. Nobody has been up there. Ever."
                            #z "Well then bend over Mommy, let's get you prepared shall we..."
                            #seira bends over - face down ass up that's the way she likes to fuck
                            #z starts eating seira's ass
                            #s "Hmmmnnn~"
                            #s "Ahhhhnnn~ Oh Gods! I've never felt anything like this!"
                            #z "Mmm? Mmmf?"
                            #s "Hnnnmmm~ Honey! I think I'm going to cum!"
                            #s "AHHNN!"
                            #s "Oh Gods! I never thought that could feel so good!"
                            #z "Are you ready now?"
                            #seira wiggling her ass
                            #s "Come on baby... Please fuck Mommy's ass..."
                            #z "With pleasure."
                            #z slowly inserts himself into seira's ass
                            #s "Holy shit! I forgot how big you are... Please go slowly."
                            #z "Gods that feels amazing Mommy."
                            #s "AHhnn~ I agree honey!"                        
        #else:
            #z "What should I do with you, Seira?"
            #s "Why don't you come down here and find out sweetie?"
        #z goes down and starts undressing seira whilst kissing her
            #s "Mmmmf~"
            #z "Have I ever told you how nice your tits are Seira?"
        #I'm here R <-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
        #Aggressively plays with her boobs while doing so.
        #Throws her on all four and rams her, has a choice to try anal.
        #Z warns S that he's gonna be rough, she says she'd like that.
    #else:
        #scene v184
        #$ dummy += 1
        #scene v185
        #Skip to him sleeping on his own in the darkness.