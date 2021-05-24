from random import choice, randint


class Computer:
    def __init__(self, board_size):
        self.board_size = board_size
        self.computer_board = []
        self.computer_target_board = []
        self.ship_list = [5, 4, 3, 3, 2, 1]
        self.aircraft_carrier = 5
        self.cruiser = 4
        self.destroyer = 3
        self.frigate = 3
        self.torpedo_boat = 2
        self.submarine = 1
        self.letter_list = ["A", "C", "D", "F", "T", "S"]

    def terminal_computer_board_creation(self):
        # while True:
        for x in range(self.board_size):
            self.computer_board.append(["O"]*self.board_size)
        for x in self.computer_board:
            print("  "+"- "*self.board_size)
            print("| "+" ".join(x)+" |")
        print("  "+"- "*self.board_size)

    def computer_target_board_creation(self):
        for x in range(self.board_size):
            self.computer_target_board.append(["O"]*self.board_size)

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

    def display_computer_target__board(self):
        for x in self.computer_target_board:
            print("  "+"- "*self.board_size)
            print("| "+" ".join(x)+" |")
        print("  "+"- "*self.board_size)

    def computer_fire_choice(self):
        shot_ship_row = randint(0, len(self.computer_target_board) - 1)
        shot_ship_col = randint(0, len(self.computer_target_board[0]) - 1)
        if self.computer_target_board[shot_ship_row, shot_ship_col] != "X":
            self.computer_target_board[shot_ship_row][shot_ship_col] = "X"
        self.computer_fire_choice()

    def choose_random_ships_positions(self):
        counter = -1

        # while list of ships is not over
        while counter < len(self.ship_list)-1:
            i = 0
            y = 0
            counter += 1
            letter = self.letter_list[counter]
            ship_row = randint(0, len(self.computer_board)-1)
            ship_col = randint(0, len(self.computer_board[0])-1)
            choice_position = choice(["width", "height"])
            # choice_position="width"
            while i < self.ship_list[counter]:
                # CHECK INDEXERROR AND CLEAN UP THE SHIP
                try:
                    i += 1
                    if choice_position == "width":
                        # CHECK IF LOCATION IS TAKEN BY ANOTHER SHIP
                        if self.computer_board[ship_row][ship_col] != "O":
                            # CHECK IF LOCATION IS ALREADY TAKEN BY THE SHIP
                            if self.computer_board[ship_row][ship_col] == letter:
                                # IF TAKEN BY THE SHIP SEEK WHERE TO EXTEND IT
                                if self.computer_board[ship_row][ship_col+y] == "O":
                                    self.computer_board[ship_row][ship_col+y] = letter
                                    self.display_computer_board()
                                    y += 1
                                    continue
                                if self.computer_board[ship_row][ship_col-y] == "O":
                                    self.computer_board[ship_row][ship_col-y] = letter
                                    self.display_computer_board()
                                    y += 1
                                    continue
                                raise IndexError
                            raise IndexError
                        self.computer_board[ship_row][ship_col] = letter
                        self.display_computer_board()
                        y += 1
                    if choice_position == "height":
                        # CHECK IF LOCATION IS TAKEN BY ANOTHER SHIP
                        if self.computer_board[ship_row][ship_col] != "O":
                            # CHECK IF LOCATION IS ALREADY TAKEN BY THE SHIP
                            if self.computer_board[ship_row][ship_col] == letter:
                                # IF TAKEN BY THE SHIP SEEK WHERE TO EXTEND IT
                                if self.computer_board[ship_row+y][ship_col] == "O":
                                    self.computer_board[ship_row +
                                                        y][ship_col] = letter
                                    self.display_computer_board()
                                    y += 1
                                    continue
                                if self.computer_board[ship_row-y][ship_col] == "O":
                                    self.computer_board[ship_row -
                                                        y][ship_col] = letter
                                    self.display_computer_board()
                                    y += 1
                                    continue
                                raise IndexError
                            raise IndexError
                        self.computer_board[ship_row][ship_col] = letter
                        self.display_computer_board()
                        y += 1
                except IndexError:
                    for nested_list in self.computer_board:
                        for index, e in enumerate(nested_list):
                            if nested_list[index] == letter:
                                nested_list[index] = "O"
                    i = 0
                    y = 0
                    ship_row = randint(0, len(self.computer_board)-1)
                    ship_col = randint(0, len(self.computer_board[0])-1)
                    print("---------------- ERROR ----------------")
                    self.display_computer_board()
                    print("---------------- ERROR ----------------")
                    #counter -= 1
                    continue


#g = Game(10)
# g.terminal_board_creation()
# 
# c.computer_fire_choice()
# 