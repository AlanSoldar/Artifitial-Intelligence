from common import board
import copy

MAX, MIN = [(0,0,1000),1000], [(0,0,-1000), -1000]
MAX_LEVEL = 3

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

def getNewMoveRecursive(the_board, player, level, actualColor, alpha, beta, initialMove):
    #print("player",actualColor,"alpha",alpha,"beta",beta,"deep", level)

    if player == actualColor: 
        best = MIN

        # Recur for left and right children 
        for move in the_board.legal_moves(actualColor): 
            if level >= MAX_LEVEL:
                return [initialMove, move[2]]
            if level == 0:
                initialMove = move

            newBoard = copy.deepcopy(the_board)
            newBoard.process_move([move[0],move[1],move[2]], actualColor)

            val = getNewMoveRecursive(newBoard, player,  level+1, newBoard.opponent(actualColor), alpha, beta, initialMove)
            best = maxScore(best, val) 
            alpha = maxScore(alpha, best) 

            # Alpha Beta Pruning 
            if beta[1] <= alpha[1]: 
                break
        
        #print(best)
        return best 
    
    else: 
        best = MAX

        # Recur for left and 
        # right children 
        for move in the_board.legal_moves(actualColor): 
            if level >= MAX_LEVEL:
                return [initialMove, move[2]]
            if level == 0:
                initialMove = move

            newBoard = copy.deepcopy(the_board)
            newBoard.process_move([move[0],move[1],move[2]], actualColor)

            val = getNewMoveRecursive(newBoard, player,  level+1, newBoard.opponent(actualColor), alpha, beta, initialMove)
            best = minScore(best, val) 
            beta = minScore(beta, best) 

            # Alpha Beta Pruning 
            if beta[1] <= alpha[1]: 
                break
        
        #print(best)
        return best 

def getNewMove(the_board, color):
    print(the_board.legal_moves(color))
    bestMove = getNewMoveRecursive(the_board, color,  0, color, MIN, MAX, [(0,0,0), 0])

    print("best move:", bestMove) 

    return bestMove[0]