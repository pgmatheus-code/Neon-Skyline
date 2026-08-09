#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Const import FOE_SHIP_DICT, BACKGROUND_SPEED, WIN_WIDTH, FOE_SPEED_MULTIPLIER, ENTITY_DEFAULT_HEALTH, \
    FOE_SHOT_DELAY, ENTITY_DEFAULT_DAMAGE, FOE_SCORE
from code.Entity import Entity
from code.FoeShot import FoeShot


class Foe(Entity):
    def __init__(self, name: str, position: tuple):
        # pick random
        foe_ship_size = random.choice(list(FOE_SHIP_DICT.keys()))
        super().__init__(
            entity_type='ship',
            name=f'{name}_ship_{foe_ship_size}',
            position=position,
            health=ENTITY_DEFAULT_HEALTH[f'foe_{foe_ship_size}'],
            damage=ENTITY_DEFAULT_DAMAGE[f'foe_{foe_ship_size}'],
            score=FOE_SCORE[f'foe_{foe_ship_size}']
        )
        self.current_foe_speed = FOE_SHIP_DICT[foe_ship_size]
        self.shot_timer = FOE_SHOT_DELAY

    def move(self):
        layer_name = self.name[6:]
        self.rect.centerx -= self.current_foe_speed * FOE_SPEED_MULTIPLIER  # scrolling movement

    def shoot(self):
        if self.shot_timer > 0:
            self.shot_timer -= 1
        else:
            self.shot_timer = FOE_SHOT_DELAY * random.randint(1, 5)
            return FoeShot(name='foe_shot', position=(self.rect.centerx, self.rect.centery), entity_name=self.name)
        return None
