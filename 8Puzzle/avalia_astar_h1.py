import sys
from time import time

DIREITA = 'direita'
ESQUERDA = 'esquerda'
ACIMA = 'acima'
ABAIXO = 'abaixo'
EMPTY_SPACE = '0'
FINAL_STATE = '123456780'
t = 0

class Node:
    def __init__(self, initialState, direction, cost, newState):
        self.initialState = initialState
        self.direction = direction
        self.cost = cost
        self.newState = newState

    def existInList(self, nodeList):
        if(nodeList.get(int(self.newState)) is None):
            return False
        else:
            return True

    def toString(self):
        return '(' + self.direction + ','+ self.newState+','+ str(self.cost) +',' + self.initialState + ')'

def avaliaHamming():
    t_start = time()
    max_t_loop = 0
    n_loop = 0
    inPuzzle = str(sys.argv[1]).replace('_', '0')
    puzzle = Node(inPuzzle, 'start', 0, inPuzzle)
    totalCost = 0
    bestScore = 8
    frontier = {int(puzzle.newState):puzzle}
    expandedList = {}
    while(puzzle.newState != FINAL_STATE):
        t_start_loop = time()
    #for i in range(3):
        frontier = addOnFrontier(frontier, expandedList ,expande(puzzle.newState, totalCost))
        if not frontier:
            return
        del frontier[int(puzzle.newState)]
        expandedList[int(puzzle.newState)] = puzzle

        bestState = figureOutBestState(frontier)
        puzzle = bestState
        
        #print('current best state:', puzzle.newState, puzzle.cost, ' frontier len:', len(frontier), ' expanded nodes:', len(expandedList), ' current score:', hammingScore(puzzle))
        
        totalCost = puzzle.cost
        t_end_loop = time()
        n_loop+=1
        if (t_end_loop- t_start_loop > max_t_loop):
            max_t_loop = t_end_loop- t_start_loop
    
    #print('success',expandedList.__len__())
    t_end = time()
    print("while time", max_t_loop)
    print("n loop", n_loop)
    print("avaliaH time", t_end-t_start)
    traceTree(expandedList, puzzle)

def traceTree(expandedList, finalNode):
    successPath = []
    currentNode = finalNode
    while currentNode.cost != 0:
        successPath.append(currentNode)
        currentNode=expandedList.get(int(currentNode.initialState))
    
    successPath.append(currentNode)
    successPath.reverse()
    successPath.pop(0)
    for node in successPath:
        print(node.direction, end=' ')
        

def figureOutBestState(frontier):
    bestScoredNode = list(frontier.values())[0]

    for node in frontier.values():
        if hammingScore(node) + node.cost < hammingScore(bestScoredNode) + bestScoredNode.cost:
            #print(node.toString(), hammingScore(node))
            bestScore = hammingScore(node)
            bestScoredNode = node

    return bestScoredNode



def addOnFrontier(frontier, expandedList, nodeList):
    for node in nodeList:
        if not node.existInList(frontier) and not node.existInList(expandedList):
            frontier[int(node.newState)] = node
    return frontier


def expande(currentState, currentCost):
    emptyPos = currentState.find(EMPTY_SPACE)

    nodeList = getNodeList(getLeft(currentState, emptyPos, currentCost), getDown(currentState, emptyPos, currentCost), getRight(currentState, emptyPos, currentCost), getUp(currentState, emptyPos, currentCost))
    #printFrontier(nodeList)

    return nodeList

def hammingScore(node):
    score = 0
    for i in range(len(node.newState)):
        if node.newState[i] != EMPTY_SPACE and int(node.newState[i])-1!=i:
            score+=1
    return score

def getNodeList(left, down, right, up):
    nodeList = []
    if left is not None:
        nodeList.append(left)
    if down is not None:
        nodeList.append(down)
    if right is not None:
        nodeList.append(right)
    if up is not None:
        nodeList.append(up)
    return nodeList

def printFrontier(nodeList):
    outputString = ''
    for node in nodeList:
        outputString+=node.toString()+' '
    print(outputString)


def getRight(puzzle, emptyPos, cost):
    if(emptyPos!=2 and emptyPos!=5 and emptyPos!=8):
        newState = puzzle[:emptyPos] + puzzle[emptyPos+1] + EMPTY_SPACE + puzzle[emptyPos+2:]
        return Node(puzzle, DIREITA, cost+1, newState)
    else:
        return None
        
def getLeft(puzzle, emptyPos, cost):
    if(emptyPos!=0 and emptyPos!=3 and emptyPos!=6):
        newState = puzzle[:emptyPos-1] + EMPTY_SPACE + puzzle[emptyPos-1] + puzzle[emptyPos+1:]
        return Node(puzzle, ESQUERDA, cost+1, newState)
    else:
        return None

def getUp(puzzle, emptyPos, cost):
    if(emptyPos-3 >= 0):
        newState = puzzle[:emptyPos-3] + EMPTY_SPACE + puzzle[emptyPos-2:emptyPos] + puzzle[emptyPos-3] + puzzle[emptyPos+1:]
        return Node(puzzle, ACIMA, cost+1, newState)
    else:
        return None

def getDown(puzzle, emptyPos, cost):
    if(emptyPos+3 <= 8):
        newState = puzzle[:emptyPos] + puzzle[emptyPos+3] + puzzle[emptyPos+1:emptyPos+3] + EMPTY_SPACE + puzzle[emptyPos+4:]
        return Node(puzzle, ABAIXO, cost+1, newState)
    else:
        return None

if __name__ == '__main__':
    avaliaHamming()