import os
from objects.Settings import *
from typing import Optional

##########################
# Spécial Test unitaire  #
##########################
import unittest
from unittest.mock import patch


###################################################
#       METHODE QUI GERE LES PATHS                #
###################################################
# def handle_path(folders : list, file, debugg = True):
#         '''
#         Construction fonction to manage file path
#         :params:
#         - folder : str : subfile name
#         - file : str : file name with extension
#         '''
#         parts = [str(folder) for folder in folders] + [str(file)]
#         result = os.path.join("..", *parts)
#         if debugg == True :
#             print(f'Path created for {file} : ', result )
#             return result   


def handle_path(folders: list, file, debug=True):
    # Obtenir le chemin de base (dossier parent de `src`)
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    # Construire le chemin complet du fichier
    parts = [str(folder) for folder in folders] + [str(file)]
    result = os.path.join(base_path, *parts)
    if debug:
        print(f'Path created for {file} : ', result)
    return result

#########################################################
#       CLASSE STATIQUE JSON STYLE ASSET                #
#########################################################


class Asset_bank:

    """ Classe statique contenant les images des entités du jeu
        Permet facilement d'ajouter d'autres élèments et propriétés
    """
    
    Asset_bank = {
        "UI":
            {
                "caption":handle_path(UI, "ufo.png")
            },
        "Player":
            {"sprite":
                {
                    "default":handle_path(PLAYER,'player.png'),
                    "red_squad":
                        {
                            "battlecruiser":handle_path(SHIP,'Battlecruiser.png'),
                            "bomber":handle_path(SHIP,'Bomber.png'),
                            "dreadnought":handle_path(SHIP,'Dreadnought.png'),
                            "fighter":handle_path(SHIP,'Fighter.png'),
                            "frigate":handle_path(SHIP,'Frigate.png'),
                            "scout":handle_path(SHIP,"Scout.png"),
                            "support_ship":handle_path(SHIP,"Support_ship.png"),
                            "torpedo_ship":handle_path(SHIP,"Torpedo_Ship.png")
                        }
                },
            "sfx":
                {0:
                    ["default", None],
                 1: 
                    ["destruction", handle_path(SFX,'explosion.wav')]}}, 
        "Invader":                                                                     
                {
                "sprite":
                    {
                        0: handle_path(ENEMY, 'enemy.png')
                    },
                "sfx":
                    {
                        "thrusters": None,                                         
                        "destruction": handle_path(SFX, 'explosion.wav')
                    }
                },
        "Celestial_objects":
                {
                "asteroids":
                    {
                        "meteor_spaceshooter": 
                        {
                            'meteorBrown_big1.png':handle_path(ENEMY, "meteorBrown_big1.png"),
                            'meteorBrown_big2.png':handle_path(ENEMY,"meteorBrown_big2.png"), 
                            'meteorBrown_med1.png':handle_path(ENEMY,"meteorBrown_med1.png"), 
                            'meteorBrown_med3.png':handle_path(ENEMY,"meteorBrown_med3.png"),
                            'meteorBrown_small1.png':handle_path(ENEMY,"meteorBrown_small1.png"),
                            'meteorBrown_small2.png':handle_path(ENEMY,"meteorBrown_small2.png"),
                            'meteorBrown_tiny1.png':handle_path(ENEMY,"meteorBrown_tiny1.png")
                        } 
                    }
                },
        "Game":
            {
                "menu":
                {
                    "main_menu":handle_path(UI,"main_menu_bg.png")
                },
                "background":
                    {0:
                        [handle_path(SPACE_BACK, "Space-Free-PNG-Image.png"), 
                        handle_path(SPACE_BACK,"default800x600.png"),   # [1]  center_tile
                        handle_path(SPACE_BACK,"upper800x600.png"),     # [2]  upper_tile
                        handle_path(SPACE_BACK,"lower800x600.png"),     # [3]  lower_tile
                        handle_path(SPACE_BACK,"left800x600.png"),      # [4]  left_tile
                        handle_path(SPACE_BACK,"right800x600.jpg")      # [5]  right_tile
                        ]},
                "bgm":
                {   
                    "main_menu":handle_path(MUSIC,'music_mainmenu.wav'),
                    "level_1":handle_path(MUSIC, "music_001.wav"),
                    "level_2":None
                },
                "sfx":
                {
                    "get_ready":handle_path(SFX, 'get_ready_1.wav'),
                    "go":handle_path(SFX, 'go.wav')
                }
            },
        "Weapon":
            {
                "machine_gun":
                {
                    "blast_sprt": handle_path(BULLET,"bullet.png"),
                    "charge_sprt": None,
                    "sfx_blast": handle_path(SFX_SHOOT,"gun-gunshot-02.wav"),
                    "sfx_charge_opening": None,
                    "sfx_charge": None,
                    "sfx_charge_release": None,
                    "muzzle_sprt":handle_path(BULLET, "muzzle-flashes.png")
                },
                "blaster":
                {
                    "blast_sprt": handle_path(BULLET,"laserRed16.png"),
                    "charge_sprt": None,
                    "sfx_blast": handle_path(SFX_SHOOT,"laser_0.wav"),
                    "sfx_charge_opening": None,
                    "sfx_charge": None,
                    "sfx_charge_release": None,
                    "muzzle_sprt":handle_path(BULLET,"muzzle-flashes.png")
                },
                "missile":
                {
                    "blast_sprt": handle_path(BULLET,"missile.png"),
                    "charge_sprt": None,
                    "sfx_blast": handle_path(SFX_SHOOT,"rocket.ogg"),
                    "sfx_charge_opening": None,
                    "sfx_charge": None,
                    "sfx_charge_release": None,
                    "muzzle_sprt":handle_path(BULLET,"muzzle-flashes.png")
                },
            },
        "Explosions":
            {
                "sprites":
                {
                    "default_explosion00": handle_path(EXPLO,"regularExplosion00.png"),
                    "default_explosion01": handle_path(EXPLO,"regularExplosion01.png"),
                    "default_explosion02": handle_path(EXPLO,"regularExplosion02.png"),
                    "default_explosion03": handle_path(EXPLO,"regularExplosion03.png"),
                    "default_explosion04": handle_path(EXPLO,"regularExplosion04.png"),
                    "default_explosion05": handle_path(EXPLO,"regularExplosion05.png"),
                    "default_explosion06": handle_path(EXPLO,"regularExplosion06.png"),
                    "default_explosion07": handle_path(EXPLO,"regularExplosion07.png"),
                    "default_explosion08": handle_path(EXPLO,"regularExplosion08.png"),
                    "player_explosion00": handle_path(EXPLO,"sonicExplosion00.png"),
                    "player_explosion01": handle_path(EXPLO,"sonicExplosion01.png"),
                    "player_explosion02": handle_path(EXPLO,"sonicExplosion02.png"),
                    "player_explosion03": handle_path(EXPLO,"sonicExplosion03.png"),
                    "player_explosion04": handle_path(EXPLO,"sonicExplosion04.png"),
                    "player_explosion05": handle_path(EXPLO,"sonicExplosion05.png"),
                    "player_explosion06": handle_path(EXPLO,"sonicExplosion06.png"),
                    "player_explosion07": handle_path(EXPLO,"sonicExplosion07.png"),
                    "player_explosion08": handle_path(EXPLO,"sonicExplosion08.png"),
                },
                "sfx":
                {
                    "explosion_1": handle_path(EXPLO_SFX,"explosion_1.wav"),
                    "explosion_2": handle_path(EXPLO_SFX,"explosion_2.wav"),
                    "explosion_3": handle_path(EXPLO_SFX,"explosion_3.wav")
                }
            },
        "Powerup":
            {
                "sprite":
                {
                    "weapon_pwrup": handle_path(POWERUP, "bolt_gold.png"),
                    "shield_pwrup": handle_path(POWERUP,"shield_gold.png")
                },
                "sfx":
                {
                    "weapon_pwrup": None,
                    "shield_pwrup": None
                }
            },
        "Invader":
            {
                "Default":
                {
                    "main_sprt": handle_path(ENEMY, "enemy.png"),
                    "dest_sprt": None,
                    "snd_destr": None
                }
            }   
        }
    def __init__(self):
        self.asset = Asset_bank
        
    def get_asset_info(cls, category: str, subcategory: Optional[str] = None, subsubcategory: Optional[str] = None):
        """
        Récupère les informations d'un asset à partir des catégories, sous-catégories et sous-sous-catégories spécifiées.
        """
        asset_category = cls.Asset_bank.get(category)
        
        if not asset_category:
            return None
        
        if not subcategory:
            return asset_category
        
        asset_subcategory = asset_category.get(subcategory)
        
        if not asset_subcategory:
            return None
        
        if not subsubcategory:
            return asset_subcategory
        
        asset_subsubcategory = asset_subcategory.get(subsubcategory)
        
        return asset_subsubcategory
     
#=========================================================================================

