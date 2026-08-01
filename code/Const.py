# window size
import pygame

WIN_WIDTH = 800
WIN_HEIGHT = 420

# logo size
LOGO_WIDTH = 400
LOGO_HEIGHT = 210

# font file
FONT_SMALLFONTS = './assets/fonts/BULKYPIX.TTF'
FONT_LARGEFONTS = './assets/fonts/acknowtt.ttf'

# color
NEON_SALMON = (255,231,189)
NEON_PURPLE = (100,6,189)
NEON_PINK = (255,20,189)
NEON_CYAN = (96,249,253)

# main menu
MENU_HEIGHT = 235
MENU_OPT_SIZE = 55
MENU_OPT_SPACING = 30
SIGN_SIZE = 15
SHADOW_COLOR = NEON_CYAN
SHADOW_DIRECTION = (1, 1)

MAIN_MENU_OPT = (
    'NEW GAME - 1P',
    'NEW GAME - 2P (VS)',
    'NEW GAME - 2P (COOP)',
    'SCOREBOARD',
    'QUIT GAME'
)

# background layers speed
BACKGROUND_SPEED = {
    'layer1': 0,
    'layer2': 0.5,
    'layer3': 1,
    'layer4': 1.5,
    'layer5': 2,
    'layer6': 2.5,
    'layer7': 3,
    'layer8': 3.5,
}

# entity default health
ENTITY_DEFAULT_HEALTH = {
    'player': 300,
    'foe_small_1': 50,
    'foe_small_2': 50,
    'foe_medium_1': 100,
    'foe_medium_2': 100,
    'foe_medium_3': 100,
    'foe_large_1': 150,
    'foe_large_2': 150,
    'foe_large_3': 150,
    'shot' : 1,
}

# foes
FOE_SPAWNING_INTERVAL = 3000
FOE_EVENT = pygame.USEREVENT + 1
FOE_SPEED_MULTIPLIER = 2
FOE_SHIP_DICT = {
    'small_1' : 3.5,
    'small_2' : 3.5,
    'medium_1' : 2.5,
    'medium_2': 2.5,
    'medium_3': 2.5,
    'large_1': 2,
    'large_2': 2,
    'large_3' : 2
}

# global level settings
LEVEL_FPS = 60
STANDARD_TIMEOUT = 20000

# player defaults
PLAYER_SPEED = 5

# key binding
KEY_UP =\
    {
        'player1': pygame.K_w,
        'player2': pygame.K_UP
    }

KEY_DOWN =\
    {
        'player1': pygame.K_s,
        'player2': pygame.K_DOWN
    }

KEY_LEFT =\
    {
        'player1': pygame.K_a,
        'player2': pygame.K_LEFT
    }
KEY_RIGHT =\
    {
        'player1': pygame.K_d,
        'player2': pygame.K_RIGHT
    }
KEY_SHOOT =\
    {
        'player1': pygame.K_SPACE,
        'player2': pygame.K_KP_PLUS
    }