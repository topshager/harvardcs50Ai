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
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)

    if x_count <= o_count:
        return  'X'
    else:
        return  'O'
    




def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = []
    for i , row in enumerate(board):
        for j,cell in enumerate(row):
           if cell is None:
                action.append((i,j))
    return action




    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    if board[i][j]  is not None:
        raise Exception("Invalid action")
    
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return  new_board


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
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board) ,None
    
    current = player(board)

    def max_value(board):
        if terminal(board):
            return utility(board) , None
        v = -math.inf
        best_action = None
        for action in actions(board):
            min_result =  mini_value(result(board,action))[0]
            if min_result > v:
                v = min_result
                best_action = action
            if v == 1:
                break 
        return v,best_action
    
    def mini_value(board):
        if terminal(board):
            return utility(board),None
        v = math.inf
        best_action = None
        for action in actions(board):
            max_result = max_value(result(board,action))[0]
            if max_result < v:
                v = max_result
                best_action = action
            if v == -1:
                break 
        return v,best_action
    if current == X:
        return max_value(board)[1]
    else:
        return  mini_value(board)[1]
        

    





