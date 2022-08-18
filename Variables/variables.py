from time import sleep
import pygame
import sys
from random import randint, choice
from copy import deepcopy

pygame.init()  # Initialize pygame

WIN = WIDTH, HEIGHT = 1000, 1000  # Width and height of the window

ROWS = 200  # Numbers of rows / cols

CELL_HEIGHT, CELL_WIDTH = WIDTH // ROWS, HEIGHT // ROWS  # Calculation of height + width of each cell

WINDOW = pygame.display.set_mode((WIN))  # Make surface for pygame

pygame.display.set_caption("Conway's Game of Life")  # Caption title for window

CELL_ROWS = HEIGHT // CELL_HEIGHT  # Calculation of how many rows

CELL_COLS = WIDTH // CELL_WIDTH  # Calculation of how many cols

CLOCK = pygame.time.Clock()  # Clock for FPS

chances = [1, 0]  # Probability of a cell spawning (1 is alive)

font = pygame.font.Font("pixelfont1.ttf", 200)  # Pygame font

menu_font = pygame.font.Font("pixelfont1.ttf", 100)

custom_font = pygame.font.Font("pixelfont1.ttf", 20)

paused_font = font.render("PAUSED", True, pygame.Color("red"))  # Render font

menu_font_random = menu_font.render("RANDOM", True, pygame.Color("darkgreen"))

menu_font_custom = menu_font.render("CUSTOM", True, pygame.Color("darkgreen"))

custom_instructions_font = custom_font.render("DONE", True, pygame.Color("darkgreen"))

current_generation = [[choice(chances) for _ in range(CELL_COLS)] for i in range(CELL_ROWS)]  # Default random generation of alive cells 2D list
