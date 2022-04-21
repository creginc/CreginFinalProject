import random


class _SudokuGrid:

    def __init__(self):
        self.grid = [[0] * 9 for i in range(9)]

    def __str__(self):
        grid_str = ''
        for r in range(9):
            for c in range(9):
                grid_str += str(self.grid[r][c]) + '\t|\t'
            grid_str += '\n'
        return grid_str

    def valid_num(self, num, pos):
        # check if in row
        for i in range(9):
            if self.grid[pos[0]][i] == num and pos[1] != i:
                return False
        # check if in column
        for i in range(9):
            if self.grid[i][pos[1]] == num and pos[0] != i:
                return False
        # check if in box
        box_row = pos[0] // 3
        box_col = pos[1] // 3
        for i in range(box_row*3, box_row*3 + 3):
            for j in range(box_col*3, box_col*3 + 3):
                if self.grid[i][j] == num and pos != (i, j):
                    return False
        return True

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return None

    def solve_puzzle(self):
        if self.find_empty() is None:
            return True
        else:
            row, col = self.find_empty()
        for i in range(1, 10):
            if self.valid_num(i, (row, col)):
                self.grid[row][col] = i
                if self.solve_puzzle():
                    return True
                self.grid[row][col] = 0
        return False

    def generate_puzzle(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(3):
            for j in range(3):
                n = random.choice(nums)
                self.grid[i][j] = n
                nums.remove(n)

        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(3, 6):
            for j in range(3, 6):
                n = random.choice(nums)
                self.grid[i][j] = n
                nums.remove(n)

        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(6, 9):
            for j in range(6, 9):
                n = random.choice(nums)
                self.grid[i][j] = n
                nums.remove(n)
        self.solve_puzzle()
