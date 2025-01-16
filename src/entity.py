# entity

import pygame
import random

from asset_bank import Asset_bank
import game
# import objects.Settings as setting
import setting


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.player_img = pygame.image.load(Asset_bank.Asset_bank.get("Player").get("sprite").get("red_squad").get("frigate")) # .convert()
        self.image = pygame.transform.scale(self.player_img, (100, 80))    # (50, 38)
        self.player_mini_img = pygame.transform.scale(self.player_img, (40,40))
        self.player_mini_img.set_colorkey(setting.BLACK)
        self.player_die_sound = pygame.mixer.Sound(Asset_bank.Asset_bank.get("Explosions").get("sfx").get("explosion_3"))
        self.image.set_colorkey(setting.BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = setting.WIDTH / 2
        self.rect.bottom = setting.HEIGHT - 25
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
            # self.rect.centerx = setting.WIDTH / 2
            # self.rect.bottom = setting.HEIGHT - 30

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
        if self.rect.right > setting.WIDTH:
            self.rect.right = setting.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > setting.HEIGHT:
            self.rect.bottom = setting.HEIGHT

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

            game.player.current_weapon_rof = blast_ammo.fire_rate

            if now - self.last_shot > game.player.current_weapon_rof:

                self.last_shot = now

                if self.power == 1:
                    
                    game.all_sprites.add(nose, muzzle)
                    game.bullets.add(nose)

                    blast_ammo.shooting_sound.play() if game.game_inst.sfx_toggle else False

                if self.power == 2:

                    game.all_sprites.add(wing_right_1, wing_left_1)
                    game.bullets.add(wing_right_1, wing_left_1)
        
                    blast_ammo.shooting_sound.play() if game.game_inst.sfx_toggle else False

                if self.power >= 3:
    
                    game.all_sprites.add(nose, wing_right_1, wing_left_1)
                    game.bullets.add(nose, wing_right_1, wing_left_1)

                    blast_ammo.shooting_sound.play() if game.game_inst.sfx_toggle else False
            
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

            game.player.current_weapon_rof = rocket_ammo.fire_rate

            if self.power == 1:

                if now - self.last_shot > game.player.current_weapon_rof:

                    self.last_shot = now

                    game.all_sprites.add(wing_right_1, wing_left_1)
                    game.bullets.add(wing_right_1, wing_left_1)

                    rocket_ammo.shooting_sound.play() if game.game_inst.sfx_toggle else False

            if self.power == 2:
                game.player.current_weapon_rof /= 2
                    
                if now - self.last_shot > game.player.current_weapon_rof:

                    self.last_shot = now

                    game.all_sprites.add(wing_right_1, wing_left_1, wing_right_2, wing_left_2)
                    game.bullets.add(wing_right_1, wing_left_1, wing_right_2, wing_left_2)

                    rocket_ammo.shooting_sound.play() if game.game_inst.sfx_toggle else False

            if self.power >= 3:
                    
                game.player.current_weapon_rof /= 4
                    
                if now - self.last_shot > game.player.current_weapon_rof:

                    self.last_shot = now

                    game.all_sprites.add(wing_right_1, wing_left_1, wing_right_2, wing_left_2, wing_right_3, wing_left_3)                    
                    game.bullets.add(wing_right_1, wing_left_1, wing_right_2, wing_left_2, wing_right_3, wing_left_3)

                    rocket_ammo.shooting_sound.play() if game.game_inst.sfx_toggle else False
            
        if self.current_weapon == "machine_gun":

            gun_ammo = Weapon(self.rect.centerx, self.rect.top)
            gun_ammo.set_weapon(self.current_weapon) 

            nose = gun_ammo 

            wing_right_1 = Weapon(self.rect.right - 20, self.rect.centery)
            wing_right_1.set_weapon(self.current_weapon)

            wing_left_1 = Weapon(self.rect.left + 20, self.rect.centery)
            wing_left_1.set_weapon(self.current_weapon)

            game.player.current_weapon_rof = gun_ammo.fire_rate

            if now - self.last_shot > game.player.current_weapon_rof:

                self.last_shot = now

                if self.power == 1:

                    game.all_sprites.add(nose)
                    game.bullets.add(nose)

                    gun_ammo.shooting_sound.play() if game.game_inst.sfx_toggle else False

                if self.power == 2:

                    game.all_sprites.add(wing_right_1, wing_left_1)
                    game.bullets.add(wing_right_1, wing_left_1)
        
                    gun_ammo.shooting_sound.play() if game.game_inst.sfx_toggle else False

                if self.power >= 3:
    
                    game.all_sprites.add(nose, wing_right_1, wing_left_1)
                    game.bullets.add(nose, wing_right_1, wing_left_1)

                    gun_ammo.shooting_sound.play() if game.game_inst.sfx_toggle else False
                
    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        # self.rect.center = (setting.WIDTH / 2, setting.HEIGHT + 200)

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
        self.image.set_colorkey(setting.BLACK)

        if self.wpn_name == "machine_gun":
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(game.player.current_bullet_alpha)

        self.rect = self.image.get_rect()
        self.rect.bottom = self.pos_Y 
        self.rect.centerx = self.pos_X
        self.shooting_sound = pygame.mixer.Sound(Asset_bank.Asset_bank.get("Weapon").get(self.wpn_name).get("sfx_blast"))        
        self.shooting_sound.set_volume(setting.sfx_volume)
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
        self.muzzlesprt_sprtsheet_src = pygame.image.load(Asset_bank.Asset_bank.get("Weapon").get(game.player.current_weapon).get("muzzle_sprt")).convert_alpha()
        self.muzzlesprt_sprtsheet = game.Spritesheet(self.muzzlesprt_sprtsheet_src)
        for i in range(4):
            self.frame_list.append(self.muzzlesprt_sprtsheet.get_image(i, 8, 8, 1))
        self.image = self.frame_list[0]
        self.rect = self.image.get_rect()

    def update(self):
        if self.n_iter < len(self.frame_list):
            self.n_iter += 1
        else:
            self.n_iter = 0

class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)

        powerup_images = {}
        powerup_images['shield'] = pygame.image.load(Asset_bank.Asset_bank.get("Powerup").get("sprite").get("shield_pwrup")).convert()
        powerup_images['gun'] = pygame.image.load(Asset_bank.Asset_bank.get("Powerup").get("sprite").get("weapon_pwrup")).convert()
        self.type = random.choice(['shield', 'gun'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(setting.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > setting.HEIGHT:
            self.kill()                         # kill the sprite after it moves over the bottom border

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(game.meteor_images)
        self.image_orig.set_colorkey(setting.BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width *.90 / 2)
        self.rect.x = random.randrange(0, setting.WIDTH - self.rect.width)
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

        if (self.rect.top > setting.HEIGHT + 10) or (self.rect.left < -25) or (self.rect.right > setting.WIDTH + 20):
            self.rect.x = random.randrange(0, setting.WIDTH - self.rect.width)
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
            img.set_colorkey(setting.BLACK)

            ## resize the explosion
            img_lg = pygame.transform.scale(img, (75, 75))
            explosion_anim['lg'].append(img_lg)
            img_sm = pygame.transform.scale(img, (32, 32))
            explosion_anim['sm'].append(img_sm)

            ## player explosion
            filename = "player_explosion0{}".format(i)
            img = pygame.image.load(Asset_bank.Asset_bank.get("Explosions").get("sprites").get(filename)).convert()
            img.set_colorkey(setting.BLACK)
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