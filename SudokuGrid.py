import random
import copy


class _SudokuGrid:
    """generates and solves Sudoku grid"""

    def __init__(self):
        """initializes the Sudoku Grid object with a solution counter of 0 and 9x9 grid full of zeros"""
        self.counter = 0
        self.grid = [[0] * 9 for x in range(9)]
        self.generate_puzzle()
        self.original_filled = []
        for r in range(9):
            for c in range(9):
                if self.grid[r][c] != 0:
                    self.original_filled.append((r, c))
        solve = copy.deepcopy(self)
        solve.solve_puzzle(solve.grid)
        self.solution = solve.grid

    def generate_puzzle(self):
        """generates a Sudoku puzzle by finding a valid, unique puzzle solution and then removing
        numbers to result in a solvable grid with one solution"""
        self.generate_solution()
        self.solved = self.grid
        self.remove_numbers_from_grid()
        return

    def valid_spot(self, grid, row, col, num):
        """checks that the number being entered in the spot is valid (does not already exist
        in row, column, or 3x3 square
        Parameters: grid(the puzzle grid), row(row index of spot being tested), col(column index
        of spot being tested), num (number being tested at the spot in the grid)"""
        # check if in row
        if num in grid[row]:
            return False
        # check if in column
        for i in range(9):
            if grid[i][col] == num:
                return False
        # check if in 3x3 square
        box_row = row // 3
        box_col = col // 3
        for i in range(box_row * 3, box_row * 3 + 3):
            for j in range(box_col * 3, box_col * 3 + 3):
                if grid[i][j] == num:
                    return False
        return True

    def find_empty(self, grid):
        """searches the grid for the next empty spot and returns the indices of that spot
        Parameter: grid (9x9 grid being searched)"""
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return (i, j)
        return None

    def solve_puzzle(self, grid):
        """solves the Sudoku puzzle
        Parameter: grid (9x9 grid representing the puzzle)"""
        # iterates over every spot in the grid
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            # locates where the next empty spot is
            if grid[row][col] == 0:
                for number in range(1, 10):
                    # determines if number is valid in spot
                    # if so, the number is assigned to that spot
                    if self.valid_spot(grid, row, col, number):
                        grid[row][col] = number
                        # if the grid is full, it has been solved and the solution counter increases by 1
                        if not self.find_empty(grid):
                            self.counter += 1
                            break
                        else:
                            # if the grid is not full, the function calls itself recursively to continue
                            # solving the puzzle
                            if self.solve_puzzle(grid):
                                return True
                break
        return False

    def generate_solution(self):
        """generates a solution to the 9x9 puzzle grid"""
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # iterates over every spot in the grid
        for i in range(0, 81):
            row = i % 9
            col = i // 9
            # locates where the next empty spot is
            if self.grid[row][col] == 0:
                # randomizes the order of the list of values between 1 and 9, inclusive
                random.shuffle(number_list)
                for number in number_list:
                    # determines if number is valid in spot
                    # if so, the number is assigned to that spot
                    if self.valid_spot(self.grid, row, col, number):
                        self.grid[row][col] = number
                        if not self.find_empty(self.grid):
                            # if the grid is full, it has been fully generated and the function returns True
                            return True
                        else:
                            # if the grid is not full, the function recursively calls itself to
                            # finish generating the puzzle
                            if self.generate_solution():
                                return True
                break
        self.grid[row][col] = 0
        return False

    def get_filled_spots(self, grid):
        """searches the puzzle for filled spots and returns a shuffled list of their indices
        Parameter: grid(9x9 grid being searched)"""
        filled_spots = []
        # iterates over entire grid
        for i in range(len(grid)):
            for j in range(len(grid)):
                # if spot is not 0, meaning it's full, its indices are added to the list
                if grid[i][j] != 0:
                    filled_spots.append((i, j))
        # the list of indices is shuffled and then returned
        random.shuffle(filled_spots)
        return filled_spots

    def remove_numbers_from_grid(self):
        """remove numbers from the grid to create the puzzle"""
        # finds all the filled spots in the grid
        filled_spots = self.get_filled_spots(self.grid)
        filled_count = len(filled_spots)
        iteration = 3
        # traverse the grid and at each spot, remove a number, check that the puzzle is still solvable
        # with a unique solution, and then move on to the next spot
        # if not solvable after removing the number, put the number back at its spot and move to the next
        while iteration > 0 and filled_count >= 17:
            row, col = filled_spots.pop()
            filled_count -= 1
            removed_square = self.grid[row][col]
            self.grid[row][col] = 0
            grid_copy = copy.deepcopy(self.grid)
            self.counter = 0
            self.solve_puzzle(grid_copy)
            if self.counter != 1:
                self.grid[row][col] = removed_square
                filled_count += 1
                iteration -= 1
        return

    def insert_num(self, r, c, num):
        if self.grid[r][c] == 0:
            self.grid[r][c] = num

    def delete_num(self, r, c, val):
        if (r, c) not in self.original_filled:
            self.grid[r][c] = 0
