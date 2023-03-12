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


class RoboVac:
    def __init__(self, config_list):
        self.room_width, self.room_height = config_list[0]
        self.pos = config_list[1]  # starting position of vacuum
        self.block_list = config_list[2]  # blocks list (x,y,width,ht)

        # fill in with your info
        self.name = "Chip Henderson"
        self.id = "66666666"

    def get_next_move(
        self, current_pos, max_x, max_y
    ):  # called by PyGame code
        # Return a direction for the vacuum to move
        # random walk 0=north # 1=east 2=south 3=west

        visted_list = []
        visted_list.append(current_pos)

        if (
            current_pos[0] - 1,
            current_pos[1],
        ) not in visted_list and current_pos[0] != 0:
            return 3

        elif (
            current_pos[0],
            current_pos[1] + 1,
        ) not in visted_list and current_pos[1] != 0:
            return 0

        elif (
            current_pos[0] + 1,
            current_pos[1],
        ) not in visted_list and current_pos[0] != max_x:
            return 1

        elif (
            current_pos[0],
            current_pos[1] - 1,
        ) not in visted_list and current_pos[1] != max_y:
            return 2
        else:
            return random.choice([0, 1, 2, 3])
