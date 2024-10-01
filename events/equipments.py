import random
import numpy as np
from motion import Motion
from entities.player import Player


class Weapon():
    
    def __init__(self):
        self.quality = 0

    def weapon_quality(self, player_weapon, player_hp):
        max_weapon_quality = max(2, int(0.2 * player_hp))  
        weapon_quality = random.randint(1, max_weapon_quality)
        print(self.motion.wea_enc_desc())
    
class Armor():

    def __init__(self):
        self.quality = 0

    def get_armor(self, player_armor, player_hp):
        max_armor_quality = max(2, int(0.2 * player_hp))
        armor_quality = random.randint(1, max_armor_quality)
        print(self.motion.arm_enc_desc())

        if player_armor == 0 or armor_quality > player_armor:
            print(f"You upgrade your armor from quality {player_armor} to {armor_quality}.")
            return armor_quality
        else:
            print("You leave the armor behind.")
            return player_armor

class GetEquipments:
    def __init__(self, player, motion):
        self.player = player
        self.motion = motion
        player_hp = self.player.hp

    def get_armor(self, player_armor, player_hp):
        max_armor_quality = max(2, int(0.2 * player_hp))
        armor_quality = random.randint(1, max_armor_quality)
        print(self.motion.arm_enc_desc())

        if player_armor == 0 or armor_quality > player_armor:
            print(f"You upgrade your armor from quality {player_armor} to {armor_quality}.")
            return armor_quality
        else:
            print("You leave the armor behind.")
            return player_armor