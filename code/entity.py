#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame

class Entity(ABC):
    def __init__(self, type: str, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load(f'./assets/sprites/{type}/{name}.png').convert_alpha()
        #self.surf = pygame.transform.scale(self.surf, self.window.get_size()) # stretch
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass
