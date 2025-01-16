# setting

import pygame



title_game = "Odissey_Neverending"
date = 2023

font_name = pygame.font.match_font('arial')

WIDTH = 800
HEIGHT = 600
FPS = 60
POWERUP_TIME = 5000

###############################

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (40, 200, 80)  #   0, 255, 0
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

###############################

bgm_sfx = False

bgm = True
sfx = True

# volume_glob = 1
bgm_volume = 0.2 
sfx_volume = 0.05

running = True
menu_display = True