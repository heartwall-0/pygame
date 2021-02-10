'''
Author: 零到正无穷
Date: 2021-02-10 07:44:50
LastEditTime: 2021-02-10 17:57:34
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pygame\settings.py
'''
class Settings:

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        self.ship_speed = 1.5 #todo 机器人速度
        self.alien_speed = 1.0

        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        self.bullets_allowed = 100

        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.ship_limit = 3

        self.speedup_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = 1
        self.alien_points = 50



    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

         
