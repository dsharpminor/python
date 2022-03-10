import random


class Player:

    def __init__(self, name='', symbol='', position=''):
        self.name = name
        self.symbol = symbol
        self.position = position

    # Why I made Game subclass of Player:
    # I could not make these method private - they wouldn't be accessible from the Game class
    # I could make them protected Game wasn't a subclass of player
    # I could leave them as a public methods, but it would be unsafe

    def _move_it(self, b):
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

    def _win(self, b):
        if (b[0][0] == b[0][1] == b[0][2] == self.symbol or
                b[1][0] == b[1][1] == b[1][2] == self.symbol or
                b[2][0] == b[2][1] == b[2][2] == self.symbol or
                b[0][0] == b[1][0] == b[2][0] == self.symbol or
                b[0][1] == b[1][1] == b[2][1] == self.symbol or
                b[0][2] == b[1][2] == b[2][2] == self.symbol or
                b[0][0] == b[1][1] == b[2][2] == self.symbol or
                b[0][2] == b[1][1] == b[2][0] == self.symbol):
            return True
        else:
            return False

    def _remove(self, all_symbols):
        if self.symbol in all_symbols:
            all_symbols.remove(self.symbol)

    def _input_symbol(self):
        self.symbol = input("Choose your symbol: \n")
        if len(self.symbol) != 1:
            print("The symbol length must be 1. Please try again")
            self._input_symbol()
        elif self.symbol == '◻️':
            print("Please choose another symbol. This one is reserved to fill out empty spaces.")
            self._input_symbol()
        else:
            print(f"Player has chosen the following symbol: {self.symbol}")

        self._remove(self.b.possible_symbols)

    def _random_symbol(self, all_symbols):

        self.symbol = random.choice(all_symbols)
        print(f"Computer has chosen the following symbol: {self.symbol}")

    def _ask_for_position(self):
        self.position = input("Which position? ")
        return self.position





