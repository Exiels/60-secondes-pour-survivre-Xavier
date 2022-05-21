# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("TEMP NOT DEFINED")
define x = Character("Xavier")
define a = Character("Arthur")
define t = Character("Thomas")
define A = Character("Anne")
define b = Character("Benoît")

# Define Image Scenes
image hall = im.Scale("house/hall.jpg", 1920, 1080)
image bunker = im.Scale("house/bunker.jpg", 1920, 1080)

screen countdown:
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

screen soup:
    if soup_1 == 0:
        imagebutton:
            xpos 190
            ypos 450
            idle "soup.png"
            at custom_zoom
            action [SetVariable("soup_1", soup_1 + 1), Jump("add_soup")]
    if soup_2 == 0:
        imagebutton:
            xpos 490
            ypos 450
            idle "soup.png"
            at custom_zoom
            action [SetVariable("soup_2", soup_1 + 1), Jump("add_soup")]
    if soup_3 == 0:
        imagebutton:
            xpos 790
            ypos 450
            idle "soup.png"
            at custom_zoom
            action [SetVariable("soup_3", soup_1 + 1), Jump("add_soup")]
    if soup_4 == 0:
        imagebutton:
            xpos 1090
            ypos 450
            idle "soup.png"
            at custom_zoom
            action [SetVariable("soup_4", soup_1 + 1), Jump("add_soup")]

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    "Ce jeu est basé sur des fait réels..."

    scene hall
    jump continue

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    label continue:

        show screen countdown
        show screen infos
        show screen soup

        # These display lines of dialogue.

        pause

    # This ends the game.

    return
