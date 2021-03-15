import random
import sys
sys.path.append('..')
from common import board


def make_move(the_board, color):
    """
    Returns a random move from the list of possible ones
    :return: (int, int)
    """
    legal_moves = the_board.legal_moves(color)

    new_move = random.choice(legal_moves) if len(legal_moves) > 0 else (-1, -1)

    print(new_move)

    new_table = the_board.process_move(new_move, color)
    
    print(new_table)

    f = open('../playerMinMax/tabuleiro.txt', 'w')
    f.write(str(new_table))
    f.close()

    return new_move[:2]


if __name__ == '__main__':
    b = board.from_file(sys.argv[1])
    f = open('move.txt', 'w')
    f.write('%d,%d' % make_move(b, sys.argv[2]))
    f.close()
