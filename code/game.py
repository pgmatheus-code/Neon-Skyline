#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT, MAIN_MENU_OPT
from code.level import Level
from code.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MAIN_MENU_OPT[0]: # new game
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            if menu_return == MAIN_MENU_OPT[1]: # scoreboard
                pass
            if menu_return == MAIN_MENU_OPT[2]: # quit game
                pygame.quit()
                sys.exit()
