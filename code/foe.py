#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.const import FOE_SHIP_DICT, BACKGROUND_SPEED, WIN_WIDTH, FOE_SPEED_MULTIPLIER
from code.entity import Entity


class Foe(Entity):
    def __init__(self, name: str, position: tuple, auto_stretch: bool = False):
        #pick random
        random.choice(list(FOE_SHIP_DICT.keys()))
        foe_ship_size = random.choice(list(FOE_SHIP_DICT.keys()))

        super().__init__('ship', f'{name}_ship_{foe_ship_size}', position)
        self.current_foe_speed = FOE_SHIP_DICT[foe_ship_size]

    def move(self):
        layer_name = self.name[6:]
        self.rect.centerx -= self.current_foe_speed * FOE_SPEED_MULTIPLIER # scrolling movement

        # reset scrolling at the end
        #if self.rect.right <= 0:
        #    self.rect.left = WIN_WIDTH + 10
