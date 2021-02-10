'''
Author: your name
Date: 2021-02-10 17:32:28
LastEditTime: 2021-02-10 17:35:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pygame\scoreboard.py
'''
import pygame.font

class Scoreboard:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect  = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats