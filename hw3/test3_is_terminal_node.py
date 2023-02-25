import numpy as np

# test is_terminal_node
# tip: use your tested evaluate() to help with this


def evaluate(board):

    win_criteria = board.shape[0]
    # Check rows, columns, diagonal for 'X' win
    if (
        win_criteria in board.sum(axis=0)
        or win_criteria in board.sum(axis=1)
        or np.sum(np.diagonal(board)) == win_criteria
        or np.sum(np.fliplr(board).diagonal()) == win_criteria
    ):
        return 1

    # Check rows, columns, diagonal for 'O' win
    elif (
        -1 * win_criteria in board.sum(axis=0)
        or -1 * win_criteria in board.sum(axis=1)
        or np.sum(np.diagonal(board)) == -1 * win_criteria
        or np.sum(np.fliplr(board).diagonal()) == -1 * win_criteria
    ):
        return -1

    return 0


def is_terminal_node(board):
    '''
    board_val = evaluate(board)

    if board_val == 1 or board_val == -1:
        return True
    elif board_val == 0 and np.argwhere(board == 0).size == 0:
        return True
    else:
        return False
    '''

    board_val = evaluate(board)
    zero_in_board = 0 in board

    if board_val == 1 or board_val == -1:
        return True
    elif board_val == 0 and not zero_in_board:
        return True
    else:
        return False

#### TEST CODE ##########
def run_tests():

    # TEST1 : Not terminal
    b = np.array([[1, 0, -1], [1, 0, 0], [-1, 0, 0]])
    is_terminal = is_terminal_node(b)
    expected = False

    if is_terminal == expected:
        print(f"PASS Test 1 Non Terminal Board")
    else:
        print(
            f"FAIL Test 1 Non Terminal Board: \
        expect: {expected} actual: {is_terminal}"
        )

    # TEST 2: Terminal
    b = np.array([[1, 1, 1], [1, -1, -1], [-1, 0, 0]])
    is_terminal = is_terminal_node(b)
    expected = True

    if is_terminal == expected:
        print(f"PASS Test 2  Terminal Board")
    else:
        print(
            f"FAIL Test 2  Terminal Board: \
            expect: {expected} actual: {is_terminal}"
        )

    # TEST3
    b = np.array([[1, -1, 1], [1, 1, -1], [-1, 1, -1]])
    is_terminal = is_terminal_node(b)
    expected = True

    if is_terminal == expected:
        print(f"PASS Test 3  Terminal Board")
    else:
        print(
            f"FAIL Test 3  Terminal Board: \
            expect: {expected} actual: {is_terminal}"
        )

    # TEST4 Win for X on diagonal
    b = np.array([[1, 0, 0], [0, 1, -1], [-1, -1, 1]])
    is_terminal = is_terminal_node(b)
    expected = True

    if is_terminal == expected:
        print(f"PASS Test 4  Terminal Board")
    else:
        print(
            f"FAIL Test 4  Terminal Board: \
            expect: {expected} actual: {is_terminal}"
        )

    # TEST5 win for O on reverse diagonal
    b = np.array([[1, 1, -1], [0, -1, 1], [-1, -1, 1]])
    is_terminal = is_terminal_node(b)
    expected = True

    if is_terminal == expected:
        print(f"PASS Test 5  Terminal Board")
    else:
        print(
            f"FAIL Test 5  Terminal Board: \
            expect: {expected} actual: {is_terminal}"
        )

    # TEST6 win for O on reverse diagonal for 4x4 board
    b = np.array(
        [[1, 1, 0, -1], [0, 0, -1, 1], [0, -1, 1, 0], [-1, 0, 0, 0]]
    )
    is_terminal = is_terminal_node(b)
    expected = True

    if is_terminal == expected:
        print(f"PASS Test 6  Terminal Board")
    else:
        print(
            f"FAIL Test 6  Terminal Board: \
                expect: {expected} actual: {is_terminal}"
        )


run_tests()
