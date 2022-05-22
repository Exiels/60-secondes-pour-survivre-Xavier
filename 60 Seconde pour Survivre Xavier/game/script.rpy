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
    $ nb_drink = 0
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
    $ nb_child = 0
    $ is_down = 0

    $ max_food = 10
    $ max_drink = 10
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
    $ lit_1 = 0
    $ lit_1 = 0
    $ lit_1 = 0

    $ radio_1 = 0

    $ sac_1 = 0
    $ sac_1 = 0

    $ table_1 = 0

    $ violon_1 = 0

    $ child_1 = 0
    $ child_1 = 0
    $ child_1 = 0
    $ child_1 = 0

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

label add_water:
    if nb_water < max_water:
        $ nb_water += 1
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
    show screen items_hall
    screen items_hall:
        imagebutton:
            xpos 950
            ypos 450
            idle "items/balles.png"
            at custom_zoom
            action [Jump("add_balles")]
    screen arrow_hall:
        imagebutton:
            xpos 1130
            ypos 100
            idle "arrow/arrow_left.png"
            at custom_zoom
            action [Hide("arrow_hall"), Hide("items_hall"), Jump("chambre")]
        imagebutton:
            xpos 1300
            ypos 100
            idle "arrow/arrow_right.png"
            at custom_zoom
            action [Hide("arrow_hall"), Hide("items_hall"), Jump("salle_de_bain")]
        imagebutton:
            xpos 750
            ypos 500
            idle "arrow/arrow_top.png"
            at custom_zoom
            action [Hide("arrow_hall"), Hide("items_hall"), Jump("bunker")]
        imagebutton:
            xpos 150
            ypos 600
            idle "arrow/arrow_left.png"
            at custom_zoom
            action [Hide("arrow_hall"), Hide("items_hall"), Jump("salon")]
        imagebutton:
            xpos 1650
            ypos 600
            idle "arrow/arrow_right.png"
            at custom_zoom
            action [Hide("arrow_hall"), Hide("items_hall"), Jump("salle_a_manger")]
    jump continue


label chambre:
    scene chambre
    pause 0.5
    screen items_chambre:
        imagebutton:
            xpos 0
            ypos 0
            idle "empty.png"
            at custom_zoom
            action [Jump("add_soup")]
    screen arrow_chambre:
        imagebutton:
            xpos 150
            ypos 500
            idle "arrow/arrow_left.png"
            at custom_zoom
            action [Hide("arrow_chambre"), Hide("items_chambre"), Jump("hall")]
    show screen arrow_chambre
    show screen items_chambre
    jump continue

label bunker:
    play music "audio/BGM/stress.mp3" fadeout 1
    play sound "audio/sound_effect/bruit-de-porte-toc-toc.mp3"
    scene bunker
    $ bunker = 1
    jump continue

label cuisine:
    scene cuisine
    pause 0.5
    screen items_cuisine:
        imagebutton:
            xpos 0
            ypos 0
            idle "empty.png"
            at custom_zoom
            action [Jump("add_soup")]
    screen arrow_cuisine:
        imagebutton:
            xpos 1700
            ypos 600
            idle "arrow/arrow_right.png"
            at custom_zoom
            action [Hide("arrow_cuisine"), Hide("items_cuisine"), Jump("salle_a_manger")]
        imagebutton:
            xpos 100
            ypos 600
            idle "arrow/arrow_left.png"
            at custom_zoom
            action [Hide("arrow_cuisine"), Hide("items_cuisine"), Jump("salon")]
    show screen arrow_cuisine
    show screen items_cuisine
    jump continue

label salle_a_manger:
    scene salle_a_manger
    pause 0.5
    screen items_sam:
        imagebutton:
            xpos 0
            ypos 0
            idle "empty.png"
            at custom_zoom
            action [Jump("add_soup")]
    screen arrow_sam:
        imagebutton:
            xpos 950
            ypos 900
            idle "arrow/arrow_bot.png"
            at custom_zoom
            action [Hide("arrow_sam"), Hide("items_sam"), Jump("hall")]
        imagebutton:
            xpos 100
            ypos 600
            idle "arrow/arrow_left.png"
            at custom_zoom
            action [Hide("arrow_sam"), Hide("items_sam"), Jump("cuisine")]
    show screen arrow_sam
    show screen items_sam
    jump continue

label salle_de_bain:
    scene salle_de_bain
    pause 0.5
    screen items_sdb:
        imagebutton:
            xpos 0
            ypos 0
            idle "empty.png"
            at custom_zoom
            action [Jump("add_soup")]
    screen arrow_sdb:
        imagebutton:
            xpos 100
            ypos 600
            idle "arrow/arrow_left.png"
            at custom_zoom
            action [Hide("arrow_hall"), Hide("items_hall"), Jump("hall")]
    show screen arrow_sdb
    show screen items_sdb
    jump continue

label salon:
    scene salon
    pause 0.5
    screen items_salon:
        if soup_1 == 0:
            imagebutton:
                xpos 190
                ypos 450
                idle "items/soup.png"
                at custom_zoom
                action [SetVariable("soup_1", soup_1 + 1), Jump("add_soup")]
    screen arrow_salon:
        imagebutton:
            xpos 1700
            ypos 600
            idle "arrow/arrow_right.png"
            at custom_zoom
            action [Hide("arrow_cuisine"), Hide("items_cuisine"), Jump("hall")]
        imagebutton:
            xpos 100
            ypos 600
            idle "arrow/arrow_left.png"
            at custom_zoom
            action [Hide("arrow_cuisine"), Hide("items_cuisine"), Jump("salle_a_manger")]
    show screen arrow_salon
    show screen items_salon
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


# label choose_day: 
# 
# 	# faire l’aléatoire sur les jours avec des if et un else qui renvoi à normal_day

label exploration:
    $explore = renpy.random.randint(1,5)
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

    if explore > 1:
        "{who_exp} part pour {explore} jours d'exploration."
    else:
        "{who_exp} part pour {explore} jour d'exploration."


label normal_day: 

    if day % 10 == 0: 

        if benoit_soup == 0:
            "Benoît est mort de faim"
            $ benoit = False
            hide Benoit
        if anne_soup == 0:
            "Anne est morte de faim"
            $ anne = False
            hide Anne
        if thomas_soup == 0:
            "Thomas est mort de faim"
            $ thomas = False
            hide Thomas
        if arthur_soup == 0:
            "Arthur est mort de faim"
            $ arthur = False
            hide Thomas

    if day % 5 == 0:

        if benoit_eau == 0:
            "Benoît est mort de déshydratation"
            $ benoit = False
            hide Benoit
        if anne_eau == 0:
            "Anne est morte de déshydratation"
            $ anne = False
            hide Anne
        if thomas_eau == 0:
            "Thomas est mort de déshydratation"
            $ thomas = False
            hide Thomas
        if arthur_eau == 0:
            "Arthur est mort de déshydratation"
            $ arthur = False
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
        "Vérifier la santé mental": 
            jump mental 
        "Envoyer quelqu’un explorer la maison cette nuit" if explore != 0:
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

    $ day += 1
    if explore != 0:
        $ explore -= 1
        if explore == 0:
            if who_exp == "Benoit":
                "Benoît est revenu d'exploration."
                $ benoit_mental = 100
                show Benoit
            if who_exp == "Anne":
                "Anne est revenue d'exploration."
                $ anne_mental = 100
                show Anne
            if who_exp == "Thomas":
                "Thomas est revenu d'exploration."
                $ thomas_mental = 100
                show Thomas
            if who_exp == "Arthur":
                "Arthur est revenu d'exploration."
                $ arthur_mental = 100
                show Arthur
            "Sortir a permis à {who_exp} de s'aérer l'esprit, il a refait le plein de santé mental."
            $ who_exp = "personne"