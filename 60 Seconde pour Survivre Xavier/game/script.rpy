# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("TEMP NOT DEFINED")
define x = Character("Xavier")
define a = Character("Arthur")
define t = Character("Thomas")
define A = Character("Anne")
define b = Character("Benoît")

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])

    side "tl":
        text str(time)

init:
    $ timer_range = 0
    $ timer_jump = 0

label menu1:
    $ time = 60
    $ timer_range = 5
    $ timer_jump = 'menu1_slow'
    show screen countdown
    menu:
        "Choice 1":
            hide screen countdown
            e "You chose 'Choice 1'"
            jump menu1_end
        "Choice 2":
            hide screen countdown
            e "You chose 'Choice 2'"
            jump menu1_end

label menu1_slow:
    e "You didn't choose anything."

label menu1_end:
    e "Anyway, let's do something else."

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    jump menu1

    # These display lines of dialogue.

    x "Bienvenu dans mon jeu..."


    # This ends the game.

    return
