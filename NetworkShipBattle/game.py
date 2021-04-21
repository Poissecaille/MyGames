from random import randint
#from computer import Computer

class Game:
    def __init__(self, board_size):
        self.running = True
        self.game_board = []
        self.board_size=board_size

    def getter_game_board(self):
        return self.game_board

    def getter_size_board(self):
        return self.board_size

    def terminal_board_creation(self):
        # while True:
        for x in range(self.board_size):
            self.game_board.append(["O"]*self.board_size)
        for x in self.game_board:
            print("  "+"- "*self.board_size)
            print("| "+" ".join(x)+" |")
        print("  "+"- "*self.board_size)
     
    def display_updated_board(self):
        for x in self.game_board:
            print("  "+"- "*self.board_size)
            print("| "+" ".join(x)+" |")
        print("  "+"- "*self.board_size)
   
        
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
