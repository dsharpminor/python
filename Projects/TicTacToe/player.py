from board import Board


class Player(Board):

    def __init__(self, name='', symbol='', position=''):
        self.name = name
        self.symbol = symbol
        self.position = position
