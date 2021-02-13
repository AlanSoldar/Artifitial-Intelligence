import sys

def expande():
    puzzle = str(sys.argv[1])
    cost = int(sys.argv[2])
    emptyPos = puzzle.find('_')

    printLeft(puzzle, emptyPos, cost)
    printDown(puzzle, emptyPos, cost)
    printRight(puzzle, emptyPos, cost)
    printUp(puzzle, emptyPos, cost)


def printRight(puzzle, emptyPos, cost):
    if(emptyPos!=2 and emptyPos!=5 and emptyPos!=8):
        newState = puzzle[:emptyPos] + puzzle[emptyPos+1] + '_' + puzzle[emptyPos+2:]
        print('(direita,'+ newState+','+ str(cost+1) +',' + puzzle+ ')')
        
def printLeft(puzzle, emptyPos, cost):
    if(emptyPos!=0 and emptyPos!=3 and emptyPos!=6):
        newState = puzzle[:emptyPos-1] + '_' + puzzle[emptyPos-1] + puzzle[emptyPos+1:]
        print('(esquerda,'+ newState+','+ str(cost+1)+','+ puzzle+ ')')

def printUp(puzzle, emptyPos, cost):
    if(emptyPos-3 >= 0):
        newState = puzzle[:emptyPos-3] + '_' + puzzle[emptyPos-2:emptyPos] + puzzle[emptyPos-3] + puzzle[emptyPos+1:]
        print('(acima,'+ newState+','+ str(cost+1)+','+ puzzle + ')')

def printDown(puzzle, emptyPos, cost):
    if(emptyPos+3 <= 8):
        newState = puzzle[:emptyPos] + puzzle[emptyPos+3] + puzzle[emptyPos+1:emptyPos+3] + '_' + puzzle[emptyPos+4:]
        print('(abaixo,'+ newState+','+ str(cost+1)+','+ puzzle+ ')')

if __name__ == '__main__':
    expande()