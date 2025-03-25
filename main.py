import player
from game import TICTACTOA
user=player.Userplayer('x')
user.letter='x'
comp=player.Randomcomputerplayer('o')
comp.letter='o'
game=TICTACTOA()
def play(user, comp, game):

    while game.len_avai_moves() > 0:
        comp.get_move(game)
        print('\n')
        game.print_board()
        if game.check_win(comp.letter):
            print(f"com is winner  with letter   {comp.letter}")
            break

        if game.len_avai_moves() == 0:
            break

        user.get_move(game)
        print('\n')
        game.print_board()
        if game.check_win(user.letter):
            print(f"user is winner  with letter {user.letter}")
            break
        if game.len_avai_moves() == 0:
            break
    if len(game.available_moves())==0 :
        print('it a tie')


play(user, comp, game)



