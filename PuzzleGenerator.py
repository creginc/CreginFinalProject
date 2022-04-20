import numpy as np
import random

grid = np.zeros((9, 9))

def generate_puzzle(grid):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for r in range(9):
        for c in range(9):
            if grid[r, c] == 0
                random.shuffle(nums)
                number = nums[0]
                if valid_location(grid, r, c, number):
                    grid[r, c] == number
                else:
                    generate_puzzle(grid)