import numpy as np

class Board:

    def __init__(self, name='', symbol='', empty_symbol='◻️'):
        self.name = name
        self.symbol = symbol
        self.empty_symbol = empty_symbol
        self.field = np.full((3, 3), empty_symbol)

    def reset_board(self):
        self.field = np.full((3, 3), self.empty_symbol)
