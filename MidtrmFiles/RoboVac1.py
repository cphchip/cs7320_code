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

visited_list = []  # note clean_set does same thing, is this needed?

# Also if we know the clean_set do we know the 'dirty_set?'


class RoboVac:
    def __init__(self, config_list):
        self.room_width, self.room_height = config_list[0]
        self.pos = config_list[1]  # starting position of vacuum
        self.block_list = config_list[2]  # blocks list (x,y,width,ht)

        # fill in with your info
        self.name = "Chip Henderson"
        self.id = "48996654"

    # Note you don't need to parse in max_x and max_y
    # It's provided above with __init__
    def get_next_move(
        self, current_pos, max_x, max_y, is_blocked
    ):  # called by PyGame code
        # Return a direction for the vacuum to move
        # random walk 0=north # 1=east 2=south 3=west

        global visited_list
        visited_list.append(current_pos)

        # Check surrounding cells and move appropriate direction
        if (
            current_pos[0] - 1,
            current_pos[1],
        ) not in visited_list and current_pos[0] != 0:
            return 3

        elif (
            current_pos[0],
            current_pos[1] - 1,
        ) not in visited_list and current_pos[1] != 0:
            return 0

        elif (
            current_pos[0] + 1,
            current_pos[1],
        ) not in visited_list and current_pos[0] != max_x:
            return 1

        elif (
            current_pos[0],
            current_pos[1] + 1,
        ) not in visited_list and current_pos[1] != max_y:
            return 2
        else:
            return random.choice([0, 1, 2, 3])

    def get_child_floor_list(self, current_pos, max_x, max_y):

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
