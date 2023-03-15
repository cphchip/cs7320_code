"""
create robot vacuum that cleans all the floors of a grid.
main creates an instance of RoboVac (your code) and provides:
- grid size
- loc of robovac
- list of x,y,w,h tuples are instance of rectangluar blocks

goal: visit all tiles
exec will : create instance and in game loop call : nextMove()  ??
"""
import random
import numpy as np

visited_set = set()
# blocked_tile_set = set()
# block_tiles_set = set()


class RoboVac:
    def __init__(self, config_list):
        self.room_width, self.room_height = config_list[0]
        self.pos = config_list[1]  # starting position of vacuum
        self.block_list = config_list[2]  # blocks list (x,y,width,ht)
        self.blocked_tiles_set = set()
        self.free_tiles_set = set()

        # Copied code from Pygame to determine all tiles
        self.free_tiles_set = set()
        for x in range(self.room_width):
            for y in range(self.room_height):
                self.free_tiles_set.add((x, y))

        # Copied code from Pygame to determine blocked cells
        for b in self.block_list:
            for x in range(b[0], b[0] + b[2]):
                for y in range(b[1], b[1] + b[3]):
                    self.blocked_tiles_set.add((x, y))

        self.free_tiles_set = (self.free_tiles_set 
                               - self.blocked_tiles_set)


        global visited_set
        
        # Treat blocked as visited for simplicity
        for tile in self.blocked_tiles_set:
            visited_set.add(tile) 

        self.name = "Chip Henderson"
        self.id = "48996654"


    def get_next_move(self, vac_pos):  # called by PyGame code
        # Return a direction for the vacuum to move
        max_x, max_y = self.room_width, self.room_height
        vac_x, vac_y = vac_pos[0], vac_pos[1]
        global visited_set
        visited_set.add((vac_x, vac_y))
        # global blocked_tile_set

        # Check surrounding cells and move appropriate direction
        if ((vac_x - 1, vac_y) not in visited_set
            and vac_x != 0
        ):
            return 3
        elif ((vac_x, vac_y - 1) not in visited_set 
            and vac_y != 0
        ):
            return 0
        elif ((vac_x + 1, vac_y) not in visited_set
            and vac_x != max_x - 1
        ):
            return 1
        elif ((vac_x, vac_y + 1) not in visited_set
            and vac_y != max_y - 1
        ):
            return 2
        else:  # if we get stuck
            return random.choice([0, 1, 2, 3])

    def get_child_floor_list(self, current_pos):

        """Uses code modified from 8-game homework"""
        # Get x,y of surrounding blocks of current pos
        x, y = current_pos
        try:
            move_left = (x - 1, y)
        except IndexError:
            move_left = None
        try:
            move_right = (x + 1, y)
        except IndexError:
            move_right = None
        try:
            move_down = (x, y + 1)
        except IndentationError:
            move_down = None
        try:
            move_up = (x, y - 1)
        except IndexError:
            move_up = None

        # Consider board conditions for possible moves
        if x > 0 and y > 0:  # Center condition
            # child0 = North move
            # child1 = East move
            # child2 = South move
            # child3 = West move
            return

        if x == 0 and y == 0:  # Upper left hand corner condition
            # child1 = East move
            # child2 = South move
            return

        if x > 0 and y == 0:  # Top edge condition
            # child1 = East move
            # child2 = South move
            # child3 = West move
            return

        if x == 0 and y >= 1 and y <= max_y:  # Left edge condition
            # child0 = North move
            # child1 = East move
            # child2 = South move
            return

        if x >= 1 and x <= max_x and y == 0:  # Bottom edge condition
            # child0 = North move
            # child1 = East move
            # child3 = West move
            return

        if x == max_x and y >= 1 and y <= max_y:  # Right edge condition
            # child0 = North move
            # child2 = South move
            # child3 = West move
            return

        if x == max_x and y == max_y:  # Bottom right corner condition
            # child0 = North move
            # child3 = West move
            return

        if x == max_x and y == 0:  # Top right corenr condition
            # child2 = South move
            # child3 = West move
            return

        if x == 0 and y == 0:  # Top left corner condition
            # child1 = East move
            # child2 = South move
            return

        if x == 0 and y == max_y:  # Bottom left corner condition
            # child0 = North move
            # child1 = East move
            return
