'''
Author: your name
Date: 2021-02-08 21:40:20
LastEditTime: 2021-02-10 08:25:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pygame\alien.py
'''


import sys
import pygame
from settings import settings
from ship import ship

class AlienInvasion:

    def __init__(self):

        pygame.init()
        self.settings = settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = ship(self)

    def run_game(self):

        while True:
            self._check_events()
            self._update_screen()

            def _check_events(self):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
            
            def _update_screen(self):
                self.screen.fill(self.settings.bg_color)
                self.ship.blitme()
                pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()