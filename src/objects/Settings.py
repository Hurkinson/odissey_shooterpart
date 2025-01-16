import pygame
from pygame import mixer
import os

mixer.init()


title_game = "Odissey_Neverending"
date = 2023

font_name = pygame.font.match_font('arial')

bgm_sfx = False

bgm = True
bgm_volume = 0.2 

sfx = True
sfx_volume = 0.05

running = True
menu_display = True

###############################
        # COLORS
##############################
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (40, 200, 80)  #   0, 255, 0
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
###############################
        # SCREEN
###############################
WIDTH = 800
HALF_WIDTH = WIDTH / 2
HEIGHT = 600
HALF_HEIGHT = HEIGHT / 2

RESOLUTION = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60
###############################
        # TITLES
#############################

TITLE = None
# Pygame error : font not initialized
# font = pygame.font.Font('freesansbold.ttf', 32)
FONT_NAME = pygame.font.match_font('arial')
DATE = 2023
POWERUP_TIME = 5000
#############################
        # GAMEPLAY
#############################
        
difficulty = 5
        # AUDIO
SFX_TOGGLE = True
BGM_TOGGLE = True
        
##############################
#       PATHS
##############################
# Default Player spaceship
PLAYER = ['Player']
# For player spaceship
SHIP = ['sprites','player','red_squad']
# For explosion sound
SFX = ['Sounds','sfx','Fx']
SFX_SHOOT = ['Sounds','sfx','Shoot']
# For enemy (metors)
ENEMY = ['sprites', 'Enemy']
# For animation skills / weapon sprites
BULLET = ['sprites', 'Weapon']
# Powerup Sprites
POWERUP = ['sprites','powerup']
# Explosion sprites
EXPLO = ['sprites', 'explosions']
EXPLO_SFX = ['sounds', 'sfx', 'fx']
# UI Elements
UI = ['ui']

# Space Background
SPACE_BACK = ['maps','Space_Background']
# Sounds for fight
MUSIC = ['sounds','bgm','wav']

##############################
        
def handle_path(folders : list, file, debugg = True):
        '''
        Construction fonction to manage file path
        :params:
        - folder : str : subfile name
        - file : str : file name with extension
        '''
        parts = [str(folder) for folder in folders] + [str(file)]
        result = os.path.join("..", *parts)
        if debugg == True :
            print(f'Path created for {file} : ', result )
            return result        
 

