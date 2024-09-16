import time
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
# # board = [[0,0,0,1,0,2,0,0,0],
# #          [0,6,0,0,0,0,0,7,0],
# #          [0,0,8,0,0,0,9,0,0],
# #          [4,0,0,0,0,0,0,0,3],
# #          [0,5,0,0,0,7,0,0,0],
# #          [2,0,0,0,8,0,0,0,1],
# #          [0,0,9,0,0,0,8,0,5],
# #          [0,7,0,0,0,0,0,6,0],
# #          [0,0,0,3,0,4,0,0,0]]
board =  [[0,0,0,8,0,1,0,0,0],
          [0,0,0,0,0,0,0,4,3],
          [5,0,0,0,0,0,0,0,0],
          [0,0,0,0,7,0,8,0,0],
          [0,0,0,0,0,0,1,0,0],
          [0,2,0,0,3,0,0,0,0],
          [6,0,0,0,0,0,0,7,5],
          [0,0,3,4,0,0,0,0,0],
          [0,0,0,2,0,0,6,0,0]]
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0: return (i,j)
    return None
def checkAccuracy(board, row: int, col: int, num: int) -> bool:
    #check row
    if num in board[row]: return False
    #check column
    for i in range(9):
        if board[i][col] == num: return False
    #check square
    startrow, startcol = (row // 3) * 3, (col // 3) * 3
    for i in range(startrow, startrow+3): 
        for j in range(startcol, startcol+3):
            if board[i][j] == num: return False
    #none found
    return True
def solveSudoku(board) -> bool:
    empty = find_empty(board)
    #Sudoku is solved
    if empty is None: return True
    #try the 9 numbers
    row, col = empty[0], empty[1]
    for num in range(1,10):
        if checkAccuracy(board, row, col, num):
            board[row][col] = num
            if solveSudoku(board): return True
    #didn't find any
    board[row][col] = 0
    return False
def printBoard(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(board[i][j], end=" ")
        print("")
starttime = time.time()
print("Board:")
printBoard(board)
print("")
if solveSudoku(board):
    printBoard(board)
    duration = time.time() - starttime
    print(f"Sudoku Solver took {duration:.6f} seconds to execute")
else:
    print("UNSOLVABLE :(")