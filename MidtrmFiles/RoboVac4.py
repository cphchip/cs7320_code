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

# Global variable declarations
visited_set = set()
floor = np.array
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

        self.name = "Chip Henderson"
        self.id = "48996654"


    def get_next_move(self, vac_pos):  # called by PyGame code
        # Return a direction for the vacuum to move
        global call_count
        global move_list

        if call_count == 0:
            move_list = self.next_step_dfs(vac_pos) # Change to alter search
        call_count += 1
        
        return move_list[call_count]


    def next_step_bfs(self, vac_pos):

        '''Copied from 8-game - BFS'''
        global visited_set
        arr_pos = vac_pos[::-1]
        queue = [[(None, arr_pos, floor)]]
        goal_board = len(self.free_tiles_set)
        final_path = []

        while queue:
            path = queue.pop(0)
            # Clear visited set so only traversed tiles are saved            
            visited_set.clear() 
            for items in path:
                visited_set.add((items[1])) # In array format (row, col)
            vertex = path[-1][2]
            cur_pos = path[-1][1] 
            child_list = self.get_child_floor_list(cur_pos, vertex)

            next_node_list = ([x for x in child_list 
                               if x[2] not in path])

            for next in next_node_list:
                if np.sum(next[2]) == goal_board or len(path) == 400:
                    for x in path:
                        final_path.append(x[0])
                    return final_path
                else:
                    queue.append(path + [next])
    
    '''Copied from 8 game DFS'''
    def next_step_dfs(self, vac_pos):
        global visited_set
        arr_pos = vac_pos[::-1]
        stack = [[(None, arr_pos, floor)]]
        goal_board = len(self.free_tiles_set)
        final_path = []

        while stack:
            path = stack.pop()
            # Clear visited set so only traversed tiles are saved            
            visited_set.clear() 
            for items in path:
                visited_set.add((items[1])) # In array format (row, col)
            vertex = path[-1][2]
            cur_pos = path[-1][1] 
            child_list = self.get_child_floor_list(cur_pos, vertex)

            next_node_list = ([x for x in child_list 
                               if x[2] not in path])

            for next in next_node_list:
                if np.sum(next[2]) == goal_board or len(path) == 400:
                    for x in path:
                        final_path.append(x[0])
                    return final_path
                else:
                    stack.append(path + [next])
    
    def get_child_floor_list(self, arr_pos, current_floor):

        max_row, max_col = self.room_height - 1, self.room_width - 1
        current_floor = np.array(current_floor)
        array_blocked_tiles = set()
        moves = []

        for b_tiles in self.blocked_tiles_set:
            array_blocked_tiles.add(b_tiles[::-1])

        children = []

        """Uses code modified from 8-game homework"""
        # Get row, col of surrounding blocks of current pos
        row, col = arr_pos

        # Create new positions
        if col > 0:
            move_west = (row, col - 1)
            moves.append((move_west))
        if col < max_col:
            move_east = (row, col + 1)
            moves.append((move_east))
        if row > 0:
            move_north = (row - 1, col)
            moves.append((move_north))
        if row < max_row:
            move_south = (row + 1, col)
            moves.append((move_south))

        # Consider board conditions for possible moves, 9 total
        if (row > 0 and row < max_row
            and col > 0 and col < max_col
        ):  # Center condition
            if (move_north not in array_blocked_tiles 
                and move_north not in visited_set
            ):
                child0 = self.child_gen(0, current_floor, move_north)
                children.append(child0)

            if (move_east not in array_blocked_tiles 
                and move_east not in visited_set
            ):
                child1 = self.child_gen(1, current_floor, move_east)
                children.append(child1)

            if (move_south not in array_blocked_tiles 
                and move_south not in visited_set
            ):
                child2 = self.child_gen(2, current_floor, move_south)
                children.append(child2)

            if (move_west not in array_blocked_tiles 
                and move_west not in visited_set
            ):
                child3 = self.child_gen(3, current_floor, move_west)
                children.append(child3)

            if not children: # Get un-stuck
                options = ([x for x in moves 
                            if x not in array_blocked_tiles])
                choice = random.choice(options)

                if choice == move_north:
                    child0 = self.child_gen(0, current_floor, move_north)
                    children.append(child0)
                elif choice == move_east:
                    child1 = self.child_gen(1, current_floor, move_east)
                    children.append(child1)
                elif choice == move_south:
                    child2 = self.child_gen(2, current_floor, move_south)
                    children.append(child2)
                elif choice == move_west:
                    child3 = self.child_gen(3, current_floor, move_west)
                    children.append(child3)
                            
        elif row == 0 and col > 0 and col < max_col:  # Top edge 
            if (move_east not in array_blocked_tiles 
                and move_east not in visited_set
            ):
                child1 = self.child_gen(1, current_floor, move_east)
                children.append(child1)
            
            if (move_south not in array_blocked_tiles 
                and move_south not in visited_set
            ):
                child2 = self.child_gen(2, current_floor, move_south)
                children.append(child2)
            
            if (move_west not in array_blocked_tiles 
                and move_west not in visited_set
            ):
                child3 = self.child_gen(3, current_floor, move_west)
                children.append(child3)

            if not children: # Get un-stuck
                options = ([x for x in moves 
                            if x not in array_blocked_tiles])
                choice = random.choice(options)

                if choice == move_east:
                    child1 = self.child_gen(1, current_floor, move_east)
                    children.append(child1)
                elif choice == move_south:
                    child2 = self.child_gen(2, current_floor, move_south)
                    children.append(child2)
                elif choice == move_west:
                    child3 = self.child_gen(3, current_floor, move_west)
                    children.append(child3)
                    
        elif row > 0 and col == 0 and row < max_row: # Left edge 
            if (move_north not in array_blocked_tiles 
                and move_north not in visited_set
            ):
                child0 = self.child_gen(0, current_floor, move_north)
                children.append(child0)

            if (move_east not in array_blocked_tiles 
                  and move_east not in visited_set
            ):
                child1 = self.child_gen(1, current_floor, move_east)
                children.append(child1)

            if (move_south not in array_blocked_tiles 
                  and move_south not in visited_set
            ):
                child2 = self.child_gen(2, current_floor, move_south)
                children.append(child2)

            if not children: # Get un-stuck
                options = [x for x in moves if x not in array_blocked_tiles]
                choice = random.choice(options)

                if choice == move_north:
                    child0 = self.child_gen(0, current_floor, move_north)
                    children.append(child0)
                elif choice == move_east:
                    child1 = self.child_gen(1, current_floor, move_east)
                    children.append(child1)
                elif choice == move_south:
                    child2 = self.child_gen(2, current_floor, move_south)
                    children.append(child2)
            
        elif row == max_row and col > 0 and col < max_col: # Bottom edge 
            if (move_north not in array_blocked_tiles 
                and move_north not in visited_set
            ):
                child0 = self.child_gen(0, current_floor, move_north)
                children.append(child0)

            if (move_east not in array_blocked_tiles 
                and move_east not in visited_set
            ):
                child1 = self.child_gen(1, current_floor, move_east)
                children.append(child1)

            if (move_west not in array_blocked_tiles 
                  and move_west not in visited_set
            ):
                child3 = self.child_gen(3, current_floor, move_west)
                children.append(child3)

            if not children: # Get un-stuck
                options = [x for x in moves if x not in array_blocked_tiles]
                choice = random.choice(options)

                if choice == move_north:
                    child0 = self.child_gen(0, current_floor, move_north)
                    children.append(child0)
                elif choice == move_east:
                    child1 = self.child_gen(1, current_floor, move_east)
                    children.append(child1)
                elif choice == move_west:
                    child3 = self.child_gen(3, current_floor, move_west)
                    children.append(child3)
            
        elif row > 0 and row < max_row and col == max_col: # Right edge
            if (move_north not in array_blocked_tiles 
                and move_north not in visited_set
            ):
                child0 = self.child_gen(0, current_floor, move_north)
                children.append(child0)

            if (move_south not in array_blocked_tiles 
                  and move_south not in visited_set
            ):
                child2 = self.child_gen(2, current_floor, move_south)
                children.append(child2)

            if (move_west not in array_blocked_tiles 
                  and move_west not in visited_set
            ):
                child3 = self.child_gen(3, current_floor, move_west)
                children.append(child3)

            if not children: # Get un-stuck
                options = [x for x in moves if x not in array_blocked_tiles]
                choice = random.choice(options)

                if choice == move_north:
                    child0 = self.child_gen(0, current_floor, move_north)
                    children.append(child0)
                elif choice == move_south:
                    child2 = self.child_gen(2, current_floor, move_south)
                    children.append(child2)
                elif choice == move_west:
                    child3 = self.child_gen(3, current_floor, move_west)
                    children.append(child3)
            
        elif row == max_row and col == max_col: # Bottom right corner 
            if (move_north not in array_blocked_tiles 
                and move_north not in visited_set
            ):
                child0 = self.child_gen(0, current_floor, move_north)
                children.append(child0)

            if (move_west not in array_blocked_tiles 
                  and move_west not in visited_set
            ):
                child3 = self.child_gen(3, current_floor, move_west)
                children.append(child3)

            if not children: # Get un-stuck
                options = [x for x in moves if x not in array_blocked_tiles]
                choice = random.choice(options)

                if choice == move_north:
                    child0 = self.child_gen(0, current_floor, move_north)
                    children.append(child0)
                elif choice == move_west:
                    child3 = self.child_gen(3, current_floor, move_west)
                    children.append(child3)
            
        elif row == 0 and col == max_col: # Top right corner
            if (move_south not in array_blocked_tiles 
                and move_south not in visited_set
            ):
                child2 = self.child_gen(2, current_floor, move_south)
                children.append(child2)

            if (move_west not in array_blocked_tiles 
                and move_west not in visited_set
            ):
                child3 = self.child_gen(3, current_floor, move_west)
                children.append(child3)

            if not children: # Get un-stuck
                options = [x for x in moves if x not in array_blocked_tiles]
                choice = random.choice(options)

                if choice == move_south:
                    child2 = self.child_gen(2, current_floor, move_south)
                    children.append(child2)
                elif choice == move_west:
                    child3 = self.child_gen(3, current_floor, move_west)
                    children.append(child3)
            
        elif row == 0 and col == 0: # Top left corner
            if (move_east not in array_blocked_tiles 
                and move_east not in visited_set
            ):
                child1 = self.child_gen(1, current_floor, move_east)
                children.append(child1)

            if (move_south not in array_blocked_tiles 
                and move_south not in visited_set
            ):
                child2 = self.child_gen(2, current_floor, move_south)
                children.append(child2)

            if not children: # Get un-stuck
                options = [x for x in moves if x not in array_blocked_tiles]
                choice = random.choice(options)

                if choice == move_east:
                    child1 = self.child_gen(1, current_floor, move_east)
                    children.append(child1)
                elif choice == move_south:
                    child2 = self.child_gen(2, current_floor, move_south)
                    children.append(child2)

        elif row == max_row and col == 0: # Bottom left corner
            if (move_north not in array_blocked_tiles 
                and move_north not in visited_set
            ):
                child0 = self.child_gen(0, current_floor, move_north)
                children.append(child0)

            if (move_east not in array_blocked_tiles 
                and move_east not in visited_set
            ):
                child1 = self.child_gen(1, current_floor, move_east)
                children.append(child1)

            if not children: # Get un-stuck
                options = [x for x in moves if x not in array_blocked_tiles]
                choice = random.choice(options)

                if choice == move_north:
                    child0 = self.child_gen(0, current_floor, move_north)
                    children.append(child0)
                elif choice == move_east:
                    child1 = self.child_gen(1, current_floor, move_east)
                    children.append(child1)

        return children
        

    def child_gen(self, move, current_floor, new_pos):
        global visited_set

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