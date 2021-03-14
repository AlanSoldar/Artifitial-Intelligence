from common import board
import copy

MAX, MIN = [(0,0,1000),1000], [(0,0,-1000), -1000]
MAX_LEVEL = 5

# Returns optimal value for current player 
#(Initially called for root and maximizer) 
def minimax(depth, nodeIndex, maximizingPlayer, 
            values, alpha, beta): 

    # Terminating condition. i.e 
    # leaf node is reached 
    if depth == 3: 
        return values[nodeIndex] 

    if maximizingPlayer: 
    
        best = MIN

        # Recur for left and right children 
        for i in range(0, 2): 
            
            val = minimax(depth + 1, nodeIndex * 2 + i, 
                        False, values, alpha, beta) 
            best = max(best, val) 
            alpha = max(alpha, best) 

            # Alpha Beta Pruning 
            if beta <= alpha: 
                break
        
        return best 
    
    else: 
        best = MAX

        # Recur for left and 
        # right children 
        for i in range(0, 2): 
        
            val = minimax(depth + 1, nodeIndex * 2 + i, 
                            True, values, alpha, beta) 
            best = min(best, val) 
            beta = min(beta, best) 

            # Alpha Beta Pruning 
            if beta <= alpha: 
                break
        
        return best 

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

def getNewMoveRecursive(the_board, player, level, actualColor, alpha, beta, initialMove, lastScore):
    legalMoves = the_board.legal_moves(actualColor)
    #print("player",actualColor,"alpha",alpha,"beta",beta,"deep", level, "legalMoves:",legalMoves)

    if level >= MAX_LEVEL or not legalMoves:        #se atingiu o limite de profundidade ou o jogo acabou
        return [initialMove, lastScore]             #retorna a jogada inicial que levou a esse futuro e a pontuação atual

    best = MIN if player == actualColor else MAX    #inicializa o score com minimo ou max dependendo se o jogador atual é o que iniciou a predição

    for move in legalMoves: 
        if level == 0:                              #se profundidade for 0 inicializa a jogada inicial deste stack para cada jogada na profundidade 0
            initialMove = move

        newBoard = copy.deepcopy(the_board)         #cria um novo board
        newBoard.process_move(move, actualColor)    #altera o board com a jogada atual

        val = getNewMoveRecursive(newBoard, player,  level+1, newBoard.opponent(actualColor), alpha, beta, initialMove, move[2])    #recursão

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

    print("best move:", bestMove) 

    return bestMove[0]