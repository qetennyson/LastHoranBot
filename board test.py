class Board(list):

    def __str__(self):
        return "\n".join(" ".join(row) for row in self)


class Game(object):
    MARKER_X = "X"
    MARKER_O = "O"
    CTRLS = [
        "left",
        None,
        "right",
        "up",
        None,
        "down",
    ]

    EXIT = "stop"
    START = [2, 2]
    DEFAULT = [["O"] * 4 for _ in range(4)]

    def __init__(self):
        self.flag = True
        self.arena = Board(Game.DEFAULT)
        self.prev_pos = Game.START[:]
        self.curr_pos = Game.START[:]
        self.move_player()

    def move_player(self):
        px, py = self.prev_pos  # Split apart the previous x and y coordinates
        cx, cy = self.curr_pos  # Split apart the current x and y coordinates
        if (- 1 < cx < 4) and (-1 < cy < 4):  # Check to make sure our coordinates are valid.
            self.arena[py][px] = Game.MARKER_O  # Set the previous position to empty.
            self.arena[cy][cx] = Game.MARKER_X  # Set our current position to our marker.

        else:
            print("Please enter a proper direction.")  # Notify the player.
            self.curr_pos = self.prev_pos[:]  # The "new" position becomes the old position.
            self.move_player()

    def play(self):
        print(" You are: \nX")
        while self.flag:
            print(str(self.arena))
            ctrl = input("Move left, right, up, down, or stop").lower()
            if ctrl in Game.CTRLS:
                d = Game.CTRLS.index(ctrl)
                self.prev_pos = self.curr_pos[:]
                self.curr_pos[d > 2] += d - (1 if d < 3 else 4)
            elif ctrl == Game.EXIT:
                self.flag = False
            else:
                print("Please enter a proper direction.")

my_game = Game()
my_game.play()