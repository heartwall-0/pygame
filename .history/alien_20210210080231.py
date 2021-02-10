'''
Author: your name
Date: 2021-02-08 21:40:20
LastEditTime: 2021-02-10 08:02:31
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
    
        self.bg_color = (230, 230, 230)

    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()