import sys

def sucessor():
    puzzle = str(sys.argv[1])

    emptyPos = puzzle.find('_')
    printLeft(puzzle, emptyPos)
    printDown(puzzle, emptyPos)
    printRight(puzzle, emptyPos)
    printUp(puzzle, emptyPos)


def printRight(puzzle, emptyPos):
    if(emptyPos!=2 and emptyPos!=5 and emptyPos!=8):
        newState = puzzle[:emptyPos] + puzzle[emptyPos+1] + '_' + puzzle[emptyPos+2:]
        print('(direita,“' + newState + '”)')
        
def printLeft(puzzle, emptyPos):
    if(emptyPos!=0 and emptyPos!=3 and emptyPos!=6):
        newState = puzzle[:emptyPos-1] + '_' + puzzle[emptyPos-1] + puzzle[emptyPos+1:]
        print('(esquerda,“' + newState + '”)')

def printUp(puzzle, emptyPos):
    if(emptyPos-3 >= 0):
        newState = puzzle[:emptyPos-3] + '_' + puzzle[emptyPos-2:emptyPos] + puzzle[emptyPos-3] + puzzle[emptyPos+1:]
        print('(acima,“' + newState + '”)')

def printDown(puzzle, emptyPos):
    if(emptyPos+3 <= 8):
        newState = puzzle[:emptyPos] + puzzle[emptyPos+3] + puzzle[emptyPos+1:emptyPos+3] + '_' + puzzle[emptyPos+4:]
        print('(abaixo,“' + newState + '”)')

if __name__ == '__main__':
    sucessor()