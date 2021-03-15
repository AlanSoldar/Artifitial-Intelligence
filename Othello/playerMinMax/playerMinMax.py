import random
import sys
sys.path.append('..')
from common import board
from common import moveService
from randomplayer import randomplayer


def make_move(the_board, color):
    """
    Returns a random move from the list of possible ones
    :return: (int, int)
    """
    legal_moves = the_board.legal_moves(color)

    newMove = moveService.getNewMove(the_board, color)
    
    new_table = the_board.process_move(newMove, color)

    f = open('tabuleiro.txt', 'w')
    f.write(str(new_table))
    f.close()

    return newMove[:2]


    #return random.choice(legal_moves) if len(legal_moves) > 0 else (-1, -1)

def playAlone(b,color):
    try:
        for i in range(60):
            print(color)
            if color == 'B':
                #randomplayer.make_move(b, color)
                make_move(b, color)
            else:
                #make_move(b, color)
                randomplayer.make_move(b, color)
            color = b.opponent(color)
    except:
        print("fim prematuro")

    print("black score:", b.piece_count['B'])
    print("white score:", b.piece_count['W'])

if __name__ == '__main__':
    b = board.from_file(sys.argv[1])
    color = sys.argv[2]
    color = board.Board.WHITE if color == 'white' else board.Board.BLACK
    bestMove = make_move(b, color)

    f = open('move.txt', 'w')
    f.write('%d,%d' % bestMove)
    f.close()
