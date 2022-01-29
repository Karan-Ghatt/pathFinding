import pygame
import math
from queue import PriorityQueue


# Setting up width of display window, taking value and passing
# to pygame.display.set_mode((width, height))
WIN_WIDTH = 800
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_WIDTH))

# Setting caption for display window
pygame.display.set_caption("path finding algo")

# Defining RGB colour values to be used in grid
# used to make path, starting and end points, barriers etc.
# defined w/ capital letters to denote constants
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# CubeNode class
# Each Node will have to keep track of several values to determine characteristics
# such as where it is position (col, row), the width of its self so it knows how to
# be rendered (what colour/purpose it is - start/end node, barrier, etc)
# and, it's neighbors


class CubeNode:


    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width  # Used to determine position on grid
        self.y = col * width  # Used to determine position on grid
        self.col = WHITE      # Starting w/ all white cubes in grid
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

        # Indexing w/ row and col position
        # Methods define state and update cube

        def get_pos(self):
            return self.row, self.col


        # Method to define status of cube, visited or not
        # what makes a spot closed - they define the colour of the cube to help
        # us know what the cube does - i.e start, finish, etc

        def is_closed(self):
            return self.color == RED

        def is_open(self):
            pass






    pass















