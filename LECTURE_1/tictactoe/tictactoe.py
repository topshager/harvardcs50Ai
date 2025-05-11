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
    """ 
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)

    if x_count <= o_count:
        return  'X'
    else:
        return  'O'
    

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = []
    for i , row in enumerate(board):
        for j,cell in enumerate(row):
           if cell is None:
                actions.append((i,j))
    return action




    
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action.pop()
    board[i][j] = player
    return board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1]  == row[2] and row[0]is not None:
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
        

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    return None
    
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        if None in row:
            return False  
    return True

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0
    
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """





    raise NotImplementedError
