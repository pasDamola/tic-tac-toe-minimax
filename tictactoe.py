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
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
          if(board[i][j] == EMPTY):
            count += 1
    if count % 2 == 0:
        turn = O
    else:
        turn = X
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
    playing = player(new_board)
    possible_actions = actions(board)
    if new_board[action[0]][action[1]] != EMPTY:
        raise ValueError("Incorrect Move")
    if playing == O:    
        new_board[action[0]][action[1]] = O
    else:
        new_board[action[0]][action[1]] = X
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
    who_won = winner(board)
    if who_won != None:
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
    if terminal(board) == False:
        return None
    if player(board) == X:
        max_value(board)
    else:
        min_value(board)


def max_value(board):
    """
    Returns the most maximum play possible, with the possible set of moves
    """
    if terminal(board) == True:
        return utility(board)
    v = -float('inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    """
    Returns the most minimum play possible, with the possible set of moves
    """
    if terminal(board) == True:
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
