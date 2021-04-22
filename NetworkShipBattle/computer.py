from random import choice, randint
from game import Game


class Computer:
    def __init__(self, board_size):
        self.board_size = board_size
        self.computer_board = []
        self.ship_list = [5, 4, 3, 3, 2, 1]
        self.aircraft_carrier = 5
        self.cruiser = 4
        self.destroyer = 3  # *2
        self.torpedo_boat = 2
        self.submarine = 1

    def terminal_board_creation(self):
        # while True:
        for x in range(self.board_size):
            self.computer_board.append(["O"]*self.board_size)
        for x in self.computer_board:
            print("  "+"- "*self.board_size)
            print("| "+" ".join(x)+" |")
        print("  "+"- "*self.board_size)

    def getter_game_board(self):
        self.game_board = Game.getter_game_board()
        return self.game_board

    def getter_size_board(self):
        self.board_size = Game.getter_size_board()
        return self.board_size

    def display_computer_board(self):
        for x in self.computer_board:
            print("  "+"- "*self.board_size)
            print("| "+" ".join(x)+" |")
        print("  "+"- "*self.board_size)

    def computer_fire_choice(self):
        shot_ship_row = randint(0, len(self.computer_board) - 1)
        shot_ship_col = randint(0, len(self.computer_board[0]) - 1)
        self.computer_board[shot_ship_row][shot_ship_col] = "X"

    def choose_random_ships_positions(self):
        counter = -1
        letter_list = ["A", "C", "D", "T", "S"]
        # while list of ships is not over
        while counter < len(self.ship_list)-1:
            i = 0
            y = 0
            counter += 1
            if self.ship_list[counter] == 5:
                letter = "A"
            if self.ship_list[counter] == 4:
                letter = "C"
            if self.ship_list[counter] == 3:
                letter = "D"
            if self.ship_list[counter] == 2:
                letter = "T"
            if self.ship_list[counter] == 1:
                letter = "S"
            ship_row = randint(0, len(self.computer_board))
            ship_col = randint(0, len(self.computer_board[0]))
            choice_position = choice(["width", "height"])
            while i < self.ship_list[counter]:
                i += 1
                if choice_position == "width":
                    if self.computer_board[ship_row][ship_col+i]:
                        if self.computer_board[ship_row][ship_col] in letter_list:
                            i -= 1
                            continue
                        self.computer_board[ship_row][ship_col] == letter
                        if self.computer_board[ship_row][ship_col] in letter_list:
                            y += 1
                            self.computer_board[ship_row][ship_col-y] = letter

                        self.computer_board[ship_row][ship_col+i] = letter
                        self.display_computer_board()
                    else:
                        y += 1
                        self.computer_board[ship_row][ship_col-y]
                if choice_position == "height":
                    if self.computer_board[ship_row+i][ship_col]:
                        if self.computer_board[ship_row][ship_col] in letter_list:
                            i -= 1
                            continue
                        self.computer_board[ship_row][ship_col] == letter
                        if self.computer_board[ship_row][ship_col] in letter_list:
                            y += 1
                            self.computer_board[ship_row-y][ship_col] = letter

                        self.computer_board[ship_row+i][ship_col] = letter
                        self.display_computer_board()
                    else:
                        y += 1
                        self.computer_board[ship_row-y][ship_col]


#g = Game(10)
# g.terminal_board_creation()
c = Computer(10)
c.terminal_board_creation()
# c.computer_fire_choice()
c.choose_random_ships_positions()
c.display_computer_board()
