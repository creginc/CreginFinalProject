from SudokuGrid import _SudokuGrid
import pygame


class GameBoard:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont("timesnewroman", 38)

    def display_board(self):
        pygame.init()
        g = _SudokuGrid()
        screen = pygame.display.set_mode([500, 500])

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((255, 255, 255))

            pygame.draw.rect(screen, (0, 0, 255), (0, 0, 500, 500), 8)
            for i in range(500 // 3, 500 * 2 // 3, 500 // 3):
                pygame.draw.line(screen, (0, 0, 255), (i, 0), (i, 500), 8)
                pygame.draw.line(screen, (0, 0, 255), (0, i), (500, i), 8)
            for i in range(500 // 9, 500 * 8 // 9, 500 // 9):
                pygame.draw.line(screen, (0, 0, 255), (0, i), (500, i), 5)
                pygame.draw.line(screen, (0, 0, 255), (i, 0), (i, 500), 5)

            for i in range(9):
                for j in range(9):
                    if g.grid[i][j] != 0:
                        text1 = self.font.render(str(g.grid[i][j]), 1, (0, 0, 0))
                        screen.blit(text1, (i * 56 + 10, j * 56 + 5))
            pygame.display.flip()

        pygame.quit()
