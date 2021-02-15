import sys

DIREITA = 'direita'
ESQUERDA = 'esquerda'
ACIMA = 'acima'
ABAIXO = 'abaixo'

class Node:
    def __init__(self, initialState, direction, cost, newState):
        self.initialState = initialState
        self.direction = direction
        self.cost = cost
        self.newState = newState

    


def expande():
    puzzle = str(sys.argv[1])
    cost = int(sys.argv[2])
    emptyPos = puzzle.find('_')

    print(getLeft(puzzle, emptyPos, cost), getDown(puzzle, emptyPos, cost), getRight(puzzle, emptyPos, cost), getUp(puzzle, emptyPos, cost))


def getRight(puzzle, emptyPos, cost):
    if(emptyPos!=2 and emptyPos!=5 and emptyPos!=8):
        newState = puzzle[:emptyPos] + puzzle[emptyPos+1] + '_' + puzzle[emptyPos+2:]
        return '(' + DIREITA + ','+ newState+','+ str(cost+1) +',' + puzzle+ ')'
    else:
        return ''
        
def getLeft(puzzle, emptyPos, cost):
    if(emptyPos!=0 and emptyPos!=3 and emptyPos!=6):
        newState = puzzle[:emptyPos-1] + '_' + puzzle[emptyPos-1] + puzzle[emptyPos+1:]
        return '(' + ESQUERDA + ',' + newState+','+ str(cost+1)+','+ puzzle+ ')'
    else:
        return ''

def geUp(puzzle, emptyPos, cost):
    if(emptyPos-3 >= 0):
        newState = puzzle[:emptyPos-3] + '_' + puzzle[emptyPos-2:emptyPos] + puzzle[emptyPos-3] + puzzle[emptyPos+1:]
        return '(' + ACIMA + ',' + newState+','+ str(cost+1)+','+ puzzle + ')'
    else:
        return ''

def getDown(puzzle, emptyPos, cost):
    if(emptyPos+3 <= 8):
        newState = puzzle[:emptyPos] + puzzle[emptyPos+3] + puzzle[emptyPos+1:emptyPos+3] + '_' + puzzle[emptyPos+4:]
        return '(' + ABAIXO + ',' + newState+','+ str(cost+1)+','+ puzzle+ ')'
    else:
        return ''

if __name__ == '__main__':
    expande()