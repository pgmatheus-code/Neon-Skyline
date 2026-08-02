#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MAIN_MENU_OPT
from code.Level import Level
from code.Menu import Menu
from code.Scoreboard import Scoreboard


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        while True:
            scoreboard = Scoreboard(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MAIN_MENU_OPT[0], MAIN_MENU_OPT[1], MAIN_MENU_OPT[2]]:  # new game
                player_score = [0, 0]  # [player1, player2]

                # city 1
                level = Level(self.window, 'city1', menu_return, player_score)
                level_return = level.run(player_score)

                if level_return:  # city 2
                    level = Level(self.window, 'city2', menu_return, player_score)
                    level_return = level.run(player_score)

                    if level_return:  # city 3
                        level = Level(self.window, 'city3', menu_return, player_score)
                        level_return = level.run(player_score)

                        if level_return:  # city 4
                            level = Level(self.window, 'city4', menu_return, player_score)
                            level_return = level.run(player_score)

                            if level_return:  # end game
                                scoreboard.save(menu_return, player_score)

            if menu_return == MAIN_MENU_OPT[3]:  # scoreboard
                scoreboard.show()
            if menu_return == MAIN_MENU_OPT[4]:  # quit game
                pygame.quit()
                sys.exit()
