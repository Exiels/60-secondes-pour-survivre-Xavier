# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("TEMP NOT DEFINED")
define x = Character("Xavier")
define a = Character("Arthur")
define t = Character("Thomas")
define A = Character("Anne")
define b = Character("Benoît")

# Define Image house Scenes
image hall = im.Scale("house/hall.jpg", 1920, 1080)
image bunker = im.Scale("house/bunker.jpg", 1920, 1080)
image chambre = im.Scale("house/chambre.jpg", 1920, 1080)
image maison = im.Scale("house/maison.jpg", 1920, 1080)
image salle_a_manger = im.Scale("house/salle_a_manger.jpg", 1920, 1080)
image salon = im.Scale("house/salon.jpg", 1920, 1080)
image salle_de_bain = im.Scale("house/sdb.jpg", 1920, 1080)
image cuisine = im.Scale("house/cuisine.jpg", 1920, 1080)

image Benoit = "familly/Benoit.png"
image Anne = "familly/Anne.png"
image Thomas = "familly/Thomas.png"
image Arthur = "familly/Arthur.png"
image Xavier = im.Scale("familly/Xavier.png", 800, 1000)

# Define Image Items
image soup = im.Scale("items/soup.png", 30, 50)

screen countdown:
    if bunker == 0:
        timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])

        side "tl":
            frame xpos 20 ypos 20:
                text str(time)

transform custom_zoom:
    zoom 0.2

transform hache:
    zoom 0.15

transform fusil:
    zoom 0.4

transform kit_med:
    zoom 0.5

transform cadena:
    zoom 0.05

transform eau:
    zoom 0.075

init -3 python:
    if persistent.lang is None:
        persistent.lang = "english"

    lang = persistent.lang

init python:
    config.main_menu.insert(3, (u'Language', "language_chooser", "True"))

init:
    $ time = 60
    $ timer_range = 5
    $ timer_jump = 'xavier_caught_you'

    $ nb_food = 0
    $ nb_soup = 0
    $ nb_water = 0
    $ nb_eau = 0
    $ nb_balles = 0
    $ nb_bible = 0
    $ nb_cadena = 0
    $ nb_cagoule = 0
    $ nb_cartes = 0
    $ nb_chaise = 0
    $ nb_fusil = 0
    $ nb_hache = 0
    $ nb_kit_med = 0
    $ nb_lampe = 0
    $ nb_lit = 0
    $ nb_radio = 0
    $ nb_sac = 0
    $ nb_table = 0
    $ nb_violon = 0
    $ nb_child = 4
    $ is_down = 0

    $ max_food = 10
    $ max_water = 10
    $ max_balles = 2
    $ max_bible = 1
    $ max_cadena = 1
    $ max_cagoule = 1
    $ max_cartes = 1
    $ max_chaise = 4
    $ max_fusil = 1
    $ max_hache = 1
    $ max_kit_med = 2
    $ max_lampe = 1
    $ max_lit = 4
    $ max_radio = 1
    $ max_sac = 2
    $ max_table = 1
    $ max_violon = 1
    $ max_child = 4
    $ is_down = 0

    $ soup_1 = 0
    $ soup_2 = 0
    $ soup_3 = 0
    $ soup_4 = 0
    $ soup_5 = 0
    $ soup_6 = 0
    $ soup_7 = 0
    $ soup_8 = 0
    $ soup_9 = 0
    $ soup_10 = 0

    $ water_1 = 0
    $ water_2 = 0
    $ water_3 = 0
    $ water_4 = 0
    $ water_5 = 0
    $ water_6 = 0
    $ water_7 = 0
    $ water_8 = 0
    $ water_9 = 0
    $ water_10 = 0

    $ balles_1 = 0
    $ balles_2 = 0

    $ bible_1 = 0

    $ cadena_1 = 0

    $ cagoule_1 = 0

    $ cartes_1 = 0

    $ chaise_1 = 0
    $ chaise_1 = 0
    $ chaise_1 = 0
    $ chaise_1 = 0

    $ fusil_1 = 0

    $ hache_1 = 0

    $ kit_med_1 = 0
    $ kit_med_1 = 0

    $ lampe_1 = 0

    $ lit_1 = 0

    $ radio_1 = 0

    $ sac_1 = 0
    $ sac_1 = 0

    $ table_1 = 0

    $ violon_1 = 0

    $ arthur = True
    $ thomas = True
    $ anne = True
    $ benoit = True

    $ day = 0
    $ bunker = 0

    $ benoit_soup = 10
    $ anne_soup = 10
    $ thomas_soup = 10
    $ arthur_soup = 10

    $ benoit_eau = 5
    $ anne_eau = 5
    $ thomas_eau = 5
    $ arthur_eau = 5

    $ benoit_mental = 100
    $ anne_mental = 100
    $ thomas_mental = 100
    $ arthur_mental = 100

    $ music_init = 0

    $ explore = 0
    $ who_exp = "personne"


label xavier_caught_you:
    "Malheureusement, vous avez été trop lent... Xavier vous a attrapé avant que vous n'atténiez le bunker."
    return

screen infos:
    frame xpos 1750 ypos 20:
        text "FOOD: " + str(nb_food)

label add_soup:
    if nb_food < max_food:
        $ nb_food += 1
        "Vous avez trouvé une soupe !"
    else:
        "Vous avez trop de nourriture sur vous !"
    jump continue

label add_soup_1:
    if nb_food < max_food:
        $ nb_soup += 1
        $ nb_food += 2
        "Vous avez trouvé une soupe !"
    else:
        "Vous avez trop de nourriture sur vous !"
    jump continue

label add_soup_2:
    if nb_food < max_food:
        $ nb_soup += 1
        $ nb_food += 4
        "Vous avez trouvé une soupe !"
    else:
        "Vous avez trop de nourriture sur vous !"
    jump continue

label add_soup_3:
    if nb_food < max_food:
        $ nb_food += 7
        $ nb_soup += 1
        "Vous avez trouvé une soupe !"
    else:
        "Vous avez trop de nourriture sur vous !"
    jump continue

label add_balles:
    if nb_balles < max_balles:
        $ nb_balles += 1
        "Vous avez trouvé une balle !"
    else:
        "Vous avez trop de balles sur vous !"
    jump continue

label add_bible:
    if nb_bible < max_bible:
        $ nb_bible += 1
        "Vous avez trouvé une bible !"
    else:
        "Vous avez trop de bible sur vous !"
    jump continue

label add_cadena:
    if nb_cadena < max_cadena:
        $ nb_cadena += 1
        "Vous avez trouvé un cadena !"
    else:
        "Vous avez trop de cadena sur vous !"
    jump continue

label add_cagoule:
    if nb_cagoule < max_cagoule:
        $ nb_cagoule += 1
        "Vous avez trouvé une cagoule !"
    else:
        "Vous avez trop de cagoule sur vous !"
    jump continue

label add_cartes:
    if nb_cartes < max_cartes:
        $ nb_cartes += 1
        "Vous avez trouvé un jeu de cartes !"
    else:
        "Vous avez trop de cartes sur vous !"
    jump continue

label add_chaise:
    if nb_chaise < max_chaise:
        $ nb_chaise += 1
        "Vous avez trouvé une chaise !"
    else:
        "Vous avez trop de chaise sur vous !"
    jump continue

label add_eau_1:
    if nb_water < max_water:
        $ nb_water += 1
        $ nb_eau += 2
        "Vous avez trouvé de l'eau !"
    else:
        "Vous avez trop d'eau sur vous !"
    jump continue

label add_eau_2:
    if nb_water < max_water:
        $ nb_water += 1
        $ nb_eau += 4
        "Vous avez trouvé de l'eau !"
    else:
        "Vous avez trop d'eau sur vous !"
    jump continue

label add_eau_3:
    if nb_water < max_water:
        $ nb_water += 1
        $ nb_eau += 7
        "Vous avez trouvé de l'eau !"
    else:
        "Vous avez trop d'eau sur vous !"
    jump continue

label add_fusil:
    if nb_fusil < max_fusil:
        $ nb_fusil += 1
        "Vous avez trouvé un fusil !"
    else:
        "Vous avez trop de fusil sur vous !"
    jump continue

label add_hache:
    if nb_hache < max_hache:
        $ nb_hache += 1
        "Vous avez trouvé une hache !"
    else:
        "Vous avez trop de hache sur vous !"
    jump continue

label add_kit_med:
    if nb_kit_med < max_kit_med:
        $ nb_kit_med += 1
        "Vous avez trouvé un kit_med !"
    else:
        "Vous avez trop de kit_med sur vous !"
    jump continue

label add_lampe:
    if nb_lampe < max_lampe:
        $ nb_lampe += 1
        "Vous avez trouvé une lampe !"
    else:
        "Vous avez trop de lampe sur vous !"
    jump continue

label add_lit:
    if nb_lit < max_lit:
        $ nb_lit += 1
        "Vous avez trouvé un lit !"
    else:
        "Vous avez trop de lit sur vous !"
    jump continue

label add_radio:
    if nb_radio < max_radio:
        $ nb_radio += 1
        "Vous avez trouvé une radio !"
    else:
        "Vous avez trop de radio sur vous !"
    jump continue

label add_sac:
    if nb_sac < max_sac:
        $ nb_sac += 1
        "Vous avez trouvé un sac !"
    else:
        "Vous avez trop de sac sur vous !"
    jump continue

label add_table:
    if nb_table < max_table:
        $ nb_table += 1
        "Vous avez trouvé une table !"
    else:
        "Vous avez trop de table sur vous !"
    jump continue

label add_violon:
    if nb_violon < max_violon:
        $ nb_violon += 1
        "Vous avez trouvé un violon !"
    else:
        "Vous avez trop de violon sur vous !"
    jump continue

# The game starts here.

label hall:
    if music_init == 0:
        play music "audio/BGM/outbreak.mp3"
        play sound "audio/sound_effect/bruit-de-porte-toc-toc.mp3"
        $ music_init += 1
    scene hall
    pause 0.5
    show screen arrow_hall
    if nb_balles == 0:
        show screen items_balle
    screen items_balle:
        imagebutton:
            xpos 950
            ypos 450
            idle "items/balles.png"
            at custom_zoom
            action [Hide("items_balle"), Jump("add_balles")]
    screen arrow_hall:
        imagebutton:
            xpos 1130
            ypos 100
            idle "arrow/arrow_left.png"
            at custom_zoom
            action [Hide("arrow_hall"), Hide("items_balle"), Jump("chambre")]
        imagebutton:
            xpos 1300
            ypos 100
            idle "arrow/arrow_right.png"
            at custom_zoom
            action [Hide("arrow_hall"), Hide("items_balle"), Jump("salle_de_bain")]
        imagebutton:
            xpos 750
            ypos 500
            idle "arrow/arrow_top.png"
            at custom_zoom
            action [Hide("arrow_hall"), Hide("items_balle"), Jump("bunker")]
        imagebutton:
            xpos 150
            ypos 600
            idle "arrow/arrow_left.png"
            at custom_zoom
            action [Hide("arrow_hall"), Hide("items_balle"), Jump("salon")]
        imagebutton:
            xpos 1650
            ypos 600
            idle "arrow/arrow_right.png"
            at custom_zoom
            action [Hide("arrow_hall"), Hide("items_balle"), Jump("salle_a_manger")]
    jump continue


label chambre:
    scene chambre
    pause 0.5
    screen items_violon:
        imagebutton:
            xpos 1025
            ypos 650
            idle "items/violon.png"
            at fusil
            action [Hide("items_violon"), Jump("add_violon")]
    screen items_bible:
        imagebutton:
            xpos 25
            ypos 650
            idle "items/bible.png"
            at custom_zoom
            action [Hide("items_bible"), Jump("add_bible")]
    screen arrow_chambre:
        imagebutton:
            xpos 150
            ypos 500
            idle "arrow/arrow_left.png"
            at custom_zoom
            action [Hide("arrow_chambre"), Hide("items_bible"), Hide("items_violon"), Jump("hall")]
    show screen arrow_chambre
    if nb_bible == 0:
        show screen items_bible
    if nb_violon == 0:
        show screen items_violon
    jump continue

label bunker:
    play music "audio/BGM/stress.mp3" fadeout 1
    play sound "audio/sound_effect/bruit-de-porte-toc-toc.mp3"
    scene bunker
    $ bunker = 1
    jump first_day

label cuisine:
    scene cuisine
    pause 0.5
    screen items_soupe_1:
        imagebutton:
            xpos 1500
            ypos 290
            idle "items/soup.png"
            at custom_zoom
            action [Hide("items_soupe_1"), Jump("add_soup_1")]
    screen items_soupe_2:
        imagebutton:
            xpos 1320
            ypos 545
            idle "items/soup.png"
            at custom_zoom
            action [Hide("items_soupe_2"), Jump("add_soup_2")]
    screen items_soupe_3:
        imagebutton:
            xpos 535
            ypos 300
            idle "items/soup.png"
            at custom_zoom
            action [Hide("items_soupe_3"), Jump("add_soup_3")]
    screen items_radio:
        imagebutton:
            xpos 1410
            ypos -50
            idle "items/radio.png"
            at fusil
            action [Hide("items_radio"), Jump("add_radio")]
    screen items_hache:
        imagebutton:
            xpos 1010
            ypos 685
            idle "items/hache.png"
            at hache
            action [Hide("items_hache"), Jump("add_hache")]
    screen arrow_cuisine:
        imagebutton:
            xpos 1700
            ypos 600
            idle "arrow/arrow_right.png"
            at custom_zoom
            action [Hide("arrow_cuisine"), Hide("items_soupe_1"), Hide("items_soupe_2"), Hide("items_soupe_3"), Hide("items_hache"), Hide("items_radio"), Hide("items_cuisine"), Jump("salle_a_manger")]
        imagebutton:
            xpos 100
            ypos 600
            idle "arrow/arrow_left.png"
            at custom_zoom
            action [Hide("arrow_cuisine"), Hide("items_soupe_1"), Hide("items_soupe_2"), Hide("items_soupe_3"), Hide("items_hache"), Hide("items_radio"), Hide("items_cuisine"), Jump("salon")]
    show screen arrow_cuisine
    if nb_hache == 0:
        show screen items_hache
    if nb_radio == 0:
        show screen items_radio
    if nb_soup != 2 and nb_soup != 6 and nb_soup != 9 and nb_soup != 13:
        show screen items_soupe_1
    if nb_soup != 4 and nb_soup != 6 and nb_soup != 11 and nb_soup != 13:
        show screen items_soupe_2
    if nb_soup != 7 and nb_soup != 9 and nb_soup != 11 and nb_soup != 13:
        show screen items_soupe_3
    jump continue

label salle_a_manger:
    scene salle_a_manger
    pause 0.5
    screen item_cadena:
        imagebutton:
            xpos 1210
            ypos 415
            idle "items/cadena.png"
            at cadena
            action [Hide("item_cadena"), Jump("add_cadena")]
    screen item_chaise:
        imagebutton:
            xpos 1300
            ypos 340
            idle "items/chaise.png"
            action [Hide("item_chaise"), Jump("add_chaise")]
    screen arrow_sam:
        imagebutton:
            xpos 950
            ypos 900
            idle "arrow/arrow_bot.png"
            at custom_zoom
            action [Hide("arrow_sam"), Hide("item_cadena"), Hide("item_chaise"), Jump("hall")]
        imagebutton:
            xpos 100
            ypos 600
            idle "arrow/arrow_left.png"
            at custom_zoom
            action [Hide("arrow_sam"), Hide("item_cadena"), Hide("item_chaise"), Jump("cuisine")]
    show screen arrow_sam
    if nb_cadena == 0:
        show screen item_cadena
    if nb_chaise == 0:
        show screen item_chaise
    jump continue

label salle_de_bain:
    scene salle_de_bain
    pause 0.5
    screen items_eau_1:
        imagebutton:
            xpos 1750
            ypos 220
            idle "items/eau.png"
            at eau
            action [Hide("items_eau_1"), Jump("add_eau_1")]
    screen items_eau_2:
        imagebutton:
            xpos 1220
            ypos 545
            idle "items/eau.png"
            at eau
            action [Hide("items_eau_2"), Jump("add_eau_2")]
    screen items_eau_3:
        imagebutton:
            xpos 450
            ypos 300
            idle "items/eau.png"
            at eau
            action [Hide("items_eau_3"), Jump("add_eau_3")]
    screen items_kit_med:
        imagebutton:
            xpos 650
            ypos 780
            idle "items/kit_med.png"
            at kit_med
            action [Hide("items_kit_med"), Jump("add_kit_med")]
    screen items_lampe:
        imagebutton:
            xpos 670
            ypos 140
            idle "items/lampe.png"
            at custom_zoom
            action [Hide("items_lampe"), Jump("add_lampe")]
    screen arrow_sdb:
        imagebutton:
            xpos 100
            ypos 600
            idle "arrow/arrow_left.png"
            at custom_zoom
            action [Hide("arrow_hall"), Hide("items_kit_med"), Hide("items_eau_1"), Hide("items_eau_2"), Hide("items_eau_3"), Hide("items_lampe"), Jump("hall")]
    show screen arrow_sdb
    if nb_lampe == 0:
        show screen items_lampe
    if nb_kit_med == 0:
        show screen items_kit_med
    if nb_eau != 2 and nb_eau != 6 and nb_eau != 9 and nb_eau != 13:
        show screen items_eau_1
    if nb_eau != 4 and nb_eau != 6 and nb_eau != 11 and nb_eau != 13:
        show screen items_eau_2
    if nb_eau != 7 and nb_eau != 9 and nb_eau != 11 and nb_eau != 13:
        show screen items_eau_3
    jump continue

label salon:
    scene salon
    pause 0.5
    screen items_fusil:
        imagebutton:
            xpos 750
            ypos -25
            idle "items/fusil.png"
            at fusil
            action [Hide("items_fusil"), Jump("add_fusil")]
    screen items_cartes:
        imagebutton:
            xpos 1450
            ypos 615
            idle "items/cartes.png"
            at custom_zoom
            action [Hide("items_cartes"), Jump("add_cartes")]
    screen items_cagoule:
        imagebutton:
            xpos 910
            ypos 515
            idle "items/cagoule.png"
            at custom_zoom
            action [Hide("items_cagoule"), Jump("add_cagoule")]
    screen arrow_salon:
        imagebutton:
            xpos 1700
            ypos 600
            idle "arrow/arrow_right.png"
            at custom_zoom
            action [Hide("arrow_salon"), Hide("items_cagoule"), Hide("items_fusil"), Hide("items_cartes"), Jump("hall")]
        imagebutton:
            xpos 100
            ypos 600
            idle "arrow/arrow_left.png"
            at custom_zoom
            action [Hide("arrow_salon"), Hide("items_cagoule"), Hide("items_fusil"), Hide("items_cartes"), Jump("salle_a_manger")]
    show screen arrow_salon
    if nb_cagoule == 0:
        show screen items_cagoule
    if nb_fusil == 0:
        show screen items_fusil
    if nb_cartes == 0:
        show screen items_cartes
    jump continue

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    "Ce jeu est basé sur des faits réels..."

    jump hall

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

label continue:

    show screen countdown
    show screen infos

    # These display lines of dialogue.

    pause

    jump continue
    # This ends the game.

label first_day:

    show Benoit:
        xalign 0.2
        yalign 0.8
    show Anne:
        xalign 0.4
        yalign 0.8
    show Thomas:
        xalign 0.6
        yalign 0.8
    show Arthur:
        xalign 0.8
        yalign 0.8

    "Vous êtes rentré à temps dans le bunker."
    "Vous entendez Xavier, votre père, cogner à la porte."
    "Vous êtes coincé ici."
    "Heureusement, en fouillant un peu le bunker, vous trouvez de l'eau et de la soupe en boite."
    $ nb_food += 3
    $ nb_eau += 3
    "Vous avez [nb_food] soupes et [nb_eau] bouteilles eau pour vous alimenter."
    if nb_cartes != 0 and nb_bible != 0 and nb_violon != 0:
        "Vous avez [nb_cartes] jeux des 7 Familles, [nb_violon] violons et [nb_bible] bibles pour vous divertir."
    if nb_cartes != 0 and nb_bible != 0 and nb_violon == 0:
        "Vous avez [nb_cartes] jeux des 7 Familles et [nb_bible] bibles pour vous divertir."
    if nb_cartes != 0 and nb_bible == 0 and nb_violon == 0:
        "Vous avez [nb_cartes] jeux des 7 Familles pour vous divertir."
        "Il n'y a rien de plus précieux que la famille !"
    if nb_cartes == 0 and nb_bible != 0 and nb_violon != 0:
        "Vous avez [nb_bible] bibles et [nb_violon] violons pour vous divertir."
        "Le catholisme et la musique, le propre de la famille Dupont de Ligonnès."
    if nb_cartes == 0 and nb_bible != 0 and nb_violon == 0:
        "Vous avez [nb_bible] bibles pour vous divertir."
    if nb_cartes != 0 and nb_bible == 0 and nb_violon != 0:
        "Vous avez [nb_cartes] jeux des 7 Familles et [nb_violon] violons pour vous divertir."
    if nb_kit_med != 0:
        "Heureusement, vous avez [nb_kit_med] kit médical pour soigner les bobos."
    if nb_hache != 0:
        "[nb_hache] hache ne sera pas de trop pour vous protéger de votre père."
    if nb_fusil != 0:
        if nb_balles != 0:
            "Un fusil et [nb_balles] balles, cela sera certainement votre meilleure défense, votre père lui même vous à appris à vous en servir."
        else:
            "Un fusil c'est bien, mais avoir des balles aurait été mieux..."
    if nb_chaise != 0:
        "La survie va être longue, pouvoir s'assoir confortablement fera défiler le temps plus vite, je suppose..."
            


label choose_day: 

    "La journée est enfin terminée, Xavier est certainement toujours en colère..."
    "Ca fait [day] jours que vous survivez."

    if day == 2:
        jump Xavier_toc
    if day == 56:
        jump anniversaire_benoit
    if day == 94:
        jump anniversaire_arthur
    if day == 119:
        jump anniversaire_anne

    jump normal_day

label Xavier_toc:

        play sound "audio/sound_effect/bruit-de-porte-toc-toc.mp3"
        "On frappe à la porte, mais pas comme hier..."
        x "Les enfants ?"
        x "Je vais vous faire une offre."
        x "Vous ne pourrez pas survivre longtemps dans ce bunker avec si peu de réserve."
        x "Je vous propose donc de vous échanger votre fusil et ses balles contre 2 canettes de soupe et 3 bouteilles d'eau chacun."

        menu:
            x "Qu'en pensez-vous ?"
            "Donner le fusil et les balles" if nb_fusil != 0 and nb_balles != 0:
                x "Que vous êtes stupides !"
                show Xavier
                with hpunch
                x "DADDY IS HERE !"
                hide Benoit
                hide Anne
                hide Thomas
                hide Arthur
                scene black
                "Xavier a tué tous ses enfants de deux balles dans la tête."
                "La réalité a rattrapé la fiction."
                return
            "Donner le fusil uniquement" if nb_fusil != 0:
                x "Je trouverais bien les balles..."
                $ nb_fusil -= 1
                jump normal_day
            "Donner les balles uniquement" if nb_balles != 0:
                x "Vous êtes de petits malins... Vous ne m'échapperez pas longtemp."
                $ nb_balles -= 1
                jump normal_day
            "Ne rien donner":
                x "Vous regretterez cette décision."
                jump normal_day

label anniversaire_benoit:
    "Aujourd'hui c'est l'anniversaire de Benoît !"

    play sound "audio/sound_effect/bruit-de-porte-toc-toc.mp3"

    "On frappe à la porte... Mais ça ne ressemble pas à Xavier."
    "Prêtre" "Mes enfants, je saviez que vous étiez là !"
    "Prêtre" "J'ai remarqué la disparition de Benoît."
    "Prêtre" "Je peux le sauver.\nSi vous me le laissez, je le sortirai des griffes de votre père."
    "Prêtre" "Malheureusement, je ne peux que le prendre lui, mais à vous autre, je peux vous donner une boite de soupe et une bouteille d'eau chacun !"

    menu:
        "Libérer Benoît" if benoit == True and who_exp != "Benoit":
            "Prêtre" "Merci de votre confiance ! Viens, jeune homme."
            $ nb_child -= 1
            $ nb_soup += nb_child
            $ nb_eau += nb_child
            hide Benoit
            $ benoit = False
            if nb_radio != 0:
                "On entendit plus tard à la radio que Benoît avait subit les sévices sexuel du prêtre."
                "Il s'est suicidé."
            jump normal_day
        "Garder Benoît" if benoit == True and who_exp != "Benoit":
            "Prêtre" "Que Dieu vous vienne en aide."
            "Prêtre" "Tenez, prennez ma bible."
            $ nb_bible += 1
            jump normal_day
        "Benoît est malheureusement mort..." if benoit == False:
            "Prêtre" "J'arrive donc trop tard..."
            "Prêtre" "Que Dieu vous protège.\nPrenez donc ma bible, mon eau et ma soupe."
            $ nb_bible += 1
            $ nb_food += nb_child
            $ nb_eau += nb_child
            jump normal_day
        "Benoît n'est pas là." if who_exp == "Benoît":
            "Prêtre" "Ah bon ?"
            "Prêtre" "..."
            "Prêtre" "Je sens son odeur..."
            "Le prêtre a pris en chasse Benoît.\nIl l'a trouvé et nous n'avons plus jamais revu Benoît après avoir entendu son cri."
            $ benoit = False
            $ nb_child -= 1
            $ who_exp = "personne"
            $ explore = 0
            jump normal_day


label anniversaire_arthur:
    "Bon anniversaire Athur !"
    "Nous sommes le 7 juillet."

    if arthur == True:
        "Vous trouvez un papier coincé dans les briques du mur."
        "Cette note vous donne une recette pour transformer la poussière en eau."
        "Malheureusement cette recette ne fonctionnera qu'une fois."
        "Toutefois, vous gagnez quand même une bouteille chacun !"
        $ nb_eau += nb_child
    jump normal_day

label anniversaire_anne:
    "C'est l'anniversaire d'Anne !"
    "Déjà 17 ans ! Nous sommes le 2 août."

    if anne == True:
        play sound "audio/sound_effect/bruit-de-porte-toc-toc.mp3"
        "Tiens ? Ca frappe à la porte, mais différemment de quand Xavier le fait..."
        "Les voisins" ""
        

label manger:
    menu:
        "Vérifier l'alimentation de :"
        "Arthur" if arthur == True and who_exp != "Arthur":
            "Arthur peut tenir [arthur_eau] jours sans boire et [arthur_soup] jours sans manger."
            menu:
                "Nourrir Arthur" if arthur_soup != 10:
                    if nb_food == 0:
                        "Vous n'avez pas assez de soupe."
                        jump manger
                    $ arthur_soup = 10
                    $ nb_food -= 0.5
                "Hydrater Arthur" if arthur_eau != 5:
                    if nb_eau == 0:
                        "Vous n'avez pas assez d'eau."
                        jump manger
                    $ arthur_eau = 5
                    $ nb_eau -= 0.5
                "Ne rien faire":
                    jump manger
            jump manger
        "Thomas" if thomas == True and who_exp != "Thomas":
            "Thomas peut tenir [thomas_eau] jours sans boire et [thomas_soup] jours sans manger."
            menu:
                "Nourrir Thomas" if thomas_soup != 10:
                    if nb_food == 0:
                        "Vous n'avez pas assez de soupe."
                        jump manger
                    $ thomas_soup = 10
                    $ nb_food -= 0.5
                "Hydrater Thomas" if thomas_eau != 5:
                    if nb_eau == 0:
                        "Vous n'avez pas assez d'eau."
                        jump manger
                    $ thomas_eau = 5
                    $ nb_eau -= 0.5
                "Ne rien faire":
                    jump manger
            jump manger
        "Anne" if anne == True and who_exp != "Anne":
            "Anne peut tenir [anne_eau] jours sans boire et [anne_soup] jour sans manger."
            menu:
                "Nourrir Anne" if anne_soup != 10:
                    if nb_food == 0:
                        "Vous n'avez pas assez de soupe."
                        jump manger
                    $ anne_soup = 10
                    $ nb_food -= 0.5
                "Hydrater Anne" if anne_eau != 5:
                    if nb_eau == 0:
                        "Vous n'avez pas assez d'eau."
                        jump manger
                    $ anne_eau = 5
                    $ nb_eau -= 0.5
                "Ne rien faire":
                    jump manger
            jump manger
        "Benoît" if benoit == True and who_exp != "Benoit":
            "Benoît peut tenir [benoit_eau] jours sans boire et [benoit_soup] jours sans manger."
            menu:
                "Nourrir Benoît" if benoit_soup != 10:
                    if nb_food == 0:
                        "Vous n'avez pas assez de soupe."
                        jump manger
                    $ benoit_soup = 10
                    $ nb_food -= 0.5
                "Hydrater Benoît" if benoit_eau != 5:
                    if nb_eau == 0:
                        "Vous n'avez pas assez d'eau."
                        jump manger
                    $ benoit_eau = 5
                    $ nb_eau -= 0.5
                "Ne rien faire":
                    jump manger
            jump manger
        "Personne":
            jump normal_day

label mental:
    menu:
        "Vérifier la santé de :"
        "Arthur" if arthur == True and who_exp != "Arthur":
            "Arthur a [arthur_mental]\% de santé mental."
            if arthur_mental < 20:
                "Il serait peut-être bien de s'occuper d'Arthur, son état se dégrade..."
            menu:
                "Jouer avec Arthur" if nb_cartes != 0:
                    $ arthur_mental = 80
                    jump mental
                "Jouer pour Arthur" if nb_violon != 0:
                    $ arthur_mental = 100
                    jump mental
                "Lire des psaumes" if nb_bible != 0:
                    $ arthur_mental = 100 - day
                    "Arthur perd un peu plus la foi chaque jour qui passe, même si ça fait un peu de bien."
                    jump mental
                "Utiliser le kit médical" if nb_kit_med != 0:
                    "C'est une solution bien étrange..."
                    "Cependant Arthur a bien rit, il est plus stable mentalement que jamais"
                    "Par contre ce n'est pas le cas de Benoît qui est très anxieux dans ce bunker"
                    $ benoit_mental -= 30
                    $ nb_kit_med -= 1
                    $ arthur_mental = 200
                    jump mental
                "Ne rien faire":
                    jump mental
            jump mental
        "Thomas" if thomas == True and who_exp != "Thomas":
            "Thomas a [thomas_mental]\% de santé mental."
            menu:
                "Jouer avec Thomas" if nb_cartes != 0:
                    $ thomas_mental = 100
                    jump mental
                "Jouer pour Thomas" if nb_violon != 0:
                    $ thomas_mental = 30
                    "Cette mélodie est un peu triste pour Thomas, son truc c'est la batterie...'"
                    jump mental
                "Lire des psaumes" if nb_bible != 0:
                    $ thomas_mental = 80
                    jump mental
                "Utiliser le kit médical" if nb_kit_med != 0:
                    "C'est une solution bien étrange..."
                    "Cependant Thomas a bien rit, il est plus stable mentalement que jamais"
                    "Par contre ce n'est pas le cas de Benoît qui est très anxieux dans ce bunker"
                    $ benoit_mental -= 30
                    $ nb_kit_med -= 1
                    $ thomas_mental = 200
                    jump mental
                "Ne rien faire":
                    jump mental
            jump mental
        "Anne" if anne == True and who_exp != "Anne":
            "Anne a [anne_mental]\% de santé mental."
            menu:
                "Jouer avec Anne" if nb_cartes != 0:
                    $ anne_mental = 100 - (day + 5)
                    "Anne sent les regards sur elle quand elle joue..."
                    jump mental
                "Jouer pour Anne" if nb_violon != 0:
                    $ anne_mental = 90
                    jump mental
                "Lire des psaumes" if nb_bible != 0:
                    $ anne_mental = 80
                    jump mental
                "Utiliser le kit médical" if nb_kit_med != 0:
                    "C'est une solution bien étrange..."
                    "Cependant Anne a bien rit, il est plus stable mentalement que jamais"
                    "Par contre ce n'est pas le cas de Benoît qui est très anxieux dans ce bunker"
                    $ benoit_mental -= 30
                    $ nb_kit_med -= 1
                    $ anne_mental = 200
                    jump mental
                "Ne rien faire":
                    jump mental
            jump mental
        "Benoît" if benoit == True and who_exp != "Benoit":
            "Benoît a [benoit_mental]\% de santé mental."
            menu:
                "Jouer avec Benoît" if nb_cartes != 0:
                    $ benoit_mental = 150
                    "Benoît sent le sens de la famille monter en lui"
                    jump mental
                "Jouer pour Benoît" if nb_violon != 0:
                    $ benoit_mental = 50
                    jump mental
                "Lire des psaumes" if nb_bible != 0:
                    $ benoit_mental = 90
                    jump mental
                "Utiliser le kit médical" if nb_kit_med != 0:
                    "C'est une solution bien étrange..."
                    "Ca ne fait pas rire Benoît qui est déjà bien assez inquiet."
                    "Vous l'avez détruit psychologiquement, cela peut avoir des conséquences..."
                    $ nb_kit_med -= 1
                    $ benoit_mental = -100
                    jump mental
                "Ne rien faire":
                    jump mental
            jump mental
        "Personne":
            jump normal_day
    

label exploration:
    menu:
        "Qui est envoyé ?"
        "Benoît" if benoit == True:
            $ who_exp = "Benoit"
            hide Benoit
        "Anne" if anne == True:
            $ who_exp = "Anne"
            hide Anne
        "Thomas" if thomas == True:
            $ who_exp = "Thomas"
            hide Thomas
        "Arthur" if arthur == True:
            $ who_exp = "Arthur"
            hide Arthur
        "Personne":
            jump normal_day

    $ explore = renpy.random.randint(1,5)
    if explore > 1:
        "[who_exp] part pour [explore] jours d'exploration."
    else:
        "[who_exp] part pour [explore] jour d'exploration."


label normal_day: 

    if benoit == True:
        if benoit_soup == 0:
            "Benoît est mort de déshydratation"
            $ benoit = False
            $ nb_child -= 1
            hide Benoit
    if anne == True:
        if anne_soup == 0:
            "Anne est morte de déshydratation"
            $ anne = False
            $ nb_child -= 1
            hide Anne
    if thomas == True:
        if thomas_soup == 0:
            "Thomas est mort de déshydratation"
            $ thomas = False
            $ nb_child -= 1
            hide Thomas
    if arthur == True:
        if arthur_soup == 0:
            "Arthur est mort de déshydratation"
            $ arthur = False
            $ nb_child -= 1
            hide Arthur

    if benoit == True:
        if benoit_eau == 0:
            "Benoît est mort de déshydratation"
            $ benoit = False
            $ nb_child -= 1
            hide Benoit
    if anne == True:
        if anne_eau == 0:
            "Anne est morte de déshydratation"
            $ anne = False
            $ nb_child -= 1
            hide anne
    if thomas == True:
        if thomas_eau == 0:
            "Thomas est mort de déshydratation"
            $ thomas = False
            $ nb_child -= 1
            hide Thomas
    if arthur == True:
        if arthur_eau == 0:
            "Arthur est mort de déshydratation"
            $ arthur = False
            $ nb_child -= 1
            hide Arthur

    if arthur == False: 
        if thomas == False:
            if anne == False:
                if benoit == False:
                    scene black
                    "Toute la famille est morte.\nVous n’avez pas survécu à Xavier."
                    return 

    menu:
        "Voulez-vous faire une action particulière ?"
        "Regarder les stats d’alimentation et d’hydratation": 
            jump manger 
        "Vérifier la santé de la fraterie": 
            jump mental 
        "Envoyer quelqu’un explorer la maison cette nuit" if explore == 0:
            jump exploration
        "Finir la journée": 
            jump normal_day_next

label normal_day_next:
    if benoit == True:
        if who_exp != "Benoit":
            $ benoit_eau -= 1
            $ benoit_soup -= 1
            $ benoit_mental -= 5
    if anne == True:
        if who_exp != "Anne":
            $ anne_eau -= 1
            $ anne_soup -= 1
            $ anne_mental -= 5
    if thomas == True:
        if who_exp != "Thomas":
            $ thomas_eau -= 1
            $ thomas_soup -= 1
            $ thomas_mental -= 5
    if arthur == True:
        if who_exp != "Arthur":
            $ arthur_eau -= 1
            $ arthur_soup -= 1
            $ arthur_mental -= 5

    if anne_mental < 20 or benoit_mental < 20 or thomas_mental < 20 or arthur_mental < 20:
        "L'un des enfants est fou... Quelqu'un a mangé 2 boites de soupes pendant que tout le monde dormait."
        "Les enfants deviennent méfiants entre eux..."
        $ anne_mental -= 20
        $ arthur_mental -= 20
        $ thomas_mental -= 20
        $ benoit_mental -= 20
        $ nb_food -= 2
        if nb_food < 0:
            $ nb_food = 0
        "Il vous reste maintenant [nb_food] soupes, on espère pouvoir tenir avec ça..."

    $ day += 1
    if explore != 0:
        $ explore -= 1
        $ xavier_found_you = renpy.random.randint(0,(20 - explore))
        if xavier_found_you == 2:
            "[who_exp] met trop de temps à revenir..."
            "On a entendu un hurlement tout à l'heure, ça fait un survivant de moins..."
            if who_exp == "Benoit":
                $ benoit = False
                $ nb_child -= 1
            if who_exp == "Anne":
                $ anne = False
                $ nb_child -= 1
            if who_exp == "Thomas":
                $ thomas = False
                $ nb_child -= 1
            if who_exp == "Arthur":
                $ arthur = False
                $ nb_child -= 1
            $ explore = 0
            $ who_exp = "personne"
        if explore == 0 and who_exp != "personne":
            if who_exp == "Benoit":
                "Benoît est revenu d'exploration."
                $ benoit_mental = 100
                $ benoit_eau = 5
                $ who_exp = "personne"
                show Benoit:
                    xalign 0.2
                    yalign 0.8
            if who_exp == "Anne":
                "Anne est revenue d'exploration."
                $ anne_mental = 100
                $ anne_eau = 5
                $ who_exp = "personne"
                show Anne:
                    xalign 0.4
                    yalign 0.8
            if who_exp == "Thomas":
                "Thomas est revenu d'exploration."
                $ thomas_mental = 100
                $ thomas_eau = 5
                $ who_exp = "personne"
                show Thomas:
                    xalign 0.6
                    yalign 0.8
            if who_exp == "Arthur":
                "Arthur est revenu d'exploration."
                $ arthur_mental = 100
                $ arthur_eau = 5
                $ who_exp = "personne"
                show Arthur:
                    xalign 0.8
                    yalign 0.8
            "Sortir a permis à [who_exp] de s'aérer l'esprit, il a refait le plein de santé mental."
            $ nb_food += renpy.random.randint(0,3)
            $ nb_eau += renpy.random.randint(0,5)
            "Vous avez [nb_food] soupes et [nb_eau] bouteilles d'eau après cette expédition."
    jump choose_day