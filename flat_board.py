from cell import Cell
from typing import List, Tuple
import pygame
from settings import *
import math

surface = pygame.Surface(size)
surface.fill(WHITE)


class FlatBoard:
    """
    _board:
        A 2 dimensional board that has a size length * length.
        Each unit of the board is a size 1 Cell.
    """
    _board: List[List[Cell]]

    def __init__(self, length: int) -> None:
        """
        Initialize the game board, with <length> columns and <length> rows to
        generate a square 2 dimensional array of Cells.
        """
        self._board = []

        for i in range(length):
            column = []
            x = i * (size[0] // length)
            for j in range(length):
                y = j * (size[1] // length)
                column.append(Cell(x, y, 0))
            self._board.append(column)

    def __len__(self):
        return len(self._board)

    def create_copy(self) -> 'FlatBoard':
        """Create a copy of the board, so when checking if neighbours are
         alive/dead, can make valid comparisons, meanwhile changing status of
         Cell in the original board"""
        board_copy = FlatBoard(len(self))
        board_copy.set_cell_neighbours()
        for column in self._board:
            for cell in column:
                board_copy._board[cell.x // spacing][
                    cell.y // spacing].set_state(cell.get_state())
        return board_copy

    def get_cell(self) -> Cell:
        """Return a cell found at coordinates, x, y"""
        mouse_pos = pygame.mouse.get_pos()
        mouse_pos_update = (mouse_pos[0] - spacing//2,
                            mouse_pos[1] - spacing//2)
        return self._get_cell_at_position(mouse_pos_update)

    def _get_cell_at_position(self, location: Tuple[int, int]) -> Cell:
        """Get the cell that is has a position under <location>"""
        x = location[0]
        y = location[1]

        if x % spacing < math.ceil(spacing / 2):
            # if the remainder is less than half of spacing, then round down
            x -= (x % spacing)
        else:
            # if the remainder is greater than half of spacing, the round up
            x += (spacing - (x % spacing))

        if y % spacing < math.ceil(spacing / 2):
            y -= (y % spacing)
        else:
            y += (spacing - (y % spacing))

        return self._board[x//spacing][y//spacing]

    def update_cell_status(self, cell: Cell, status: int) -> None:
        """Update the status of a cell"""
        cell.set_state(status)

    def set_cell_neighbours(self) -> None:
        # set the neighbours for every cell
        for column in self._board:
            for cell in column:
                # get all potential positions of cells
                diff = size[0] // length
                neighbours_pos = [(cell.x - diff, cell.y - diff),
                                  (cell.x - diff, cell.y),
                                  (cell.x - diff, cell.y + diff),
                                  (cell.x, cell.y - diff),
                                  (cell.x, cell.y + diff),
                                  (cell.x + diff, cell.y - diff),
                                  (cell.x + diff, cell.y),
                                  (cell.x + diff, cell.y + diff)]
                # check if any of the neighbours are out of bounds
                neighbour_cells = []
                for pos in neighbours_pos:
                    if (len(self) > (pos[0] // spacing) >= 0) and \
                            (len(self) > (pos[1] // spacing) >= 0):
                        neighbour_cells.append(self._board[pos[0] // spacing]\
                                                   [pos[1] // spacing])
                cell.set_neighbours(neighbour_cells)

    def draw_board(self) -> pygame.Surface:
        """Draw a rectangle for each cell on the board."""
        for column in self._board:
            for cell in column:
                if cell.get_state() == 0:
                    pygame.draw.rect(surface, GREY, (cell.x, cell.y,
                                                     size[0]//length,
                                                     size[0]//length), 1)
                else:
                    colour = len(cell.get_active_neighbours())
                    # draw a filled rectangle based on active neighbours
                    pygame.draw.rect(surface, cell_colour[colour],
                                     (cell.x, cell.y,
                                     size[0] // length,
                                     size[0] // length), 0)
                    # draw a black outline
                    pygame.draw.rect(surface, BLACK,
                                     (cell.x, cell.y,
                                      size[0] // length,
                                      size[0] // length), 1)

        # draw a black box over the current highlighted cell
        curr_cell = self.get_cell()
        pygame.draw.rect(surface, BLACK, (curr_cell.x, curr_cell.y,
                                          size[0]//length,
                                          size[0]//length), 1)
        return surface

    def update_board(self) -> None:
        """Update <self> to be the next generation of the board."""
        board_copy = self.create_copy()
        for column in board_copy._board:
            for cell in column:
                active = cell.get_active_neighbours()
                if (cell.get_state() == 0) and (len(active) == 3):
                    # if the cell is dead, but has 3 active neighbours,
                    # it becomes alive in the next generation, as by
                    # reproduction
                    self._board[cell.x//spacing][cell.y//spacing].set_state(1)
                elif (cell.get_state() == 1) and \
                        ((len(active) == 2) or (len(active) == 3)):
                    # if the cell is alive, and has 2 or 3 live neighbours,
                    # survives to the next generation
                    self._board[cell.x//spacing][cell.y//spacing].set_state(1)
                else:
                    # all other cells die
                    self._board[cell.x//spacing][cell.y//spacing].set_state(0)

