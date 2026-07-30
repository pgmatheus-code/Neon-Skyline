#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('city1'))

    def run(self):
        # music
        pygame.mixer.music.load('./assets/sounds/game1.mp3')
        pygame.mixer.music.play(-1)  # minus one for loop

        while True:
            for entity in self.entity_list:
                entity.surf = pygame.transform.scale(entity.surf, self.window.get_size()) # stretch
                self.window.blit(source=entity.surf, dest=entity.rect) # apply
                entity.move() # movement
            pygame.display.flip() # refresh
        pass
