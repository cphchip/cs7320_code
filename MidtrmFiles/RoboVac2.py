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

visited_list = []
blocked_tile_list = []


class RoboVac:
    def __init__(self, config_list):
        self.room_width, self.room_height = config_list[0]
        self.pos = config_list[1]  # starting position of vacuum
        self.block_list = config_list[2]  # blocks list (x,y,width,ht)

        # Create a list of the blocked tiles
        count = 0
        global blocked_tile_list

        blocked_dims = [x[2] * x[3] for x in self.block_list]
        blocked_qty = sum(blocked_dims)

        # for blocks in self.block_list:
        #     while (count < self.block_list[0][2] 
        #            * self.block_list[0][3]
        #         ):
        #         blocking_tile = (self.block_list[0][0] 
        #                         + count, self.block_list[0][1])
        #         blocked_tile_list.append(blocking_tile)
        #         count += 1
        for blocks in range(blocked_qty):
            blocking_tile = (self.block_list[blocks][0], 
                             self.block_list[blocks][1])
            blocked_tile_list.append(blocking_tile)
        
        global visited_list
        
        # Treat blocked as visited for simplicity
        for tile in blocked_tile_list:
            visited_list.append(tile) 

        self.name = "Chip Henderson"
        self.id = "48996654"


    def get_next_move(self, vac_pos):  # called by PyGame code
        # Return a direction for the vacuum to move
        max_x, max_y = self.room_width, self.room_height
        vac_x, vac_y = vac_pos[0], vac_pos[1]
        global visited_list
        visited_list.append((vac_x, vac_y))
        global blocked_tile_list

        # Check surrounding cells and move appropriate direction
        if ((vac_x - 1, vac_y) not in visited_list
            and vac_x != 0
        ):
            return 3
        elif ((vac_x, vac_y - 1) not in visited_list 
            and vac_y != 0
        ):
            return 0
        elif ((vac_x + 1, vac_y) not in visited_list
            and vac_x != max_x - 1
        ):
            return 1
        elif ((vac_x, vac_y + 1) not in visited_list
            and vac_y != max_y - 1
        ):
            return 2
        else:  # if we get stuck
            return random.choice([0, 1, 2, 3])

    def get_child_floor_list(self, current_pos, max_x, max_y):

        """Uses code modified from 8-game homework"""

        """Not used at this time

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
        """
