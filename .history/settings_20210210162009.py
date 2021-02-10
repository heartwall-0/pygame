'''
Author: 零到正无穷
Date: 2021-02-10 07:44:50
LastEditTime: 2021-02-10 16:20:09
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

         self.bullet_speed = 1.0
         self.bullet_width = 3
         self.bullet_height = 15
         self.bullet_color = (60, 60, 60)

         self.bullets_allowed = 10

         self.fleet_drop_speed = 10
         self.fleet_direction = 1

         
