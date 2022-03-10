import random
from player import Player
from board import Board


class Game(Player):

    def __init__(self):
        super().__init__()
        self.first_player = Player()
        self.second_player = Player()
        self.b = Board()
        self.b.set_board()

    def start(self):
        while True:
            self.__play_a_game()
            print("---------")
            repeat = input("Would you like to play again? ")
            print("---------")
            if 'yes' not in repeat:
                return False

    def __play_a_game(self):
        self.__choose_symbols()
        self.__draw_field()
        self.b.set_board()

    def __choose_symbols(self):
        self.first_player._input_symbol()
        self.second_player._random_symbol(self.b.possible_symbols)

    def __the_winner(self):
        first_wins = self.first_player._win(self.b.field)
        second_wins = self.second_player._win(self.b.field)
        if first_wins:
            print("🎉 Player 1 (human) won! 🎉 ")
            return True
        elif second_wins:
            print("🎉 Player 2 (computer) won! 🎉 ")
            return True
        else:
            return False

    def __ask_first(self):  # for 1st player
        pos = self.first_player._ask_for_position()
        if pos in self.b.left_positions:
            self.b.left_positions.remove(pos)
        else:
            print("Invalid input")
            self.__ask_first()

    def __randomize(self):  # for 2nd player
        self.second_player.position = random.choice(self.b.left_positions)
        self.b.left_positions.remove(self.second_player.position)

    def __iterate_moves(self):

        self.b.moves_number += 1

        print("---------")
        print(f"Iteration nr. {self.b.moves_number}")
        print("---------")

    def __draw_field(self):

        if len(self.b.left_positions) > 0:

            self.__iterate_moves()

            if self.b.moves_number % 2 != 0:
                self.__ask_first()
                self.first_player._move_it(self.b.field)

            else:
                self.__randomize()
                self.second_player._move_it(self.b.field)

            won = self.__the_winner()

            print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.b.field]))

            if not won:
                self.__draw_field()

        else:
            print("It's a draw!")
