import time
import booths
import random

from booths import glasses, jacket, walkman, horan, starting


def print_greeting(location):
    print("--------------------------------------------------")
    print("WELCOME TO {} PEDDLER'S MALL, ADVENTURER".format(location.upper()))
    print("--------------------------------------------------")

    time.sleep(3)

    print("You find yourself standing in a cold, dark, and desolate atrium.  The light of dusk shines "
          "through the glass double doors.\n")

    time.sleep(3)

    print("Suddenly, in the silence, a din of flapping wings approaches your position.\n")

    print("You look above and see Agatha Christie and James Patterson novels flying "
          "about, pursuing Little Golden Books which fall to the ground when "
          "their pages are filled with pecking holes.")


def get_name():
    name = input("What is your name adventurer: ")
    while name == '':
        name = input("What is your name adventurer: ")
        if not name:
            print("You must enter a name of some kind.")
    return name


def describe_booth(pl_x, pl_y):
    if (pl_y, pl_x) == (booths.glasses.y, booths.glasses.x):
        glasses.intro_text()
    elif (pl_y, pl_x) == (booths.jacket.y, booths.jacket.x):
        jacket.intro_text()
    elif (pl_y, pl_x) == (booths.walkman.y, booths.walkman.x):
        walkman.intro_text()
    elif (pl_y, pl_x) == (booths.horan.y, booths.horan.x):
        horan.intro_text()
    elif (pl_y, pl_x) == (booths.starting.y, booths.starting.x):
        starting.intro_text()
    else:
        curr_empty = random.choice(booths.empties)
        curr_empty.intro_text()


def interact_booth(pl_x, pl_y, player):
    if (pl_y, pl_x) == (booths.glasses.y, booths.glasses.x):
        glasses.glasses_puzzle(player)
    elif (pl_y, pl_x) == (booths.jacket.y, booths.jacket.x):
        jacket.jacket_puzzle(player)
    elif (pl_y, pl_x) == (booths.walkman.y, booths.walkman.x):
        walkman.walkman_puzzle(player)
    elif (pl_y, pl_x) == (booths.horan.y, booths.horan.x):
        print("An ominous door is here.  Fog of a milky yellow color rolls from beneath.\n")
        door_input = input("Do you [o]pen the door? ")
        if door_input.upper() == 'O':
            horan.battle_horan(player)
        else:
            print("You back away from the door")

    else:
        return -1
