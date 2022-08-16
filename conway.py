import pygame
import sys

pygame.init()

WIN = WIDTH, HEIGHT = 1000, 1000
ROWS = 200
WINDOW = pygame.display.set_mode((WIN))

def grid():

  def draw(width, cell_height, cell_width, surface, rows):
    x, y = 0, 0

    for i in range(rows):
      x += cell_width
      y += cell_height
      pygame.draw.line(surface, (100, 100, 100), (x, 0), (x, width))
      pygame.draw.line(surface, (100, 100, 100), (0, y), (width, y))

  
  while True:
    draw(WIDTH, HEIGHT/ROWS, WIDTH/ROWS, WINDOW, ROWS)
    draw_cell(WINDOW)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    
    pygame.display.flip()  # Flip changed to update


def draw_cell(surface):
  pygame.draw.rect(surface, (54, 115, 64), (5, 5, 5, 5))

grid()