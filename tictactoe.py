"""
Tic Tac Toe Player
"""

import math
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
    """
    #check if thee board is in the initial state
    if board == initial_state():
        turn = X
    #if it is not initial state and X has played then return O
    elif board != initial_state() and turn == X:
        turn = O
    return turn



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    #loop over the game board
    for i in range(len(board)):
        for j in range(len(board[i])):
            #check if any of the cells are empty and add them to the set
            if board[i][j] != X and board[i][j] != O:
                possible_actions.add((i,j))
    return possible_actions
                
            



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    player = player(new_board)
    possible_moves = actions(new_board)
    possible_moves = list(possible_moves)
    action = possible_moves[0]
    i = action[0]
    j = action[1]
    new_board[i][j] = player
    return new_board

    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # horizontal wins for X
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == "X":
        return X
    else:
        return None
    if board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == "X":
        return X
    else:
        return None
    if board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == "X":
        return X
    else:
        return None
    # vertical wins for X
    if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == "X":
        return X
    else:
        return None
    if board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == "X":
        return X
    else:
        return None
    if board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == "X":
        return X
    else:
        return None
    # diagonal wins for X
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return X
    else:
        return None
    if board[0][2] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
        return X
    else:
        return None
     # horizontal wins for O
    if board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
        return O
    else:
        return None
    if board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
        return O
    else:
        return None
    if board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
        return O
    else:
        return None
    # vertical wins for O
    if board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
        return O
    else:
        return None
    if board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        return O
    else:
        return None
    if board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        return O
    else:
        return None
    # diagonal wins for O
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        return O
    else:
        return None
    if board[0][2] == 'O' and board[1][1] == 'O' and board[0][2] == 'O':
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    winner = winner(board)
    if winner != None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        player = player(board)
        if player == X:
            return 1
        elif player == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
