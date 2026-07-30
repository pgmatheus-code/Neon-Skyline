#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import FONT_SMALLFONTS, NEON_SALMON, STANDARD_TIMEOUT, WIN_HEIGHT, NEON_PURPLE, NEON_PINK, LEVEL_FPS
from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('city1'))
        self.timeout = STANDARD_TIMEOUT

    def run(self):
        # music
        pygame.mixer.music.load('./assets/sounds/game1.mp3')
        pygame.mixer.music.play(-1)  # minus one for loop
        clock = pygame.time.Clock()

        while True:
            clock.tick(LEVEL_FPS)
            for entity in self.entity_list:
                entity.surf = pygame.transform.scale(entity.surf, self.window.get_size()) # stretch
                self.window.blit(source=entity.surf, dest=entity.rect) # apply
                entity.move() # movement

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # UI
            self.level_text(18, f'{self.name} - Timeout: {self.timeout / 1000 : .1f}s', NEON_PINK, (10, 10))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', NEON_PINK, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entities: {len(self.entity_list)}', NEON_PINK, (10, WIN_HEIGHT - 20))
            pygame.display.flip() # refresh

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        # shadow
        text_font: Font = pygame.font.Font(FONT_SMALLFONTS, text_size)

        text_shadow_surf: Surface = text_font.render(text, True, NEON_PURPLE).convert_alpha()
        text_shadow_rect: Rect = text_shadow_surf.get_rect(left=text_pos[0] + 1, top=text_pos[1] + 1)
        self.window.blit(source=text_shadow_surf, dest=text_shadow_rect)

        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
