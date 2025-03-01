"""
Tic Tac Toe Player
"""
import copy
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
    xcount = 0
    ocount = 0
    for line in board:
        for cell in line:
            if cell == X:
                xcount += 1
            elif cell == O:
                ocount += 1
    
    if xcount > ocount:
        return O
    else:
        return X

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibilites=set()
    for line in range(3):
        for cell in range(3):
            if board[line][cell] is None:
                possibilites.add((line, cell))

    return possibilites
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardresult = copy.deepcopy(board)
    if action not in actions(boardresult):
        raise Exception
    if player(boardresult) == X:
        boardresult[action[0]][action[1]] = X
    else:
        boardresult[action[0]][action[1]] = O
    
    return boardresult
    raise NotImplementedError

def equal(list):

    if list[0] is not None:
        if list[0] == list[1] == list[2]:
            return True
    return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    fordiag = []
    backdiag = []
    for line in range(3):

        checkline = [None, None, None]
        checkcolumn = [None, None, None]
        backdiag.append(board[line][line])
        fordiag.append(board[line][-1-line])

        for cell in range(3):

            checkline[cell] = board[line][cell]
            checkcolumn[cell] = board[cell][line]

        
        if equal(checkline):
            return checkline[0]

        if equal(checkcolumn):
            return checkcolumn[0]

    if equal(fordiag):
        return fordiag[0]
        
    if equal(backdiag):
        return backdiag[0]
    
    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    ecount = 0

    for line in range(3):
        for cell in range(3):
            if board[line][cell] is None:
                ecount += 1
    
    if ecount == 0:
        return True

    return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) is None:
        return 0

    elif winner(board) == X:
        return 1
    
    else:
        return -1
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        return maxvalue(board)[1]

    else:
        return minvalue(board)[1]

    raise NotImplementedError

def minvalue(board):
    if terminal(board):
        return (utility(board), None)

    v = math.inf

    for action in actions(board):
        a = v
        v = min(v, maxvalue(result(board, action))[0])
        if a != v:
            tmp = action

    return (v, tmp)
    raise NotImplementedError

def maxvalue(board):
    if terminal(board):
        return (utility(board), None)

    v = - math.inf

    for action in actions(board):
        a = v
        v = max(v, minvalue(result(board, action))[0])
        if a != v:
            tmp= action

    return (v, tmp)