from SudokuGrid import _SudokuGrid
import pygame


pygame.init()
pygame.font.init()
font1 = pygame.font.SysFont("timesnewroman", 38)
g = _SudokuGrid()
screen = pygame.display.set_mode([500, 500])


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

screen.fill((255, 255, 255))

pygame.draw.rect(screen, (0, 0, 255), (0, 0, 500, 500), 8)
pygame.draw.line(screen, (0, 0, 255), (167, 0), (167, 500), 8)
pygame.draw.line(screen, (0, 0, 255), (333, 0), (333, 500), 8)
pygame.draw.line(screen, (0, 0, 255), (0, 167), (500, 167), 8)
pygame.draw.line(screen, (0, 0, 255), (0, 333), (500, 333), 8)
pygame.draw.line(screen, (0, 0, 255), (0, 56), (500, 56), 5)
pygame.draw.line(screen, (0, 0, 255), (0, 111), (500, 111), 5)
pygame.draw.line(screen, (0, 0, 255), (0, 222), (500, 222), 5)
pygame.draw.line(screen, (0, 0, 255), (0, 278), (500, 278), 5)
pygame.draw.line(screen, (0, 0, 255), (0, 389), (500, 389), 5)
pygame.draw.line(screen, (0, 0, 255), (0, 444), (500, 444), 5)
pygame.draw.line(screen, (0, 0, 255), (56, 0), (56, 500), 5)
pygame.draw.line(screen, (0, 0, 255), (111, 0), (111, 500), 5)
pygame.draw.line(screen, (0, 0, 255), (222, 0), (222, 500), 5)
pygame.draw.line(screen, (0, 0, 255), (278, 0), (278, 500), 5)
pygame.draw.line(screen, (0, 0, 255), (389, 0), (389, 500), 5)
pygame.draw.line(screen, (0, 0, 255), (444, 0), (444, 500), 5)

for i in range(9):
    for j in range(9):
        if g.grid[i][j] != 0:
            text1 = font1.render(str(g.grid[i][j]), True, (0, 0, 0))
            screen.blit(text1, (i*56 + 10, j*56 + 5))
        pygame.display.flip()

pygame.quit()
