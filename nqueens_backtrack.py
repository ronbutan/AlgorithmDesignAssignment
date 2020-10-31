import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time() * 1000
        func(*args, **kwargs)
        end = time.time() * 1000
        print("Time taken by {} is {} ms".format(func.__name__, str(end - start)))
    return wrapper


class NQueensPermutation:
    def __init__(self, N):
        self.diagonals = {}
        self.anti_diagonals = {}
        self.N = N
        self.board = [i for i in range(N)]
        self.number_of_solutions = 0
        self.queensLeft = N
        self.rowsLeft = [i for i in range(N)]
        self.colsLeft = [i for i in range(N)]

    def setBoard(self,pos):
        self.queensLeft = self.N - len(pos)
        for q in pos:
            r = q[0] - 1
            c = q[1] - 1
            self.diagonals[r - c] = 1
            self.anti_diagonals[r + c] = 1
            self.board[r] = c
            self.rowsLeft.remove(r)
            self.colsLeft.remove(c)
        print(self.anti_diagonals)

    def is_cell_safe(self, row, col):
        return not (row-col in self.diagonals or row+col in self.anti_diagonals)

    def place_a_queen(self, r, c):
        self.diagonals[r - c] = 1
        self.anti_diagonals[r + c] = 1

    def undo_placing_a_queen(self, r, c):
        del self.diagonals[r - c]
        del self.anti_diagonals[r + c]

    @timer
    def run(self):
        self.solve(0)
        print(self.get_number_of_solutions())

    def solve(self, row):
        if row == self.queensLeft:
            self.number_of_solutions += 1
            return
        # if row == self.N:
        #     self.number_of_solutions += 1
        #     return
        board = self.board
        n = self.N
        for i in range(row, self.queensLeft):
            one = self.rowsLeft[i]
            two = self.rowsLeft[row]
            board[one], board[two] = board[two], board[one]
            #print('i=',i,'row=',row,board)
            if self.is_cell_safe(two, board[two]):
                self.place_a_queen(two, board[two])
                self.solve(row + 1)
                self.undo_placing_a_queen(two, board[two])
        # for i in range(row, self.N):
        #     board[i], board[row] = board[row], board[i]
        #     #print('i=',i,'row=',row,board)
        #     if self.is_cell_safe(row, board[row]):
        #         self.place_a_queen(row, board[row])
        #         self.solve(row + 1)
        #         self.undo_placing_a_queen(row, board[row])

        # x = board[row]
        # for k in range(row + 1, n):
        #     board[k - 1] = board[k]
        # board[n - 1] = x
        x = board[two]
        for k in range(two + 1, n):
            board[k - 1] = board[k]
        board[n - 1] = x

    def get_number_of_solutions(self):
        return self.number_of_solutions

if __name__ == "__main__":
    solver = NQueensPermutation(14)
    solver.setBoard([(1, 1),(2, 9),(3, 6),(4, 10)])
    solver.run()