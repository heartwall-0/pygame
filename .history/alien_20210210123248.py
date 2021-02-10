'''
Author: your name
Date: 2021-02-10 12:28:04
LastEditTime: 2021-02-10 12:32:48
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pygame\alien.py
'''
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super.__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('image/alien.bmp')

