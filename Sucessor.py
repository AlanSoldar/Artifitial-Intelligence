import sys

def sucessor():
    puzzle = str(sys.argv[1])
    emptyPos = puzzle.find('_')

    print(getLeft(puzzle, emptyPos), getDown(puzzle, emptyPos), getRight(puzzle, emptyPos), getUp(puzzle, emptyPos))


def getRight(puzzle, emptyPos):
    if(emptyPos!=2 and emptyPos!=5 and emptyPos!=8):
        newState = puzzle[:emptyPos] + puzzle[emptyPos+1] + '_' + puzzle[emptyPos+2:]
        return '(direita,“' + newState + '”)'
    else:
        return ''
        
def getLeft(puzzle, emptyPos):
    if(emptyPos!=0 and emptyPos!=3 and emptyPos!=6):
        newState = puzzle[:emptyPos-1] + '_' + puzzle[emptyPos-1] + puzzle[emptyPos+1:]
        return '(esquerda,“' + newState + '”)'
    else:
        return ''

def getUp(puzzle, emptyPos):
    if(emptyPos-3 >= 0):
        newState = puzzle[:emptyPos-3] + '_' + puzzle[emptyPos-2:emptyPos] + puzzle[emptyPos-3] + puzzle[emptyPos+1:]
        return '(acima,“' + newState + '”)'
    else:
        return ''

def getDown(puzzle, emptyPos):
    if(emptyPos+3 <= 8):
        newState = puzzle[:emptyPos] + puzzle[emptyPos+3] + puzzle[emptyPos+1:emptyPos+3] + '_' + puzzle[emptyPos+4:]
        return '(abaixo,“' + newState + '”)'
    else:
        return ''

if __name__ == '__main__':
    sucessor()