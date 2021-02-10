'''
Author: your name
Date: 2021-02-10 07:55:21
LastEditTime: 2021-02-10 08:33:26
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

        #todo 移动标志

        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''根据移动标志调整飞船位置'''
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)