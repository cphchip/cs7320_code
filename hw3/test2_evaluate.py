import numpy as np

def evaluate(board):
    '''returns 1 for X win, -1 for O win, 0 for tie OR game in progress
    Using numpy functions to add values in rows and cols
    If we get a sum equal to size of row,col,diag (plus or minus)
     we have a winner
    '''

    '''
    i = 0
    j = 0

    while i <= 2:
        while j <= 2:
            if ((board[i][j] == board[i][j+1] and 
                board[i][j+1] == board[i][j+2]) or 
                (board[i][j] == board[i+1][j] and 
                board[i+1][j] == board[i+2][j])):

                if board[i][j] == 1:
                    return 1
                elif board[i][j] == -1:
                    return -1
                elif board[i][j] == 0:
                    return 0
        j += 1
    i += 1
    '''
    
    i = 0
    print(np.sum(board,0)[0]) # sum the first column
    # FYI Axis 0 in numpy refers to columns
    # Axis 1 refers to rows
    
    while i <= 2:
        print (np.sum(board,0)[i] == 1)
        print (np.sum(board,1)[i])
        if np.sum(board,0)[i] == 3 or np.sum(board,1)[i] == 3:
            return 1
        elif np.sum(board,0)[i] == -3 or np.sum(board,1)[i] == -3:
            return -1

        i += 1
    return 0

    i = 0
    j = 0

    while i <= 2: # Detect row win

        if (board[i][j] == board[i][j+1] and 
            board[i][j+1] == board[i][j+2]): 

            if board[i][j] == 1:
                return 1
            elif board[i][j] == -1:
                return -1
            elif board[i][j] == 0:
                return 0
            
        i += 1


    i = 0
    j = 0

    while j <= 2: # Detect column win
        
        if (board[i][j] == board[i+1][j] and 
            board[i+1][j] == board[i+2][j]):

            if board[i][j] == 1: 
                return 1
            elif board[i][j] == -1:
                return -1
            elif board[i][j] == 0:
                return 0
                    
        j += 1

    # Detect diagaonal win
    if board[0][0] == board [1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][0]:
        return board[0][2]


#### TEST CODE ##########
def run_tests():
    b = np.array([[1, 0, -1], [1, 0, 0], [-1, 0, 0]])

    #TEST1 : No winner
    b = np.array([[1, 0, -1], [1, 0, 0], [-1, 0, 0]])
    score = evaluate(b)
    expect = 0

    if score == expect:
        print (f"PASS Test 1 No Win")
    else: print (f"FAIL Test 1 No Win: \
        expect: {expect} actual: {score}")

    #TEST 2: Win for X
    b = np.array([[1, 0, -1], [1, 0, 0], [1, 0, -1]])
    score = evaluate(b)
    expect = 1

    if score == expect:
        print (f"PASS Test 2  column win")
    else: print (f"FAIL Test 2: column win \
        expect: {expect} actual: {score}")

    #TEST3 Win for O
    b = np.array([[-1, -1, -1], [1, 0, 1], [1, 0, 1]])
    score = evaluate(b)
    expect = -1

    if score == expect:
        print (f"PASS Test 3  row win")
    else: print (f"FAIL Test 3: row win \
        expect: {expect} actual: {score}")


    #TEST4 Win for X on diagonal
    b = np.array([[-1, -1, 1], [1, 1, 1], [1, 0, -1]])
    score = evaluate(b)
    expect = 1

    if score == expect:
        print (f"PASS Test 4  diag win")
    else: print (f"FAIL Test 4: diag win \
        expect: {expect} actual: {score}")

    #TEST5 win for O on reverse diagonal
    b = np.array([[-1, 1, 1], [1, -1, -1], [1, 0, -1]])
    score = evaluate(b)
    expect = -1

    if score == expect:
        print (f"PASS Test 5  diag2 win")
    else: print (f"FAIL Test 5: diag2 win \
        expect: {expect} actual: {score}")

    #TEST6 win for O on reverse diagonal for 4x4 board
    b = np.array([[-1, 1, 1, 0], [1, -1, -1, 0], \
                  [1, 0, -1, 0], [1,0,0,-1]])
    score = evaluate(b)
    expect = -1

    if score == expect:
        print (f"PASS Test 6  diag2 win 4x4")
    else: print (f"FAIL Test 6: diag2 win 4x4 \
        expect: {expect} actual: {score}")


run_tests()