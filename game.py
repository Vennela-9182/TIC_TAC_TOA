

from player import Player
class TICTACTOA:
    def __init__(self):
        self.board=['_' for i in range(9)]
        self.winner=None
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' +'|'.join(row) + '|')
    @staticmethod
    def print_num_board():
        number_board=[[str(i)  for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|'+'|'.join(row)+'|')

    def available_moves(self):
        return [i for (i,spot) in enumerate(self.board) if spot=='_']

    def len_avai_moves(self):
            return len(self.available_moves())

    def check_win(self,letter):
        possible_com=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for com in possible_com:
            if all(self.board[pos]==letter for pos in com):
                self.winner=letter
                return True
        return False


