import pygame
from Variables.variables import *

def main():  # Displays the menu options
  global current_generation 

  while True:
    WINDOW.fill(pygame.Color("black"))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pressed()

        if mouse[0]:
          pos = pygame.mouse.get_pos()
          print(pos)

          if pos[0] <= 470 and pos[0] >= 120:
            if pos[1] <= 270 and pos[1] >= 120:
              life(current_generation)
          
          if pos[0] <= 470 and pos[0] >= 120:
            if pos[1] <= 470 and pos[1] >= 320:
              current_generation = [[0 for _ in range(CELL_COLS)] for i in range(CELL_ROWS)]
              sleep(0.1)
              custom_map()

      pygame.draw.rect(WINDOW, pygame.Color("darkgrey"), (WIDTH/2 - 180, HEIGHT/2 - 180, 350, 150))
      WINDOW.blit(menu_font_random, (WIDTH/2 - 155, HEIGHT/2 - 145))
      pygame.draw.rect(WINDOW, pygame.Color("darkgrey"), (WIDTH/2 - 180, HEIGHT/2 + 20, 350, 150))
      WINDOW.blit(menu_font_custom, (WIDTH/2 - 140, HEIGHT/2 + 60))
      pygame.display.update()
      CLOCK.tick(30)


def life(current_generation):  # Runs the simulation itself
  STATE = 1  # 1 means unpaused, 0 means paused
  FPS = 8  # Frames per second of window
  next_generation = [[0 for _ in range(CELL_COLS)] for i in range(CELL_ROWS)]
  colors = ["darkgrey", "white", "red", "orange", "yellow", "green", "blue", "purple"]
  color = colors[0]
  color_index = 0

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
              if STATE:
                STATE = 0
              else:
                STATE = 1
    
    if STATE:  # If 0, does not update the window's drawings
      
      WINDOW.fill(pygame.Color("black"))
      keys = pygame.key.get_pressed()
      
      if keys[pygame.K_RIGHT]:
        color_index += 1
        if color_index == len(colors):
          color_index = 0
        color = colors[color_index]

      if keys[pygame.K_LEFT]:
        color_index -= 1
        if color_index == -1:
          color_index = len(colors) - 1
        color = colors[color_index]

      if keys[pygame.K_UP]:
        if FPS <= 18:
          FPS += 2
      
      if keys[pygame.K_DOWN]:
        if FPS >= 4:
          FPS -= 2
      if keys[pygame.K_g]:
        grid(WIDTH, CELL_HEIGHT, CELL_WIDTH, WINDOW, ROWS)

      for col in range(1, CELL_COLS - 1):  # -1 necessary???
        for row in range(1, CELL_ROWS - 1):
          if current_generation[row][col]:
            draw_cell(WINDOW, col, row, color)  # Might be flipped

          next_generation[row][col] = check_cell_neighbors(current_generation, row, col)
      
      current_generation = deepcopy(next_generation)  # Deep copy does not use address, uses values once done calculating not async
    
    else:
      WINDOW.blit(paused_font, (WIDTH/2 - 250, HEIGHT/2 - 80))

    pygame.display.update()
    pygame.display.update()  # Flip changed to update
    CLOCK.tick(FPS)


def custom_map():  # Allows user to choose what cells are alive
  while True:
    WINDOW.fill(pygame.Color("black"))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      
    mouse = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_g]:
      grid(WIDTH, CELL_HEIGHT, CELL_WIDTH, WINDOW, ROWS)


    if mouse[0]:
      pos = pygame.mouse.get_pos()
      spawn_cell(WINDOW, *pos)
      print(pos)
      if pos[0] <= 65:
            if pos[1] <= 35:
              life(current_generation)

    for col in range(1, CELL_COLS - 1):  # -1 necessary???
        for row in range(1, CELL_ROWS - 1):
          if current_generation[row][col]:
            draw_cell(WINDOW, col, row,"darkgrey")  # Might be flipped

    pygame.draw.rect(WINDOW, pygame.Color("darkgrey"), (0, 0, 65, 35))
    WINDOW.blit(custom_instructions_font, (10, 10))
    pygame.display.update()
    CLOCK.tick(100)


def check_cell_neighbors(current_generation, row, col):  # Logic for the game of life
  neighbor_count = 0
  for i in range(row - 1, row + 2):  # Check surrounding cells
    for j in range(col - 1, col + 2):  
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


def grid(width, cell_height, cell_width, surface, rows):  # A grid representation of cells
    x, y = 0, 0

    for i in range(rows):
      x += cell_width
      y += cell_height
      pygame.draw.line(surface, (100, 100, 100), (x, 0), (x, width))
      pygame.draw.line(surface, (100, 100, 100), (0, y), (width, y))


def draw_cell(surface, x, y, color):  # Draw cell on window
  pygame.draw.rect(surface, pygame.Color(color), (x * CELL_WIDTH, y * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))


def spawn_cell(surface, x, y):  # Spawns in cell and documents alive in current_generation 2D list
  global current_generation
  current_generation[y // CELL_HEIGHT][x // CELL_WIDTH] = 1
  pygame.draw.rect(surface, pygame.Color("darkgrey"), ((x // CELL_WIDTH) * CELL_WIDTH, (y // CELL_HEIGHT) * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))


if __name__ == '__main__':
  print("Testing")