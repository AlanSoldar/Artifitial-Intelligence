from common import board
import copy

MAX, MIN = 1000, -1000

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


def getNewMoveRecursive(the_board, color, level):
    legal_moves = the_board.legal_moves(color)
    finalList = []
    opponentColor = "B" if color == "W" else "W"
    if level > 1:
        return legal_moves
    for move in legal_moves:
        print("move", move, color, level)
        newBoard = the_board.process_move([move[0],move[1],move[2]], color)
        finalList += getNewMoveRecursive(newBoard, opponentColor,  level+1)
    return finalList

def getNewMoveRecursivePrint(the_board, color, level):
    print("oldBoard:")
    print(the_board)
    finalList = []
    print("valid moves:",the_board.legal_moves(color))
    if level > 1:
        return the_board.legal_moves(color)
    for move in the_board.legal_moves(color):
        newBoard = copy.deepcopy(the_board)
        if(move[0] == 2 and move[1] == 0) or (move[0] == 5 and move[1] == 3):
            return finalList
        print("move", move, color, level)
        newBoard.process_move([move[0],move[1],move[2]], color)
        print("newBoard:")
        print(newBoard)
        finalList += getNewMoveRecursivePrint(newBoard, newBoard.opponent(color),  level+1)
    return finalList

def getNewMove(the_board, color):
    print(the_board)
    listOfMoves = getNewMoveRecursivePrint(the_board, color, 0)

    print("list of leafs:", listOfMoves) 

    return (1,2)