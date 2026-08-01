#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import FONT_SMALLFONTS, STANDARD_TIMEOUT, WIN_HEIGHT, NEON_PURPLE, NEON_PINK, LEVEL_FPS, MAIN_MENU_OPT, \
    FOE_EVENT, FOE_SPAWNING_INTERVAL
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Foe import Foe
from code.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        # attributes
        self.timeout = STANDARD_TIMEOUT
        self.window = window
        self.name = name
        self.game_mode = game_mode

        # spawning
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('city3'))
        self.entity_list.append(EntityFactory.get_entity('player1'))
        if game_mode in [MAIN_MENU_OPT[1], MAIN_MENU_OPT[2]]:
            self.entity_list.append(EntityFactory.get_entity('player2'))
        pygame.time.set_timer(FOE_EVENT, FOE_SPAWNING_INTERVAL)


    def run(self):
        # music
        pygame.mixer.music.load('./assets/sounds/game1.mp3')
        pygame.mixer.music.play(-1)  # minus one for loop
        clock = pygame.time.Clock()

        while True:
            clock.tick(LEVEL_FPS)
            for entity in self.entity_list:
                if entity.auto_stretch:
                    entity.surf = pygame.transform.scale(entity.surf, self.window.get_size()) # stretch

                self.window.blit(source=entity.surf, dest=entity.rect) # apply
                entity.move() # movement
                if isinstance(entity, (Player)):
                    shot = entity.shoot()
                    if shot is not None:
                        self.entity_list.append(shot)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == FOE_EVENT:
                    self.entity_list.append(EntityFactory.get_entity('foe'))

            # UI
            self.level_text(18, f'{self.name} - Timeout: {self.timeout / 1000 : .1f}s', NEON_PINK, (10, 10))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', NEON_PINK, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entities: {len(self.entity_list)}', NEON_PINK, (10, WIN_HEIGHT - 20))
            pygame.display.flip() # refresh

            # Entity mediator - entity damage and destruction
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        # shadow
        text_font: Font = pygame.font.Font(FONT_SMALLFONTS, text_size)

        text_shadow_surf: Surface = text_font.render(text, True, NEON_PURPLE).convert_alpha()
        text_shadow_rect: Rect = text_shadow_surf.get_rect(left=text_pos[0] + 1, top=text_pos[1] + 1)
        self.window.blit(source=text_shadow_surf, dest=text_shadow_rect)

        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
