#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Rect, Surface, KEYDOWN
from pygame.font import Font
from code.const import WIN_WIDTH, WIN_HEIGHT, LOGO_WIDTH, LOGO_HEIGHT, SIGN_SIZE, MAIN_MENU_OPT, \
    MENU_OPT_SIZE, NEON_PINK, FONT_SMALLFONTS, FONT_LARGEFONTS, NEON_PURPLE, NEON_CYAN, MENU_OPT_SPACING, MENU_HEIGHT, \
    SHADOW_COLOR, SHADOW_DIRECTION


class Menu:
    def __init__(self, window):
        self.window = window

        # background
        self.background = pygame.image.load('./assets/sprites/background/main_menu_background.png').convert_alpha()
        self.background = pygame.transform.scale(self.background, self.window.get_size())
        self.rect = self.background.get_rect(topleft=(0, 0))

        # background
        self.logo = pygame.image.load('./assets/sprites/logo.png').convert_alpha()
        self.logo = pygame.transform.scale(self.logo, size=(LOGO_WIDTH, LOGO_HEIGHT))
        self.small_rect = self.logo.get_rect(
            topleft=((WIN_WIDTH / 2) - (LOGO_WIDTH / 2), (WIN_HEIGHT / 3.3) - (LOGO_HEIGHT / 2)))

    def run(self, ):
        selected_option = 0

        # music
        pygame.mixer.music.load('./assets/sounds/main_menu.mp3')
        pygame.mixer.music.play(-1) # minus one for loop


        while True:
            # DRAW -----------------------------------------------------------------------------------------------------
            # image
            self.window.blit(source=self.background, dest=self.rect)
            self.window.blit(source=self.logo, dest=self.small_rect)

            # main menu
            for i in range(len(MAIN_MENU_OPT)):
                if i == selected_option:
                    menu_opt_str = f'> {MAIN_MENU_OPT[i]} <'
                    color = NEON_PINK
                else:
                    menu_opt_str = MAIN_MENU_OPT[i]
                    color = NEON_PURPLE

                # menu opt pos
                menu_opt_x = (WIN_WIDTH / 2)
                menu_opt_y = (MENU_HEIGHT + MENU_OPT_SPACING * i)

                # color main
                self.menu_text(
                    font_path=FONT_LARGEFONTS,
                    text_size=MENU_OPT_SIZE,
                    text=menu_opt_str,
                    text_color=color,
                    text_pos=(menu_opt_x, menu_opt_y)
                )

            sign_str = 'Created by: pgmatheus-code'
            sign_x = WIN_WIDTH - 160
            sign_y = WIN_HEIGHT - SIGN_SIZE

            # sign main
            self.menu_text(
                font_path=FONT_SMALLFONTS,
                text_size=SIGN_SIZE,
                text=sign_str,
                text_color=NEON_PINK,
                text_pos=(sign_x, sign_y)
            )
            # draw everything
            pygame.display.flip()

            # EVENTS ---------------------------------------------------------------------------------------------------
            # checking all events
            for event in pygame.event.get():

                # quit events
                if event.type == pygame.QUIT:
                    pygame.quit()  # end pygame
                    sys.exit()  # close window

                if event.type == KEYDOWN:
                    # directional events
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if selected_option > 0:
                            selected_option -= 1
                        else:
                            selected_option = len(MAIN_MENU_OPT) - 1
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if selected_option < len(MAIN_MENU_OPT) - 1:
                            selected_option += 1
                        else:
                            selected_option = 0

                    # enter events
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.stop()
                        return MAIN_MENU_OPT[selected_option]

    def menu_text(self, font_path: str, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: pygame.font.Font = pygame.font.Font(font_path, text_size)

        # shadow
        text_shadow2_surface: Surface = text_font.render(text, True, SHADOW_COLOR).convert_alpha()
        text_shadow2_rect: Rect = text_shadow2_surface.get_rect(
            center=(text_pos[0] - SHADOW_DIRECTION[0], text_pos[1] - SHADOW_DIRECTION[1]))
        self.window.blit(source=text_shadow2_surface, dest=text_shadow2_rect)

        # shadow
        text_shadow_surface: Surface = text_font.render(text, True, SHADOW_COLOR).convert_alpha()
        text_shadow_rect: Rect = text_shadow_surface.get_rect(
            center=(text_pos[0] + SHADOW_DIRECTION[0], text_pos[1] + SHADOW_DIRECTION[1]))
        self.window.blit(source=text_shadow_surface, dest=text_shadow_rect)

        # main
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(center=text_pos)
        self.window.blit(source=text_surface, dest=text_rect)