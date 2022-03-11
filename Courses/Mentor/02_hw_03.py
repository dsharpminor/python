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

my_dict = {'1h': 'wpawn', '6c': 'wpawn', '2g': 'wpawn', '3g': 'bking', '4g': 'bking',
           '2h': 'wpawn', '7c': 'wpawn',
           '3h': 'wpawn', '8c': 'wpawn',
           '4h': 'wpawn', '9c': 'wpawn'}


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
            print(f"There cannot be more than eight {color} pawns.")
            a = False
        if k == 'rooks' and v > 2:
            print(f"There cannot be more than two {color} rooks.")
            a = False
        if k == 'knights' and v > 2:
            print(f"There cannot be more than two {color} knights.")
            a = False
        if k == 'bishops' and v > 2:
            print(f"There cannot be more than two {color} bishops.")
            a = False
        if k == 'queen' and v > 1:
            print(f"There cannot be more than one {color} queen.")
            a = False
        if k == 'king' and v > 1:
            print(f"There cannot be more than one {color} king.")
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
        if key[0] not in '123456789' or key[1] not in 'abcdefgh':
            print(f"{key} is wrong")
            answer = False

        # check whether the figure names are valid or not
        if value[0] not in 'bw' or value[1:] not in figures:
            print(f"{value[0]} not in b or {value[1:]} is not a valid figure")
            answer = False

        if value[0] == 'b':
            calculate(value[1:], black)

        if value[0] == 'w':
            calculate(value[1:], white)

    wa = restrict_pieces(white, 'white')
    ba = restrict_pieces(black, 'black')

    boolean_list = [wa, ba, answer]

    if False in boolean_list:
        return False
    else:
        return True


print(isValidChessBoard(my_dict))
