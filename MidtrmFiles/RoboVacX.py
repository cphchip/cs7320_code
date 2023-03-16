# this is left over code from a failed attempt at level 4

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
queue = []


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

        # Represent the gameboard as an array
        global floor
        floor = np.zeros((self.room_height,self.room_width),dtype=int)
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

        # child_floors = self.get_child_floor_list(vac_pos)
        # print(child_boards)

        '''Copied from 8-game - BFS'''
        global queue
        queue = [(vac_pos)]

        while queue:
            path = queue.pop(0)
            # vertex = path[-1]
            # global bfs_count
            # child_list = self.get_child_floor_list(path)
            move = self.get_child_floor_list(path)

            if move == 0:
                next_node = (vac_x - 1, vac_y)
            elif move == 1:
                next_node = (vac_x, vac_y + 1)
            elif move == 2:
                next_node = (vac_x + 1, vac_y)
            elif move == 3:
                next_node = (vac_x, vac_y - 1)
            
            visited_set.add(next_node)
            # next_node_list = [x for x in child_list if x not in path]

            queue.append([path] + [next_node])
            # for next in next_node_list:
                # bfs_count += 1
                # print(bfs_count)
                # if next == goal_board:
                #     return path + [next]
                # else:
                # queue.append(path + next)
                # return next
                
            return move

    
    def get_child_floor_list(self, current_pos):

        max_y, max_x = self.room_height - 1, self.room_width - 1
        # array_blocked_tiles = set()
        # array_visited_set = set()
        # for tiles in self.blocked_tiles_set:
        #     array_blocked_tiles.add(tiles[::-1])

        # for tiles in visited_set:
        #     array_visited_set.add(tiles[::-1])
        # array_blocked_tiles = reversed(self.blocked_tiles_set)
        # children = []

        """Uses code modified from 8-game homework"""
        # Get row, col of surrounding blocks of current pos, opposite of (x,y) coordinates
        x, y = current_pos

        # Create new positions
        if x > 0 and (x - 1, y) not in self.blocked_tiles_set and (x - 1, y) not in visited_set:
            # move_west = (y, x - 1)
            # return move_west
            return 3
        elif y > 0 and (x, y - 1) not in self.blocked_tiles_set and (x, y - 1) not in visited_set:
            # move_north = (y - 1, x)
            # return move_north
            return 0
        elif (x < max_x
            and (x + 1, y) not in self.blocked_tiles_set 
            and (x + 1, y) not in visited_set
        ):
            # move_east = (y, x + 1)
            # return move_east
            return 1
        elif (y < max_y 
            and (x, y + 1) not in self.blocked_tiles_set 
            and (x, y + 1) not in visited_set
        ):
            # move_south = (row + 1, x)
            # return move_south
            return 2
        else:  # if we get stuck
            return random.choice([0, 1, 2, 3])
            
        '''Hiding this code until later
        # Consider board conditions for possible moves
        if (row > 0 and row < max_row 
            and col > 0 and col < max_col
        ):  # Center condition
            if move_north not in array_blocked_tiles:
                child0 = copy.deepcopy(floor)
                child0[move_north] = 1
                children.append(child0.tolist())
            else:
                child0 = None

            if move_east not in array_blocked_tiles:
                child1 = copy.deepcopy(floor)
                child1[move_east] = 1
                children.append(child1.tolist())
            else:
                child1 = None

            if move_south not in array_blocked_tiles:
                child2 = copy.deepcopy(floor)
                child2[move_south] = 1
                children.append(child2.tolist())
            else:
                child2 = None

            if move_west not in array_blocked_tiles:
                child3 = copy.deepcopy(floor)
                child3[move_west] = 1
                children.append(child3.tolist())
            else:
                child3 = None
            
            return children

        if row == 0 and col == 0:  # Upper left corner 
            if move_east not in array_blocked_tiles:
                child1 = copy.deepcopy(floor)
                child1[move_east] = 1
            else:
                child1 = None
            
            if move_south not in array_blocked_tiles:
                child2 = copy.deepcopy(floor)
                child2[move_south] = 1
            else:
                child2 = None
            
            return [child1] + [child2]

        if row > 0 and col == 0:  # Top edge 
            if move_east not in array_blocked_tiles:
                child1 = copy.deepcopy(floor)
                child1[move_east] = 1
            else:
                child1 = None
            
            if move_south not in array_blocked_tiles:
                child2 = copy.deepcopy(floor)
                child2[move_south] = 1
            else:
                child2 = None
            
            if move_west not in array_blocked_tiles:
                child3 = copy.deepcopy(floor)
                child3[move_west] = 1
            else:
                child3 = None
            
            return [child1] + [child2] + [child3]

        if row > 0 and col == 0 and row < max_row: # Left edge 
            if move_north not in array_blocked_tiles:
                child0 = copy.deepcopy(floor)
                child0[move_north] = 1
            else:
                child0 = None

            if move_east not in array_blocked_tiles:
                child1 = copy.deepcopy(floor)
                child1[move_east] = 1
            else:
                child1 = None

            if move_south not in array_blocked_tiles:
                child2 = copy.deepcopy(floor)
                child2[move_south] = 1
            else:
                child2 = None
            
            return [child0] + [child1] + [child2]

        if row == max_row and col > 0 and col < max_col: # Bottom edge 
            if move_north not in array_blocked_tiles:
                child0 = copy.deepcopy(floor)
                child0[move_north] = 1
            else:
                child0 = None

            if move_east not in array_blocked_tiles:
                child1 = copy.deepcopy(floor)
                child1[move_east] = 1
            else:
                child1 = None

            if move_west not in array_blocked_tiles:
                child3 = copy.deepcopy(floor)
                child3[move_west] = 1
            else:
                child3 = None
            
            return [child0] + [child1] + [child3]

        if row > 0 and row < max_row and col == max_col: # Right edge
            if move_north not in array_blocked_tiles:
                child0 = copy.deepcopy(floor)
                child0[move_north] = 1
            else:
                child0 = None

            if move_south not in array_blocked_tiles:
                child2 = copy.deepcopy(floor)
                child2[move_south] = 1
            else:
                child2 = None

            if move_west not in array_blocked_tiles:
                child3 = copy.deepcopy(floor)
                child3[move_west] = 1
            else:
                child3 = None
            
            return [child0] + [child2] + [child3]

        if row == max_row and col == max_col: # Bottom right corner 
            if move_north not in array_blocked_tiles:
                child0 = copy.deepcopy(floor)
                child0[move_north] = 1
            else:
                child0 = None

            if move_west not in array_blocked_tiles:
                child3 = copy.deepcopy(floor)
                child3[move_west] = 1
            else:
                child3 = None
            
            return [child0] + [child3]

        if row == 0 and col == max_col: # Top right corenr
            if move_south not in array_blocked_tiles:
                child2 = copy.deepcopy(floor)
                child2[move_south] = 1
            else:
                child2 = None

            if move_west not in array_blocked_tiles:
                child3 = copy.deepcopy(floor)
                child3[move_west] = 1
            else:
                child3 = None
            
            return [child2] + [child3]

        if row == 0 and col == 0: # Top left corner
            if move_east not in array_blocked_tiles:
                child1 = copy.deepcopy(floor)
                child1[move_east] = 1
            else:
                child1 = None

            if move_south not in array_blocked_tiles:
                child2 = copy.deepcopy(floor)
                child2[move_south] = 1
            else:
                child2 = None
            
            return [child1] + [child2]

        if row == max_row and col == 0: # Bottom left corner
            if move_north not in array_blocked_tiles:
                child0 = copy.deepcopy(floor)
                child0[move_north] = 1
            else:
                child0 = None

            if move_east not in array_blocked_tiles:
                child1 = copy.deepcopy(floor)
                child1[move_east] = 1
            else:
                child1 = None
            
            return [child0] + [child1]
            '''