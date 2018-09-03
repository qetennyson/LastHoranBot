import random
import time
import booths
import sys
from ped_locations import peddlers_locations
from player import Player

import game_functions as gf


# todo: async work remains :| oof

def main():
    location = random.choice(peddlers_locations)

    gf.print_greeting(location)

    player = Player(gf.get_name())

    game_loop(player)


def game_loop(player):
    time.sleep(2)

    print("Make haste, {}, you sense great danger here.".format(player.name))
    booths.pause_text()

    while True:

        pl_y = player.position_y
        pl_x = player.position_x

        gf.describe_booth(pl_y, pl_x)

        cmd = input("Do you move [N, S, E, W], [l]ook around or [q]uit?")
        print()

        if cmd.upper() == 'N':
            player.move_north()

        elif cmd.upper() == 'S':
            player.move_south()

        elif cmd.upper() == 'E':
            player.move_east()

        elif cmd.upper() == 'W':
            player.move_west()

        elif cmd.upper() == 'L':

            gf.interact_booth(pl_y, pl_x, player)

        elif cmd.upper() == 'Q':
            print("Goodbye.")
            sys.exit()

        else:
            print("You must do something.  \n")

            time.sleep(2)
            print("A wicked screeching, like fingernails on "
                  "chalkboard, draws closer...")
            print()


if __name__ == '__main__':
    main()
