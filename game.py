import pygame
import sys
from flat_board import FlatBoard
from settings import *


class Game:
    """
    Create a template game of the Game of Life

    === Attributes ===
    screen:
        The main screen where the board is located.
    caption:
        The title of the game
    """
    screen: pygame.display
    caption: pygame.display

    def __init__(self) -> None:
        """Initialize the game"""
        self.screen = pygame.display.set_mode(size)
        self.caption = pygame.display.set_caption("Game of Life")

    def run_game(self, mode) -> None:
        """The main game loop"""

        # set the background to white

        pygame.display.flip()
        self.screen.fill(WHITE)
        mode.set_cell_neighbours()

        running = True
        while running:
            frame = mode.draw_board(True)
            self.screen.blit(frame, (0, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    cell = mode.get_cell()
                    mode.update_cell_status(cell,
                                            (cell.get_state() + 1) % 2)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    game_mode = 0
                    while game_mode == 0:
                        frame = mode.draw_board(False)
                        self.screen.blit(frame, (0, 0))
                        pygame.time.wait(game_speed)
                        pygame.display.flip()
                        mode.update_board()
                        frame.fill(WHITE)
                        for e in pygame.event.get():
                            if e.type == \
                              pygame.MOUSEBUTTONDOWN and event.button == 3:
                                game_mode = 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        mode.reset_board()
            frame.fill(WHITE)





if __name__ == '__main__':
    pygame.init()

    mode = FlatBoard(length)
    game = Game()

    game.run_game(mode)

    pygame.quit()
    sys.exit()




