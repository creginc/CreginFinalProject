import pygame
from SudokuGrid import _SudokuGrid


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
        # creates a 1000x500 pixel screen
        screen = pygame.display.set_mode([1000, 500])
        r = 0
        c = 0
        check = False

        # runs another application to display the board that continues to run until the user
        # exits the application
        running = True
        while running:
            val = 0
            # sets the screen background to white
            screen.fill((255, 255, 255))
            # draws the outline of the board with 81 individual squares to the screen
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, 500, 500), 8)
            for i in range(500 // 3, 500 * 2 // 3, 500 // 3):
                pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 500), 8)
                pygame.draw.line(screen, (0, 0, 0), (0, i), (500, i), 8)
            for i in range(500 // 9, 500 * 8 // 9, 500 // 9):
                pygame.draw.line(screen, (0, 0, 0), (0, i), (500, i), 5)
                pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 500), 5)
            pygame.draw.rect(screen, (225, 0, 0), (c * 500 // 9, r * 500 // 9, 500 // 9, 500 // 9), 8)
            text = self.font.render(f'SUDOKU\nRules:\n 1. Each row and column must have numbers 1 through 9, '
                                    f'without repetition.\n2. Each 3x3 square must have numbers 1 through 9, '
                                    f'without repetition.\n\nUse the ')
            # iterates over the Sudoku grid and displays the numbers of the filled spots
            # to their respective spot on the board in black Times New Roman font
            if check:
                for i in range(9):
                    for j in range(9):
                        if g.grid[i][j] == g.solution[i][j]:
                            colors = (0, 0, 0)
                        else:
                            colors = (225, 0, 0)
                        if g.grid[i][j] != 0:
                            num_txt = self.font.render(str(g.grid[i][j]), 1, colors)
                            screen.blit(num_txt, (j * 56 + 10, i * 56 + 5))

            else:
                for i in range(9):
                    for j in range(9):
                        if g.grid[i][j] != 0:
                            if (i, j) in g.original_filled:
                                num_txt = self.font.render(str(g.grid[i][j]), 1, (0, 0, 0))
                                screen.blit(num_txt, (j * 56 + 10, i * 56 + 5))
                            else:
                                num_txt = self.font.render(str(g.grid[i][j]), 1, (0, 0, 225))
                                screen.blit(num_txt, (j * 56 + 10, i * 56 + 5))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if c > 0:
                            c -= 1
                        elif c == 0 and r > 0:
                            r -= 1
                            c = 8
                        else:
                            r = 8
                            c = 8
                    if event.key == pygame.K_RIGHT:
                        if c < 8:
                            c += 1
                        elif c == 8 and r < 8:
                            c = 0
                            r += 1
                        else:
                            r = 0
                            c = 0
                    if event.key == pygame.K_UP:
                        if r > 0:
                            r -= 1
                        else:
                            r = 8
                    if event.key == pygame.K_DOWN:
                        if r < 8:
                            r += 1
                        else:
                            r = 0
                    if event.key == pygame.K_1:
                        val = 1
                    if event.key == pygame.K_2:
                        val = 2
                    if event.key == pygame.K_3:
                        val = 3
                    if event.key == pygame.K_4:
                        val = 4
                    if event.key == pygame.K_5:
                        val = 5
                    if event.key == pygame.K_6:
                        val = 6
                    if event.key == pygame.K_7:
                        val = 7
                    if event.key == pygame.K_8:
                        val = 8
                    if event.key == pygame.K_9:
                        val = 9
                    if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                        g.delete_num(r, c, val)
                    if event.key == pygame.K_c:
                        check = True
                g.insert_num(r, c, val)
            pygame.display.flip()

        # ends the application after the loop stops running when the user presses the exit button
        pygame.quit()
