from common import board
import copy

MAX, MIN = [(0,0,1000),1000], [(0,0,-1000), -1000]
MAX_LEVEL = 5


def minScore(move, minMove):
    if move[1] < minMove[1]:
        return move
    else:
        return minMove

def maxScore(move, maxMove):
    if move[1] > maxMove[1]:
        return move
    else:
        return maxMove  

def evaluateScore(actualMove):
    finalScore = actualMove[2]
    if actualMove[0] == 0 or actualMove[0] == 7:
        finalScore += 1
    if actualMove[1] == 0 or actualMove[1] == 7:
        finalScore += 1
    if (actualMove[0] == 1 and actualMove[1] != 7 and actualMove[1] != 0) or (actualMove[0] == 6 and actualMove[1] != 7 and actualMove[1] != 0):
        finalScore -= 1
    if (actualMove[1] == 1 and actualMove[0] != 7 and actualMove[0] != 0) or (actualMove[1] == 6 and actualMove[0] != 7 and actualMove[0] != 0):
        finalScore -= 1

    return (finalScore)

def getNewMoveRecursive(the_board, player, level, actualColor, alpha, beta, initialMove, lastScore):
    legalMoves = the_board.legal_moves(actualColor)
    #print("player",actualColor,"alpha",alpha,"beta",beta,"deep", level, "legalMoves:",legalMoves)
    pieceCount10 = the_board.piece_count['.'] // 10
    MAX_LEVEL =  pieceCount10 if pieceCount10 > 3 else 3

    if level >= MAX_LEVEL or not legalMoves:        #se atingiu o limite de profundidade ou o jogo acabou
        return [initialMove, lastScore]             #retorna a jogada inicial que levou a esse futuro e a pontuação atual

    best = MIN if player == actualColor else MAX    #inicializa o score com minimo ou max dependendo se o jogador atual é o que iniciou a predição

    for move in legalMoves: 
        if level == 0:                              #se profundidade for 0 inicializa a jogada inicial deste stack para cada jogada na profundidade 0
            initialMove = move

        newBoard = copy.deepcopy(the_board)         #cria um novo board
        newBoard.process_move(move, actualColor)    #altera o board com a jogada atual

        val = getNewMoveRecursive(newBoard, player,  level+1, newBoard.opponent(actualColor), alpha, beta, initialMove, move[2])    #recursão
        val = [val[0],evaluateScore(move)]
        if player == actualColor:                   #decide se o jogador atual é min ou max
            best = maxScore(best, val)              
            alpha = maxScore(alpha, best) 

            if beta[1] <= alpha[1]:                 #poda alpha beta
                break
        
        else:
            best = minScore(best, val) 
            beta = minScore(beta, best) 

            if beta[1] <= alpha[1]:                 #poda alpha beta
                break
        
        #print(best)
    return best 
    
def getNewMove(the_board, color):
    bestMove = getNewMoveRecursive(the_board, color,  0, color, MIN, MAX, [(0,0,0), 0], (0,0,0))

    #print("best move:", bestMove) 

    return bestMove[0]