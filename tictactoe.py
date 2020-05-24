"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.

    - takes a state, tells whos turn it is
    - assuming x makes a first move on an empty game board, player is x
    - if x has made a move, o is the player
    - takes a game board, and returns whos turn it is
    """
    empty_board = True
    count_x = 0
    count_o = 0
    f_list = []

    """
    for cell in board:
        empty_board = all(c is None for c in cell)
        print(all(c is None for c in cell))
    """

    # Check every item in board.
    # Flatten list, and put all elements in new list, for later use
    # Check if any of the cells contain X or O. If so, the board is not empty,
    # game has began, so we switch empty_board to False
    for cell in board:
        for i in cell:
            f_list.append(i)
            if i == X or i == O:
                empty_board = False




    # If board is empty, return X as the first player
    # else, figure out who's turn is next, by counting how many X and O's on the game board.
    if empty_board == True:
        return X
    else:
        count_x = f_list.count("X")
        count_o = f_list.count("O")
        if count_x > count_o:
            print("Computer turn")
            return O
        else:
            print("Player turn")
            return X




def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    
    - Figures out which possible moves to do next

    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    If having a state, and taking an action, we need a result

    - takes the board, and the move as input, and returns the new board
      with the new action
    """
    
    nboard = board.copy()
    if nboard[action[0]][action[1]] == None:
        nboard[action[0]][action[1]] = player(board)
    else:
        raise ValueError("Already taken")
    print("board from restult", nboard)
    return nboard



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.

    - takes the game board as input. If the game is over, returns true
    """
    l_flatten = []

    # Flattens the board, and check if None is in any of the cells.
    # If None is in any cells, the game is not finished, return False.
    # If None is NOT in any cells, the game board is filled out, and the game is over
    for cell in board:
        for i in cell:
            l_flatten.append(i)

    if None not in l_flatten:
        return True
    return False
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    
    should call action to get every move possible for the current player
    """
    print("From minimax")
    print(board)
    return (0,1)
    raise NotImplementedError

"""
function MAX-VALUE(state):
    if terminal(state):
        return utility(state)
    v = "-inf"
    for action in actions(state):
        v = max(v, min-value(result(state, action)))
    return v

function Min-Value(state):
    if terminal(state):
        return utility(state)
    v = "inf"
    for action in actions(state):
        v = min(v, max-value(result(state, action)))
    return v
"""