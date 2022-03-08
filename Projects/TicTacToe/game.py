import random
import numpy as np
from player import Player
from board import Board


class Game:
    player_symbol = ''
    computer_symbol = ''

    possible_symbols = ['🌸', '🌻', '🌷', '💻']
    # possible_symbols = ['🌸', '🌻']

    left_positions = ['1', '2', '3',
                      '4', '5', '6',
                      '7', '8', '9']

    empty_symbol = '◻️'

    moves_number = 0

    def __init__(self):
        # print("Loading...")
        self.first_player = Player()
        self.second_player = Player()
        self.b = Board()

    def start(self):
        self.greeting()
        self.__draw_field()

    def greeting(self):
        # print(f"Hello! \nLet us begin the game.")

        self.choose_symbols()

    def choose_symbols(self):
        self.__set_symbol()
        self.__computer_set_symbol()

    def __set_symbol(self):
        self.first_player.symbol = input("Choose your symbol: \n")
        if len(self.first_player.symbol) != 1:
            print("The symbol length must be 1. Please try again")
            self.__set_symbol()
        elif self.first_player.symbol == '◻️':
            print("Please choose another symbol. This one is reserved to fill out empty spaces.")
            self.__set_symbol()
        else:
            print(f"Player has chosen the following symbol: {self.first_player.symbol}")

        # print(f"HERE: {self.first_player.symbol}")

    def __computer_set_symbol(self):
        if self.first_player.symbol in Game.possible_symbols:
            Game.possible_symbols.remove(self.first_player.symbol)

        self.second_player.symbol = random.choice(Game.possible_symbols)
        # print(*Game.possible_symbols)
        print(f"Prohor has chosen the following symbol: {self.second_player.symbol}")
        # print("Out of:")

    def the_winner(self):
        first_wins = self.first_player.win(self.b.field)
        second_wins = self.second_player.win(self.b.field)
        if first_wins:
            print("Player 1 won. I love you Prohor <3")
            return True
        elif second_wins:
            print("Player 2 won - Prohor <3")
            return True
        else:
            return False


    def ask_first(self):
        self.first_player.position = input("Which position? ")
        if self.first_player.position in Game.left_positions:
            Game.left_positions.remove(self.first_player.position)
        else:
            print("Invalid input")
            self.ask_first()

    def randomize(self):
        self.second_player.position = random.choice(Game.left_positions)
        # print(f"AAA Prohor's pos: {self.second_player.position}")
        # print("Second player")
        Game.left_positions.remove(self.second_player.position)

    def __draw_field(self):

        Game.moves_number += 1
        won = False

        print("---------")
        print(f"Iteration nr. {Game.moves_number}")
        print("---------")

        if Game.moves_number % 2 != 0:
            self.ask_first()
            self.first_player.move_it(self.b.field)

        else:
            self.randomize()
            self.second_player.move_it(self.b.field)

        # won = self.first_player.win()
        won = self.the_winner()

        # self.move(first, position)
        # print(f"\nProhor's move:")
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.b.field]))

        if not won:
            self.__draw_field()
