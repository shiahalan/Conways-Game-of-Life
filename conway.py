import pygame
import sys
from random import randint, choice
from copy import deepcopy

pygame.init()
WIN = WIDTH, HEIGHT = 1000, 1000  
ROWS = 200  # 200
CELL_HEIGHT, CELL_WIDTH = WIDTH // ROWS, HEIGHT // ROWS
WINDOW = pygame.display.set_mode((WIN))
CELL_ROWS = HEIGHT // CELL_HEIGHT  # COULD BE WRONG
CELL_COLS = WIDTH // CELL_WIDTH
CLOCK = pygame.time.Clock()
FPS = 8

chances = [1, 0]

def check_cell_neighbors(current_generation, row, col):  # Do not start at 0 for row or col, exclude outer rim of box for life
  neighbor_count = 0
  for i in range(row - 1, row + 2):  # Check one row up, and one down +2 noninclusive
    for j in range(col - 1, col + 2):  # ^^^ same
      if current_generation[i][j]:
        neighbor_count += 1
  
  if current_generation[row][col]:
    neighbor_count -= 1
    
    if neighbor_count >= 2 and neighbor_count <= 3:
      return 1
    return 0

  else:
    if neighbor_count == 3:
      return 1
    return 0
    

def grid(width, cell_height, cell_width, surface, rows):
    x, y = 0, 0

    for i in range(rows):
      x += cell_width
      y += cell_height
      pygame.draw.line(surface, (100, 100, 100), (x, 0), (x, width))
      pygame.draw.line(surface, (100, 100, 100), (0, y), (width, y))


def main():
  next_generation = [[0 for _ in range(CELL_COLS)] for i in range(CELL_ROWS)]
  current_generation = [[choice(chances) for _ in range(CELL_COLS)] for i in range(CELL_ROWS)]
  
  # grid(WIDTH, HEIGHT/ROWS, WIDTH/ROWS, WINDOW, ROWS)  # Moved out of loop
  while True:
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    
    for col in range(1, CELL_COLS - 1):  # -1 necessary???
      for row in range(1, CELL_ROWS - 1):
        if current_generation[row][col]:
          draw_cell(WINDOW, col, row, 1)  # Might be flipped
        else:
          draw_cell(WINDOW, col, row, 0)

        next_generation[row][col] = check_cell_neighbors(current_generation, row, col)
    
    current_generation = deepcopy(next_generation)  # Deep copy does not use address, uses values once done calculating not async
    pygame.display.update()  # Flip changed to update
    CLOCK.tick(FPS)


def draw_cell(surface, x, y, doa):
  if doa:
    pygame.draw.rect(surface, (54, 115, 64), (x * CELL_WIDTH, y * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))  # CHANGE THIS TO COORDINATES
    return None
  pygame.draw.rect(surface, (0, 0, 0), (x * CELL_WIDTH, y * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))
  return None

main()