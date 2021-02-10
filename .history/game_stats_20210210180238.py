'''
Author: your name
Date: 2021-02-10 16:33:59
LastEditTime: 2021-02-10 18:02:38
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pygame\game_stats.py
'''
class GameStats:

    def __init__(self, ai_game):

        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0




