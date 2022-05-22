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
    $ nb_child = 0
    $ is_down = 0

    $ max_food = 10
    $ max_drink = 10

    $ soup_1 = 0
    $ soup_2 = 0
    $ soup_3 = 0
    $ soup_4 = 0

    $ arthur == True
    $ thomas == True
    $ anne == True
    $ benoit == True


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

# The game starts here.

label hall:
    scene hall
    pause 0.5
    show screen arrow_hall
    show screen items_hall
    screen items_hall:
        imagebutton:
            xpos 0
            ypos 0
            idle "empty.png"
            at custom_zoom
            action [Jump("add_soup")]
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


label choose_day: 

	# faire l’aléatoire sur les jours avec des if et un else qui renvoi à normal_day 

 

label expedition: 

	 

 

label normal_day: 

	if day%10 == 0: 

		if benoit_soup == 0:
			"Benoît est mort de faim"
			benoit = False
            hide Benoit
		if anne_soup == 0:
			"Anne est morte de faim"
			anne = False
            hide Anne
		if thomas_soup == 0:
			"Thomas est mort de faim"
			thomas = False
            hide Thomas
		if arthur_soup == 0:
			"Arthur est mort de faim"
			arthur = False
            hide Thomas

	if day%5 == 0:

		if benoit_eau == 0:
			"Benoît est mort de déshydratation"
			benoit = False
		if anne_eau == 0:
			"Anne est morte de déshydratation"
			anne = False
		if thomas_eau == 0:
			"Thomas est mort de déshydratation"
			thomas = False
		if arthur_eau == 0:
			"Arthur est mort de déshydratation"
			arthur = False 

	if arthur == False && thomas == False && anne == False && benoit == False:

		scene black
		"Toute la famille est morte.\nVous n’avez pas survécu à Xavier."
		return 

	menu:
		"Voulez-vous faire une action particulière ?"
		"Regarder les stats d’alimentation et d’hydratation": 
			jump manger 
		"Vérifier la santé mental": 
			jump mental 
		"Envoyer quelqu’un explorer la maison cette nuit": 
			$ explore = renpy.random.randint(1,3)		 
        "Finir la journée": 
            jump choose_day 

	    if explore != 0:

            menu:
                "Qui est envoyé ?"
                 "Benoît" if benoit == True: 