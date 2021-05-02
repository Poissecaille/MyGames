from random import randint
from computer import Computer
from network import Network_connection


class Game:
    def __init__(self, board_size):
        self.running = True
        self.game_board = []
        self.board_size = board_size
        self.ship_list = [5, 4, 3, 3, 2, 1]
        self.aircraft_carrier = 5
        self.cruiser = 4
        self.destroyer = 3  # *2
        self.torpedo_boat = 2
        self.submarine = 1

    def getter_game_board(self):
        return self.game_board

    def getter_size_board(self):
        return self.board_size

    def player_fire_choice(self):
        print("REALOADED! PREPARE TO FIRE!")
        row_shot = input("choose a row: ")
        col_shot = input("choose a col: ")
        self.game_board[row_shot][col_shot] = "X"

    def player_choose_ship_positions(self):
        counter = -1
        ship_list = [5, 4, 3, 3, 2, 1]
        letter_list = ["A", "C", "D", "D", "T", "S"]
        ships_name = ["aircraft_carrier", "cruiser",
                      "destroyer", "destroyer", "torpedo_boat", "submarine"]
        while counter < len(self.ship_list)-1:
            i=0
            # if self.ship_list[counter] == 5:
            #     letter = "A"
            # if self.ship_list[counter] == 4:
            #     letter = "C"
            # if self.ship_list[counter] == 3:
            #     letter = "D"
            # if self.ship_list[counter] == 2:
            #     letter = "T"
            # if self.ship_list[counter] == 1:
            #     letter = "S"
            print(f"COMMANDER DEFINE POSITION OF YOUR {ships_name[counter]}")
            while i<ship_list[counter]:
                try:
                    i+=1
                    ship_row = input("position your ship on row: ")
                    ship_col = input("position yout ship on col: ")
                    self.game_board[ship_row][ship_col]=letter_list[counter]
                except IndexError:
                    i-=1
                    self.display_computer_board()
                    print("ERROR choose a valide position!")
                    continue

    def terminal_board_creation(self):
        # while True:
        for x in range(self.board_size):
            self.game_board.append(["O"]*self.board_size)
        for x in self.game_board:
            print("  "+"- "*self.board_size)
            print("| "+" ".join(x)+" |")
        print("  "+"- "*self.board_size)

    def display_board(self):
        for x in self.game_board:
            print("  "+"- "*self.board_size)
            print("| "+" ".join(x)+" |")
        print("  "+"- "*self.board_size)

    def read_position_and_save_it(self, data: str):
        return tuple(map(str, data.split(",")))

    def main(self):
        n = Network()
        starting_position = n.get_boat_positions()
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
