# board = [[7,8,6,1,2,3,9,4,5],
#          [5,2,9,4,7,8,1,3,6],
#          [4,3,1,6,5,9,7,8,2],
#          [2,1,7,3,9,4,6,5,8],
#          [3,5,8,7,1,6,4,2,9],
#          [6,9,4,5,8,2,3,1,7],
#          [8,6,2,9,3,1,5,7,4],
#          [9,7,3,8,4,5,2,6,1],
#          [1,4,5,2,6,7,8,9,3]]
board = [[0,0,0,0,0,4,5,3,0],
         [7,4,0,0,0,3,0,0,0],
         [0,6,3,0,0,0,4,0,8],
         [0,0,2,0,0,0,7,6,5],
         [0,3,0,0,1,0,9,4,0],
         [0,0,0,0,2,7,0,8,0],
         [1,8,4,7,0,0,0,2,3],
         [0,7,5,1,3,2,0,0,0],
         [0,0,0,4,0,0,1,0,0]]
# board = [[0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0]]
#PUZZLE 105
# board = [[9,0,0,0,0,4,0,5,7],
#          [0,3,4,5,0,0,6,0,0],
#          [0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,5,0,0,6,8],
#          [0,0,0,0,3,2,1,0,0],
#          [6,0,0,0,9,8,0,0,0],
#          [8,0,1,0,0,0,0,0,4],
#          [0,0,5,0,8,0,0,0,0],
#          [0,0,7,0,0,0,0,0,9]]
#PUZZLE 62
# board = [[0,2,0,0,0,0,7,6,5],
#          [3,1,0,0,0,0,0,0,0],
#          [0,0,7,0,2,0,0,0,8],
#          [0,0,0,0,0,1,3,0,9],
#          [0,3,0,2,5,0,0,0,0],
#          [0,0,0,0,0,8,0,2,0],
#          [0,8,0,0,0,0,0,0,4],
#          [2,5,0,1,0,0,8,0,7],
#          [0,7,0,0,8,9,0,0,0]]
# board = [[7,0,6,1,2,3,0,0,0],
#          [5,2,9,4,7,8,0,0,0],
#          [4,3,1,6,5,9,0,0,0],
#          [2,1,7,3,9,4,6,5,8],
#          [3,5,8,7,1,6,4,2,9],
#          [6,9,4,5,8,2,3,1,7],
#          [8,6,2,9,3,1,5,7,4],
#          [9,7,3,8,4,5,2,6,1],
#          [1,4,5,2,6,7,8,9,3]]

def printBoard(board):
    for i in board:
        print(i)

def checkAccuracy(board) -> bool:
    # check rows
    for i in board:
        temp = set()
        for j in i:
            if type(j) != type(set()) and j != 0:
                if j in temp:
                    return False
                else:
                    temp.add(j)
    
    #check columns
    for i in range(9):
        temp = set()
        for j in range(9):
            if type(board[j][i]) != type(set()) and board[j][i] != 0:
                if board[j][i] in temp:
                    return False
                else:
                    temp.add(board[j][i])
    
    #check squares
    for i in range(3):
        for j in range(3):
            #inside a square
            temp = set()
            for k in range(3):
                for l in range(3):
                    square = board[(i*3)+k][(j*3)+l]
                    if type(square) != type(set()) and square != 0:
                        if square in temp:
                            return False
                        else:
                            temp.add(square)
    return True
            
def fillIndex(board, row: int, column: int, value: int):
    #fill
    board[row][column] = value

    #remove from row
    for i in range(9):
        if type(board[row][i]) == type(set()) and value in board[row][i]:
            board[row][i].remove(value)

    #remove from column
    for i in range(9):
        if type(board[i][column]) == type(set()) and value in board[i][column]:
            board[i][column].remove(value)

    #remove from square
    startcol = 0
    startrow = 0
    if column > 5:
        startcol = 6
    elif column > 2:
        startcol = 3
    if row > 5:
        startrow = 6
    elif row > 2:
        startrow = 3
    
    for i in range(startrow, startrow+3):
        for j in range(startcol, startcol+3):
            if type(board[i][j]) == type(set()) and value in board[i][j]:
                board[i][j].remove(value)
        





    return True
                
def fillPossibilities(board):
    #create sets of possibilites
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                #create set
                board[i][j] = set()
                #add all numbers
                for k in range(1,10):
                    board[i][j].add(k)
    
    #remove possibilites
    for i in range(9):
        for j in range(9):
            if type(board[i][j]) != type(set()):
                fillIndex(board, i, j, board[i][j])

def checkForOnlyOnePossibilityInIndex(board, row: int, column: int) -> bool:
    assert(type(board[row][column]) == type(set()))
    if len(board[row][column]) == 1:
        fillIndex(board, row, column, list(board[row][column])[0])
        return True
    return False

def checkRow(board, row: int, column: int) -> bool:
    
    for i in board[row][column]:
        found = False
        for j in range(9):
            if type(board[row][j]) == type(set()) and i in board[row][j] and j != column:
                found = True
                break
        if not found:
            fillIndex(board, row, column, i)
            return True
    return False

def checkColumn(board, row: int, column: int) -> bool:
    
    for i in board[row][column]:
        found = False
        for j in range(9):
            if type(board[j][column]) == type(set()) and i in board[j][column] and j != row:
                found = True
                break
        
        if not found:
            fillIndex(board, row, column, i)
            return True
    
    return False



def Solved(board) -> int:
    current = 0
    for i in range(9):
        for j in range(9):
            if type(board[i][j]) != type(set()):
                current += 1
    return current



fillPossibilities(board)
printBoard(board)
print("solved: ", Solved(board))

#main loop
for k in range(100):

    for i in range(9):
        for j in range(9):
            if type(board[i][j]) == type(set()):
                if checkForOnlyOnePossibilityInIndex(board, i, j): pass
                elif checkRow(board, i, j): pass
                elif checkColumn(board, i, j): pass
                
    
print("")
printBoard(board)
print("solved: ", Solved(board))
print(checkAccuracy(board))
