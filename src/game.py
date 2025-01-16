import pygame
from pygame import mixer

from asset_bank import Asset_bank
import game
import entity
# import objects.Settings as setting
import setting


#=========================================================================================
class Game:

    '''
    Class that manages game basic settings

    '''   

    def __init__(self, width=0, height=0):

        #Screen
        self.width = width
        self.height = height
        self.resolution = None
        self.background = None
        self.background_rect = None
        self.freeze = False
        self.caption =  pygame.display.set_caption("Odissey: Neverending")
        self.icon = pygame.image.load(Asset_bank.Asset_bank.get("UI").get("caption"))
        self.disp_icon = pygame.display.set_icon(self.icon)
        #Audio
        self.sfx_toggle = setting.sfx
        self.bgm_toggle = setting.bgm
        self.difficulty = 5

        self.font = pygame.font.Font('freesansbold.ttf', 32)

        #-------------------------------------------------------------------

    def set_difficulty(self, mode):    # WIP
        self.difficulty = mode
        pass

    def set_level_design(self, level=0, speed=5):
        self.background = Background(level=level, speed=speed)

    def set_resolution(self,width=0, height=0,):
        self.resolution = pygame.display.set_mode((width,height))

    def bgm_play(self):
        mixer.music.load(Asset_bank.Asset_bank.get("Game").get("bgm").get("level_1"))
        mixer.music.set_volume(setting.bgm_volume)
        mixer.music.play(-1)

    def pause_toggle(self):                                          # WIP
        pass
    

#==========================================================================================

class tile():
    """
    Classe paramètrant une tuile de fond  

    """
    def __init__(self, loc = "center", level=0, id=1):
        
        self.loc = loc
        self.level = level
        self.id = id
        self.comment = None
                                                                    # class pygame.Rect
        self.image = pygame.Rect(0, 0, 800, 600)                    # pygame object for storing rectangular coordinates
                                                                    # Rect(left, top, width, height) -> Rect
                                                                    # Rect((left, top), (width, height)) -> Rect
                                                                    # Rect(object) -> Rect

        if self.loc == "center":
            self.id = 1
            self.pos_X, self.pos_Y = 0, 0
        elif self.loc == "upper":
            self.id = 2
            self.pos_X, self.pos_Y = 0, - self.image.height
        elif self.loc == "lower":
            self.id = 3
            self.pos_X, self.pos_Y = 0, self.image.height
        elif self.loc == "left":
            self.id = 4
            self.pos_X, self.pos_Y = -self.image.width, 0
        elif self.loc == "right":
            self.id = 5
            self.pos_X, self.pos_Y = self.image.width, 0
        else: 
            self.pos_X, self.pos_Y = 1000, 1000
        
        #-------------------------------------------------------------------

    def set_tile_image(self, level=0, id=1):
        
        self.level = level
        self.id = id
        self.image = pygame.image.load(Asset_bank.Asset_bank.get("Game").get("background").get(level)[self.id])


#==========================================================================================

class Background():

    """
    Classe paramètrant les images de fond et les paramètres de scrolling 

    """

    def __init__(self, level=0, speed=1 ):

        self.name = "test_name"
        self.current_bg = 4
        
        self.center_tile = tile()
        self.center_tile.set_tile_image(0,self.current_bg)     # remplace tile 1

        self.upper_tile = tile("upper")
        self.upper_tile.set_tile_image(0,self.current_bg)     # remplace tile 2

        self.lower_tile = tile("lower")
        self.lower_tile.set_tile_image(0,self.current_bg)
        
        self.left_tile = tile("left")
        self.left_tile.set_tile_image(0,self.current_bg)
        
        self.right_tile = tile("right")
        self.right_tile.set_tile_image(0,self.current_bg)

        self.rect_background = self.center_tile.image.get_rect()         # create a rect object based on the initial image sizes

        self.moving_speed = speed

        #-------------------------------------------------------------------

    def __repr__(self):
        
        return f"""
                {self.name}
                \ncenter_tile: {self.center_tile.image}\npox_X: {self.center_tile.pos_X}\npos_Y: {self.center_tile.pos_Y}
                \nupper_tile: {self.upper_tile.image}\npox_X: {self.upper_tile.pos_X}\npos_Y: {self.upper_tile.pos_Y}
                \nlower_tile: {self.lower_tile.image}\npox_X: {self.lower_tile.pos_X}\npos_Y: {self.lower_tile.pos_Y}
                \nleft_tile: {self.left_tile.image}\npox_X: {self.left_tile.pos_X}\npos_Y: {self.left_tile.pos_Y}
                \nright_tile: {self.right_tile.image}\npox_X: {self.right_tile.pos_X}\npos_Y: {self.right_tile.pos_Y}
                """
    
    def change_background(self):
        self.current_bg += 1
        if self.current_bg > 5:
            self.current_bg = 0

        if self.scroll_mode == "vertical":
            if self.direction == "desc":
                self.center_tile.set_tile_image(0,self.current_bg)
                self.upper_tile.set_tile_image(0,self.current_bg)


    def update(self, scroll_mode=None, direction=None):    # handles all the movements for backgrounds
        
        self.scroll_mode = scroll_mode                          
        self.direction = direction

        if scroll_mode == "vertical":
        
            if direction == "desc":   

                self.center_tile.pos_Y, self.upper_tile.pos_Y = (tile + self.moving_speed  for tile in (self.center_tile.pos_Y, self.upper_tile.pos_Y))     # applique la vitesse

                self.center_tile.pos_Y = -self.rect_background.height if self.center_tile.pos_Y >= self.rect_background.height else self.center_tile.pos_Y   # raffraichi l'enchainement des tuiles
                self.upper_tile.pos_Y = -self.rect_background.height if self.upper_tile.pos_Y >= self.rect_background.height else self.upper_tile.pos_Y           

            if direction == "asc":
                
                self.center_tile.pos_Y, self.lower_tile.pos_Y = (pos - self.moving_speed  for pos in (self.center_tile.pos_Y, self.lower_tile.pos_Y))

                self.center_tile.pos_Y = self.rect_background.height if self.center_tile.pos_Y <= -self.rect_background.height else self.center_tile.pos_Y   
                self.lower_tile.pos_Y = self.rect_background.height if self.lower_tile.pos_Y <= -self.rect_background.height else self.lower_tile.pos_Y
                
        if scroll_mode == "horizontal":

            if direction == "left":
                
                self.center_tile.pos_X, self.right_tile.pos_X = (pos - self.moving_speed  for pos in (self.center_tile.pos_X, self.right_tile.pos_X))

                self.center_tile.pos_X = self.rect_background.width if self.center_tile.pos_X <= -self.rect_background.width else self.center_tile.pos_X   
                self.right_tile.pos_X = self.rect_background.width if self.right_tile.pos_X <= -self.rect_background.width else self.right_tile.pos_X
    
            if direction == "right":

                self.center_tile.pos_X, self.left_tile.pos_X = (pos + self.moving_speed  for pos in (self.center_tile.pos_X, self.left_tile.pos_X))     # applique la vitesse

                self.center_tile.pos_X = -self.rect_background.width if self.center_tile.pos_X >= self.rect_background.width else self.center_tile.pos_X   # raffraichi l'enchainement des tuiles
                self.left_tile.pos_X = -self.rect_background.width if self.left_tile.pos_X >= self.rect_background.width else self.left_tile.pos_X
    
        if scroll_mode == "centered":
            pass
    

    def render(self):
        
        if self.scroll_mode == "vertical":

            game.game_inst.resolution.blit(self.center_tile.image, (self.center_tile.pos_X, self.center_tile.pos_Y))
            game.game_inst.resolution.blit(self.upper_tile.image, (self.upper_tile.pos_X, self.upper_tile.pos_Y))
            game.game_inst.resolution.blit(self.lower_tile.image, (self.lower_tile.pos_X, self.lower_tile.pos_Y))

        if self.scroll_mode == "horizontal":

            game.game_inst.resolution.blit(self.center_tile.image, (self.center_tile.pos_X, self.center_tile.pos_Y))
            game.game_inst.resolution.blit(self.left_tile.image, (self.left_tile.pos_X, self.left_tile.pos_Y))
            game.game_inst.resolution.blit(self.right_tile.image, (self.right_tile.pos_X, self.right_tile.pos_Y))


#==========================================================================================

    
class Spritesheet():
    def __init__(self, image) :
        self.sheet = image

    def get_image(self, frame, width, height, scale, colour = None):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet,  (0,0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)
        
        return image
    
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

# Intialize a game instance
def set_game(level=0): # level=0, bgm=setting.bgm, sfx=setting.sfx
    global lvl
    global game_inst
    global clock
    global player
    global all_sprites
    global bullets
    global powerups
    global ent_group

    game_inst = Game()
    lvl = level
    game_inst.sfx_toggle = setting.sfx
    game_inst.bgm_toggle = setting.bgm
    game_inst.set_resolution(800,600)                         # create the screen
    game_inst.set_level_design(lvl, speed = 10)                                            
    game_inst.bgm_play() if game.game_inst.bgm_toggle else False              # lance la musique (ou pas)

    clock = pygame.time.Clock()             ## For syncing the FPS

    ## groups
    player = entity.Player()

    all_sprites = pygame.sprite.Group()
    ent_group = pygame.sprite.Group()

    bullets = pygame.sprite.Group()
    powerups = pygame.sprite.Group()

    ent_group.explosion_sounds = []
    for sound in ["explosion_1", "explosion_2"]:
        ent_group.explosion_sounds.append(pygame.mixer.Sound(Asset_bank.Asset_bank.get("Explosions").get("sfx").get(sound)))

    all_sprites.add(player)

    player.player_img.convert()


def gen_meteor_field(count):
    global meteor_images

    meteor_images = []

    meteor_list = Asset_bank.Asset_bank.get("Celestial_objects").get("asteroids").get("meteor_spaceshooter") 

    for file in list(meteor_list.values()):
        meteor_images.append(pygame.image.load(file).convert())
    
    for i in range(count):      ## 8 mobs
                    add_entity("meteor")

def add_entity(event_type):
    ent_dict = {
                    "meteor": entity.Meteor()
                }
    
    choice = ent_dict.get(event_type)
    all_sprites.add(choice)
    ent_group.add(choice)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-