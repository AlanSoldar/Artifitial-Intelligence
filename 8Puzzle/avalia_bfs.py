import sys

DIREITA = 'direita'
ESQUERDA = 'esquerda'
ACIMA = 'acima'
ABAIXO = 'abaixo'
EMPTY_SPACE = '0'
FINAL_STATE = '123456780'

class Node:
    def __init__(self, previous, direction, cost, current):
        self.previous = previous
        self.direction = direction
        self.cost = cost
        self.current = current

    def existInList(self, nodeList):
        if(nodeList.get(int(self.current)) is None):
            return False
        else:
            return True

    def toString(self):
        return '(' + self.direction + ',' + self.current+',' + str(self.cost) + ',' + self.previous + ')'


def bfs():
    inPuzzle = str(sys.argv[1]).replace('_', '0')
    puzzle = Node(inPuzzle, 'start', 0, inPuzzle)
    frontier = []
    expandedList = {}
    while(puzzle.current != FINAL_STATE):
        expandedList[int(puzzle.current)] = puzzle
        frontier = addOnFrontier(frontier, expandedList, expande(puzzle.current, puzzle.cost))
        if not frontier:
            return
        puzzle = frontier.pop(0)
    #print('success',expandedList.__len__())
    traceTree(expandedList, puzzle)


def addOnFrontier(frontier, expandedList, nodeList):
    for node in nodeList:
        if not node in frontier and not node.existInList(expandedList):
            frontier.append(node)
    return frontier


def expande(currentState, currentCost):
    emptyPos = currentState.find(EMPTY_SPACE)

    nodeList = getNodeList(getLeft(currentState, emptyPos, currentCost), getDown(currentState, emptyPos, currentCost), getRight(
        currentState, emptyPos, currentCost), getUp(currentState, emptyPos, currentCost))
    # printFrontier(nodeList)

    return nodeList


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


def traceTree(expandedList, finalNode):
    successPath = []
    currentNode = finalNode
    while currentNode.cost != 0:
        successPath.append(currentNode)
        currentNode = expandedList.get(int(currentNode.previous))

    successPath.append(currentNode)
    successPath.reverse()
    successPath.pop(0)
    for node in successPath:
        print(node.direction, end=' ')

def getRight(puzzle, emptyPos, cost):
    if(emptyPos != 2 and emptyPos != 5 and emptyPos != 8):
        newState = puzzle[:emptyPos] + puzzle[emptyPos+1] + \
            EMPTY_SPACE + puzzle[emptyPos+2:]
        return Node(puzzle, DIREITA, cost+1, newState)
    else:
        return None


def getLeft(puzzle, emptyPos, cost):
    if(emptyPos != 0 and emptyPos != 3 and emptyPos != 6):
        newState = puzzle[:emptyPos-1] + EMPTY_SPACE + \
            puzzle[emptyPos-1] + puzzle[emptyPos+1:]
        return Node(puzzle, ESQUERDA, cost+1, newState)
    else:
        return None


def getUp(puzzle, emptyPos, cost):
    if(emptyPos-3 >= 0):
        newState = puzzle[:emptyPos-3] + EMPTY_SPACE + puzzle[emptyPos -
                                                              2:emptyPos] + puzzle[emptyPos-3] + puzzle[emptyPos+1:]
        return Node(puzzle, ACIMA, cost+1, newState)
    else:
        return None


def getDown(puzzle, emptyPos, cost):
    if(emptyPos+3 <= 8):
        newState = puzzle[:emptyPos] + puzzle[emptyPos+3] + \
            puzzle[emptyPos+1:emptyPos+3] + EMPTY_SPACE + puzzle[emptyPos+4:]
        return Node(puzzle, ABAIXO, cost+1, newState)
    else:
        return None

if __name__ == '__main__':
    bfs()
