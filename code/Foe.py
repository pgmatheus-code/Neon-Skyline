#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Const import FOE_SHIP_DICT, BACKGROUND_SPEED, WIN_WIDTH, FOE_SPEED_MULTIPLIER, ENTITY_DEFAULT_HEALTH
from code.Entity import Entity

class Foe(Entity):
    def __init__(self, name: str, position: tuple, auto_stretch: bool = False):
        #pick random
        foe_ship_size = random.choice(list(FOE_SHIP_DICT.keys()))
        super().__init__(entity_type='ship', name=f'{name}_ship_{foe_ship_size}', position=position, health=ENTITY_DEFAULT_HEALTH[f'foe_{foe_ship_size}'])
        self.current_foe_speed = FOE_SHIP_DICT[foe_ship_size]

        # debug
        #print(f'spawned foe_{foe_ship_size} with health = {self.health}')

    def move(self):
        layer_name = self.name[6:]
        self.rect.centerx -= self.current_foe_speed * FOE_SPEED_MULTIPLIER # scrolling movement

        # reset scrolling at the end
        #if self.rect.right <= 0:
        #    self.rect.left = WIN_WIDTH + 10
