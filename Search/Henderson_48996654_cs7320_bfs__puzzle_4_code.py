# bfs__puzzle_4a
import copy
import math
from queue import PriorityQueue


def get_child_boards_list(board) -> list:
    # Get index of blank tile
    blank_position = get_index(board)

    # Collect values of surrounding tiles, handle bounds errors
    try:
        r_tile = board[blank_position[0]][blank_position[1] + 1]
    except IndexError:
        r_tile = None
    try:
        l_tile = board[blank_position[0]][blank_position[1] - 1]
    except IndexError:
        l_tile = None
    try:
        u_tile = board[blank_position[0] - 1][blank_position[1]]
    except IndexError:
        u_tile = None
    try:
        d_tile = board[blank_position[0] + 1][blank_position[1]]
    except IndexError:
        d_tile = None

    # The following section of code accounts for all possible board configurations that would affect the child outcome
    # [middle, middle] condition
    if (
        blank_position[0] >= 1
        and blank_position[1] >= 1
        and blank_position[0] < len(board) - 1
        and blank_position[1] < len(board) - 1
    ):

        child1 = create_child(board, l_tile, "l", blank_position)
        child2 = create_child(board, r_tile, "r", blank_position)
        child3 = create_child(board, u_tile, "u", blank_position)
        child4 = create_child(board, d_tile, "d", blank_position)

        return [child1] + [child2] + [child3] + [child4]

    # [0, 0] condition
    elif blank_position[0] == 0 and blank_position[1] == 0:
        child2 = create_child(board, r_tile, "r", blank_position)
        child4 = create_child(board, d_tile, "d", blank_position)

        return [child2] + [child4]

    # [0, max] condition
    elif blank_position[0] == 0 and blank_position[1] == len(board) - 1:
        child1 = create_child(board, l_tile, "l", blank_position)
        child4 = create_child(board, d_tile, "d", blank_position)

        return [child1] + [child4]

    # [max, max] condition
    elif blank_position[0] == blank_position[1] == len(board) - 1:
        child1 = create_child(board, l_tile, "l", blank_position)
        child3 = create_child(board, u_tile, "u", blank_position)

        return [child1] + [child3]

    # [max, 0] condition
    elif blank_position[0] == len(board) - 1 and blank_position[1] == 0:
        child2 = create_child(board, r_tile, "r", blank_position)
        child3 = create_child(board, u_tile, "u", blank_position)

        return [child2] + [child3]

    # left edge condition
    elif (
        blank_position[0] > 0
        and blank_position[0] < len(board) - 1
        and blank_position[1] == 0
    ):
        child2 = create_child(board, r_tile, "r", blank_position)
        child3 = create_child(board, u_tile, "u", blank_position)
        child4 = create_child(board, d_tile, "d", blank_position)

        return [child2] + [child3] + [child4]

    # right edge condition
    elif (
        blank_position[0] > 0
        and blank_position[0] < len(board) - 1
        and blank_position[1] == len(board) - 1
    ):
        child1 = create_child(board, l_tile, "l", blank_position)
        child3 = create_child(board, u_tile, "u", blank_position)
        child4 = create_child(board, d_tile, "d", blank_position)

        return [child1] + [child3] + [child4]

    # bottom edge condition
    elif (
        blank_position[0] == len(board) - 1
        and blank_position[1] < len(board) - 1
        and blank_position[1] > 0
    ):
        child1 = create_child(board, l_tile, "l", blank_position)
        child2 = create_child(board, r_tile, "r", blank_position)
        child3 = create_child(board, u_tile, "u", blank_position)

        return [child1] + [child2] + [child3]

    # top edge condition
    elif (
        blank_position[0] == 0
        and blank_position[1] > 0
        and blank_position[1] < len(board) - 1
    ):
        child1 = create_child(board, l_tile, "l", blank_position)
        child2 = create_child(board, r_tile, "r", blank_position)
        child4 = create_child(board, d_tile, "d", blank_position)

        return [child1] + [child2] + [child4]


# Creates child configurations based on possible combination of moves
def create_child(board, tile_val, type, blank_position):
    if type == "l":
        child1 = copy.deepcopy(board)
        child1[blank_position[0]][blank_position[1]] = tile_val
        child1[blank_position[0]][blank_position[1] - 1] = 0

        return child1

    elif type == "r":

        child2 = copy.deepcopy(board)

        child2[blank_position[0]][blank_position[1]] = tile_val
        child2[blank_position[0]][blank_position[1] + 1] = 0

        return child2

    elif type == "u":
        child3 = copy.deepcopy(board)
        child3[blank_position[0]][blank_position[1]] = tile_val
        child3[blank_position[0] - 1][blank_position[1]] = 0

        return child3

    else:
        child4 = copy.deepcopy(board)
        child4[blank_position[0]][blank_position[1]] = tile_val
        child4[blank_position[0] + 1][blank_position[1]] = 0

        return child4


def get_index(board) -> list:
    for row in board:
        for tile in row:
            if tile == 0:
                return [board.index(row), row.index(tile)]


# Declare global board count variable
bfs_count = 0


def bfs2(start_board, goal_board):
    queue = [([start_board])]

    while queue:
        path = queue.pop(0)
        vertex = path[-1]
        global bfs_count
        child_list = get_child_boards_list(vertex)

        next_node_list = [x for x in child_list if x not in path]

        for next in next_node_list:
            bfs_count += 1
            print(bfs_count)
            if next == goal_board:
                return path + [next]
            else:
                queue.append(path + [next])


def bfs2_euclidean(start_board, goal_board):
    queue = PriorityQueue()

    # Establish dictionary with goal_board x, y coordinates
    goal_dict = {}
    for y_val, row in enumerate(goal_board):
        for x_val, tile in enumerate(row):
            goal_dict.setdefault(tile, [x_val, y_val])

    # Establish dictionary with start_board x, y coordinates
    start_dict = {}
    for y_val, row in enumerate(start_board):
        for x_val, tile in enumerate(row):
            start_dict.setdefault(tile, [x_val, y_val])

    # Calculate ED for start_board to goal_board
    euc_dist = 0
    for tile in start_dict:
        euc_dist = euc_dist + math.dist(
            start_dict.get(tile), goal_dict.get(tile)
        )

    # Put this initial value in the priority queue
    queue.put((euc_dist, [start_board]))

    while not queue.empty():
        euc_dist, path = queue.get()
        vertex = path[-1]
        global bfs_count

        vertex_dict = {}
        for y_val, row in enumerate(vertex):
            for x_val, tile in enumerate(row):
                vertex_dict.setdefault(tile, [x_val, y_val])

        euc_dist = 0
        for tile in vertex_dict:
            euc_dist = euc_dist + math.dist(
                vertex_dict.get(tile), goal_dict.get(tile)
            )

        child_list = get_child_boards_list(vertex)

        next_node_list = [x for x in child_list if x not in path]

        for next in next_node_list:
            next_dict = {}
            for y_val, row in enumerate(next):
                for x_val, tile in enumerate(row):
                    next_dict.setdefault(tile, [x_val, y_val])

            next_euc_dist = 0
            for tile in next_dict:
                next_euc_dist = euc_dist + math.dist(
                    next_dict.get(tile), goal_dict.get(tile)
                )

            bfs_count += 1
            print(bfs_count)
            if next == goal_board:
                return path + [next]
            else:
                total_distance = next_euc_dist + euc_dist
                queue.put((total_distance, path + [next]))


def bfs2_manhattan(start_board, goal_board):

    queue = PriorityQueue()

    goal_dict = {}
    for y_val, row in enumerate(goal_board):
        for x_val, tile in enumerate(row):
            goal_dict.setdefault(tile, [x_val, y_val])

    start_dict = {}
    for y_val, row in enumerate(start_board):
        for x_val, tile in enumerate(row):
            start_dict.setdefault(tile, [x_val, y_val])

    man_dist = 0
    for tile in start_dict:
        man_dist = (
            man_dist
            + abs(start_dict.get(tile)[0] - goal_dict.get(tile)[0])
            + abs(start_dict.get(tile)[1] - goal_dict.get(tile)[1])
        )

    queue.put((man_dist, [start_board]))

    while not queue.empty():
        man_dist, path = queue.get()
        vertex = path[-1]
        global bfs_count

        vertex_dict = {}
        for y_val, row in enumerate(vertex):
            for x_val, tile in enumerate(row):
                vertex_dict.setdefault(tile, [x_val, y_val])

        man_dist = 0
        for tile in start_dict:
            man_dist = (
                man_dist
                + abs(vertex_dict.get(tile)[0] - goal_dict.get(tile)[0])
                + abs(vertex_dict.get(tile)[1] - goal_dict.get(tile)[1])
            )

        child_list = get_child_boards_list(vertex)

        next_node_list = [x for x in child_list if x not in path]

        for next in next_node_list:
            next_dict = {}
            for y_val, row in enumerate(next):
                for x_val, tile in enumerate(row):
                    next_dict.setdefault(tile, [x_val, y_val])

            next_man_dist = 0
            for tile in next_dict:
                next_man_dist = (
                    man_dist
                    + abs(
                        next_dict.get(tile)[0] - goal_dict.get(tile)[0]
                    )
                    + abs(
                        next_dict.get(tile)[1] - goal_dict.get(tile)[1]
                    )
                )

            bfs_count += 1
            print(bfs_count)
            if next == goal_board:
                return path + [next]
            else:
                total_distance = man_dist + next_man_dist
                queue.put((total_distance, path + [next]))


def main():
    # Start/goal for 8-puzzle
    # start_state = [[4,1,3],[2,0,6],[7,5,8]]
    # goal_state = [[1,2,3],[4,5,6],[7,8,0]]

    # Start/goal for 15 puzzle
    start_state = [
        [2, 3, 7, 4],
        [1, 6, 8, 12],
        [5, 9, 11, 15],
        [13, 10, 0, 14],
    ]
    goal_state = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0],
    ]

    print(bfs2(start_state, goal_state))


# Declare global board count variable
bfs_count = 0


# run the main function
main()
