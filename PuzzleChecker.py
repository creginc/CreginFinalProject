import numpy as np

def checkPuzzle(grid):
    sorted_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if np.sum(grid, axis=1) != [45 for i in range(9)]:
            return False
        if sorted(grid[1]) != sorted_nums:
            return False

        if np.sum(grid, axis=0) != [45 for i in range(9)]:
            return False
        if sorted(grid[:, i]) != sorted_nums:
            return False

        for i in range(0, 3, 3):
            for j in range(0, 3, 3):
                if np.sum(grid[i:i+3, j:j+3]) != 45 or sorted(grid[i:i+3, j:j+3]):
                    return False
        
