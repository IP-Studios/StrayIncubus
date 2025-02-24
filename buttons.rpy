
image label1 = ParameterizedText(xalign=0.12, yalign=0.47)
image label2 = ParameterizedText(xalign=0.37, yalign=0.47)
image label3 = ParameterizedText(xalign=0.62, yalign=0.47)
image label4 = ParameterizedText(xalign=0.90, yalign=0.47)
image label5 = ParameterizedText(xalign=0.12, yalign=0.92)
image label6 = ParameterizedText(xalign=0.37, yalign=0.92)
image label7 = ParameterizedText(xalign=0.62, yalign=0.92)
image label8 = ParameterizedText(xalign=0.90, yalign=0.92)
image label9 = ParameterizedText(xalign=0.11, yalign=0.92)
image label10 = ParameterizedText(xalign=0.88, yalign=0.92)
image label11 = ParameterizedText(xalign=0.89, yalign=0.47)

#hide_all:

label hide_all:
    #System
    hide screen button_1
    hide screen button_2
    hide screen button_lst
    hide screen button_aff
    hide screen button_res
    hide screen button_trst
    hide screen button_next_page
    hide screen button_previous_page
    #Characters
    hide screen button_candy
    hide screen button_candy_u
    hide screen button_torr
    hide screen button_torr_u
    hide screen button_seira
    hide screen button_seira_u
    hide screen button_centoria
    hide screen button_centoria_u
    hide screen button_stephanie
    hide screen button_stephanie_u
    hide screen button_venus
    hide screen button_venus_u
    hide screen button_yumi
    hide screen button_yumi_u
    hide screen button_gabriella
    hide screen button_gabriella_u
    hide screen button_tamara
    hide screen button_tamara_u
    hide screen button_hailey
    hide screen button_hailey_u
    hide screen button_anabelle
    hide screen button_anabelle_u
    hide screen button_jenny
    hide screen button_jenny_u
    hide screen button_nixie
    hide screen button_nixie_u
    hide screen button_irena
    hide screen button_irena_u
    hide screen button_fransisca
    hide screen button_fransisca_u
    hide screen button_misty
    hide screen button_candy_next
    hide screen button_candy_back
    hide screen button_torr_next
    hide screen button_torr_back
    hide screen button_seira_next
    hide screen button_centoria_next
    hide screen button_centoria_back
    hide screen button_stephanie_next
    hide screen button_stephanie_back
    hide screen button_venus_next
    hide screen button_venus_back
    hide screen button_yumi_next
    hide screen button_yumi_back
    hide screen button_gabriella_next
    hide screen button_gabriella_back
    hide screen button_tamara_next
    hide screen button_tamara_back
    hide screen button_hailey_next
    hide screen button_hailey_back
    hide screen button_anabelle_next
    hide screen button_anabelle_back
    hide screen button_jenny_next
    hide screen button_jenny_back
    hide screen button_nixie_next
    hide screen button_nixie_back
    hide screen button_irena_next
    hide screen button_irena_back
    hide screen button_fransisca_next
    hide screen button_fransisca_back
    hide screen button_misty_back
    hide screen button_misty_u
    #Gallery
    hide screen button_g
    #Extra chars
    hide screen button_extra_char
    hide screen button_axius
    hide screen button_axius_u
    hide screen button_axius_next
    hide screen button_artemis
    hide screen button_artemis_u
    hide screen button_artemis_next
    hide screen button_artemis_back
    hide screen button_athena2
    hide screen button_athena_u
    hide screen button_athena_next
    hide screen button_athena_back
    hide screen button_sirius
    hide screen button_sirius_u
    hide screen button_sirius_next
    hide screen button_sirius_back
    hide screen button_clair
    hide screen button_clair_u
    hide screen button_clair_next
    hide screen button_clair_back
    hide screen button_theseus
    hide screen button_theseus_u
    hide screen button_theseus_next
    hide screen button_theseus_back
    hide screen button_nari
    hide screen button_margot_u
    hide screen button_margot
    hide screen button_margot_next
    hide screen button_margot_back
    hide screen button_nari_u
    hide screen button_nari_next
    hide screen button_nari_back
    hide screen button_back_to_extra_char
    hide screen back_to_char2
    hide screen button_prev_page_extra_char
    hide screen button_next_page_extra_char
    hide screen button_back_to_extra_char_2
    hide screen button_cat
    hide screen button_cat_u
    hide screen button_cat_next
    hide screen button_cat_back
    hide screen button_tresha
    hide screen button_tresha_u
    hide screen button_tresha_next
    hide screen button_tresha_back
    hide screen button_mercury
    hide screen button_mercury2
    hide screen button_mercury_u
    hide screen button_mercury_next
    hide screen button_mercury_back
    hide screen button_sol
    hide screen button_sol_u
    hide screen button_sol_next
    hide screen button_sol_back
    hide screen button_elnor
    hide screen button_elnor_u
    hide screen button_elnor_back
    hide screen button_elnor_next
    hide screen button_helena
    hide screen button_helena_back
    hide screen button_helena_next
    hide screen button_alura
    hide screen button_alura_back

    #System:
    screen button_1:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.97
            ypos 0.06
            idle "images/Buttons/button_idle.png"
            hover "images/Buttons/button_hover.png"
            action ui.callsinnewcontext("characters")
    screen button_2:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.97
            ypos 0.06
            idle "images/Buttons/button_hover.png"
            hover "images/Buttons/button_idle.png"
            action renpy.curry(renpy.end_interaction)(True)
    screen button_lst:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.97
            ypos 0.06
            idle "images/Buttons/button_lst.png"
            hover "images/Buttons/button_lst.png"
            action NullAction()
    screen button_aff:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.97
            ypos 0.06
            idle "images/Buttons/button_aff.png"
            hover "images/Buttons/button_aff.png"
            action NullAction()
    screen button_aff_minus:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.97
            ypos 0.06
            idle "images/Buttons/button_aff_minus.png"
            hover "images/Buttons/button_aff_minus.png"
            action NullAction()
    screen button_res:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.97
            ypos 0.06
            idle "images/Buttons/button_res.png"
            hover "images/Buttons/button_res.png"
            action NullAction()
    screen button_trst:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.97
            ypos 0.06
            idle "images/Buttons/button_trst.png"
            hover "images/Buttons/button_trst.png"
            action NullAction()
    screen button_misty_stats:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.97
            ypos 0.06
            idle "images/Buttons/button_misty.png"
            hover "images/Buttons/button_misty.png"
            action NullAction()
    screen button_next_page:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.95
            ypos 0.95
            idle "images/Buttons/next_u.png"
            hover "images/Buttons/next_h.png"
            action Jump("characters_2")
    screen button_previous_page:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.05
            ypos 0.95
            idle "images/Buttons/back_u.png"
            hover "images/Buttons/back_h.png"
            action Jump("characters")
    #Characters:
    screen button_candy:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.86
            ypos 0.72
            idle "images/Stats_stuff/Candy_F_U.webp"
            hover "images/Stats_stuff/Candy_F_H.webp"
            action Jump("stats_candy")
    screen button_candy_u:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.86
            ypos 0.72
            idle "images/Stats_stuff/Unknown_F_U.webp"
            hover "images/Stats_stuff/Unknown_F_H.webp"
            action NullAction()
    screen button_candy_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("stats_torr")
    screen button_candy_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("stats_hailey")
    screen button_torr:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.14
            ypos 0.28
            idle "images/Stats_stuff/Torr_F_U.webp"
            hover "images/Stats_stuff/Torr_F_H.webp"
            action Jump("stats_torr")
    screen button_torr_u:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.14
            ypos 0.28
            idle "images/Stats_stuff/Unknown_F_U.webp"
            hover "images/Stats_stuff/Unknown_F_H.webp"
            action NullAction()
    screen button_torr_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("stats_venus")
    screen button_torr_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("stats_candy")
    screen button_seira:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.14
            ypos 0.28
            idle "images/Stats_stuff/Seira_F_U.webp"
            hover "images/Stats_stuff/Seira_F_H.webp"
            action Jump("stats_seira")
    screen button_seira_u:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.14
            ypos 0.28
            idle "images/Stats_stuff/Unknown_F_U.webp"
            hover "images/Stats_stuff/Unknown_F_H.webp"
            action NullAction()
    screen button_seira_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("stats_gabriella")
    screen button_centoria:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.62
            ypos 0.28
            idle "images/Stats_stuff/Centoria_F_U.webp"
            hover "images/Stats_stuff/Centoria_F_H.webp"
            action Jump("stats_centoria")
    screen button_centoria_u:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.62
            ypos 0.28
            idle "images/Stats_stuff/Unknown_F_U.webp"
            hover "images/Stats_stuff/Unknown_F_H.webp"
            action NullAction()
    screen button_centoria_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("stats_jenny")
    screen button_centoria_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("stats_venus")
    screen button_stephanie:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.86
            ypos 0.28
            idle "images/Stats_stuff/Stephanie_F_U.webp"
            hover "images/Stats_stuff/Stephanie_F_H.webp"
            action Jump("stats_stephanie")
    screen button_stephanie_u:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.86
            ypos 0.28
            idle "images/Stats_stuff/Unknown_F_U.webp"
            hover "images/Stats_stuff/Unknown_F_H.webp"
            action NullAction()
    screen button_stephanie_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("stats_anabelle")
    screen button_stephanie_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("stats_yumi")
    screen button_venus:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.38
            ypos 0.28
            idle "images/Stats_stuff/Venus_F_U.webp"
            hover "images/Stats_stuff/Venus_F_H.webp"
            action Jump("stats_venus")
    screen button_venus_u:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.38
            ypos 0.28
            idle "images/Stats_stuff/Unknown_F_U.webp"
            hover "images/Stats_stuff/Unknown_F_H.webp"
            action NullAction()
    screen button_venus_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("stats_centoria")
    screen button_venus_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("stats_torr")
    screen button_yumi:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.62
            ypos 0.28
            idle "images/Stats_stuff/Yumi_F_U.webp"
            hover "images/Stats_stuff/Yumi_F_H.webp"
            action Jump("stats_yumi")
    screen button_yumi_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("stats_stephanie")
    screen button_yumi_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("stats_gabriella")
    screen button_gabriella:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.38
            ypos 0.28
            idle "images/Stats_stuff/Gabriella_F_U.webp"
            hover "images/Stats_stuff/Gabriella_F_H.webp"
            action Jump("stats_gabriella")
    screen button_gabriella_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("stats_yumi")
    screen button_gabriella_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("stats_seira")
    #Characters_2 buttons:
    screen button_tamara:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.38
            ypos 0.72
            idle "images/Stats_stuff/Tamara_F_U.webp"
            hover "images/Stats_stuff/Tamara_F_H.webp"
            action Jump("stats_tamara")
    screen button_tamara_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("stats_hailey")
    screen button_tamara_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("stats_anabelle")
    screen button_hailey:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.62
            ypos 0.72
            idle "images/Stats_stuff/Hailey_F_U.webp"
            hover "images/Stats_stuff/Hailey_F_H.webp"
            action Jump("stats_hailey")
    screen button_hailey_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("stats_candy")
    screen button_hailey_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("stats_tamara")
    screen button_anabelle:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.14
            ypos 0.72
            idle "images/Stats_stuff/Anabelle_F_U.webp"
            hover "images/Stats_stuff/Anabelle_F_H.webp"
            action Jump("stats_anabelle")
    screen button_anabelle_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("stats_tamara")
    screen button_anabelle_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("stats_stephanie")
    screen button_jenny:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.86
            ypos 0.28
            idle "images/Stats_stuff/Jenny_F_U.webp"
            hover "images/Stats_stuff/Jenny_F_H.webp"
            action Jump("stats_jenny")
    screen button_jenny_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("stats_fransisca")
    screen button_jenny_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("stats_centoria")
    screen button_nixie:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.62
            ypos 0.72
            idle "images/Stats_stuff/Nixie_F_U.webp"
            hover "images/Stats_stuff/Nixie_F_H.webp"
            action Jump("stats_nixie")
    screen button_nixie_u:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.62
            ypos 0.72
            idle "images/Stats_stuff/Unknown_F_U.webp"
            hover "images/Stats_stuff/Unknown_F_H.webp"
            action NullAction()
    screen button_nixie_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("stats_misty")
    screen button_nixie_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("stats_irena")
    screen button_irena:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.38
            ypos 0.72
            idle "images/Stats_stuff/Irena_F_U.webp"
            hover "images/Stats_stuff/Irena_F_H.webp"
            action Jump("stats_irena")
    screen button_irena_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("stats_nixie")
    screen button_irena_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("stats_fransisca")
    screen button_fransisca:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.14
            ypos 0.72
            idle "images/Stats_stuff/Fransisca_F_U.webp"
            hover "images/Stats_stuff/Fransisca_F_H.webp"
            action Jump("stats_fransisca")
    screen button_fransisca_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("stats_irena")
    screen button_fransisca_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("stats_jenny")
    screen button_misty:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.86
            ypos 0.72
            idle "images/Stats_stuff/Misty_F_U.webp"
            hover "images/Stats_stuff/Misty_F_H.webp"
            action Jump("stats_misty")
    screen button_misty_u:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.86
            ypos 0.72
            idle "images/Stats_stuff/Unknown_F_U.webp"
            hover "images/Stats_stuff/Unknown_F_H.webp"
            action NullAction()
    screen button_misty_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("stats_nixie")
    #Gallery buttons:
    screen button_g:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.05
            idle "images/Buttons/gallery_button.png"
            hover "images/Buttons/gallery_button_h.png"
            action Jump("gallery")
    #Extra characters
    screen button_extra_char:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.95
            ypos 0.95
            idle "images/Buttons/extra_char.png"
            hover "images/Buttons/extra_char_h.png"
            action Jump("extra_characters")
    screen back_to_char2:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.05
            ypos 0.95
            idle "images/Buttons/back_u.png"
            hover "images/Buttons/back_h.png"
            action Jump("characters_2")
    screen button_axius:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.14
            ypos 0.28
            idle "images/extra char/buttons/axius_u.webp"
            hover "images/extra char/buttons/axius_h.webp"
            action Jump("extra_axius")
    screen button_axius_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("extra_artemis")
    screen button_artemis:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.38
            ypos 0.28
            idle "images/extra char/buttons/artemis_u.webp"
            hover "images/extra char/buttons/artemis_h.webp"
            action Jump("extra_artemis")
    screen button_artemis_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("extra_athena")
    screen button_artemis_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("extra_axius")
    screen button_athena2:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.62
            ypos 0.28
            idle "images/extra char/buttons/athena_u.webp"
            hover "images/extra char/buttons/athena_h.webp"
            action Jump("extra_athena")
    screen button_athena_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("extra_sirius")
    screen button_athena_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("extra_artemis")
    screen button_sirius:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.86
            ypos 0.28
            idle "images/extra char/buttons/sirius_u.webp"
            hover "images/extra char/buttons/sirius_h.webp"
            action Jump("extra_sirius")
    screen button_sirius_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("extra_clair")
    screen button_sirius_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("extra_athena")
    screen button_clair:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.14
            ypos 0.72
            idle "images/extra char/buttons/clair_u.webp"
            hover "images/extra char/buttons/clair_h.webp"
            action Jump("extra_clair")
    screen button_clair_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("extra_theseus")
    screen button_clair_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("extra_sirius")
    screen button_theseus:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.38
            ypos 0.72
            idle "images/extra char/buttons/theseus_u.webp"
            hover "images/extra char/buttons/theseus_h.webp"
            action Jump("extra_theseus")
    screen button_theseus_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("extra_margot")
    screen button_theseus_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("extra_clair")
    screen button_margot:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.62
            ypos 0.72
            idle "images/extra char/buttons/margot_u.webp"
            hover "images/extra char/buttons/margot_h.webp"
            action Jump("extra_margot")
    screen button_margot_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("extra_nari")
    screen button_margot_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("extra_theseus")
    screen button_nari:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.86
            ypos 0.72
            idle "images/extra char/buttons/nari_u.webp"
            hover "images/extra char/buttons/nari_h.webp"
            action Jump("extra_nari")
    screen button_nari_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("extra_cat")
    screen button_nari_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("extra_margot")
    screen button_back_to_extra_char:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.97
            ypos 0.06
            idle "images/Buttons/button_idle.png"
            hover "images/Buttons/button_hover.png"
            action Jump("extra_characters")

    screen button_next_page_extra_char: #NEW
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.95
            ypos 0.95
            idle "images/Buttons/next_u.png"
            hover "images/Buttons/next_h.png"
            action Jump("extra_characters_2")
    screen button_prev_page_extra_char: #NEW
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.05
            ypos 0.95
            idle "images/Buttons/back_u.png"
            hover "images/Buttons/back_h.png"
            action Jump("extra_characters")
    screen button_back_to_extra_char_2: #NEW
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.97
            ypos 0.06
            idle "images/Buttons/button_idle.png"
            hover "images/Buttons/button_hover.png"
            action Jump("extra_characters_2")
    #Extra characters page 2:
    screen button_cat:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.14
            ypos 0.28
            idle "images/extra char/buttons/cat_u.webp"
            hover "images/extra char/buttons/cat_h.webp"
            action Jump("extra_cat")
    screen button_cat_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("extra_tresha")
    screen button_cat_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("extra_nari")
    screen button_tresha:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.38
            ypos 0.28
            idle "images/extra char/buttons/tresha_u.webp"
            hover "images/extra char/buttons/tresha_h.webp"
            action Jump("extra_tresha")
    screen button_tresha_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("extra_mercury")
    screen button_tresha_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("extra_cat")
    screen button_mercury:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.62
            ypos 0.28
            idle "images/extra char/buttons/mercury_u.webp"
            hover "images/extra char/buttons/mercury_h.webp"
            action Jump("extra_mercury")
    screen button_mercury2:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.62
            ypos 0.28
            idle "images/extra char/buttons/mercury2_u.webp"
            hover "images/extra char/buttons/mercury2_h.webp"
            action Jump("extra_mercury")
    screen button_mercury_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("extra_sol")
    screen button_mercury_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("extra_tresha")
    screen button_sol:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.86
            ypos 0.28
            idle "images/extra char/buttons/sol_u.webp"
            hover "images/extra char/buttons/sol_h.webp"
            action Jump("extra_sol")
    screen button_sol_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("extra_elnor")
    screen button_sol_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("extra_mercury")
    screen button_elnor:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.14
            ypos 0.72
            idle "images/extra char/buttons/elnor_u.webp"
            hover "images/extra char/buttons/elnor_h.webp"
            action Jump("extra_elnor")
    screen button_elnor_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("extra_sol")
    screen button_elnor_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("extra_helena")
    screen button_helena:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.38
            ypos 0.72
            idle "images/extra char/buttons/helena_u.webp"
            hover "images/extra char/buttons/helena_h.webp"
            action Jump("extra_helena")
    screen button_helena_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("extra_elnor")
    screen button_helena_next:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.93
            ypos 0.96
            idle "images/Buttons/next_smol_u.png"
            hover "images/Buttons/next_smol_h.png"
            action Jump("extra_alura")
    screen button_alura:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.62
            ypos 0.72
            idle "images/extra char/buttons/alura_u.webp"
            hover "images/extra char/buttons/alura_h.webp"
            action Jump("extra_alura")
    screen button_alura_back:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.07
            ypos 0.96
            idle "images/Buttons/back_smol_u.png"
            hover "images/Buttons/back_smol_h.png"
            action Jump("extra_helena")
