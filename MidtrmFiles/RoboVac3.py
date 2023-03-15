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
import copy

visited_set = set()
floor = np.array


class RoboVac:
    def __init__(self, config_list):
        self.room_width, self.room_height = config_list[0]
        self.pos = config_list[1]  # starting position of vacuum
        self.block_list = config_list[2]  # blocks list (x,y,width,ht)
        self.blocked_tiles_set = set()
        self.free_tiles_set = set()

        # Copied code from Pygame to determine all tiles
        # Note this may need to to different function if updates are needed at each turn
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

        global floor
        floor = np.zeros((self.room_height,self.room_width))
        floor[self.pos[1], self.pos[0]] = 1
        for b_tile in self.blocked_tiles_set:
            floor[b_tile[1], b_tile[0]] = -1

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

        '''Old code replaced by dfs code
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
        '''

        child_boards = self.get_child_floor_list(vac_pos)
        print(child_boards)
    
    def get_child_floor_list(self, current_pos):

        max_row, max_col = self.room_height, self.room_width

        """Uses code modified from 8-game homework"""
        # Get row, col of surrounding blocks of current pos
        col, row = current_pos
        try:
            move_west = (row, col - 1)
        except IndexError:
            move_west = None
        try:
            move_east = (row, col + 1)
        except IndexError:
            move_east = None
        try:
            move_south = (row + 1, col)
        except IndexError:
            move_south = None
        try:
            move_north = (row - 1, col)
        except IndexError:
            move_north = None

        # Consider board conditions for possible moves
        if row > 0 and col > 0:  # Center condition
            child0 = copy.deepcopy(floor)
            child0[move_north] = 1

            child1 = copy.deepcopy(floor)
            child1[move_east] = 1

            child2 = copy.deepcopy(floor)
            child2[move_south] = 1

            child3 = copy.deepcopy(floor)
            child3[move_west] = 1
            
            return [child0] + [child1] + [child2] + [child3]

        if row == 0 and col == 0:  # Upper left corner 
            child1 = copy.deepcopy(floor)
            child1[move_east] = 1
            
            child2 = copy.deepcopy(floor)
            child2[move_south] = 1
            
            return [child1] + [child2]

        if row > 0 and col == 0:  # Top edge 
            child1 = copy.deepcopy(floor)
            child1[move_east] = 1
            
            child2 = copy.deepcopy(floor)
            child2[move_south] = 1
            
            child3 = copy.deepcopy(floor)
            child3[move_west] = 1
            
            return [child1] + [child2] + [child3]

        if row > 0 and col == 0 and row < max_row: # Left edge 
            child0 = copy.deepcopy(floor)
            child0[move_north] = 1

            child1 = copy.deepcopy(floor)
            child1[move_east] = 1

            child2 = copy.deepcopy(floor)
            child2[move_south] = 1
            
            return [child0] + [child1] + [child2]

        if row == max_row and col > 0 and col < max_col: # Bottom edge 
            child0 = copy.deepcopy(floor)
            child0[move_north] = 1

            child1 = copy.deepcopy(floor)
            child1[move_east] = 1

            child3 = copy.deepcopy(floor)
            child3[move_west] = 1
            
            return [child0] + [child1] + [child3]

        if row > 0 and row < max_row and col == max_col: # Right edge
            child0 = copy.deepcopy(floor)
            child0[move_north] = 1

            child2 = copy.deepcopy(floor)
            child2[move_south] = 1

            child3 = copy.deepcopy(floor)
            child3[move_west] = 1
            
            return [child0] + [child2] + [child3]

        if row == max_row and col == max_col: # Bottom right corner 
            child0 = copy.deepcopy(floor)
            child0[move_north] = 1

            child3 = copy.deepcopy(floor)
            child3[move_west] = 1
            
            return [child0] + [child3]

        if row == 0 and col == max_col: # Top right corenr
            child2 = copy.deepcopy(floor)
            child2[move_south] = 1

            child3 = copy.deepcopy(floor)
            child3[move_west] = 1
            
            return [child2] + [child3]

        if row == 0 and col == 0: # Top left corner
            child1 = copy.deepcopy(floor)
            child1[move_east] = 1
            child2 = copy.deepcopy(floor)
            child2[move_south] = 1
            
            return [child1] + [child2]

        if row == max_row and col == 0: # Bottom left corner
            child0 = copy.deepcopy(floor)
            child0[move_north] = 1
            child1 = copy.deepcopy(floor)
            child1[move_east] = 1
            
            return [child0] + [child1]
