import numpy as np
from player import Player


class Board(Player):

    def __init__(self, name=None, symbol=None, empty_symbol='◻️', possible_symbols=None, left_positions=None,
                 moves_number=0, won=False):

        super().__init__(name, symbol)

        self.name = name
        self.symbol = symbol
        self.empty_symbol = empty_symbol
        self.field = np.full((3, 3), empty_symbol)
        self.possible_symbols = possible_symbols
        self.left_positions = left_positions
        self.moves_number = moves_number
        self.won = won

    def set_board(self):
        self.field = np.full((3, 3), self.empty_symbol)
        self.possible_symbols = ['🌸', '🌻', '🌷', '💻']
        self.left_positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.moves_number = 0
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.field]))

