import random
import numpy as np
from firstplayer import FirstPlayer
from secondplayer import SecondPlayer


class Game:
    player_symbol = ''
    computer_symbol = ''

    possible_symbols = ['🌸', '🌻', '🌷', '💻']
    left_positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    empty_symbol = '◻️'

    moves_number = 0
    board = np.full((3, 3), empty_symbol)

    first = ''
    second = ''

    def __init__(self):
        print("Loading...")
        self.first_player = FirstPlayer()
        self.second_player = SecondPlayer()
        print(self.second_player)

    def start(self):
        self.greeting()
        self.__draw_field()

    def greeting(self):
        print(f"Hello! \nLet us begin the game.")

        fp_name = input("What is your name?\n")
        FirstPlayer.name = fp_name
        print(FirstPlayer.name)

        sp_name = input("What is the name of your opponent?\n")
        SecondPlayer.name = sp_name
        print(SecondPlayer.name)

        self.choose_symbols()

    def choose_symbols(self):
        self.__player_set_symbol()
        self.__computer_set_symbol()

    def __player_set_symbol(self):
        Game.player_symbol = input("Choose your symbol: \n")
        if len(Game.player_symbol) != 1:
            print("The symbol length must be 1. Please try again")
            self.__player_set_symbol()
        elif Game.player_symbol == '◻️':
            print("Please choose another symbol. This one is reserved to fill out empty spaces.")
            self.__player_set_symbol()
        else:
            print(f"Player has chosen the following symbol: {Game.player_symbol}")

    @staticmethod
    def __computer_set_symbol():
        if Game.player_symbol in Game.possible_symbols:
            Game.possible_symbols.remove(Game.player_symbol)

        Game.computer_symbol = random.choice(Game.possible_symbols)

        print(f"Prohor has chosen the following symbol: {Game.computer_symbol}")

        print(f"Empty symbol: {Game.empty_symbol}")

    @staticmethod
    def win_check():
        if (Game.board[0][0] == Game.board[0][1] == Game.board[0][2] == Game.player_symbol or
                Game.board[1][0] == Game.board[1][1] == Game.board[1][2] == Game.player_symbol or
                Game.board[2][0] == Game.board[2][1] == Game.board[2][2] == Game.player_symbol or
                Game.board[0][0] == Game.board[1][0] == Game.board[2][0] == Game.player_symbol or
                Game.board[0][1] == Game.board[1][1] == Game.board[2][1] == Game.player_symbol or
                Game.board[0][2] == Game.board[1][2] == Game.board[2][2] == Game.player_symbol or
                Game.board[0][0] == Game.board[1][1] == Game.board[2][2] == Game.player_symbol or
                Game.board[0][2] == Game.board[1][1] == Game.board[2][0] == Game.player_symbol):
            print("I love you Prohor")

            return True

        elif (Game.board[0][0] == Game.board[0][1] == Game.board[0][2] == Game.computer_symbol or
              Game.board[1][0] == Game.board[1][1] == Game.board[1][2] == Game.computer_symbol or
              Game.board[2][0] == Game.board[2][1] == Game.board[2][2] == Game.computer_symbol or
              Game.board[0][0] == Game.board[1][0] == Game.board[2][0] == Game.computer_symbol or
              Game.board[0][1] == Game.board[1][1] == Game.board[2][1] == Game.computer_symbol or
              Game.board[0][2] == Game.board[1][2] == Game.board[2][2] == Game.computer_symbol or
              Game.board[0][0] == Game.board[1][1] == Game.board[2][2] == Game.computer_symbol or
              Game.board[0][2] == Game.board[1][1] == Game.board[2][0] == Game.computer_symbol):
            print("Computer won")

            return True
        else:
            return False

    def ask_first(self):
        Game.first = input("Which position? ")
        if Game.first in Game.left_positions:
            Game.left_positions.remove(Game.first)
        else:
            print("Invalid input")
            self.ask_first()

    def randomize(self):
        Game.second = random.choice(Game.left_positions)
        Game.left_positions.remove(Game.second)

    def move_first(self):  # Game.first/Game.second, Game.player_symbol/Game.computer_symbol

        if Game.first == '1':
            Game.board[0][0] = Game.player_symbol
        if Game.first == '2':
            Game.board[0][1] = Game.player_symbol
        if Game.first == '3':
            Game.board[0][2] = Game.player_symbol
        if Game.first == '4':
            Game.board[1][0] = Game.player_symbol
        if Game.first == '5':
            Game.board[1][1] = Game.player_symbol
        if Game.first == '6':
            Game.board[1][2] = Game.player_symbol
        if Game.first == '7':
            Game.board[2][0] = Game.player_symbol
        if Game.first == '8':
            Game.board[2][1] = Game.player_symbol
        if Game.first == '9':
            Game.board[2][2] = Game.player_symbol

    def move_second(self):  # Game.first/Game.second, Game.player_symbol/Game.computer_symbol

        if Game.second == '1':
            Game.board[0][0] = Game.computer_symbol
        if Game.second == '2':
            Game.board[0][1] = Game.computer_symbol
        if Game.second == '3':
            Game.board[0][2] = Game.computer_symbol
        if Game.second == '4':
            Game.board[1][0] = Game.computer_symbol
        if Game.second == '5':
            Game.board[1][1] = Game.computer_symbol
        if Game.second == '6':
            Game.board[1][2] = Game.computer_symbol
        if Game.second == '7':
            Game.board[2][0] = Game.computer_symbol
        if Game.second == '8':
            Game.board[2][1] = Game.computer_symbol
        if Game.second == '9':
            Game.board[2][2] = Game.computer_symbol


    def move(self, num, sym):  # Game.first/Game.second, Game.player_symbol/Game.computer_symbol

        if num == '1':
            Game.board[0][0] = sym
        # if Game.second == '2':
        #     Game.board[0][1] = Game.computer_symbol
        # if Game.second == '3':
        #     Game.board[0][2] = Game.computer_symbol
        # if Game.second == '4':
        #     Game.board[1][0] = Game.computer_symbol
        # if Game.second == '5':
        #     Game.board[1][1] = Game.computer_symbol
        # if Game.second == '6':
        #     Game.board[1][2] = Game.computer_symbol
        # if Game.second == '7':
        #     Game.board[2][0] = Game.computer_symbol
        # if Game.second == '8':
        #     Game.board[2][1] = Game.computer_symbol
        # if Game.second == '9':
        #     Game.board[2][2] = Game.computer_symbol

    def __draw_field(self):
        print("---------")
        print(f"Iteration nr. {Game.moves_number}")
        print("---------")

        Game.moves_number += 1
        won = False

        fp = FirstPlayer()
        sp = SecondPlayer()


        if Game.moves_number % 2 != 0:
            self.ask_first()
            self.move_first()

        else:
            self.randomize()
            self.move_second()

        # self.move(first, position)
        print(f"\nProhor's move:")
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in Game.board]))

        won = self.win_check()

        if not won:
            self.__draw_field()