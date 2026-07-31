#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import KEYDOWN

from code.const import BACKGROUND_SPEED, WIN_WIDTH, PLAYER_SPEED, WIN_HEIGHT
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple, auto_stretch: bool = False):
        super().__init__('ship', f'{name}_ship', position)

    def move(self):
        pressed_key = pygame.key.get_pressed()

        if (pressed_key[pygame.K_LEFT] or pressed_key[pygame.K_a]) and self.rect.left > 10:
            self.rect.centerx -= PLAYER_SPEED
        if (pressed_key[pygame.K_RIGHT] or pressed_key[pygame.K_d]) and self.rect.right < (WIN_WIDTH / 1.5) - 10:
            self.rect.centerx += PLAYER_SPEED
        if (pressed_key[pygame.K_UP] or pressed_key[pygame.K_w]) and self.rect.top > 10:
            self.rect.centery -= PLAYER_SPEED
        if (pressed_key[pygame.K_DOWN] or pressed_key[pygame.K_s]) and self.rect.bottom < WIN_HEIGHT - 10:
            self.rect.centery += PLAYER_SPEED
