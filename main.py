import random

def valid_num(grid, num, pos):
    # check if in row
    for i in range(9):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False
    # check if in column
    for i in range(9):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False
    # check if in box
    box_row = pos[0] // 3
    box_col = pos[1] // 3
    for i in range(box_row*3, box_row*3 + 3):
        for j in range(box_col*3, box_col*3 + 3):
            if grid[i][j] == num and pos != (i, j):
                return False
    return True


def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None


def solve_puzzle(grid):
    if find_empty(grid) is None:
        return True
    else:
        row, col = find_empty(grid)
        for i in range(1, 10):
            if valid_num(grid, i, (row, col)):
                grid[row][col] = i
                if solve_puzzle(grid):
                    return True
                grid[row][col] = 0
    return False


def generate_puzzle(grid):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        random.shuffle(nums)
        for j in range(9):
            for n in nums:
                while not valid_num(grid, n, (i, j)) and grid[i][j] != 0:
                    
                    grid[i][j] = n
                if find_empty(grid) is None:
                    return True
    return False


grid = [[0] * 9 for i in range(9)]
generate_puzzle(grid)
for row in grid:
    print(row)

