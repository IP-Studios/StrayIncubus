label characters:
        call hide_all from _call_hide_all
        hide screen button_1
        scene wood
        show screen button_next_page
        show screen button_g
        show screen button_candy
        show label10 "{color=#d93675}Candy{/color}"
        show screen button_gabriella
        show label2 "{color=#e3661e}Gabriella{/color}"
        show screen button_seira
        show label1 "{color=#d15adb}Seira{/color}"
        show screen button_stephanie
        show label4 "{color=#e3d12d}Stephanie{/color}"
        show screen button_yumi
        show label3 "{color=#0091cf}Yumi{/color}"
        show screen button_tamara
        show label6 "{color=#de1b1b}Tamara{/color}"
        show screen button_hailey
        show label7 "{color=#6ebaf5}Hailey{/color}"
        show screen button_anabelle
        show label5 "{color=#c9f7ff}Anabelle{/color}"
        call screen button_2
        return
label characters_2:
        call hide_all from _call_hide_all_1
        scene wood
        show screen button_2
        show screen button_extra_char
        show screen button_venus
        show label2 "{color=#db4242}Venus{/color}"
        show screen button_torr
        show label1 "{color=#2ad14f}Torr{/color}"
        show screen button_centoria
        show label3 "{color=#399fed}Centoria{/color}"
        show screen button_jenny
        show label11 "{color=#f76e11}Jeniffer{/color}"
        if succubus_incountered >= 1:
            show screen button_nixie
            show label7 "{color=#a244c7}Nixie{/color}"
        else:
            show screen button_nixie_u
        show screen button_irena
        show label6 "{color=#a6a1f7}Irena{/color}"
        show screen button_fransisca
        show label9 "{color=#f77440}Fransisca{/color}"
        if invited_misty >= 1:
            show screen button_misty
            show label10 "{color=#d9d9d9}Misty{/color}"
        else:
            show screen button_misty_u
        call screen button_previous_page
        return
label stats_candy:
    call hide_all from _call_hide_all_2
    scene stats2
    show name_text Text("{color=#8f254e}Candy{/color}", size=100)
    show species "Species"
    show species_value "Nymph"
    show sex "Sex"
    show sex_value "Female"
    show age "Age"
    show age_value "19"
    show height1 "Height"
    show height1_value "153cm"
    show weight "Weight"
    show weight_value "46kg"
    show rank "Rank"
    show rank_value "Purple Belt"
    show trust "Trust"
    show trust_value "[cndy_trst]"
    show affection "Affection"
    show affection_value "[cndy_aff]"
    show respect "Respect"
    show respect_value "[cndy_res]"
    show lust "Lust"
    show lust_value "[cndy_lst]"
    show screen button_candy_next
    show screen button_candy_back
    call screen button_2
    jump characters
label stats_torr:
    call hide_all from _call_hide_all_3
    scene stats1
    show name_text Text("{color=#1a702d}Torr{/color}", size=100)
    show species "Species"
    show species_value "Elf"
    show sex "Sex"
    show sex_value "Female"
    show age "Age"
    show age_value "19"
    show height1 "Height"
    show height1_value "153cm"
    show weight "Weight"
    show weight_value "47kg"
    show rank "Rank"
    if tr_red_belt == 0:
        show rank_value "Purple Belt"
    else:
        show rank_value "Red Belt"
    show trust "Trust"
    show trust_value "[tr_trst]"
    show affection "Affection"
    show affection_value "[tr_aff]"
    show respect "Respect"
    show respect_value "[tr_res]"
    show lust "Lust"
    show lust_value "[tr_lst]"
    show screen button_torr_next
    show screen button_torr_back
    call screen button_2
    jump characters_2
label stats_centoria:
    call hide_all from _call_hide_all_4
    scene stats6
    show name_text Text("{color=#3286c7}Centoria{/color}", size=100)
    show species "Species"
    show species_value "Elf"
    show sex "Sex"
    show sex_value "Female"
    show age "Age"
    show age_value "21"
    show height1 "Height"
    show height1_value "163cm"
    show weight "Weight"
    show weight_value "51kg"
    show rank "Rank"
    show rank_value "Purple Belt"
    show trust "Trust"
    show trust_value "[cnt_trst]"
    show affection "Affection"
    show affection_value "[cnt_aff]"
    show respect "Respect"
    show respect_value "[cnt_res]"
    show lust "Lust"
    show lust_value "[cnt_lst]"
    show screen button_centoria_next
    show screen button_centoria_back
    call screen button_2
    jump characters_2
label stats_gabriella:
    call hide_all from _call_hide_all_5
    scene stats10
    show name_text Text("{color=#964211}Gabriella{/color}", size=100)
    show species "Species"
    show species_value "Human"
    show sex "Sex"
    show sex_value "Female"
    show age "Age"
    show age_value "19"
    show height1 "Height"
    show height1_value "150cm"
    show weight "Weight"
    show weight_value "44kg"
    show rank "Rank"
    show rank_value "Purple Belt"
    show trust "Trust"
    show trust_value "[gbrla_trst]"
    show affection "Affection"
    show affection_value "[gbrla_aff]"
    show respect "Respect"
    show respect_value "[gbrla_res]"
    show lust "Lust"
    show lust_value "[gbrla_lst]"
    show screen button_gabriella_next
    show screen button_gabriella_back
    call screen button_2
    jump characters
label stats_seira:
    call hide_all from _call_hide_all_6
    scene stats11
    show name_text Text("{color=#d15adb}Seira{/color}", size=100)
    show species "Species"
    show species_value "Demi-god"
    show sex "Sex"
    show sex_value "Female"
    show age "Age"
    show age_value "42"
    show height1 "Height"
    show height1_value "182cm"
    show weight "Weight"
    show weight_value "71kg"
    show rank "Rank"
    show rank_value "Keres"
    show trust "Trust"
    show trust_value "[s_trst]"
    show affection "Affection"
    show affection_value "[s_aff]"
    show respect "Respect"
    show respect_value "[s_res]"
    show lust "Lust"
    show lust_value "[s_lst]"
    show screen button_seira_next
    call screen button_2
    jump characters
label stats_stephanie:
    call hide_all from _call_hide_all_7
    scene stats4
    show name_text Text("{color=#e3d12d}Stephanie{/color}", size=100)
    show species "Species"
    show species_value "Human"
    show sex "Sex"
    show sex_value "Female"
    show age "Age"
    show age_value "24"
    show height1 "Height"
    show height1_value "157cm"
    show weight "Weight"
    show weight_value "50kg"
    show rank "Rank"
    show rank_value "Brown Belt"
    show trust "Trust"
    show trust_value "[stfny_trst]"
    show affection "Affection"
    show affection_value "[stfny_aff]"
    show respect "Respect"
    show respect_value "[stfny_res]"
    show lust "Lust"
    show lust_value "[stfny_lst]"
    show screen button_stephanie_next
    show screen button_stephanie_back
    call screen button_2
    jump characters
label stats_venus:
    call hide_all from _call_hide_all_8
    scene stats5
    show name_text Text("{color=#912d2d}Venus{/color}", size=100)
    show species "Species"
    show species_value "Nymph"
    show sex "Sex"
    show sex_value "Female"
    show age "Age"
    show age_value "23"
    show height1 "Height"
    show height1_value "159cm"
    show weight "Weight"
    show weight_value "49kg"
    show rank "Rank"
    show rank_value "Brown Belt"
    show trust "Trust"
    show trust_value "[vns_trst]"
    show affection "Affection"
    show affection_value "[vns_aff]"
    show respect "Respect"
    show respect_value "[vns_res]"
    show lust "Lust"
    show lust_value "[vns_lst]"
    show screen button_venus_next
    show screen button_venus_back
    call screen button_2
    jump characters_2
label stats_yumi:
    call hide_all from _call_hide_all_9
    scene stats9
    show name_text Text("{color=#0091cf}Yumi{/color}", size=100)
    show species "Species"
    show species_value "Human"
    show sex "Sex"
    show sex_value "Female"
    show age "Age"
    show age_value "23"
    show height1 "Height"
    show height1_value "159cm"
    show weight "Weight"
    show weight_value "48kg"
    show rank "Rank"
    show rank_value "Blue Belt"
    show trust "Trust"
    show trust_value "[ymi_trst]"
    show affection "Affection"
    show affection_value "[ymi_aff]"
    show respect "Respect"
    show respect_value "[ymi_res]"
    show lust "Lust"
    show lust_value "[ymi_lst]"
    show screen button_yumi_next
    show screen button_yumi_back
    call screen button_2
    jump characters
#Characters_2:
label stats_tamara:
    call hide_all from _call_hide_all_10
    scene stats8
    show name_text Text("{color=#8f0000}Tamara{/color}", size=100)
    show species "Species"
    show species_value "Nymph"
    show sex "Sex"
    show sex_value "Female"
    show age "Age"
    show age_value "18"
    show height1 "Height"
    show height1_value "148cm"
    show weight "Weight"
    show weight_value "44kg"
    show rank "Rank"
    if tmra_orange_belt == 1:
        show rank_value "Orange Belt"
    else:
        show rank_value "Red Belt"
    show trust "Trust"
    show trust_value "[tmra_trst]"
    show affection "Affection"
    show affection_value "[tmra_aff]"
    show respect "Respect"
    show respect_value "[tmra_res]"
    show lust "Lust"
    show lust_value "[tmra_lst]"
    show screen button_tamara_next
    show screen button_tamara_back
    call screen button_2
    jump characters
label stats_hailey:
    call hide_all from _call_hide_all_11
    scene stats7
    show name_text Text("{color=#74abd6}Hailey{/color}", size=100)
    show species "Species"
    show species_value "Nymph"
    show sex "Sex"
    show sex_value "Female"
    show age "Age"
    show age_value "25"
    show height1 "Height"
    show height1_value "180cm"
    show weight "Weight"
    show weight_value "69kg"
    show rank "Rank"
    show rank_value "Brown Belt"
    show trust "Trust"
    show trust_value "[hly_trst]"
    show affection "Affection"
    show affection_value "[hly_aff]"
    show respect "Respect"
    show respect_value "[hly_res]"
    show lust "Lust"
    show lust_value "[hly_lst]"
    show screen button_hailey_next
    show screen button_hailey_back
    call screen button_2
    jump characters
label stats_anabelle:
    call hide_all from _call_hide_all_12
    scene stats3
    show name_text Text("{color=#bfd7db}Anabelle{/color}", size=100)
    show species "Species"
    show species_value "Human"
    show sex "Sex"
    show sex_value "Female"
    show age "Age"
    show age_value "26"
    show height1 "Height"
    show height1_value "162cm"
    show weight "Weight"
    show weight_value "57kg"
    show rank "Rank"
    show rank_value "Keres"
    show trust "Trust"
    show trust_value "[a_trst]"
    show affection "Affection"
    show affection_value "[a_aff]"
    show respect "Respect"
    show respect_value "[a_res]"
    show lust "Lust"
    show lust_value "[a_lst]"
    show screen button_anabelle_next
    show screen button_anabelle_back
    call screen button_2
    jump characters
label stats_jenny:
    call hide_all from _call_hide_all_13
    scene stats12
    show name_text Text("{color=#c44f00}Jeniffer{/color}", size=100)
    show species "Species"
    show species_value "Human"
    show sex "Sex"
    show sex_value "Female"
    show age "Age"
    show age_value "25"
    show height1 "Height"
    show height1_value "161cm"
    show weight "Weight"
    show weight_value "57kg"
    show rank "Rank"
    show rank_value "None"
    show trust "Trust"
    show trust_value "[jnfr_trst]"
    show affection "Affection"
    show affection_value "[jnfr_aff]"
    show respect "Respect"
    show respect_value "[jnfr_res]"
    show lust "Lust"
    show lust_value "[jnfr_lst]"
    show screen button_jenny_next
    show screen button_jenny_back
    call screen button_2
    jump characters_2
label stats_nixie:
    call hide_all from _call_hide_all_14
    scene stats16
    show name_text Text("{color=#a244c7}Nixie{/color}", size=100)
    show species "Species"
    show species_value "Succubus"
    show sex "Sex"
    show sex_value "Female"
    show age "Age"
    show age_value "19"
    show height1 "Height"
    show height1_value "147cm\n{size=-20}(156cm with horns){/size}"
    show weight "Weight"
    show weight_value "39kg"
    show rank "Rank"
    show rank_value "None"
    show trust "Trust"
    show trust_value "[nxi_trst]"
    show affection "Affection"
    show affection_value "[nxi_aff]"
    show respect "Respect"
    show respect_value "[nxi_res]"
    show lust "Lust"
    show lust_value "[nxi_lst]"
    if invited_misty >= 1:
        show screen button_nixie_next
    show screen button_nixie_back
    call screen button_2
    jump characters_2
label stats_fransisca:
    call hide_all from _call_hide_all_15
    scene stats13
    show name_text Text("{color=#f77440}Fransisca{/color}", size=100)
    show species "Species"
    show species_value "Human"
    show sex "Sex"
    show sex_value "Female"
    show age "Age"
    show age_value "44"
    show height1 "Height"
    show height1_value "165cm"
    show weight "Weight"
    show weight_value "63kg"
    show rank "Rank"
    show rank_value "None"
    show trust "Trust"
    show trust_value "[frnsska_trst]"
    show affection "Affection"
    show affection_value "[frnsska_aff]"
    show respect "Respect"
    show respect_value "[frnsska_res]"
    show lust "Lust"
    show lust_value "[frnsska_lst]"
    show screen button_fransisca_next
    show screen button_fransisca_back
    call screen button_2
    jump characters_2
label stats_irena:
    call hide_all from _call_hide_all_16
    scene stats15
    show name_text Text("{color=#9a97cc}Irena{/color}", size=100)
    show species "Species"
    show species_value "{size=-17}half nymph half succubus{/size}"
    show sex "Sex"
    show sex_value "Female"
    show age "Age"
    show age_value "20"
    show height1 "Height"
    show height1_value "168cm"
    show weight "Weight"
    show weight_value "61kg"
    show rank "Rank"
    show rank_value "None"
    show affection "Affection"
    show trust "Trust"
    show trust_value "[irna_trst]"
    show affection "Affection"
    show affection_value "[irna_aff]"
    show respect "Respect"
    show respect_value "[irna_res]"
    show lust "Lust"
    show lust_value "[irna_lst]"
    if succubus_incountered >= 1: #KEEEEEEEPPPPP!
        show screen button_irena_next
    show screen button_irena_back
    call screen button_2
    jump characters_2
label stats_misty:
    call hide_all from _call_hide_all_17
    scene stats17
    show name_text Text("{color=#a80035}Misty{/color}", size=100)
    show species "Species"
    show species_value "Demi-human"
    show sex "Sex"
    show sex_value "Female"
    show age "Age"
    show age_value "22"
    show height1 "Height"
    show height1_value "169cm"
    show weight "Weight"
    show weight_value "70kg"
    show rank "Rank"
    show rank_value "White Belt"
    show trust "Trust"
    show trust_value "[misty_trst]"
    show affection "Affection"
    show affection_value "[misty_aff]"
    show respect "Respect"
    show respect_value "[misty_res]"
    show lust "Lust"
    show lust_value "[misty_lst]"
    if succubus_incountered >= 1: #KKKKKKKKKKEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEP!
        show screen button_misty_back
    call screen button_2
    jump characters_2
label extra_characters:
        call hide_all from _call_hide_all_18
        scene wood
        show screen button_axius
        show label1 "{color=#ceb8ff}Axius{/color}"
        show screen button_artemis
        show label2 "{color=#95b033}Artemis{/color}"
        show screen button_athena2
        show label3 "{color=#d1d1d1}Athena{/color}"
        show screen button_sirius
        show label4 "{color=#fff6bd}Sirius{/color}"
        show screen button_clair
        show label5 "{color=#948173}Clair{/color}"
        show screen button_theseus
        show label6 "{color=#fffa6e}Theseus{/color}"
        show screen button_margot
        show label7 "{color=#a14545}Margot{/color}"
        show screen button_nari
        show label8 "{color=#ffffff}Nari{/color}"
        show screen button_next_page_extra_char
        call screen back_to_char2
label extra_characters_2:
        call hide_all from _call_hide_all_19
        scene wood
        show screen button_cat
        show label1 "{color=#a3a3a3}Cat{/color}"
        show screen button_tresha
        show label2 "{color=#754b17}Tresha{/color}"
        if mercury_ch14_met == 0:
            show screen button_mercury
        else:
            show screen button_mercury2
        show label3 "{color=#e667a6}Mercury{/color}"
        show screen button_sol
        show label4 "{color=#18aac7}Sol{/color}"
        show screen button_elnor
        show label5 "{color=#d9b800}Elnor{/color}"
        show screen button_helena
        show label6 "{color=#7d7a4a}Helena{/color}"
        show screen button_alura
        show label7 "{color=#a80041}Alura{/color}"
        call screen button_prev_page_extra_char
label extra_axius:
    call hide_all from _call_hide_all_20
    scene axius_extra
    show screen button_axius_next
    "Race: Incubus."
    "Affiliation: Underworld City./General. (Formally)"
    "First encounter: In Venus's illusion after infiltrating it."
    "Status: Alive."
    "Connection to you: Seems to be interested in convincing you to come to his side?"
    call screen button_back_to_extra_char
label extra_artemis:
    call hide_all from _call_hide_all_21
    scene artemis_extra
    show screen button_artemis_next
    show screen button_artemis_back
    "Race: God."
    "Affiliation: Artemis's hunting group."
    "First encounter: At the forest when she saved your group from a minotur."
    "Status: Alive."
    call screen button_back_to_extra_char
label extra_athena:
    call hide_all from _call_hide_all_22
    scene athena_extra
    show screen button_athena_next
    show screen button_athena_back
    "Race: God."
    "Affiliation: Olympus."
    "First encounter: At the town of the faceless god."
    "Status: Alive."
    if v4_obeyed_athena == 1:
        "Connection to you: You obeyed her and left the town of the faceless god without further interference.)"
    else:
        "Connection to you: You disobeyed her, killing her fury and ending the curse of the town of the faceless god."
    call screen button_back_to_extra_char
label extra_sirius:
    call hide_all from _call_hide_all_23
    scene sirius_extra
    show screen button_sirius_next
    show screen button_sirius_back
    "Race: Demi-god."
    "Affiliation: Unknown"
    "First encounter: During the assualt on the incubi."
    "Status: Alive."
    call screen button_back_to_extra_char
label extra_clair:
    call hide_all from _call_hide_all_24
    scene clair_extra
    show screen button_clair_next
    show screen button_clair_back
    "Race: Human."
    "Affiliation: Bouncty Hunter."
    "First encounter: At a tavern on the way back from Esyl."
    "Status: Alive."
    "Connection to you: Seemed to 'like' you..."
    call screen button_back_to_extra_char
label extra_theseus:
    call hide_all from _call_hide_all_25
    scene theseus_extra
    show screen button_theseus_next
    show screen button_theseus_back
    "Race: Demi-god."
    "Affiliation: Olympus./Champion."
    "First encounter: During the assualt on the incubi."
    "Status: Unknown."
    "Connection to you: Was against sparing you."
    z "Seira's mentor and the guy who wanted me killed as a child. I wonder how he'd react to seeing me now..."
    call screen button_back_to_extra_char
label extra_margot:
    call hide_all from _call_hide_all_26
    scene margot_extra
    show screen button_margot_next
    show screen button_margot_back
    "Race: Human."
    "Affiliation: Fransisca./Assistant."
    "First encounter: At Fransisca's house."
    "Status: Alive."
    "Connection to you: Seems to really want to fuck you..."
    z "Fransisca's nutjob of an assistant."
    call screen button_back_to_extra_char
label extra_nari:
    call hide_all from _call_hide_all_27
    scene nari_extra
    show screen button_nari_back
    show screen button_nari_next
    "Race: Unknown."
    "Affiliation: Axius."
    "First encounter: Kalytro."
    "Status: Alive."
    "Connection to you: None."
    z "This guy seems to be working for Axius and he seems quite dangerous..."
    call screen button_back_to_extra_char
label extra_cat:
    call hide_all from _call_hide_all_28
    scene cat_extra
    show screen button_cat_back
    show screen button_cat_next
    "Race: Cat."
    "Affiliation: Ninja village./Local cat."
    "First encounter: At the ninja village."
    "Status: Alive."
    "Connection to you: He kinda likes you."
    "Notable deeds: Being a cat. Scratched Torr when she tried to pet him."
    call screen button_back_to_extra_char_2
label extra_tresha:
    call hide_all from _call_hide_all_29
    scene tresha_extra
    show screen button_tresha_back
    show screen button_tresha_next
    "Race: Human."
    "Affiliation: Artemis's hunting group."
    "First encounter: At fransisca's house."
    "Status: Alive."
    "Connection to you: Helped you with disposing of the specter."
    call screen button_back_to_extra_char_2
label extra_mercury:
    call hide_all from _call_hide_all_30
    if mercury_ch14_met == 0:
        scene mercury_extra
    else:
        scene v14798
    show screen button_mercury_back
    show screen button_mercury_next
    if mercury_ch14_met == 0:
        "Race: Unknown."
        "Affiliation: Unknown."
        "First encounter: None."
        "Status: Unknown."
    elif mercury_ch14_met == 1:
        "Race: Unknown."
        "Affiliation: Jacqueline's handmaiden."
        "First encounter: Brethren."
        "Status: Alive."
    elif mercury_ch14_met == 2:
        "Race: Nymph."
        "Affiliation: Jacqueline's handmaiden."
        "First encounter: Brethren."
        "Status: Alive."
    elif mercury_ch14_met == 3:
        "Race: Nymph./Fury."
        "Affiliation: Jacqueline's handmaiden./Athena."
        "First encounter: Brethren."
        "Status: Alive."
    else:
        "Race: Nymph./Fury."
        "Affiliation: Jacqueline's handmaiden./Athena."
        "First encounter: Brethren."
        "Status: Deceased."
    call screen button_back_to_extra_char_2
label extra_sol:
    call hide_all from _call_hide_all_31
    scene sol_extra
    show screen button_sol_back
    show screen button_sol_next
    "Race: Nymph."
    "Affiliation: Ninja village./Brown belt."
    "First encounter: None."
    "Status: Deceased."
    "Connection to you: None."
    "Notable deeds: Convinced Venus of joining the ninja village..."
    call screen button_back_to_extra_char_2
label extra_elnor:
    call hide_all from _call_hide_all_32
    scene elnor_extra
    show screen button_elnor_back
    show screen button_elnor_next
    "Race: Incubus (Demi-god)."
    "Affiliation: Underworld City./Ruler."
    "First encounter: None."
    "Status: Deceased."
    "Connection to you: Believed to be your father."
    call screen button_back_to_extra_char_2
label extra_helena:
    call hide_all from _call_hide_all_33
    scene helena_extra
    show screen button_helena_back
    show screen button_helena_next
    "Race: Human."
    "Affiliation: Ninja village./Black belt."
    "First encounter: When you wanted to join the ninja village."
    "Status: Alive."
    "Connection to you: Was unsure about you at first, but she seems to have warmed up to you."
    call screen button_back_to_extra_char_2
label extra_alura:
    call hide_all from _call_hide_all_34
    scene alura_extra
    show screen button_alura_back
    "Race: Unknown."
    "Affiliation: Axius."
    "First encounter: Kalytro."
    "Status: Alive."
    "She seems to be close with Nari."
    call screen button_back_to_extra_char_2
