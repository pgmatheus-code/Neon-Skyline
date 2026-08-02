#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Const import PLAYER_SPEED, KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, KEY_SHOOT, WIN_HEIGHT, WIN_WIDTH, \
    ENTITY_DEFAULT_HEALTH, PLAYER_SHOT_DELAY, ENTITY_DEFAULT_DAMAGE
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(
            entity_type='ship',
            name=f'{name}_ship',
            position=position,
            health=ENTITY_DEFAULT_HEALTH['player'],
            damage=ENTITY_DEFAULT_DAMAGE['player'],
            score=0
        )

        self.shot_timer = PLAYER_SHOT_DELAY
        self.is_shot_ready = False


    def move(self):
        pressed_key = pygame.key.get_pressed()
        player_name = self.name[:7]

        if pressed_key[KEY_LEFT[player_name]] and self.rect.left > 10:
            self.rect.centerx -= PLAYER_SPEED
        if pressed_key[KEY_RIGHT[player_name]] and self.rect.right < (WIN_WIDTH) - 10:
            self.rect.centerx += PLAYER_SPEED
        if pressed_key[KEY_UP[player_name]] and self.rect.top > 10:
            self.rect.centery -= PLAYER_SPEED
        if pressed_key[KEY_DOWN[player_name]] and self.rect.bottom < WIN_HEIGHT - 10:
            self.rect.centery += PLAYER_SPEED

    def shoot(self):

        player_name = self.name[:7]
        pressed_key = pygame.key.get_pressed()

        if self.shot_timer > 0:
            self.shot_timer -= 1
        else:
            self.is_shot_ready = True

        if pressed_key[KEY_SHOOT[player_name]] and self.is_shot_ready:
            self.shot_timer = PLAYER_SHOT_DELAY
            self.is_shot_ready = False
            return PlayerShot(name=f'{player_name}_shot', position=(self.rect.centerx, self.rect.centery))
        return None