#take a dictionary argument
# return True or False depending on if the board is valid
#valid board =
    # one black king
    # one white king
    # at most 16 pieces per color
    # at most 8 wpawn and 8 bpawn
    # all pieces on valid spaces
    # piece names begin with w or b follwed by pawn, knight, bishop, rook, queen or king

import string

test_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

rows = list(range(1,9))
columns = list(string.ascii_lowercase[:8])

validspaces = []
for row in rows:
    for column in columns:
        validspaces.append(str(row) + column)

print(validspaces)


def checkkings(board):
    duplicatelist = []
    uniquelist = []
    for value in board.values():
        if value in uniquelist:
            duplicatelist.append(value)
        else:
            uniquelist.append(value)
    if ('bking' and 'wking') in board.values() and ('bking' and 'wking') not in duplicatelist:
        print('bking')
        return True
    else:
        print('not legit!')
        return False

def piececount(board):
    if len(board.values()) > 16:
        print('too many pieces!', len(board.values()))
        return False
    else:
        print('good number of pieces')
        return True

def validspace(board):
    for space in board:
        if space not in validspaces:
            print('not a valid space')
            return False
    else:
        print('spaces are good')


def validchessboard(board):
    checkkings(board)
    piececount(board)
    validspace(board)

validchessboard(test_board)
