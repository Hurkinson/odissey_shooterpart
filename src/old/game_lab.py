import pygame
import random
from asset_bank import Asset_bank
from pygame import mixer

# Kraken\Odyssey_Neverending\Odyssey_NeverEnding\HKSN

## assets folder

title_game = "Odissey_Neverending"
date = 2023

font_name = pygame.font.match_font('arial')


###############################
## to be placed in "constant.py" later
WIDTH = 800
HEIGHT = 600
FPS = 60
POWERUP_TIME = 5000


# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (40, 200, 80)  #   0, 255, 0
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
###############################






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
        self.sfx_toggle = True
        self.bgm_toggle = True
        self.difficulty = 5
        # score
        # self.score_value = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        # self.textX = 10
        # self.testY = 10
        # Font
        # self.over_font = pygame.font.Font('freesansbold.ttf', 64)

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
        mixer.music.set_volume(bgm_volume)
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

            game.resolution.blit(self.center_tile.image, (self.center_tile.pos_X, self.center_tile.pos_Y))
            game.resolution.blit(self.upper_tile.image, (self.upper_tile.pos_X, self.upper_tile.pos_Y))
            game.resolution.blit(self.lower_tile.image, (self.lower_tile.pos_X, self.lower_tile.pos_Y))

        if self.scroll_mode == "horizontal":

            game.resolution.blit(self.center_tile.image, (self.center_tile.pos_X, self.center_tile.pos_Y))
            game.resolution.blit(self.left_tile.image, (self.left_tile.pos_X, self.left_tile.pos_Y))
            game.resolution.blit(self.right_tile.image, (self.right_tile.pos_X, self.right_tile.pos_Y))


#==========================================================================================


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.player_img = pygame.image.load(Asset_bank.Asset_bank.get("Player").get("sprite").get("red_squad").get("frigate")).convert()
        self.image = pygame.transform.scale(self.player_img, (100, 80))    # (50, 38)
        self.player_die_sound = pygame.mixer.Sound(Asset_bank.Asset_bank.get("Explosions").get("sfx").get("explosion_3"))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 25
        self.speed = 6
        self.posX_change = 0 
        self.posY_change = 0
        self.score = 0
        self.shield = 100
        self.current_weapon = "blaster"
        self.current_weapon_rof = 250
        self.current_bullet_alpha = 255
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_timer = pygame.time.get_ticks()

    def update(self):
        ## unhide 
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 30

        self.posX_change = 0                    ## makes the player static in the screen by default. 
        self.posY_change = 0

        ## will give back a list of the keys which happen to be pressed down at that moment
        keystate = pygame.key.get_pressed()  

         #Fire weapons by holding spacebar
        if keystate[pygame.K_SPACE]:
            self.shoot()   

        if keystate[pygame.K_LEFT]:
            self.posX_change = -(self.speed)
        if keystate[pygame.K_RIGHT]:
            self.posX_change = self.speed
        if keystate[pygame.K_UP]:
            self.posY_change = -(self.speed)
        if keystate[pygame.K_DOWN]:
            self.posY_change = self.speed
        
        ## check for the borders at the left and right
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        self.rect.x += self.posX_change
        self.rect.y += self.posY_change

    def shoot(self):
        
        now = pygame.time.get_ticks()

        if self.current_weapon == "blaster":

            muzzle = Weapon_muzzle(self.rect.centerx, self.rect.top)
            muzzle.set_muzzle_img()

            blast_ammo = Weapon(self.rect.centerx, self.rect.top)
            blast_ammo.set_weapon(self.current_weapon) 

            nose = blast_ammo 

            wing_right_1 = Weapon(self.rect.right - 20, self.rect.centery)
            wing_right_1.set_weapon(self.current_weapon)

            wing_left_1 = Weapon(self.rect.left + 20, self.rect.centery)
            wing_left_1.set_weapon(self.current_weapon)

            player.current_weapon_rof = blast_ammo.fire_rate

            if now - self.last_shot > player.current_weapon_rof:

                self.last_shot = now

                if self.power == 1:
                    
                    all_sprites.add(nose, muzzle)
                    bullets.add(nose)

                    blast_ammo.shooting_sound.play() if game.sfx_toggle else False

                if self.power == 2:

                    all_sprites.add(wing_right_1, wing_left_1)
                    bullets.add(wing_right_1, wing_left_1)
        
                    blast_ammo.shooting_sound.play() if game.sfx_toggle else False

                if self.power >= 3:
    
                    all_sprites.add(nose, wing_right_1, wing_left_1)
                    bullets.add(nose, wing_right_1, wing_left_1)

                    blast_ammo.shooting_sound.play() if game.sfx_toggle else False
            
        if self.current_weapon == "missile":

            rocket_ammo = Weapon(self.rect.centerx, self.rect.top)
            rocket_ammo.set_weapon(self.current_weapon)

            wing_right_1 = Weapon(self.rect.right - 20, self.rect.centery)
            wing_right_1.set_weapon(self.current_weapon)
            wing_right_2 = Weapon(self.rect.right , self.rect.centery)
            wing_right_2.set_weapon(self.current_weapon)
            wing_right_3 = Weapon(self.rect.right + 20, self.rect.centery)
            wing_right_3.set_weapon(self.current_weapon)

            wing_left_1 = Weapon(self.rect.left + 20, self.rect.centery)
            wing_left_1.set_weapon(self.current_weapon)
            wing_left_2 = Weapon(self.rect.left , self.rect.centery)
            wing_left_2.set_weapon(self.current_weapon)
            wing_left_3 = Weapon(self.rect.left - 20, self.rect.centery)
            wing_left_3.set_weapon(self.current_weapon)

            player.current_weapon_rof = rocket_ammo.fire_rate

            if self.power == 1:

                if now - self.last_shot > player.current_weapon_rof:

                    self.last_shot = now

                    all_sprites.add(wing_right_1, wing_left_1)
                    bullets.add(wing_right_1, wing_left_1)

                    rocket_ammo.shooting_sound.play() if game.sfx_toggle else False

            if self.power == 2:
                player.current_weapon_rof /= 2
                    
                if now - self.last_shot > player.current_weapon_rof:

                    self.last_shot = now

                    all_sprites.add(wing_right_1, wing_left_1, wing_right_2, wing_left_2)
                    bullets.add(wing_right_1, wing_left_1, wing_right_2, wing_left_2)

                    rocket_ammo.shooting_sound.play() if game.sfx_toggle else False

            if self.power >= 3:
                    
                player.current_weapon_rof /= 4
                    
                if now - self.last_shot > player.current_weapon_rof:

                    self.last_shot = now

                    all_sprites.add(wing_right_1, wing_left_1, wing_right_2, wing_left_2, wing_right_3, wing_left_3)                    
                    bullets.add(wing_right_1, wing_left_1, wing_right_2, wing_left_2, wing_right_3, wing_left_3)

                    rocket_ammo.shooting_sound.play() if game.sfx_toggle else False
            
        if self.current_weapon == "machine_gun":

            gun_ammo = Weapon(self.rect.centerx, self.rect.top)
            gun_ammo.set_weapon(self.current_weapon) 

            nose = gun_ammo 

            wing_right_1 = Weapon(self.rect.right - 20, self.rect.centery)
            wing_right_1.set_weapon(self.current_weapon)

            wing_left_1 = Weapon(self.rect.left + 20, self.rect.centery)
            wing_left_1.set_weapon(self.current_weapon)

            player.current_weapon_rof = gun_ammo.fire_rate

            if now - self.last_shot > player.current_weapon_rof:

                self.last_shot = now

                if self.power == 1:

                    all_sprites.add(nose)
                    bullets.add(nose)

                    gun_ammo.shooting_sound.play() if game.sfx_toggle else False

                if self.power == 2:

                    all_sprites.add(wing_right_1, wing_left_1)
                    bullets.add(wing_right_1, wing_left_1)
        
                    gun_ammo.shooting_sound.play() if game.sfx_toggle else False

                if self.power >= 3:
    
                    all_sprites.add(nose, wing_right_1, wing_left_1)
                    bullets.add(nose, wing_right_1, wing_left_1)

                    gun_ammo.shooting_sound.play() if game.sfx_toggle else False
                
    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)

#==========================================================================================

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

## defines the sprite for weapons

class Weapon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.n_iter = 0
        self.pos_X = x
        self.pos_Y = y
        
         

    def set_weapon(self, wpn_name = "blaster"):

        self.weapon_specs = {
                        "blaster":
                        {
                            "speedy": -20,
                            "damage": 20,
                            "fire_rate": 250
                        },
                        "missile":
                        {
                            "speedy": 5,
                            "damage": 100,
                            "fire_rate": 800
                        },
                        "machine_gun":
                        {
                            "speedy": -20,
                            "damage": 20,
                            "fire_rate": 150
                        }
        }
               
        self.wpn_name = wpn_name
        self.image = pygame.image.load(Asset_bank.Asset_bank.get("Weapon").get(self.wpn_name).get("blast_sprt")).convert_alpha()
        self.image.set_colorkey(BLACK)

        if self.wpn_name == "machine_gun":
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(player.current_bullet_alpha)

        self.rect = self.image.get_rect()
        self.rect.bottom = self.pos_Y 
        self.rect.centerx = self.pos_X
        self.shooting_sound = pygame.mixer.Sound(Asset_bank.Asset_bank.get("Weapon").get(self.wpn_name).get("sfx_blast"))        
        self.shooting_sound.set_volume(sfx_volume)
        self.speedy = self.weapon_specs.get(self.wpn_name).get("speedy")
        self.damage = self.weapon_specs.get(self.wpn_name).get("damage")
        self.fire_rate = self.weapon_specs.get(self.wpn_name).get("fire_rate")

    def update(self):
        self.n_iter += 1
        self.behaviour_manager()
        self.rect.y += self.speedy
        
        if self.rect.bottom < 0:
            self.kill()  

    def behaviour_manager(self):
        if self.wpn_name == "missile":
            self.speedy = self.missile_thruster(self.n_iter)

    def missile_thruster(self, n_iter):
        if n_iter <= 15:
            return 5
        else :
            return -25

class Weapon_muzzle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.n_iter = 0
        self.pos_X = x
        self.pos_Y = y
        self.frame_list = []
        

    def set_muzzle_img(self):
        self.muzzlesprt_sprtsheet_src = pygame.image.load(Asset_bank.Asset_bank.get("Weapon").get(player.current_weapon).get("muzzle_sprt")).convert_alpha()
        self.muzzlesprt_sprtsheet = Spritesheet(self.muzzlesprt_sprtsheet_src)
        for i in range(4):
            self.frame_list.append(self.muzzlesprt_sprtsheet.get_image(i, 8, 8, 1))
        self.image = self.frame_list[0]
        self.rect = self.image.get_rect()

    def update(self):
        if self.n_iter < len(self.frame_list):
            self.n_iter += 1
        else:
            self.n_iter = 0
    
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


class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)

        powerup_images = {}
        powerup_images['shield'] = pygame.image.load(Asset_bank.Asset_bank.get("Powerup").get("sprite").get("shield_pwrup")).convert()
        powerup_images['gun'] = pygame.image.load(Asset_bank.Asset_bank.get("Powerup").get("sprite").get("weapon_pwrup")).convert()
        self.type = random.choice(['shield', 'gun'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()                         # kill the sprite after it moves over the bottom border

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteor_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width *.90 / 2)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedy = random.randrange(5, 20)        ## for randomizing the speed of the Mob

        ## randomize the movements a little more 
        self.speedx = random.randrange(-3, 3)

        ## adding rotation to the mob element
        self.rotation = 0
        self.rotation_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()  ## time when the rotation has to happen
        
    def rotate(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.last_update > 50: # in milliseconds
            self.last_update = time_now
            self.rotation = (self.rotation + self.rotation_speed) % 360 
            new_image = pygame.transform.rotate(self.image_orig, self.rotation)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        ## now what if the mob element goes out of the screen

        if (self.rect.top > HEIGHT + 10) or (self.rect.left < -25) or (self.rect.right > WIDTH + 20):
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)        ## for randomizing the speed of the Mob

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)

        explosion_anim = {}
        explosion_anim['lg'] = []
        explosion_anim['sm'] = []
        explosion_anim['player'] = []

        for i in range(9):
            filename = "default_explosion0{}".format(i)
            img = pygame.image.load(Asset_bank.Asset_bank.get("Explosions").get("sprites").get(filename)).convert()
            img.set_colorkey(BLACK)

            ## resize the explosion
            img_lg = pygame.transform.scale(img, (75, 75))
            explosion_anim['lg'].append(img_lg)
            img_sm = pygame.transform.scale(img, (32, 32))
            explosion_anim['sm'].append(img_sm)

            ## player explosion
            filename = "player_explosion0{}".format(i)
            img = pygame.image.load(Asset_bank.Asset_bank.get("Explosions").get("sprites").get(filename)).convert()
            img.set_colorkey(BLACK)
            explosion_anim['player'].append(img)

        self.explosion_anim = explosion_anim
        self.size = size
        self.image = self.explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0 
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center



###################################################

# Intialize a game instance
def set_game(level=0, bgm=True, sfx=True):
    global lvl
    global game

    game = Game()
    lvl = level
    game.sfx_toggle = sfx
    game.bgm_toggle = bgm
    game.set_resolution(800,600)                         # create the screen
    game.set_level_design(lvl, speed = 10)                                            
    game.bgm_play() if game.bgm_toggle else False              # lance la musique (ou pas)

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)       ## True denotes the font to be anti-aliased 
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_shield_bar(surf, x, y, pct):
    BAR_LENGTH = 80
    BAR_HEIGHT = 15
    pct = max(pct, 0) 
    
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)


def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect= img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

def main_menu():

    pygame.mixer.music.load(Asset_bank.Asset_bank.get("Game").get("bgm").get("main_menu"))
    pygame.mixer.music.play(-1) if bgm_sfx else False

    title = pygame.image.load(Asset_bank.Asset_bank.get("Game").get("menu").get("main_menu")).convert()
    title = pygame.transform.scale(title, (WIDTH, HEIGHT), game.resolution)

    game.resolution.blit(title, (0,0))
    pygame.display.update()

    while True:

        ev = pygame.event.poll()

        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                break
            elif ev.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

        elif ev.type == pygame.QUIT:
                pygame.quit()
                quit() 
        else:
            draw_text(game.resolution, "Press Enter to start", 30, WIDTH/2, HEIGHT/2+40)
            draw_text(game.resolution, "Esc to quit", 30, WIDTH/2, (HEIGHT/2)+80)
            draw_text(game.resolution, "V 1.1", 15, WIDTH - 30, HEIGHT - 20)
            draw_text(game.resolution, f"(c)Copyright {date} - Guillaume Morin-Duponchelle - Vivien Schneider", 15, 200, HEIGHT - 20)

            pygame.display.update()

    game.resolution.fill(BLACK)
    draw_text(game.resolution, "GO !", 40, WIDTH/2, HEIGHT/2)

    ready = pygame.mixer.Sound(Asset_bank.Asset_bank.get("Game").get("sfx").get("get_ready"))
    ready.play() if game.sfx_toggle else False

    pygame.time.wait(2000)

    go = pygame.mixer.Sound(Asset_bank.Asset_bank.get("Game").get("sfx").get("go"))
    go.play() if game.sfx_toggle else False
    
    pygame.display.update()

def ranking_ladder():
    pass

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
                    "meteor": Meteor()
                }
    
    entity = ent_dict.get(event_type)
    all_sprites.add(entity)
    ent_group.add(entity)
    



#============================================================================================
#======  PPPPPP LL         AA   YY    YY  ##  ##  ##  =======================================
#======  PP  PP LL        AAAA   YY  YY   ##  ##  ##  =======================================
#======  PPPPPP LL       AA  AA   YYYY    ##  ##  ##  =======================================
#======  PP     LL      AAAAAAAA   YY     ##  ##  ##  =======================================
#======  PP     LL     AA      AA  YY                 =======================================
#======  PP     LLLLL AA        AA YY     ##  ##  ##  =======================================
#============================================================================================

###############################

pygame.init()

clock = pygame.time.Clock()             ## For syncing the FPS

###############################
bgm_sfx = True
 
# volume_glob = 1
bgm_volume = 0.2 
sfx_volume = 0.05

running = True
menu_display = True

set_game(level=0, bgm=bgm_sfx, sfx=bgm_sfx)
player = Player()

## groups
all_sprites = pygame.sprite.Group()

ent_group = pygame.sprite.Group()
ent_group.explosion_sounds = []
for sound in ["explosion_1", "explosion_2"]:
    ent_group.explosion_sounds.append(pygame.mixer.Sound(Asset_bank.Asset_bank.get("Explosions").get("sfx").get(sound)))

bullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()

all_sprites.add(player)
 
###################################################
## Game loop

while running:  

    #1 Main menu
    if menu_display:

        main_menu()
        pygame.time.wait(1000)
        pygame.mixer.music.stop()

        game.bgm_play() if game.bgm_toggle else False       
        menu_display = False

    game.background.update("vertical","desc")   # "vertical","desc"  "horizontal","left"
    game.background.render()

    #2 Event check
    event_list = pygame.event.get()             
    
    for event in event_list:        
       
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:    # Press ESC to exit game
                running = False

            if event.key == pygame.K_1:        
                player.current_weapon = "blaster"
                draw_text(game.resolution, "Blaster selected", 40, player.rect.x - 50 , player.rect.y )

            if event.key == pygame.K_2:
                player.current_weapon = "missile"
                draw_text(game.resolution, "Missiles selected", 40, player.rect.x - 50 , player.rect.y )

            if event.key == pygame.K_3:
                player.current_weapon = "machine_gun"
                draw_text(game.resolution, "Machine_gun selected", 40, player.rect.x - 50 , player.rect.y )

            if event.key == pygame.K_p:
                if player.power <= 2:
                    player.power += 1 
                elif player.power >= 3:
                    player.power = 1

            if event.key == pygame.K_a:         # swap background
                game.background.change_background()
            if event.key == pygame.K_m:         # incoming asteroids field
                gen_meteor_field(8)
    
    #2 Update
    all_sprites.update()
    all_sprites.draw(game.resolution)

    #3 Collisions

    # Ent_group x bullets
    hits = pygame.sprite.groupcollide(ent_group, bullets, True, True)
    for hit in hits:
        player.score += 50 - hit.radius         ## give different scores for hitting big and small metoers
        random.choice(ent_group.explosion_sounds).play() if game.sfx_toggle else False
        
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)

        if random.random() > 0.9:
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)

    # Player x Ent_group
    hits = pygame.sprite.spritecollide(player, ent_group, True, pygame.sprite.collide_circle)        ## gives back a list, True makes the mob element disappear
    for hit in hits:
        player.shield -= hit.radius * 2
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        # newmob()
        if player.shield <= 0: 
            player.player_die_sound.play() if game.sfx_toggle else False
            death_explosion = Explosion(player.rect.center, 'player')
            all_sprites.add(death_explosion)
            # running = False     ## GAME OVER 3:D
            player.hide()
            player.lives -= 1
            player.shield = 100

    # Player x powerup
    hits = pygame.sprite.spritecollide(player, powerups, True)
    for hit in hits:
        if hit.type == 'shield':
            player.shield += random.randrange(10, 30)
            if player.shield >= 100:
                player.shield = 100
        if hit.type == 'gun':
            player.powerup()

    #4 Game over
    if player.lives == 0 and not death_explosion.alive():
        # running = False
        menu_display = True
        player.lives = 3
        player.score = 0
        player.shield = 100
        pygame.display.update()


    # draw UI
    player_mini_img = pygame.transform.scale(player.player_img, (40,40))
    player_mini_img.set_colorkey(BLACK)

    if player.shield < 100:
        draw_shield_bar(game.resolution, player.rect.x + 10 , player.rect.y + 80, player.shield)

    draw_text(game.resolution, str(player.score), 30, 60, 45)
    draw_text(game.resolution, "Press SPACE for shoot", 10, 63, 85)
    draw_text(game.resolution, "Press M for meteor shower", 10, 70, 100)
    draw_text(game.resolution, "Press P  for weapon powerup", 10, 75, 115)
    draw_text(game.resolution, "Press Esc for quit", 10, 52, 130)

    draw_lives(game.resolution, 10 , 10, player.lives, player_mini_img)

    pygame.display.flip()      

    clock.tick(FPS)                               # will make the loop run at the same speed all the time 

pygame.quit()