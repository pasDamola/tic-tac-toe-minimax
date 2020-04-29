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
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))
    return possible_actions
                
            



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    if terminal(board):
        raise ValueError("Game Over")
    elif action not in actions(board):
        return ValueError("Inappropriate Move")
    else:
        new_board = copy.deepcopy(board)
        playing = player(new_board)
        new_board[action[0]][action[1]] = playing
    return new_board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[1][0] == board[1][1] == board[1][2] != None:
        if board[1][0] == X:
            return X
        else:
            return O
    elif board[2][0] == board[2][1] == board[2][2] != None:
        if board[2][0] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][0] == board[2][0] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][1] == board[1][1] == board[2][1] != None:
        if board[0][1] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][2] == board[2][2] != None:
        if board[0][2] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][1] == board[2][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][1] == board[2][0] != None:
        if board[0][2] == X:
            return X
        else:
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
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    playing = player(board)

    if board == [[EMPTY] * 3] * 3:
        return (0,0)
    if playing == X:
        v = float('-inf')
        selected_action = None
        for action in actions(board):
            minValue = min_value(result(board, action), float('inf'))
            if minValue > v:
                v = minValue
                selected_action = action
    elif playing == O:
        v = float('inf')
        selected_action = None
        for action in actions(board):
            maxValue = max_value(result(board, action), float('-inf'))
            if maxValue < v:
                v = maxValue
                selected_action = action
    return selected_action


def max_value(board, beta):
    """
    Returns the most maximum play possible, with the possible set of moves
    """
    if terminal(board) == True:
        return utility(board)
    v = -float('inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action), beta))
        beta = max(v, beta)
    return v


def min_value(board, alpha):
    """
    Returns the most minimum play possible, with the possible set of moves
    """
    if terminal(board) == True:
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha))
        alpha = min(v, alpha)
    return v
