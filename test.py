'''
Author: your name
Date: 2021-02-08 21:40:20
LastEditTime: 2021-02-09 21:42:25
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pygame\test.py
'''

import sys
import pygame
class AlienInvasion:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
    
        self.bg_color = (230, 230, 230)

    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()