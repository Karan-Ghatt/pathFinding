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


        # If the cube is red then it is closed
        def is_closed(self):
            return self.color == RED

        ## DEF IS_x METHODS ##
        # If the cube is green then it is open
        def is_open(self):
            return self.color == GREEN

        # If the cube is a battier then it is black
        def is_barrier(slef):
            return self.color == BLACK

        # If the cube is orage then it is start node
        def is_start(self):
            return self.color == ORANGE

        # If the cube is purple  then it is end node
        def is_end(self):
            return self.color == TURQUOISE

        # Reset colour/type of node
        def reset(self):
            return self.color == WHITE

        ## DEF MAKE_x METHODS ##
        # If the cube is red then it is closed
        def make_closed(self):
            return self.color == RED

        # If the cube is green then it is open
        def make_open(self):
            self.color == GREEN

        # If the cube is a barrier then it is black
        def make_barrier(slef):
            self.color == BLACK

        # If the cube is orage then it is start node
        def make_start(self):
            self.color == ORANGE

        # If the cube is purple  then it is end node
        def make_end(self):
            self.color == TURQUOISE

        # Path of algo to be shown w/ purple cubes
        def make_path(self):
            self.color = PURPLE


        # Method to craw cube on screen - where do we want to draw cube
        # pass window, colour and rectangle, passing x, y, height, rect
        # (0,0) is the top left corner of the window, moving to the right caused
        # x to increase. Moving down causes y to increase. Start drawing from (0,0)
        def draw(self, win):
            pygame.draw.rect(win, self.color, (self.x, self.y, self.widh, self.widh))

        #
        def update_neighbors(self, grid):
            pass

        # Less than function, how we compare two cubes together.
        #
        def __lt__(self, other):
            return False


# Huristic function for algo - p1 and p2 are point one and point two:
# (x,y) = (row, col) - figuring out distance between p1 and p2
# using Manhattan distance (L-distance; the quickest L)
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return abs(x1 - x2) + abs(y1 - y2)


# Method to create gird to hold cubes
# how many rows in grid and width of each row
def make_grid(rows, width):
    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = CubeNode(i, j, gap, rows)
            grid[i].append(node)
    return grid

# Method to define gridline, to let us create cube in grid
def draw_grid(win, rows, width):
    gap = width // rows

    # Draw horizontal line for each row
    # then drawing vertical lines
    for i in range(rows):
        pygame.draw.line(win, GREY, (0,i*gap), (width, i*gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width ))

# Main draw function
def draw(win, grid, rows, width):
    win.fill(WHITE) # Redrawing w/ each frame - fill w/ white

    for row in grid:
        for cube in row:
            cube.draw(width)

    draw_grid(win, rows, width)
    pygame.display.update()

# Method to figure out cube position from mouse position
# taking x and y position and diving by width of cube
def get_clicked_(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


# Main functions - Main loop
# does the collision checks, on button press check and execute function
# changes cube type
def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width) # actually generate array

    start = None     # Variables to help us keep track of algo status
    end = None       # Variables to help us keep track of algo status
    run = True       # Variables to help us keep track of algo status
    started = False  # Variables to help us keep track of algo status

    # While run is set to True
    # At begging of while loop, check through all events that have happened and check
    # what they are
    while run:
        for event in pygame.event.get():

            # Close game if click x
            if event.type == pygame.QUIT:
                run = False

            # Stops user changing anything in grid while algo is running
            if started:
                continue

    pygame.quit()














