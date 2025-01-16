import pygame
import random
import entity
import game
import setting
import ui_manager

title_game = "Odissey_Neverending"
date = 2023

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

game.set_game()

 
###################################################
## Game loop

while setting.running:  

    #1 Main menu
    if setting.menu_display:

        ui_manager.main_menu()
        pygame.time.wait(1000)
        pygame.mixer.music.stop()

        game.game_inst.bgm_play() if game.game_inst.bgm_toggle else False       
        setting.menu_display = False

    game.game_inst.background.update("vertical","desc")
    game.game_inst.background.render()

    #2 Event check
    event_list = pygame.event.get()             
    
    for event in event_list:        
       
        if event.type == pygame.QUIT:
            setting.running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                setting.running = False

            if event.key == pygame.K_1:        
                game.player.current_weapon = "blaster"
                ui_manager.draw_text(game.game_inst.resolution, "Blaster selected", 40, game.player.rect.x - 50 , game.player.rect.y )

            if event.key == pygame.K_2:
                game.player.current_weapon = "missile"
                ui_manager.draw_text(game.game_inst.resolution, "Missiles selected", 40, game.player.rect.x - 50 , game.player.rect.y )

            if event.key == pygame.K_3:
                game.player.current_weapon = "machine_gun"
                ui_manager.draw_text(game.game_inst.resolution, "Machine_gun selected", 40, game.player.rect.x - 50 , game.player.rect.y )

            if event.key == pygame.K_p:
                if game.player.power <= 2:
                    game.player.power += 1 
                elif game.player.power >= 3:
                    game.player.power = 1

            if event.key == pygame.K_a:         # swap background
                game.game_inst.background.change_background()
            if event.key == pygame.K_m:         # incoming asteroids field
                game.gen_meteor_field(8)
    
    #2 Update
    game.all_sprites.update()
    game.all_sprites.draw(game.game_inst.resolution)

    #3 Collisions

    # Ent_group x bullets
    hits = pygame.sprite.groupcollide(game.ent_group, game.bullets, True, True)
    for hit in hits:
        game.player.score += 50 - hit.radius         ## give different scores for hitting big and small metoers
        random.choice(game.ent_group.explosion_sounds).play() if game.game_inst.sfx_toggle else False
        
        expl = entity.Explosion(hit.rect.center, 'lg')
        game.all_sprites.add(expl)

        if random.random() > 0.9:
            pow = entity.Pow(hit.rect.center)
            game.all_sprites.add(pow)
            game.powerups.add(pow)

    # Player x Ent_group
    hits = pygame.sprite.spritecollide(game.player, game.ent_group, True, pygame.sprite.collide_circle)        ## gives back a list, True makes the mob element disappear
    for hit in hits:
        game.player.shield -= hit.radius * 2
        expl = entity.Explosion(hit.rect.center, 'sm')
        random.choice(game.ent_group.explosion_sounds).play() if game.game_inst.sfx_toggle else False
        game.all_sprites.add(expl)

        # newmob()
        if game.player.shield <= 0: 

            game.player.player_die_sound.play() if game.game_inst.sfx_toggle else False

            death_explosion = entity.Explosion(game.player.rect.center, 'player')

            game.all_sprites.add(death_explosion)
            game.player.hide()
            game.player.lives -= 1
            game.player.shield = 100
            

    # Player x powerup
    hits = pygame.sprite.spritecollide(game.player, game.powerups, True)
    for hit in hits:
        if hit.type == 'shield':
            game.player.shield += random.randrange(10, 30)
            if game.player.shield >= 100:
                game.player.shield = 100
        if hit.type == 'gun':
            game.player.powerup()

    #4 Game over
    if game.player.lives == 0:
        game.player.kill()

        if not death_explosion.alive():
            
            setting.menu_display = True
            game.all_sprites.empty()
            game.set_game()
            pygame.display.update()
        
        death_explosion.kill()

    if game.player.shield < 100:
        ui_manager.draw_shield_bar(game.game_inst.resolution, game.player.rect.x + 10 , game.player.rect.y + 80, game.player.shield)

    ui_manager.draw_text(game.game_inst.resolution, str(game.player.score), 30, 60, 45)
    ui_manager.draw_text(game.game_inst.resolution, "Press SPACE for shoot", 10, 63, 85)
    ui_manager.draw_text(game.game_inst.resolution, "Press M for meteor shower", 10, 70, 100)
    ui_manager.draw_text(game.game_inst.resolution, "Press P  for weapon powerup", 10, 75, 115)
    ui_manager.draw_text(game.game_inst.resolution, "Press Esc for quit", 10, 52, 130)
    ui_manager.draw_lives(game.game_inst.resolution, 10 , 10, game.player.lives, game.player.player_mini_img)

    

    pygame.display.flip()      

    game.clock.tick(setting.FPS)                                

pygame.quit()