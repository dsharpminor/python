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

too_many_figures = {'1h': 'wpawn', '6c': 'wpawn', '2g': 'wpawn', '3g': 'bking', '4g': 'bking',
                    '2h': 'wpawn', '7c': 'wpawn', '3h': 'wpawn', '8c': 'wpawn', '4h': 'wpawn', '9c': 'wpawn',
                    '3c': 'wpawn'}

wrong_cell_names = {'ah': 'bking', '6z': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
white_only = {'1a': 'wking'}
long_cell_name = {'4a': 'wqueen', '12e': 'bking', '7e': 'wrook', '6d': 'bpawn'}


# my_dict = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def calculate(value, color):
    # print(f'{value}')
    if value == 'pawn':
        color['pawns'] += 1
    if value == 'rook':
        color['rooks'] += 1
    if value == 'knight':
        color['knights'] += 1
    if value == 'bishop':
        color['bishops'] += 1
    if value == 'queen':
        color['queen'] += 1
    if value == 'king':
        color['king'] += 1


def restrict_pieces(dictionary, color):
    a = True
    for k, v in dictionary.items():
        if k == 'pawns' and v > 8:
            print(
                f"There cannot be more than 8 {color} pawns, but there are {v} of them. Please remove {v - 8} of them.")
            a = False
        if k == 'rooks' and v > 2:
            print(
                f"There cannot be more than 2 {color} rooks, but there are {v} of them. Please remove {v - 2} of them.")
            a = False
        if k == 'knights' and v > 2:
            print(f"There cannot be more than 2 {color} knights, but there are {v} of them. Please remove {v - 2} of "
                  f"them.")
            a = False
        if k == 'bishops' and v > 2:
            print(f"There cannot be more than 2 {color} bishops, but there are {v} of them. Please remove {v - 2} of "
                  f"them.")
            a = False
        if k == 'queen' and v > 1:
            print(
                f"There cannot be more than 1 {color} queen, but there are {v} of them. Please remove {v - 1} of them.")
            a = False
        if k == 'king' and v > 1:
            print(
                f"There cannot be more than 1 {color} king, but there are {v} of them. Please remove {v - 1} of them.")
            a = False
    if sum(dictionary.values()) > 16:
        print(f"There cannot be more than 16 {color} pieces.")

    return a


def isValidChessBoard(dict):
    answer = True
    white = {'pawns': 0, 'rooks': 0, 'knights': 0, 'bishops': 0, 'queen': 0, 'king': 0}
    black = {'pawns': 0, 'rooks': 0, 'knights': 0, 'bishops': 0, 'queen': 0, 'king': 0}

    for key, value in dict.items():
        figures = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

        # check whether the board cells are valid or not
        if key[0] not in '123456789' or key[1] not in 'abcdefgh' or len(key) > 2:
            print(f"Non-existent cell: {key}")
            answer = False

        # check whether the figure names are valid or not
        if value[0] not in 'bw' or value[1:] not in figures:
            print(f"{value[0]} not in b or {value[1:]} is not a valid figure")
            answer = False

        if value[0] == 'b':
            calculate(value[1:], black)

        if value[0] == 'w':
            calculate(value[1:], white)

    all_white = sum(white.values())
    all_black = sum(black.values())

    if all_white == 0 and all_black != 0:
        print("There are 0 white pieces.")
        answer = False

    if all_black == 0 and all_white != 0:
        print("There are 0 black pieces.")
        answer = False

    if white['king'] == 0:
        print("There is no white king on the board.")
        answer = False

    if black['king'] == 0:
        print("There is no white king on the board.")
        answer = False

    wa = restrict_pieces(white, 'white')
    ba = restrict_pieces(black, 'black')

    boolean_list = [wa, ba, answer]

    if False in boolean_list:
        return False
    else:
        return True


print(isValidChessBoard(too_many_figures))
"""
There is no white king on the board.
There cannot be more than 8 white pawns, but there are 10 of them. Please remove 2 of them.
There cannot be more than 1 black king, but there are 2 of them. Please remove 1 of them.
"""
print('----------')
print(isValidChessBoard(wrong_cell_names))
"""
Non-existent cell: ah
Non-existent cell: 6z
"""
print('----------')
print(isValidChessBoard(white_only))
"""
There are 0 black pieces.
There is no white king on the board.
"""
print('----------')
print(isValidChessBoard(long_cell_name))
"""
Non-existent cell: 12e
There is no white king on the board.
False
"""
