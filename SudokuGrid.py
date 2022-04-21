import random
import copy


class _SudokuGrid:
    """generates and solves Sudoku puzzles using a backtracking algorithm"""

    def __init__(self):
        self.counter = 0
        self.grid = [[0] * 9 for x in range(9)]
        self.generate_puzzle()
        self.original = copy.deepcopy(self.grid)

    def generate_puzzle(self):
        """generates a new puzzle and solves it"""
        self.generate_solution()
        self.remove_numbers_from_grid()
        return

    def valid_spot(self, grid, row, col, number):
        # check if in row
        if number in grid[row]:
            return False
        # check if in column
        for i in range(9):
            if grid[i][col] == number:
                return False
        # check if in box
        box_row = row // 3
        box_col = col // 3
        for i in range(box_row * 3, box_row * 3 + 3):
            for j in range(box_col * 3, box_col * 3 + 3):
                if grid[i][j] == number:
                    return False
        return True

    def find_empty(self, grid):
        """return the next empty square coordinates in the grid"""
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return (i, j)
        return

    def solve_puzzle(self, grid):
        """solve the sudoku puzzle with backtracking"""
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            # find next empty cell
            if grid[row][col] == 0:
                for number in range(1, 10):

                    if self.valid_spot(grid, row, col, number):
                        grid[row][col] = number
                        if not self.find_empty(grid):
                            self.counter += 1
                            break
                        else:
                            if self.solve_puzzle(grid):
                                return True
                break
        grid[row][col] = 0
        return False

    def generate_solution(self):
        """generates a full solution with backtracking"""
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            # find next empty cell
            if self.grid[row][col] == 0:
                random.shuffle(number_list)
                for number in number_list:
                    if self.valid_spot(self.grid, row, col, number):
                        self.grid[row][col] = number
                        if not self.find_empty(self.grid):
                            return True
                        else:
                            if self.generate_solution():
                                # if the grid is full
                                return True
                break
        self.grid[row][col] = 0
        return False

    def get_filled_spots(self, grid):
        """returns a shuffled list of non-empty squares in the puzzle"""
        filled_spots = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] != 0:
                    filled_spots.append((i, j))
        random.shuffle(filled_spots)
        return filled_spots

    def remove_numbers_from_grid(self):
        """remove numbers from the grid to create the puzzle"""
        # get all non-empty squares from the grid
        filled_spots = self.get_filled_spots(self.grid)
        filled_count = len(filled_spots)
        rounds = 3
        while rounds > 0 and filled_count >= 17:

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
                rounds -= 1
        return
