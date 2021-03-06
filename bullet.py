'''
Author: your name
Date: 2021-02-10 11:52:17
LastEditTime: 2021-02-10 12:00:23
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pygame\bullet.py
'''
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)
    def update(self):
         self.y -= self.settings.bullet_speed
         self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

