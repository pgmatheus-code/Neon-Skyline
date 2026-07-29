#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Rect, Surface
from pygame.font import Font
from code.const import WIN_WIDTH, WIN_HEIGHT, LOGO_WIDTH, LOGO_HEIGHT, SIGN_SIZE, NEON_SALMON, MAIN_MENU_OPT, \
    MENU_OPT_SIZE, NEON_PINK, FONT_SMALLFONTS, FONT_LARGEFONTS


class Menu:
    def __init__(self, window):
        self.window = window

        # background
        self.background = pygame.image.load('./assets/sprites/scenery/main_menu_background.png')
        self.background = pygame.transform.scale(self.background, self.window.get_size())
        self.rect = self.background.get_rect(topleft=(0, 0))

        # background
        self.logo = pygame.image.load('./assets/sprites/logo.png')
        self.logo = pygame.transform.scale(self.logo, size=(LOGO_WIDTH, LOGO_HEIGHT))
        self.small_rect = self.logo.get_rect(
            topleft=((WIN_WIDTH / 2) - (LOGO_WIDTH / 2), (WIN_HEIGHT / 3.3) - (LOGO_HEIGHT / 2)))

    def run(self, ):
        # music
        pygame.mixer.music.load('./assets/sounds/main_menu.mp3')
        pygame.mixer.music.play(-1) # minus one for loop


        while True:
            # image
            self.window.blit(source=self.background, dest=self.rect)
            self.window.blit(source=self.logo, dest=self.small_rect)

            # main menu
            for i in range(len(MAIN_MENU_OPT)):
                self.menu_text_custom_font(FONT_LARGEFONTS, MENU_OPT_SIZE, MAIN_MENU_OPT[i], NEON_SALMON, (WIN_WIDTH/2, 250 + 35 * i) )

            # sign
            self.menu_text_custom_font(
                font_path=FONT_SMALLFONTS, text_size=SIGN_SIZE, text='Created by: pgmatheus-code', text_color=NEON_SALMON,
                text_center_pos=(WIN_WIDTH - 160, WIN_HEIGHT - SIGN_SIZE)
            )

            # draw everything
            pygame.display.flip()

            # checking all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # end pygame
                    quit()  # close window


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Comic Sans MS', size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(center=text_center_pos)
        self.window.blit(source=text_surface, dest=text_rect)

    def menu_text_custom_font(self, font_path: str, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Load font from given path
        text_font: pygame.font.Font = pygame.font.Font(font_path, text_size)

        # Render text
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()

        # Center text
        text_rect: Rect = text_surface.get_rect(center=text_center_pos)

        # Draw text on window
        self.window.blit(source=text_surface, dest=text_rect)