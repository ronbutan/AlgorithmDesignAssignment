import sys

rowsTaken = []
colsTaken = []
rowsLeft = []
colsLeft = []
BOARD_SIZE = 14
solution = 0
# lists to track placement of queens on board
ROW_STATE = []
FRONT_DIAG_STATE = []
BACK_DIAG_STATE = []
# number codes for / direction
FORWARD_DIAGONAL_CODE = [[r + c for c in range(BOARD_SIZE)] for r in range(BOARD_SIZE)]
# number codes for \ direction
BACK_DIAGONAL_CODE = [[r - c + (BOARD_SIZE - 1) for c in range(BOARD_SIZE)] for r in range(BOARD_SIZE)]

def isValidPosition(row, col):
    global FORWARD_DIAGONAL_CODE,BACK_DIAGONAL_CODE,FRONT_DIAG_STATE,BACK_DIAG_STATE,ROW_STATE
    if (FRONT_DIAG_STATE[FORWARD_DIAGONAL_CODE[row][col]] or BACK_DIAG_STATE[BACK_DIAGONAL_CODE[row][col]] or ROW_STATE[row]):
        return False
    return True

def solveNQueens(nQueensRemaining, col, rowsLeft, colsLeft):
    global solution,FORWARD_DIAGONAL_CODE,BACK_DIAGONAL_CODE,FRONT_DIAG_STATE,BACK_DIAG_STATE,ROW_STATE
    if col == nQueensRemaining:
        solution = solution + 1
        return
    
    for i in range(nQueensRemaining):
        rnum = rowsLeft[i]
        cnum = colsLeft[col]
        if isValidPosition(rnum,cnum):
            ROW_STATE[rnum] = True
            FRONT_DIAG_STATE[FORWARD_DIAGONAL_CODE[rnum][cnum]] = True
            BACK_DIAG_STATE[BACK_DIAGONAL_CODE[rnum][cnum]] = True
            
            solveNQueens(nQueensRemaining,col + 1,rowsLeft,colsLeft)

            ROW_STATE[rnum] = False
            FRONT_DIAG_STATE[FORWARD_DIAGONAL_CODE[rnum][cnum]] = False
            BACK_DIAG_STATE[BACK_DIAGONAL_CODE[rnum][cnum]] = False

def fourteen_queen(pos):
    global solution, FORWARD_DIAGONAL_CODE,BACK_DIAGONAL_CODE,FRONT_DIAG_STATE,BACK_DIAG_STATE,ROW_STATE
    solution = 0
    nQueensRemaining = BOARD_SIZE - len(pos)
    rowsTaken = [queen[0] - 1 for queen in pos]
    colsTaken = [queen[1] - 1 for queen in pos]
    rowsLeft = [i for i in range(BOARD_SIZE) if i not in rowsTaken]
    colsLeft = [i for i in range(BOARD_SIZE) if i not in colsTaken]
    ROW_STATE = [i in rowsTaken for i in range(BOARD_SIZE)]
    x = (BOARD_SIZE << 1) - 1
    FRONT_DIAG_STATE = [False for _ in range(x)]
    BACK_DIAG_STATE = [False for _ in range(x)]

    for queenOnBoard in pos:
        # get row and column index of queens on board
        r = queenOnBoard[0] - 1
        c = queenOnBoard[1] - 1
        # prefix positions of queens on board
        FRONT_DIAG_STATE[FORWARD_DIAGONAL_CODE[r][c]] = True
        BACK_DIAG_STATE[BACK_DIAGONAL_CODE[r][c]] = True
        ROW_STATE[r] = True
        
    solveNQueens(nQueensRemaining,0,rowsLeft,colsLeft)
    
    return solution

num_case = int(sys.stdin.readline())
for _ in range(num_case):
    s = sys.stdin.readline().split()
    n, pos = len(s) // 2, []
    for i in range(n):
        pos.append((int(s[2*i]), int(s[2*i+1])))
    print(fourteen_queen(pos))