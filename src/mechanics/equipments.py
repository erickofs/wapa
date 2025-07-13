import random
import numpy as np
from motion import Motion
from entities.player import Player


class Weapon():
    
    def __init__(self, motion):
        self.quality = 0
        self.motion = motion

    def weapon_quality(self, player_weapon, player_hp):
        max_weapon_quality = max(2, int(0.2 * player_hp))  
        weapon_quality = random.randint(1, max_weapon_quality)
        print(self.motion.wea_enc_desc())
        return weapon_quality
    
class Armor():

    def __init__(self, motion):
        self.quality = 0
        self.motion = motion

    def get_armor(self, player_armor, player_hp):
        """
        Calcula e retorna a qualidade da nova armadura encontrada.
        
        Args:
            player_armor (int): Qualidade atual da armadura do jogador
            player_hp (int): HP atual do jogador
            
        Returns:
            int: Nova qualidade da armadura ou a atual se não houver upgrade
        """
        max_armor_quality = max(2, int(0.2 * player_hp))
        armor_quality = random.randint(1, max_armor_quality)
        print(self.motion.arm_enc_desc())

        if player_armor == 0 or armor_quality > player_armor:
            print(f"You upgrade your armor from quality {player_armor} to {armor_quality}.")
            return armor_quality
        else:
            print("You leave the armor behind.")
            return player_armor

