#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import WIN_WIDTH, BACKGROUND_SPEED
from code.entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__('background', name, position, True)

    def move(self):
        layer_name = self.name[6:]
        self.rect.centerx -= BACKGROUND_SPEED[layer_name] # scrolling movement

        # reset scrolling at the end
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
