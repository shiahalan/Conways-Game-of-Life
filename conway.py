import pygame
import sys

pygame.init()

WIN = WIDTH, HEIGHT = 1000, 1000
ROWS = 200
WINDOW = pygame.display.set_mode((WIN))

def grid():

  def draw(width, cell_height, cell_width, window, rows):
    x, y = 0, 0

    for i in range(rows):
      x += cell_width
      y += cell_height
      pygame.draw.line(window, (100, 100, 100), (x, 0), (x, width))
      pygame.draw.line(window, (100, 100, 100), (0, y), (width, y))

  
  while True:
    draw(WIDTH, HEIGHT/ROWS, WIDTH/ROWS, WINDOW, ROWS)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    
    pygame.display.update()


grid()