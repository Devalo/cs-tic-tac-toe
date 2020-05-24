EMPTY = None
X = "X"
board = [[EMPTY, EMPTY, EMPTY],
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
    empty_board = False

    for cell in board:
        empty_board = all(c is None for c in cell)

    if empty_board == True:
        return X


print(player(board))
