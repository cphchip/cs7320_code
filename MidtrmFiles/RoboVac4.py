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
move_list = []
call_count = 0


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
        vac_x, vac_y = vac_pos[0], vac_pos[1]
        # global visited_set
        # visited_set.add((vac_x, vac_y)) # I don't think this is needed here
        global call_count
        global move_list

        if call_count == 0:
            move_list = self.next_step(vac_pos)
            # for x in arr_path_list:
            #     path_list.append(x[::-1]) # convert back to x,y from arr
        call_count += 1
        
        return move_list[call_count]


    def next_step(self, vac_pos):

        '''Copied from 8-game - BFS'''
        global queue
        global visited_set
        # curr_pos = vac_pos
        arr_pos = vac_pos[::-1]
        # queue = [[(arr_pos, floor.tolist())]]
        queue = [[(None, arr_pos, floor.tolist())]]
        goal_board = len(self.free_tiles_set)
        final_path = []

        while queue:
            path = queue.pop(0)
            # print("next path")
            # vertex = path[-1][1]
            # cur_pos = path[-1][0] 
            vertex = path[-1][2]
            cur_pos = path[-1][1] 
            child_list = self.get_child_floor_list(cur_pos, vertex)

            next_node_list = [x for x in child_list if x not in path]

            for next in next_node_list:
                visited_set.add(next[1])
                # print (np.sum(next[1])) # Debug line
                # print(len(path)) # Debug line
                if np.sum(next[2]) == goal_board or len(path) == 12:
                    for x in path:
                        final_path.append(x[0])
                    return final_path
                else:
                    queue.append(path + [next])
    
    def get_child_floor_list(self, arr_pos, current_floor):

        # print(current_floor)
        max_row, max_col = self.room_height - 1, self.room_width - 1
        current_floor = np.array(current_floor)
        array_blocked_tiles = set()
        array_visited_tiles = set()
        for b_tiles in self.blocked_tiles_set:
            array_blocked_tiles.add(b_tiles[::-1])

        for v_tiles in visited_set:
            array_visited_tiles.add(v_tiles[::-1])

        # array_blocked_tiles = reversed(self.blocked_tiles_set)
        children = []

        """Uses code modified from 8-game homework"""
        # Get row, col of surrounding blocks of current pos
        row, col = arr_pos

        # Create new positions
        if col > 0:
            move_west = (row, col - 1)
        if col < max_col:
            move_east = (row, col + 1)
        if row > 0:
            move_north = (row - 1, col)
        if row < max_row:
            move_south = (row + 1, col)

        # Consider board conditions for possible moves
        if (row > 0 and row < max_row
            and col > 0 and col < max_col
        ):  # Center condition
            if (move_north not in array_blocked_tiles 
                and move_north not in array_visited_tiles
            ):
                # child0 = copy.deepcopy(current_floor)
                # child0[move_north] = 1
                # new_pos_0 = move_north
                # children.append([(move_north), child0.tolist()])
                child0 = self.child_gen(0, current_floor, move_north)
                children.append(child0)
            else:
                child0 = None

            if (move_east not in array_blocked_tiles 
                and move_east not in array_visited_tiles
            ):
                # child1 = copy.deepcopy(current_floor)
                # child1[move_east] = 1
                # # new_pos_1 = move_east
                # children.append([(move_east), child1.tolist()])
                child1 = self.child_gen(1, current_floor, move_east)
                children.append(child1)
            else:
                child1 = None

            if (move_south not in array_blocked_tiles 
                and move_south not in array_visited_tiles
            ):
                # child2 = copy.deepcopy(current_floor)
                # child2[move_south] = 1
                # # new_pos_2 = move_south
                # children.append([(move_south), child2.tolist()])
                child2 = self.child_gen(2, current_floor, move_south)
                children.append(child2)
            else:
                child2 = None

            if (move_west not in array_blocked_tiles 
                and move_west not in array_visited_tiles
            ):
                # child3 = copy.deepcopy(current_floor)
                # child3[move_west] = 1
                # # new_pos_3 = move_west
                # children.append([(move_west), child3.tolist()])
                child3 = self.child_gen(3, current_floor, move_west)
                children.append(child3)
            else:
                child3 = None
            
            return children
        
        elif row == 0 and col == 0:  # Upper left corner 
            if move_east not in array_blocked_tiles and move_east not in array_visited_tiles:
                # child1 = copy.deepcopy(current_floor)
                # child1[move_east] = 1
                # # new_pos_1 = move_east
                # children.append([(move_east), child1.tolist()])
                child1 = self.child_gen(1, current_floor, move_east)
                children.append(child1)
            else:
                child1 = None
            
            if move_south not in array_blocked_tiles and move_south not in array_visited_tiles:
                # child2 = copy.deepcopy(current_floor)
                # child2[move_south] = 1
                # # new_pos_2 = move_south
                # children.append([(move_south), child2.tolist()])
                child2 = self.child_gen(2, current_floor, move_south)
                children.append(child2)
            else:
                child2 = None
            
            return children
        
        elif row == 0 and col > 0 and col < max_col:  # Top edge 
            if (move_east not in array_blocked_tiles 
                and move_east not in array_visited_tiles
            ):
                # child1 = copy.deepcopy(current_floor)
                # child1[move_east] = 1
                # new_pos = move_east
                # children.append([(new_pos), child1.tolist()])
                child1 = self.child_gen(1, current_floor, move_east)
                children.append(child1)
            else:
                child1 = None
            
            if move_south not in array_blocked_tiles and move_south not in array_visited_tiles:
                # child2 = copy.deepcopy(current_floor)
                # child2[move_south] = 1
                # # new_pos_2 = move_south
                # children.append([(move_south), child2.tolist()])
                child2 = self.child_gen(2, current_floor, move_south)
                children.append(child2)
            else:
                child2 = None
            
            if move_west not in array_blocked_tiles and move_west not in array_visited_tiles:
                # child3 = copy.deepcopy(current_floor)
                # child3[move_west] = 1
                # # new_pos_3 = move_west
                # children.append([(move_west), child3.tolist()])
                child3 = self.child_gen(3, current_floor, move_west)
                children.append(child3)
            else:
                child3 = None
            
            return children
        
        elif row > 0 and col == 0 and row < max_row: # Left edge 
            if move_north not in array_blocked_tiles and move_north not in array_visited_tiles:
                # child0 = copy.deepcopy(current_floor)
                # child0[move_north] = 1
                # # new_pos_0 = move_north
                # children.append([(move_north), child0.tolist()])
                child0 = self.child_gen(0, current_floor, move_north)
                children.append(child0)
            else:
                child0 = None

            if move_east not in array_blocked_tiles and move_east not in array_visited_tiles:
                # child1 = copy.deepcopy(current_floor)
                # child1[move_east] = 1
                # # new_pos_1 = move_east
                # children.append([(move_east), child1.tolist()])
                child1 = self.child_gen(1, current_floor, move_east)
                children.append(child1)
            else:
                child1 = None
            if move_south not in array_blocked_tiles and move_south not in array_visited_tiles:
                # child2 = copy.deepcopy(current_floor)
                # child2[move_south] = 1
                # # new_pos_2 = move_south
                # children.append([(move_south), child2.tolist()])
                child2 = self.child_gen(2, current_floor, move_south)
                children.append(child2)
            else:
                child2 = None
            
            return children

        elif row == max_row and col > 0 and col < max_col: # Bottom edge 
            if move_north not in array_blocked_tiles and move_north not in array_visited_tiles:
                # child0 = copy.deepcopy(current_floor)
                # child0[move_north] = 1
                # # new_pos_0 = move_north
                # children.append([(move_north), child0.tolist()])
                child0 = self.child_gen(0, current_floor, move_north)
                children.append(child0)
            else:
                child0 = None

            if move_east not in array_blocked_tiles and move_east not in array_visited_tiles:
                # child1 = copy.deepcopy(current_floor)
                # child1[move_east] = 1
                # # new_pos_1 = move_east
                # children.append([(move_east), child1.tolist()])
                child1 = self.child_gen(1, current_floor, move_east)
                children.append(child1)
            else:
                child1 = None

            if move_west not in array_blocked_tiles and move_west not in array_visited_tiles:
                # child3 = copy.deepcopy(current_floor)
                # child3[move_west] = 1
                # # new_pos_3 = move_west
                # children.append([(move_west), child3.tolist()])
                child3 = self.child_gen(3, current_floor, move_west)
                children.append(child3)
            else:
                child3 = None
            
            return children

        elif row > 0 and row < max_row and col == max_col: # Right edge
            if move_north not in array_blocked_tiles and move_north not in array_visited_tiles:
                # child0 = copy.deepcopy(current_floor)
                # child0[move_north] = 1
                # # new_pos_0 = move_north
                # children.append([(move_north), child0.tolist()])
                child0 = self.child_gen(0, current_floor, move_north)
                children.append(child0)
            else:
                child0 = None

            if move_south not in array_blocked_tiles and move_south not in array_visited_tiles:
                # child2 = copy.deepcopy(current_floor)
                # child2[move_south] = 1
                # # new_pos_2 = move_south
                # children.append([(move_south), child2.tolist()])
                child2 = self.child_gen(2, current_floor, move_south)
                children.append(child2)
            else:
                child2 = None

            if move_west not in array_blocked_tiles and move_west not in array_visited_tiles:
                # child3 = copy.deepcopy(current_floor)
                # child3[move_west] = 1
                # # new_pos_3 = move_west
                # children.append([(move_west), child3.tolist()])
                child3 = self.child_gen(3, current_floor, move_west)
                children.append(child3)
            else:
                child3 = None
            
            return children

        elif row == max_row and col == max_col: # Bottom right corner 
            if move_north not in array_blocked_tiles and move_north not in array_visited_tiles:
                # child0 = copy.deepcopy(current_floor)
                # child0[move_north] = 1
                # # new_pos_0 = move_north
                # children.append([(move_north), child0.tolist()])
                child0 = self.child_gen(0, current_floor, move_north)
                children.append(child0)
            else:
                child0 = None

            if move_west not in array_blocked_tiles and move_west not in array_visited_tiles:
                # child3 = copy.deepcopy(current_floor)
                # child3[move_west] = 1
                # # new_pos_3 = move_west
                # children.append([(move_west), child3.tolist()])
                child3 = self.child_gen(3, current_floor, move_west)
                children.append(child3)
            else:
                child3 = None
            
            return children

        elif row == 0 and col == max_col: # Top right corenr
            if move_south not in array_blocked_tiles and move_south not in array_visited_tiles:
                # child2 = copy.deepcopy(current_floor)
                # child2[move_south] = 1
                # # new_pos_2 = move_south
                # children.append([(move_south), child2.tolist()])
                child2 = self.child_gen(2, current_floor, move_south)
                children.append(child2)
            else:
                child2 = None

            if move_west not in array_blocked_tiles and move_west not in array_visited_tiles:
                # child3 = copy.deepcopy(current_floor)
                # child3[move_west] = 1
                # # new_pos_3 = move_west
                # children.append([(move_west), child3.tolist()])
                child3 = self.child_gen(3, current_floor, move_west)
                children.append(child3)
            else:
                child3 = None
            
            return children

        elif row == 0 and col == 0: # Top left corner
            if move_east not in array_blocked_tiles and move_east not in array_visited_tiles:
                # child1 = copy.deepcopy(current_floor)
                # child1[move_east] = 1
                # # new_pos_1 = move_east
                # children.append([(move_east), child1.tolist()])
                child1 = self.child_gen(1, current_floor, move_east)
                children.append(child1)
            else:
                child1 = None

            if move_south not in array_blocked_tiles and move_south not in array_visited_tiles:
                # child2 = copy.deepcopy(current_floor)
                # child2[move_south] = 1
                # # new_pos_2 = move_south
                # children.append([(move_south), child2.tolist()])
                child2 = self.child_gen(2, current_floor, move_south)
                children.append(child2)
            else:
                child2 = None
            
            return children

        elif row == max_row and col == 0: # Bottom left corner
            if (move_north not in array_blocked_tiles 
                and move_north not in array_visited_tiles
            ):
                # child0 = copy.deepcopy(current_floor)
                # child0[move_north] = 1
                # # new_pos_0 = move_north
                # children.append([(move_north), child0.tolist()])
                child0 = self.child_gen(0, current_floor, move_north)
                children.append(child0)
            else:
                child0 = None

            if (move_east not in array_blocked_tiles 
                and move_east not in array_visited_tiles
            ):
                # child1 = copy.deepcopy(current_floor)
                # child1[move_east] = 1
                # # new_pos_1 = move_east
                # children.append([(move_east), child1.tolist()])
                child1 = self.child_gen(1, current_floor, move_east)
                children.append(child1)
            else:
                child1 = None
            
            return children
        else:
            choice = random.choice([0, 1, 2, 3])
                
            if choice == 0:
                # child0 = copy.deepcopy(current_floor)
                # child0[move_north] = 1
                # # new_pos_0 = move_north
                # children.append([(move_north), child0.tolist()])
                child0 = self.child_gen(0, current_floor, move_north)
                children.append(child0)
            elif choice == 1:
                # child1 = copy.deepcopy(current_floor)
                # child1[move_east] = 1
                # # new_pos_1 = move_east
                # children.append([(move_east), child1.tolist()])
                child1 = self.child_gen(1, current_floor, move_east)
                children.append(child1)
            elif choice == 2:
                # child2 = copy.deepcopy(current_floor)
                # child2[move_south] = 1
                # # new_pos_2 = move_south
                # children.append([(move_south), child2.tolist()])
                child2 = self.child_gen(2, current_floor, move_south)
                children.append(child2)
            elif choice == 3:
                # child3 = copy.deepcopy(current_floor)
                # child3[move_west] = 1
                # # new_pos_3 = move_west
                # children.append([(move_west), child3.tolist()])
                child3 = self.child_gen(3, current_floor, move_west)
                children.append(child3)

            return children
        

    def child_gen(self, move, current_floor, new_pos):
        
        if move == 0:
            child0 = copy.deepcopy(current_floor)
            child0[new_pos] = 1

            return [move, (new_pos), child0.tolist()]
        
        elif move == 1:
            child1 = copy.deepcopy(current_floor)
            child1[new_pos] = 1

            return [move, (new_pos), child1.tolist()]
        
        elif move == 2:
            child2 = copy.deepcopy(current_floor)
            child2[new_pos] = 1

            return [move, (new_pos), child2.tolist()]
        
        elif move == 3:
            child3 = copy.deepcopy(current_floor)
            child3[new_pos] = 1

            return [move, (new_pos), child3.tolist()]