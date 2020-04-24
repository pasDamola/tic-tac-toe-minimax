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
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
