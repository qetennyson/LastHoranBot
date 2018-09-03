tile_map = [['Room 1-1', 'Room 1-2', 'Room 1-3', 'Room 1-4', 'Room 1-5', ],
            ['Room 2-1', 'Room 2-2', 'Room 2-3', 'Room 2-4', 'Room 2-5']]
print(tile_map[1][0])


class Player:

    def __init__(self, x=0, y=0):
        self.position_x = x
        self.position_y = y


player = Player()


def give_location(player):
    location = tile_map[player.position_x][player.position_y]
    print(location)


def move_player():
    pass


give_location(player)