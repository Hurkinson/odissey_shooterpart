# ui_manager
"""
prints
lives
health
score
weapon selection
energy_lvl
"""

import pygame

from asset_bank import Asset_bank
import game
# import objects.Settings as setting
import setting


#==========================================================================================

def main_menu():

    pygame.mixer.music.load(Asset_bank.Asset_bank.get("Game").get("bgm").get("main_menu"))
    pygame.mixer.music.play(-1) if game.game_inst.bgm_toggle else False

    title = pygame.image.load(Asset_bank.Asset_bank.get("Game").get("menu").get("main_menu")).convert()
    title = pygame.transform.scale(title, (setting.WIDTH, setting.HEIGHT), game.game_inst.resolution)

    game.game_inst.resolution.blit(title, (0,0))
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
            draw_text(game.game_inst.resolution, "Press Enter to start", 30, setting.WIDTH/2, setting.HEIGHT/2+40)
            draw_text(game.game_inst.resolution, "Esc to quit", 30, setting.WIDTH/2, (setting.HEIGHT/2)+80)
            draw_text(game.game_inst.resolution, "V 1.1", 15, setting.WIDTH - 30, setting.HEIGHT - 20)
            draw_text(game.game_inst.resolution, f"(c)Copyright {setting.date} - Guillaume Morin-Duponchelle - Vivien Schneider", 15, 200, setting.HEIGHT - 20)

            pygame.display.update()

    game.game_inst.resolution.fill(setting.BLACK)
    draw_text(game.game_inst.resolution, "GO !", 40, setting.WIDTH/2, setting.HEIGHT/2)

    ready = pygame.mixer.Sound(Asset_bank.Asset_bank.get("Game").get("sfx").get("get_ready"))
    ready.play() if game.game_inst.sfx_toggle else False

    pygame.time.wait(2000)

    go = pygame.mixer.Sound(Asset_bank.Asset_bank.get("Game").get("sfx").get("go"))
    go.play() if game.game_inst.sfx_toggle else False
    
    pygame.display.update()



#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(setting.font_name, size)
    text_surface = font.render(text, True, setting.WHITE)       ## True denotes the font to be anti-aliased 
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
    pygame.draw.rect(surf, setting.GREEN, fill_rect)
    pygame.draw.rect(surf, setting.WHITE, outline_rect, 2)

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect= img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

def ranking_ladder():
    pass