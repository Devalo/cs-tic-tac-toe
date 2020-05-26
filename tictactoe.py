"""
Tic Tac Toe Player
"""

import math
import random
import copy

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
            return O
        else:
            return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    
    - Figures out which possible moves to do next

    """
    available_moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                available_moves.add((i, j))
    return available_moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    If having a state, and taking an action, we need a result

    - takes the board, and the move as input, and returns the new board
      with the new action
    """
    
    nboard = copy.deepcopy(board)

    if nboard[action[0]][action[1]] != EMPTY:
        raise ValueError("Already taken")
    else:
        nboard[action[0]][action[1]] = player(nboard)
        return nboard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
        elif board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        elif board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]

def terminal(board):
    """
    Returns True if game is over, False otherwise.

    - takes the game board as input. If the game is over, returns true
    """

    # Determine if anyone has 3 in a row
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != None:
            return True
        elif board[0][i] == board[1][i] == board[2][i] != None:
            return True
        elif board[0][0] == board[1][1] == board[2][2] != None:
            return True
        elif board[0][2] == board[1][1] == board[2][0] != None:
            return True


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

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    
    should call action to get every move possible for the current player

    """

    playing = player(board)
    
    if playing == X:
        v = -math.inf
        for action in actions(board):
            move = min_value(result(board, action))
            if move > v:
                v = move
                best_move = action
    else:
        v = math.inf 
        for action in actions(board):
            move = max_value(result(board, action))
            if move < v:
                v = move
                best_move = action
    return best_move

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v
    
def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v