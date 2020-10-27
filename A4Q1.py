import sys
import time

rowsTaken = []
colsTaken = []
rowsLeft = []
colsLeft = []
BOARD_SIZE = 14
solution = 0
ROW_STATE = []
# /
FORWARD_DIAGONAL_CODE = [[0 for c in range(BOARD_SIZE)] for r in range(BOARD_SIZE)]
# \
BACK_DIAGONAL_CODE = [[0 for c in range(BOARD_SIZE)] for r in range(BOARD_SIZE)]
for rr in range(BOARD_SIZE):
    for cc in range(BOARD_SIZE):
        FORWARD_DIAGONAL_CODE[rr][cc] = rr + cc
        BACK_DIAGONAL_CODE[rr][cc] = rr - cc + 13

# for i in BACK_DIAGONAL_CODE:
#     print(i)
# for i in FORWARD_DIAGONAL_CODE:
#     print(i)

FRONT_DIAG_STATE = []
BACK_DIAG_STATE = []

def isValidPosition(row, col):
    global FORWARD_DIAGONAL_CODE,BACK_DIAGONAL_CODE,FRONT_DIAG_STATE,BACK_DIAG_STATE,ROW_STATE
    if (FRONT_DIAG_STATE[FORWARD_DIAGONAL_CODE[row][col]] or BACK_DIAG_STATE[BACK_DIAGONAL_CODE[row][col]] or ROW_STATE[row]):
        return False
    return True

def solveNQueens(nQueensRemaining, col, rowsLeft, colsLeft):
    global solution,FORWARD_DIAGONAL_CODE,BACK_DIAGONAL_CODE,FRONT_DIAG_STATE,BACK_DIAG_STATE,ROW_STATE
    if col >= nQueensRemaining:
        solution = solution + 1
        return
    
    for i in range(nQueensRemaining):
        rnum = rowsLeft[i]
        cnum = colsLeft[col]
        
        if isValidPosition(rnum,cnum):
            ROW_STATE[rnum] = True
            FRONT_DIAG_STATE[FORWARD_DIAGONAL_CODE[rnum][cnum]] = True
            BACK_DIAG_STATE[BACK_DIAGONAL_CODE[rnum][cnum]] = True

            solveNQueens(nQueensRemaining,col+1,rowsLeft,colsLeft)

            ROW_STATE[rnum] = False
            FRONT_DIAG_STATE[FORWARD_DIAGONAL_CODE[rnum][cnum]] = False
            BACK_DIAG_STATE[BACK_DIAGONAL_CODE[rnum][cnum]] = False


def fourteen_queen(pos):
    global solution, FORWARD_DIAGONAL_CODE,BACK_DIAGONAL_CODE,FRONT_DIAG_STATE,BACK_DIAG_STATE,ROW_STATE
    solution = 0
    nQueensRemaining = BOARD_SIZE - len(pos)
    rowsTaken = [queen[0]-1 for queen in pos]
    colsTaken = [queen[1]-1 for queen in pos]
    rowsLeft = [i for i in range(BOARD_SIZE) if i not in rowsTaken]
    colsLeft = [i for i in range(BOARD_SIZE) if i not in colsTaken]
    ROW_STATE = [i in rowsTaken for i in range(BOARD_SIZE)]
    x = (BOARD_SIZE << 1) - 1
    FRONT_DIAG_STATE = [False for _ in range(x)]
    BACK_DIAG_STATE = [False for _ in range(x)]

    for q in pos:
        r = q[0] - 1
        c = q[1] - 1
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
    start_time = time.time()
    print(fourteen_queen(pos))
    print("--- %s seconds ---" % (time.time() - start_time)) 
