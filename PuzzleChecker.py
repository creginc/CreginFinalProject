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

        for i in range(3):
            for j in range(3):
                if np.sum(grid[i:i+3, j:j+3]) != 45 or sorted(grid[i:i+3, j:j+3])
        if np.sum(grid[:3, :3]) != 45 or sorted(grid[:3, :3].ravel) != sorted_nums:
            return False
        if np.sum(grid[3:6, :3]) != 45 or sorted(grid[3:6, :3].ravel) != sorted_nums:
            return False
        if np.sum(grid[6:9, :3]) != 45 or sorted(grid[6:9, :3].ravel) != sorted_nums:
            return False

        if np.sum(grid[:3, 3:6]) != 45 or sorted(grid[:3, 3:6].ravel) != sorted_nums:
            return False
        if np.sum(grid[3:6, 3:6]) != 45 or sorted(grid[3:6, 3:6].ravel) != sorted_nums:
            return False
        if np.sum(grid[6:9, 3:6]) != 45 or sorted(grid[6:9, 3:6].ravel) != sorted_nums:
            return False

        if np.sum(grid[:3, 6:9]) != 45 or sorted(grid[:3, 6:9].ravel) != sorted_nums:
            return False
        if np.sum(grid[3:6, 6:9]) != 45 or sorted(grid[3:6, 6:9].ravel) != sorted_nums:
            return False
        if np.sum(grid[6:9, 6:9]) != 45 or sorted(grid[6:9, 6:9].ravel) != sorted_nums:
            return False
