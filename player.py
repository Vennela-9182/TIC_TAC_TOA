import random
import math

class Player:
    def __init__(self,letter):
        self.letter=letter
    def get_move(self,game):
        pass


class Randomcomputerplayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    def get_move(self,game):
        square=random.choice(game.available_moves())
        game.board[square]=self.letter


class Userplayer(Player):
    def __init__(self,letter):

        super().__init__(letter)

    def get_move(self,game):
        valid=False
        while not valid:
            square=input(self.letter + '\'s turn.input move (0-9):')

            try:
                val=int(square)
                if val   not in  game.available_moves():
                    raise ValueError
                game.board[val]=self.letter
                valid=True
            except ValueError:
                print("try another number is not available")
