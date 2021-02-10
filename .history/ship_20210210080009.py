'''
Author: your name
Date: 2021-02-10 07:55:21
LastEditTime: 2021-02-10 08:00:09
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pygame\ship.py
'''
import pygame

class ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)