#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame

class Entity(ABC):
    def __init__(self, entity_type: str, name: str, position: tuple, health: int, damage: int, auto_stretch: bool = False):
        self.name = name
        self.surf = pygame.image.load(f'./assets/sprites/{entity_type}/{name}.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.auto_stretch = auto_stretch
        self.speed = 0
        self.health = health
        self.damage = damage
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):
        pass
