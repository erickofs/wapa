import random
import numpy as np
from 


class DamageCalc:
    def __init__(self):
        pass

    def calculate_damage(self, player_hp, player_weapon):
        damage = random.randint(int(0.1 * player_hp), int(0.5 * player_hp)) + player_weapon
        return damage

    def calculate_enemy_attack(self, enemy_hp):
        damage = random.randint(int(0.1 * enemy_hp), int(0.5 * enemy_hp))
        return damage

    def calculate_defense(self, player_hp, player_armor):
        hp_defense = random.randint(int(0.1 * player_hp), int(0.3 * player_hp))
        armor_defense = random.randint(int(0.5 * player_armor), int(0.75 * player_armor))
        return hp_defense + armor_defense

    def critical_hit_possible(self, player_hp, player_weapon, damage_to_enemy):
        if player_weapon > 0 and player_hp < 0.2 * player_weapon:
            return False

        crit_probability = np.percentile(range(int(0.1 * player_hp), int(0.5 * player_hp) + player_weapon + 1), 90)
        return player_weapon == 0 and crit_probability >= 50