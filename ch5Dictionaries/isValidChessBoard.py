import copy

testBoard = {'1h': 'bking',
         '6c': 'wqueen',
         '2g': 'bbishop',
         '5h': 'bqueen',
         '3e': 'wking'}

halfBoard = {'1a': 'brook',
          '1b': 'bknight',
          '1c': 'bbishop',
          '1d': 'bqueen',
          '1e': 'bking',
          '1f': 'bbishop',
          '1g': 'bknight',
          '1h': 'brook',
          '2a': 'bpawn',
          '2b': 'bpawn',
          '2c': 'bpawn',
          '2d': 'bpawn',
          '2e': 'bpawn',
          '2f': 'bpawn',
          '2g': 'bpawn',
          '2h': 'bpawn',
          '8d': 'wking'
          }

def isValidChessBoard(board):
    # check exactly 1 black, 1 white king
    count = {}
    for piece in board.values():
        count.setdefault(piece, 0)
        count[piece] = count[piece] + 1
    if not('wking' in count and 'bking' in count):
        print('Board is missing a king - ', end='')
        return False
    if not(count['bking'] == 1 and count['wking'] == 1):
        print('Board has too many kings - ', end='')
        return False
    # check each player max 16 pieces
    count = {}
    count.setdefault('b', 0)
    count.setdefault('w', 0)
    for piece in board.values():
        if piece[0] == 'b':
            count['b'] = count['b'] + 1
        if piece[0] == 'w':
            count['w'] = count['w'] + 1
    if not(count['b'] <= 16 and count['w'] <= 16):
        print('Board failed 16 max pieces per player - ', end='')
        return False
    # check each player max 8 pawns
    count = {}
    count.setdefault('wpawn', 0)
    count.setdefault('bpawn', 0)
    for piece in board.values():
        count.setdefault(piece, 0)
        count[piece] = count[piece] + 1
    if not(count['bpawn'] <= 8 and count['wpawn'] <= 8):
        print('Board has too many pawns - ', end='')
        return False
    # check all pieces on 1a to 8h
    height = ['1', '2', '3', '4', '5', '6', '7', '8']
    width = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for place in board.keys():
        if not(place[0] in height and place[1] in width):
            print('Piece not on valid space - ', end='')
            return False
    # check piece names start with w or b
    for piece in board.values():
        if not(piece[0] == 'b' or piece[0] == 'w'):
            print('Piece names must begin with w or b - ', end='')
            return False
    # check pieces names contain pawn, knight, bishop, rook, queen or king
    names = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    for piece in board.values():
        if not(piece[1:] in names):
            print('Piece name is not valid - ', end='')
            return False
    # if all checks passed, print validation statement and return True
    print('Board is valid - ', end='')
    return True


print('testBoard:', isValidChessBoard(testBoard))
print('halfBoard:', isValidChessBoard(halfBoard))
# remove a king and test
board1 = copy.copy(testBoard)
board1.pop('1h')
print('Board 1:', isValidChessBoard(board1))
# add an extra king and test
board2 = copy.copy(testBoard)
board2.setdefault('2h', 'bking')
print('Board 2:', isValidChessBoard(board2))
# add an extra piece to half board and test
board3 = copy.copy(halfBoard)
board3.setdefault('3a', 'bpawn')
print('Board 3:', isValidChessBoard(board3))
# swap in an extra pawn to half board and test
board4 = copy.copy(halfBoard)
board4.update({'1h': 'bpawn'})
print('Board 4:', isValidChessBoard(board4))
# add a piece on an invalid space and test
board5 = copy.copy(testBoard)
board5.update({'9a':'bpawn'})
print('Board 5:', isValidChessBoard(board5))
# add a piece that doesn't begin with w or b and test
board6 = copy.copy(testBoard)
board6.update({'3a': 'purplepawn'})
print('Board 6:', isValidChessBoard(board6))
# add a piece that doesn't contain valid name and test
board7 = copy.copy(testBoard)
board7.update({'3a': 'bhorseyguy'})
print('Board 7:', isValidChessBoard(board7))
