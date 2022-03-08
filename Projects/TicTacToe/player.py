from board import Board


class Player:

    def __init__(self, name='', symbol='', position=''):
        self.name = name
        self.symbol = symbol
        self.position = position
        b = Board()

        # print(self.b)

    def test(self):
        print(self.name)

    def move_it(self, b):
        # print(*b)

        if self.position == '1':
            b[0][0] = self.symbol
        if self.position == '2':
            b[0][1] = self.symbol
        if self.position == '3':
            b[0][2] = self.symbol
        if self.position == '4':
            b[1][0] = self.symbol
        if self.position == '5':
            b[1][1] = self.symbol
        if self.position == '6':
            b[1][2] = self.symbol
        if self.position == '7':
            b[2][0] = self.symbol
        if self.position == '8':
            b[2][1] = self.symbol
        if self.position == '9':
            b[2][2] = self.symbol

        # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in b.field]))

    # def win(self):
    #     if (self.b.field[0][0] == self.b.field[0][1] == self.b.field[0][2] == self.symbol or
    #             self.b.field[1][0] == self.b.field[1][1] == self.b.field[1][2] == self.symbol or
    #             self.b.field[2][0] == self.b.field[2][1] == self.b.field[2][2] == self.symbol or
    #             self.b.field[0][0] == self.b.field[1][0] == self.b.field[2][0] == self.symbol or
    #             self.b.field[0][1] == self.b.field[1][1] == self.b.field[2][1] == self.symbol or
    #             self.b.field[0][2] == self.b.field[1][2] == self.b.field[2][2] == self.symbol or
    #             self.b.field[0][0] == self.b.field[1][1] == self.b.field[2][2] == self.symbol or
    #             self.b.field[0][2] == self.b.field[1][1] == self.b.field[2][0] == self.symbol):
    #         print("Player 1 won. I love you Prohor")

            # return True
