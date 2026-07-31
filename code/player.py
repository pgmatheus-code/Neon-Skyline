#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.const import PLAYER_SPEED, KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, KEY_SHOOT, WIN_HEIGHT, WIN_WIDTH
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple, auto_stretch: bool = False):
        super().__init__('ship', f'{name}_ship', position)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        player_name = self.name[:7]

        if pressed_key[KEY_LEFT[player_name]] and self.rect.left > 10:
            self.rect.centerx -= PLAYER_SPEED
        if pressed_key[KEY_RIGHT[player_name]] and self.rect.right < (WIN_WIDTH / 1.5) - 10:
            self.rect.centerx += PLAYER_SPEED
        if pressed_key[KEY_UP[player_name]] and self.rect.top > 10:
            self.rect.centery -= PLAYER_SPEED
        if pressed_key[KEY_DOWN[player_name]] and self.rect.bottom < WIN_HEIGHT - 10:
            self.rect.centery += PLAYER_SPEED
