"""

Following dictionary {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
represents a chess board. Write a function named isValidChessBoard() that takes a dictionary argument
and returns True or False depending on if the board is valid.

A valid board will have exactly one black king and exactly one white king. Each player can only have
at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is,
a piece can’t be on space '9z'. The piece names begin with either a 'w' or 'b' to represent white or black,
followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. This function should detect when a bug
has resulted in an improper chess board.

"""

my_dict = {'1h': 'wpawn', '6c': 'wpawn', '2g': 'wpawn',
           '2h': 'wpawn', '7c': 'wpawn',
           '3h': 'wpawn', '8c': 'wpawn',
           '4h': 'wpawn', '9c': 'wpawn'}


def isValidChessBoard(dict):
    b = 0
    w = 0
    wpawns = 0
    wrooks = 0
    wknights = 0
    wbishops = 0
    wqueen = 0
    wking = 0

    bpawns = 0
    brooks = 0
    bknights = 0
    bbishops = 0
    bqueen = 0
    bking = 0

    for key, value in dict.items():
        figures = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
        # print(key, value)
        # print(value[1:])

        # check whether the board cells are valid or not
        if key[0] not in '123456789' or key[1] not in 'abcdefgh':
            print(f"{key} is wrong")
            return False

        # check whether the figure names are valid or not
        if value[0] not in 'bw' or value[1:] not in figures:
            print(f"{value[0]} not in b or {value[1:]} is not a valid figure")
            return False

        if value[0] == 'b':
            b += 1
            if value[1:] == 'pawn':
                bpawns += 1
            if value[1:] == 'rook':
                brooks += 1
            if value[1:] == 'knight':
                bknights += 1
            if value[1:] == 'bishop':
                bbishops += 1
            if value[1:] == 'queen':
                bqueen += 1
            if value[1:] == 'king':
                bking += 1

        if value[0] == 'w':
            w += 1
            if value[1:] == 'pawn':
                wpawns += 1
            if value[1:] == 'rook':
                wrooks += 1
            if value[1:] == 'knight':
                wknights += 1
            if value[1:] == 'bishop':
                wbishops += 1
            if value[1:] == 'queen':
                wqueen += 1
            if value[1:] == 'king':
                wking += 1

        print(b, w)
        if b >= 16 or w >= 16:
            print("There are way too many pieces")
            return False

        if (brooks or wrooks or
            bknights or wknights or
            bbishops or wbishops) > 2:
            print("There has to be only a pair of rooks, knights and bishops of each color")
            return False

        if (wking or bking or wqueen or bqueen) > 1:
            print("There has to be only one queen/king of one color")
            return False

        if w or b == 0:
            print("Pieces of both color have to be placed on the board")
            return False


print(isValidChessBoard(my_dict))
