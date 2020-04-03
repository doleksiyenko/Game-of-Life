from typing import List, Tuple, Optional


class Cell:
    """
    A cell in the board of the Game of Life

    === Private Attributes ===
    _neighbours:
        A list of the neighbour cells of
    _state:
        The state of the cell (0 means dead, 1 means alive)
    _coordinates:
        The coordinates on the game board.
    """
    _neighbours: List['Cell']
    _state: int
    _coordinates = Tuple[int, int]

    def __init__(self, pos_x: int, pos_y: int, state: int):
        self._neighbours = []
        self._state = state
        self.x = pos_x
        self.y = pos_y

    def set_state(self, state: int) -> None:
        """Change the state of the cell to <state>
        <state> == 0 or <state> == 1
        """
        self._state = state

    def set_neighbours(self, neighbours) -> None:
        """Take in a list of neighbour Cells, and set them as neighbours to
        self"""
        for neighbour in neighbours:
            self._neighbours.append(neighbour)

    def get_state(self):
        """Get the state of a cell."""
        return self._state

    def get_neighbours(self):
        return self._neighbours

    def get_active_neighbours(self) -> List['Cell']:
        active = []
        for neighbour in self._neighbours:
            if neighbour.get_state() == 1:
                active.append(neighbour)
        return active

