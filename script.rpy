# CHARACTERS

define a = Character("Amara")
define n = Character("Naomi")
define e = Character("Elijah")

# GAME STARTS HERE

label start:

    scene bg room

    # CHARACTERS APPEAR
    show eileen happy

    a "Finally, school is over."

    a "I swear this week has been exhausting."

    n "You've literally been saying that since Monday."

    a "And I'll keep saying it until Friday."

    # ELIJAH ENTERS
    show eileen happy

    e "Hey. Are you Amara?"

    a "Yeah? Do I know you?"

    e "Not exactly. I'm Elijah. I'm new here."

    n "Oh, you're the new student everyone has been talking about."

    e "I guess that's me."

    a "Well, welcome to the chaos."

    # PLAYER CHOICE
    menu:

        "What should Amara do?"

        "Invite Elijah to sit with them":

            a "You can sit with us if you want."

            e "Thanks. I appreciate it."

            n "Just don't steal my fries."

            e "I'll try my best."

        "Ask why he transferred":

            a "So, what brought you here?"

            e "It's a long story."

            n "That's suspicious."

            e "Maybe I'll tell you eventually."

    # ENDING
    a "Something tells me this year is going to be interesting."

    e "You have no idea."

    return