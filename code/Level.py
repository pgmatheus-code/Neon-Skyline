#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from re import search

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import FONT_SMALLFONTS, STANDARD_TIMEOUT, WIN_HEIGHT, NEON_PURPLE, NEON_PINK, LEVEL_FPS, MAIN_MENU_OPT, \
    FOE_EVENT, FOE_SPAWNING_INTERVAL, WIN_WIDTH, TIMEOUT_EVENT, TIMEOUT_STEP
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Foe import Foe
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        # attributes
        self.player_score = player_score
        self.timeout = STANDARD_TIMEOUT
        self.window = window
        self.name = name
        self.game_mode = game_mode

        # spawning
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(name))

        # player 1 instantiation
        player = EntityFactory.get_entity('player1')
        player.score = player_score[0]
        self.entity_list.append(player)

        # player 2 instantiation
        if game_mode in [MAIN_MENU_OPT[1], MAIN_MENU_OPT[2]]:
            player = EntityFactory.get_entity('player2')
            player.score = player_score[1]
            self.entity_list.append(player)
        pygame.time.set_timer(FOE_EVENT, FOE_SPAWNING_INTERVAL)
        pygame.time.set_timer(TIMEOUT_EVENT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
        # music
        pygame.mixer.music.load(f'./assets/sounds/{self.name}.mp3')
        pygame.mixer.music.play(-1)  # minus one for loop
        clock = pygame.time.Clock()

        # main loop
        while True:
            clock.tick(LEVEL_FPS)
            for entity in self.entity_list:

                # stretch things
                if entity.auto_stretch:
                    entity.surf = pygame.transform.scale(entity.surf, self.window.get_size())

                # apply drawing
                self.window.blit(source=entity.surf, dest=entity.rect)

                # move each stuff
                entity.move()

                # shot
                if isinstance(entity, (Player, Foe)):
                    shot = entity.shoot()
                    if shot is not None:
                        self.entity_list.append(shot)

                # player hud
                if entity.name == 'player1_ship':
                    self.level_text(
                        text_size= 14,
                        text= f'Player 1 Health: {entity.health}',
                        text_color= NEON_PINK,
                        text_pos= (10, WIN_HEIGHT - 60)
                    )
                    self.level_text(
                        text_size=14,
                        text=f'Score: {entity.score}',
                        text_color=NEON_PINK,
                        text_pos=(10, WIN_HEIGHT - 30)
                    )
                if entity.name == 'player2_ship':
                    self.level_text(
                        text_size=14,
                        text=f'Player 2 Health: {entity.health}',
                        text_color=NEON_PINK,
                        text_pos=(WIN_WIDTH - 230, WIN_HEIGHT - 60)
                    )
                    self.level_text(
                        text_size=14,
                        text=f'Score: {entity.score}',
                        text_color=NEON_PINK,
                        text_pos=(WIN_WIDTH - 230, WIN_HEIGHT - 30)
                    )

            # get any pygame event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # standard quit event
                    pygame.quit()
                    sys.exit()
                if event.type == FOE_EVENT:
                    # instantiate foes
                    self.entity_list.append(EntityFactory.get_entity('foe'))
                if event.type == TIMEOUT_EVENT:
                    if self.timeout > 0:
                        # subtract time from timeout
                        self.timeout -= TIMEOUT_STEP
                    else:
                        # pass score
                        for entity in self.entity_list:
                            if isinstance(entity, Player) and entity.name == 'player1_ship':
                                player_score[0] = entity.score
                            elif isinstance(entity, Player) and entity.name == 'player2_ship':
                                player_score[1] = entity.score
                        # jump to the next city
                        return True

                # search for player
                found_player = False
                for entity in self.entity_list:
                    if isinstance(entity, Player):
                        found_player = True

                # back to main menu if everyone's dead
                if not found_player:
                    return False


            # level hud
            if self.timeout >= 10_000:
                timeout_formatted = f'{self.timeout / 1000 : .0f}s'
            else:
                timeout_formatted = f'{self.timeout / 1000 : .1f}s'

            self.level_text(18, f'{self.name} - Timeout: {timeout_formatted}', NEON_PINK, (10, 10))
            # self.level_text(14, f'fps: {clock.get_fps():.0f}', NEON_PINK, (10, WIN_HEIGHT - 35)) # debug
            # self.level_text(14, f'entities: {len(self.entity_list)}', NEON_PINK, (10, WIN_HEIGHT - 20)) # debug

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
