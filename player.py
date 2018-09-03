class Player():

    def __init__(self, name):
        self.position_y = 0
        self.position_x = 2
        self.name = name
        self.has_glasses = False
        self.has_jacket = False
        self.has_walkman = False

    # todo: refactor movement to one function, and refactor main to reflect with error handling

    def __repr__(self):
        return "You are {}, doomed servant of the Peddlers.".format(self.name)

    def move_north(self):
        y = self.position_y
        x = self.position_x
        n_pos = y + 1

        if (-1 < n_pos < 3) and (-1 < x < 3):
            self.position_y = n_pos
            self.position_x = x
        else:
            print("You can go no further in this direction.")
            self.position_y = y
            self.position_x = x

    def move_south(self):
        y = self.position_y
        x = self.position_x
        s_pos = y - 1

        if (-1 < s_pos < 3) and (-1 < x < 3):
            self.position_y = s_pos
            self.position_x = x
        else:
            print("You can go no further in this direction.")
            self.position_y = y
            self.position_x = x

    def move_east(self):
        y = self.position_y
        x = self.position_x
        e_pos = x + 1

        if (-1 < y < 3) and (-1 < e_pos < 4):
            self.position_y = y
            self.position_x = e_pos
        else:
            print("You can go no further in this direction")
            self.position_y = y
            self.position_x = x

    def move_west(self):
        y = self.position_y
        x = self.position_x
        w_pos = x - 1

        if (-1 < y < 3) and (-1 < w_pos < 4):
            self.position_y = y
            self.position_x = w_pos
        else:
            print("You can go no further in this direction")
            self.position_y = y
            self.position_x = x

#todo: check on necessity/correctness of this method

    def show_location(self, current_booths):
        pl_y = self.position_y
        pl_x = self.position_x

        print("You are standing in " + str(current_booths[pl_y][pl_x]))

        try:
            print("To the north: " + str(current_booths[pl_y + 1][pl_x]))
        except IndexError:
            print("To the north there is only a wall, "
                  "covered in graffiti.")

        try:
            print("To the south: " + str(current_booths[pl_y - 1][pl_x]))
        except IndexError:
            print("To the south there is only a wall, "
                  "covered in giraffe drawings.")

        try:
            print("To the east: " + str(current_booths[pl_y][pl_x + 1]))
        except IndexError:
            print("To the east there is only a wall; "
                  "on the floor, a bag of trail mix sits.")

        try:
            print("To the west: " + str(current_booths[pl_y][pl_x - 1]))
        except IndexError:
            print("There the west there is only a wall, covered in "
                  "huge bugs and their caracasses.  Gross.")
