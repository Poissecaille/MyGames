from random import randint
from computer import Computer
from network import Network_connection


class Game:
    def __init__(self, board_size):
        self.running = True
        self.board_size = board_size
        self.game_board = []
        self.target_board = []
        self.ship_list = [5, 4, 3, 3, 2, 1]
        self.aircraft_carrier = 5
        self.cruiser = 4
        self.destroyer = 3
        self.frigate = 3
        self.torpedo_boat = 2
        self.submarine = 1
        self.letter_list = ["A", "C", "D", "F", "T", "S"]
        self.ships_name = ["aircraft_carrier", "cruiser",
                           "destroyer", "destroyer", "torpedo_boat", "submarine"]

    def getter_game_board(self):
        return self.game_board

    def getter_size_board(self):
        return self.board_size

    def player_fire_choice(self):
        print("REALOADED! PREPARE TO FIRE!")
        row_shot = input("choose a row: ")
        col_shot = input("choose a col: ")
        if self.target_board[row_shot][col_shot] != "X":
            self.target_board[row_shot][col_shot] = "X"
            return self.target_board[row_shot][col_shot]
        print("ERROR choose a correct target!")
        self.player_fire_choice()

    def player_choose_ship_positions(self):
        self.terminal_board_creation()
        counter = -1
        boat_position = ""
        while counter < len(self.ship_list)-1:
            i = 0
            boat_position = ""
            counter += 1
            letter = self.letter_list[counter]
            while i < self.ship_list[counter]:
                try:
                    print(
                        f"COMMANDER DEFINE POSITION OF YOUR {self.ships_name[counter].upper()}")
                    ship_row = int(
                        str(input("position your ship on row: ")[:1]))
                    ship_col = int(
                        str(input("position yout ship on col: ")[:1]))
                    i += 1
                    if self.game_board[ship_row][ship_col] != "O":
                        i -= 1
                        print(
                            "ERROR: stop drinking captain another ship is already here!")
                        continue
                    if boat_position == "height":
                        if self.game_board[ship_row+1][ship_col] != letter:
                            if self.game_board[ship_row-1][ship_col] != letter:
                                print(
                                    "ERROR: you can't put the ship at several positions you drunker!")
                                i -= 1
                                continue
                    if boat_position == "width":
                        if self.game_board[ship_row][ship_col+1] != letter:
                            if self.game_board[ship_row][ship_col-1] != letter:
                                print(
                                    "ERROR: you can't put the ship at several positions you drunker!")
                                i -= 1
                                continue
                    self.game_board[ship_row][ship_col] = letter
                    self.display_board()
                    if i == 2:
                        if self.game_board[ship_row][ship_col-1] or self.game_board[ship_row][ship_col+1] == letter:
                            boat_position = "width"
                        else:
                            boat_position = "height"
                except IndexError:
                    i -= 1
                    print("ERROR: you are out of range captain this is desertion!")
                    continue
                except ValueError:
                    i -= 1
                    continue

    def terminal_board_creation(self):
        for x in range(self.board_size):
            self.game_board.append(["O"]*self.board_size)
        for x in self.game_board:
            print("  "+"- "*self.board_size)
            print("| "+" ".join(x)+" |")
        print("  "+"- "*self.board_size)

    def terminal_target_board_creation(self):
        for x in range(self.board_size):
            self.target_board.append(["O"]*self.board_size)
        for x in self.target_board:
            print("  "+"- "*self.board_size)
            print("| "+" ".join(x)+" |")
        print("  "+"- "*self.board_size)

    def display_board(self):
        for x in self.game_board:
            print("  "+"- "*self.board_size)
            print("| "+" ".join(x)+" |")
        print("  "+"- "*self.board_size)

    def display_target_board(self):
        for x in self.target_board:
            print("  "+"- "*self.board_size)
            print("| "+" ".join(x)+" |")
        print("  "+"- "*self.board_size)

    def read_position_and_save_it(self, data: str):
        return tuple(map(str, data.split(",")))


g = Game(10)
g.player_choose_ship_positions()
# n = Network()
# starting_position = n.get_boat_positions()
# def main_loop(self):
#     while self.running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.running = False
#                 pygame.quit()


# g = Game(10)
# g.terminal_board_creation()
# c = Computer()
# c.computer_fire_choice()
# g.display_updated_board()
