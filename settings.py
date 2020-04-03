WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (191, 191, 191)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (252, 186, 3)
PURPLE = (144, 3, 252)
PINK = (255, 166, 243)
PINK2 = (171, 53, 100)
YELLOW = (250, 239, 125)

# CELL COLOUR THEMES
# cell_colour = [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]
# cell_colour = [RED, ORANGE, GREEN, BLUE, PURPLE, PINK, PINK2, YELLOW, BLACK]
cell_colour = [(0, 0, 255), (0, 28, 255), (0, 56, 255),
               (0, 84, 255), (0, 112, 255), (0, 140, 255),
               (0, 168, 255), (0, 196, 255), (0, 224, 255)]

size = (600, 600)
# can change length to have different number of cells on FlatBoard, must be
# multiple of board size
length = 30

game_speed = 100

# DO NOT CHANGE
spacing = size[0] // length

