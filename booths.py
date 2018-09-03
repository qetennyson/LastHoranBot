import random
import time
import sys


def pause_text():
    time.sleep(2)
    print("...")
    time.sleep(2)


# Define the Booth superclass.
class Booth:

    def __init__(self, name, y, x):
        self.name = name
        self.y = y
        self.x = x

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()


# The subclass for any "empty" space.
class EmptyBooth(Booth):

    def __init__(self, name, y, x):
        super().__init__(name, y, x)

    def intro_text(self):
        descriptions = ["An empty section of the mall, an overwhelming scent of "
                        "old coffee, moth balls, and odorous perfumes engulfs you..",
                        "A desolate area with little of note, on the floor lies"
                        "broken off price tags, roach carcasses, and the occasional Beanie Baby™",
                        "Nothing here but cobwebs and broken dreams of peddling age old goods."]

        print(random.choice(descriptions))

    def modify_player(self, player):
        pass


# The subclass for the starting space.
class StartingBooth(Booth):

    def __init__(self, name, y, x):
        super().__init__(name, y, x)

    def intro_text(self):
        print("You find yourself in the atrium.  The light from outside "
              "grows dimmer by the minute.")

    def modify_player(self, player):
        pass


# The subclass for the glasses booth.
class GlassesBooth(Booth):

    def __init__(self, name, y, x):
        super().__init__(name, y, x)

    def intro_text(self):
        print("A booth of extraordinary height.  Stretching up for miles,"
              "are rows and rows of glasses")

    def modify_player(self, player):
        player.has_glasses = True
        print("The glasses before you shake violently in their cradle.")
        pause_text()
        print()
        print("Suddenly, the shaking glasses explode into a cloud of dust.")
        print("Only one pair remains.  The Ray-Bans.  You put them on.\n")
        pause_text()
        print("As soon as your eyes meet the lenses, the clarity of your vision increases immensely.")
        print("You feel like you could see white rice on a paper plate in a snow storm.")

    def glasses_puzzle(self, player):

        if not player.has_glasses:
            pause_text()
            print("There are so many rows of glasses, it's hard to choose a pair.")
            pause_text()
            print("Part of you questions even putting a pair on, but something draws you in, inviting you to try.")

            while True:
                look_closer = input("Do you [l]ook closer or [n]ot?")

                if look_closer == "l":
                    print("You see writing on the wall next to you: UDB EDQ\n")
                    print("Below the letters are 3 Roman Figurines\n")

                    while True:
                        print("A tablet lights up in front of your face with a keyboard.")
                        pause_text()
                        print("You can enter any letters, in any order.")
                        print("Type QUIT to give up")

                        entry = input("What do you enter? ")
                        if entry.upper() == 'QUIT':
                            break
                        elif entry.upper() == 'RAY BAN':
                            print("The tablet blinks green.")
                            time.sleep(1)
                            glasses.modify_player(player)
                            break
                        else:
                            print("Nothing happens...")
                            time.sleep(1)


                else:
                    print("You take a step back, still in the room but further from the glasses.")
                    break
            else:
                print("You sense you've accomplished what's necessary in this booth.")


# The subclass for the jacket booth.
class JacketBooth(Booth):

    def __init__(self, name, y, x):
        super().__init__(name, y, x)

    def intro_text(self):
        print("A booth of extraordinary length.  Stretching on for what could,"
              "be infinite space are jackets and hoodies of every sort in every color.")

    def modify_player(self, player):
        player.has_jacket = True
        print("The jackets begin to drip like paint on their hangers.")
        time.sleep(2)
        print()
        print("Only one jacket remains.  It's bright orange, an odd color choice perhaps, but you are enticed.\n")
        time.sleep(1)
        print("As you pull yours arms through the sleeves, you feel an intense feeling of security")
        print("It seems like nothing could damage the leather of this jacket.")

    def jacket_puzzle(self, player):

        if not player.has_jacket:
            time.sleep(2)
            print("There are so many jackets, it's hard to know where to begin.")
            print()
            time.sleep(1)
            print("You feel overwhelmed by the sheer size of the room, but feel drawn to touch the jackets.")
            print()

            while True:
                look_closer = input("Do you [l]ook closer or [n]ot?")

                if look_closer == "l":
                    print("One of the jackets is particularly interesting.  It's logo says: FF8C00\n")
                    print("In the left breast pocket are two coloring pens.\n")

                    while True:
                        print("A canvas appears on the counter in front of you.")
                        print("Next to it appears a palette of paints with a brush.  What color do you start with?")
                        print("Type QUIT to give up")

                        entry = input("What do you enter? ")
                        if entry.upper() == 'QUIT':
                            break
                        elif entry.upper() == 'ORANGE':
                            print("The canvas absorbs the paint.. and a beautiful sunset appears.")
                            jacket.modify_player(player)
                            break
                        else:
                            print("The canvas absorbs the paint.. but as though by magic, goes blank again.")
                            time.sleep(1)


                else:
                    print("You take a step back, still in the room but further from the jackets.")
                    break
        else:
            print("You sense you've accomplished what's necessary in this booth.")


# The subclass for the walkman booth.
class WalkmanBooth(Booth):

    def __init__(self, name, y, x):
        super().__init__(name, y, x)

    def intro_text(self):
        print("A booth filled with a cacophony of sound.  You are"
              "surrounded by music devices from every generation.  iPods, CD Players,"
              "boom boxes, walkmans, and every audio accessory imaginable fills"
              "this booth to the brim.")

    def modify_player(self, player):
        player.has_walkman = True
        print("The invigorating power of the world's greatest electronic artists fills your ears.")
        pause_text()
        print("'There's not much I know about you'\n")
        print("'Fear will always make you blind'\n")
        print("'But the answer is in clear view'\n")
        print("'It's amazing what you'll find face to face'\n")

    def walkman_puzzle(self, player):

        if not player.has_walkman:
            time.sleep(2)
            print("The booth overwhelms you with sound.  It's hard to focus... "
                  "the gross mash-up of a thousand genres makes you nauseous.")
            print()
            time.sleep(1)
            print("As the music blares on, you're fascinated by a beautiful spectrum of retro music players.")
            print()

            while True:
                look_closer = input("Do you [l]ook closer or [n]ot?")

                if look_closer == "l":
                    print("You search for something to cover your ears so you can concentrate. \n")
                    pause_text()
                    print("You pick up a huge pair of headphones and place them on your ears.\n")
                    pause_text()
                    print("The sounds of the booth subside, and give way to a vigorous, but pleasant beat\n")
                    pause_text()
                    print("The lyrics become clearer, but repeat in a strange way\n")
                    pause_text()
                    print("'There's not much I know about you'\n")
                    print("'Fear will always make you blind'\n")

                    while True:
                        print("A drum pad appears, and the letters of the alphabet cover each button.\n")
                        pause_text()
                        print("You tap a couple of letters, and different beats play.\n")
                        print("The letters remain lit up as you tap them.\n")
                        print("Type QUIT to give up")

                        entry = input("What letters do you tap? ")
                        if entry.upper() == 'QUIT':
                            break
                        elif entry.upper() == 'DAFT PUNK':
                            print("The nauseating mash-up ceases... \n")

                            time.sleep(1)
                            walkman.modify_player(player)
                            break
                        else:
                            print("Carly Rae Jepsen sings off-tune runs for 15 seconds, and you barely survive.\n")
                            time.sleep(1)


                else:
                    print("You take a step back, still in the room but further from the music.")
                    break
        else:
            print("You sense you've accomplished what's necessary in this booth.")


# The subclass for the horan booth.
class HoranBooth(Booth):

    def __init__(self, name, y, x):
        super().__init__(name, y, x)

    def intro_text(self):
        pass

    def modify_player(self, player):
        pass

    def battle_horan(self, player):

        print("You turn the knob and open the door, fog rolls out into the floor")
        pause_text()
        print("Standing before you is Mr. Horan, but it is not the Mr. Horan you know.")
        print("He has been overtaken by some great corruption, and as you enter the "
              " room he looks at you with great ire.")
        player_status = horan.check_player(player)
        for status in player_status:
            pause_text()
            print(status + "\n")

        if player.has_glasses and player.has_walkman and player.has_jacket:
            time.sleep(3)
            print("Your ingenuity and perseverance has served its purpose.")
            pause_text()
            print("The glasses, jacket, and walkman fade from existence.")
            pause_text()
            print("You are standing in Mr. Horan's Lab, and Mr. Horan is sitting quietly in his chair")
            pause_text()
            print("Mr. Horan looks up and sees you, he has a smile on his face and holds out his hand")
            pause_text()
            print("With hesitation, you reach out to shake it.")
            pause_text()
            print("You feel safe and sound once again, the Mr. Horan you knew is back.")
            pause_text()
            print("He speaks: '{} I am so proud of the work you've done.  Thank you for "
                  "getting things back in order.  As a reward, please take this'".format(player.name))
            pause_text()
            print("Mr. Horan hands you a laptop computer.")
            pause_text()
            print("'Now, {}, go get the world in order.".format(player.name))
            pause_text()
            print("I hope you had fun, and learned a little with this easter egg I made.  That's what this thing called"
                  " education really is about, anyway.  See you next year!  - Mr. Tennyson")
            pause_text()
            print("THE END")
            sys.exit()
        else:
            print("If you stay here you will be destroyed.  You run from the room in terror.")

    def check_player(self, player):
        responses = []

        walk_lose = "The Mr. Horan creature shouts, and the pain in your ears is too much to take." \
                    "You have to leave."
        walk_win = "The Mr. Horan creature shouts, but the music emanating from your walkman protects your ears."

        glass_lose = "The fog is too thick.  You can see nothing.  In the chaos, you find yourself " \
                     "running in circles."

        glass_win = "The fog is thick, but with your glasses you can see clearly.  The Mr. Horan creature" \
                    "looms over you, but something is different about him."

        jacket_lose = "The Mr. Horan creature flings books, markers, and PC parts at you like a " \
                      "hurricane.  You cannot fight through the onslaught."

        jacket_win = "The Mr. Horan creature flings books and markers, but they bounce off of the jacket" \
                     "and you feel nothing.  You power through, closer to the creature."

        if player.has_walkman:
            for entry in responses:
                if entry == walk_lose:
                    responses.remove(entry)
            responses.append(walk_win)
        else:
            responses.append(walk_lose)

        if player.has_glasses:
            for entry in responses:
                if entry == glass_lose:
                    responses.remove(entry)
            responses.append(glass_win)
        else:
            responses.append(glass_lose)

        if player.has_jacket:
            for entry in responses:
                if entry == jacket_lose:
                    responses.remove(entry)
            responses.append(jacket_win)
        else:
            responses.append(jacket_lose)

        return responses


# Initialize all booths

empty0 = EmptyBooth("Darkness", 0, 1)
empty1 = EmptyBooth("Darkness", 0, 2)
empty2 = EmptyBooth("Darkness", 1, 0)
empty3 = EmptyBooth("Darkness", 1, 2)
empty4 = EmptyBooth("Darkness", 1, 3)
empty5 = EmptyBooth("Darkness", 2, 0)
empty6 = EmptyBooth("Darkness", 2, 3)

empties = [
    empty0,
    empty1,
    empty2,
    empty3,
    empty4,
    empty5,
    empty6
]

glasses = GlassesBooth("A booth with a door displaying ornate spectacles", 0, 0)
horan = HoranBooth("A sinister door with fog rolling out", 1, 1)
starting = StartingBooth("The atrium", 0, 2)
jacket = JacketBooth("A booth with a door.  A weathered leather jacket hangs on the knob", 2, 1)
walkman = WalkmanBooth("A shiny chrome door leading into what looks like a booth.", 2, 2)

game_booths = [[glasses, empty0, starting, empty1],
               [empty2, horan, empty3, empty4],
               [empty5, jacket, walkman, empty6]
               ]
