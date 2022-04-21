from SudokuGrid import _SudokuGrid
import pygame


class GameBoard:
    """displays a Sudoku puzzle to the user"""
    def __init__(self):
        """initializes a GameBoard with the Times New Roman font"""
        pygame.font.init()
        self.font = pygame.font.SysFont("timesnewroman", 38)

    def display_board(self):
        """displays the sudoku puzzle to the user in a formatted manner"""
        pygame.init()
        # generates a SudokuGrid object with a solvable puzzle
        g = _SudokuGrid()
        # creates a 500x500 pixel screen
        screen = pygame.display.set_mode([500, 500])

        # runs another application to display the board that continues to run until the user
        # exits the application
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # sets the screen background to white
            screen.fill((255, 255, 255))

            # draws the outline of the board with 81 individual squares to the screen
            pygame.draw.rect(screen, (0, 0, 255), (0, 0, 500, 500), 8)
            for i in range(500 // 3, 500 * 2 // 3, 500 // 3):
                pygame.draw.line(screen, (0, 0, 255), (i, 0), (i, 500), 8)
                pygame.draw.line(screen, (0, 0, 255), (0, i), (500, i), 8)
            for i in range(500 // 9, 500 * 8 // 9, 500 // 9):
                pygame.draw.line(screen, (0, 0, 255), (0, i), (500, i), 5)
                pygame.draw.line(screen, (0, 0, 255), (i, 0), (i, 500), 5)

            # iterates over the Sudoku grid and displays the numbers of the filled spots
            # to their respective spot on the board in black Times New Roman font
            for i in range(9):
                for j in range(9):
                    if g.grid[i][j] != 0:
                        text1 = self.font.render(str(g.grid[i][j]), 1, (0, 0, 0))
                        screen.blit(text1, (i * 56 + 10, j * 56 + 5))
            pygame.display.flip()
        # ends the application after the loop stops running when the user presses the exit button
        pygame.quit()
