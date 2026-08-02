import sys
from datetime import datetime

import pygame
from code.DBProxy import DBProxy
from pygame import Surface, Rect
from code.Const import LOGO_WIDTH, LOGO_HEIGHT, WIN_WIDTH, WIN_HEIGHT, SHADOW_COLOR, SHADOW_DIRECTION, FONT_LARGEFONTS, \
    MENU_OPT_SIZE, NEON_PINK, SCORE_POS, MAIN_MENU_OPT, NEON_SALMON, DIGIT_LIMIT, FONT_SMALLFONTS


class Scoreboard:
    def __init__(self, window):
        self.window = window

        # background
        self.background = pygame.image.load('./assets/sprites/background/score_background.png').convert_alpha()
        self.background = pygame.transform.scale(self.background, self.window.get_size())
        self.rect = self.background.get_rect(topleft=(0, 0))

    def save(self, game_mode: str, player_score: list[int]):
        # music
        pygame.mixer.music.load('./assets/sounds/endgame.mp3')
        pygame.mixer.music.play(-1)  # minus one for loop
        db_proxy = DBProxy('DBScore')
        winner_name = ''

        while True:
            # DRAW -----------------------------------------------------------------------------------------------------
            # image
            self.window.blit(source=self.background, dest=self.rect)

            title_text = 'SCOREBOARD'
            subtitle_text = ''
            score=''

            if game_mode == MAIN_MENU_OPT[0]: # 1P
                title_text = 'GAME OVER (One Player)'
                score = player_score[0]
                subtitle_text = f'Enter player 1 name <{DIGIT_LIMIT} digits>:'

            if game_mode == MAIN_MENU_OPT[1]:  # 2P VS
                title_text = 'GAME OVER (2 Players VS)'

                if player_score[0] > player_score[1]:
                    score = player_score[0]
                    subtitle_text = f'Enter player 1 name <{DIGIT_LIMIT} digits>:'
                elif player_score[0] < player_score[1]:
                    score = player_score[1]
                    subtitle_text = f'Enter player 2 name <{DIGIT_LIMIT} digits>:'
                elif player_score[0] == player_score[1]:
                    score = player_score[1]
                    subtitle_text = f'DRAW!! Enter team name <{DIGIT_LIMIT} digits>:'

            if game_mode == MAIN_MENU_OPT[2]:  # 2P COOP
                title_text = 'GAME OVER (2 Players COOP)'
                score = (player_score[0] + player_score[1]) / 2 # average of both
                subtitle_text = f'Enter team name <{DIGIT_LIMIT} digits>s:'

            title_text += f' - {score} PTS'

            # title
            self.scoreboard_text(
                font_path=FONT_LARGEFONTS,
                text_size=45,
                text=title_text,
                text_color=NEON_PINK,
                text_pos=SCORE_POS['Title']
            )

            # subtitle
            self.scoreboard_text(
                font_path=FONT_LARGEFONTS,
                text_size=30,
                text=subtitle_text,
                text_color=NEON_PINK,
                text_pos=SCORE_POS['Subtitle']
            )

            for event in pygame.event.get():
                if event.type == pygame.QUIT: # standard quit event (to avoid window freeze)
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN: # read input
                    if event.key == pygame.K_RETURN:
                        if 0 < len(winner_name) <= DIGIT_LIMIT:
                            db_proxy.save({'name': winner_name,'score': score, 'date': get_formatted_date()})
                            self.show()
                            return
                    elif event.key == pygame.K_BACKSPACE:
                        if len(winner_name) > 0:
                            winner_name = winner_name[:-1]
                    elif len(winner_name) < DIGIT_LIMIT:
                        winner_name += event.unicode

            # input text
            self.scoreboard_text(
                font_path=FONT_LARGEFONTS,
                text_size=50,
                text=winner_name,
                text_color=NEON_SALMON,
                text_pos=SCORE_POS['Input']
            )

            # update display
            pygame.display.flip()

    def show(self):
        # music
        pygame.mixer.music.load('./assets/sounds/endgame.mp3')
        pygame.mixer.music.play(-1)  # minus one for loop
        self.window.blit(source=self.background, dest=self.rect)


        # title
        self.scoreboard_text(
            font_path=FONT_LARGEFONTS,
            text_size=50,
            text='SCOREBOARD',
            text_color=NEON_PINK,
            text_pos=SCORE_POS['Title']
        )

        # title
        self.scoreboard_text(
            font_path=FONT_LARGEFONTS,
            text_size=30,
            text='NAME             SCORE            DATE          ',
            text_color=NEON_PINK,
            text_pos=SCORE_POS['Label']
        )

        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()

        for player_score in list_score:
            id_, name, score, date = player_score

            formatted_name = name + ' ' * (DIGIT_LIMIT - len(name))

            self.scoreboard_text(
                font_path=FONT_SMALLFONTS,
                text_size=20,
                text=f'{formatted_name}          {score:05d} PTS          {date}',
                text_color=NEON_SALMON,
                text_pos=SCORE_POS[list_score.index(player_score)]
            )

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # standard quit event (to avoid window freeze)
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN: # read input
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                        return

            # update display
            pygame.display.flip()

    def scoreboard_text(self, font_path: str, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: pygame.font.Font = pygame.font.Font(font_path, text_size)

        # shadow
        text_shadow_surface: Surface = text_font.render(text, True, SHADOW_COLOR).convert_alpha()
        text_shadow_rect: Rect = text_shadow_surface.get_rect(
            center=(text_pos[0] + SHADOW_DIRECTION[0], text_pos[1] + SHADOW_DIRECTION[1]))
        self.window.blit(source=text_shadow_surface, dest=text_shadow_rect)

        # main
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(center=text_pos)
        self.window.blit(source=text_surface, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%Y")
    return f'{current_time} {current_date}'