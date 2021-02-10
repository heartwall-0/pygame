'''
Author: your name
Date: 2021-02-10 12:28:04
LastEditTime: 2021-02-10 16:04:07
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pygame\alien.py
'''
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.settings = ai_game.settings

        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)

        self.alien_speed = 1.0

    def update(self):
        self.x += self.settings.alien_speed
        self.rect.x = self.x