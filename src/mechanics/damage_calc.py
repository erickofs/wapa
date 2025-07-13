import random
import numpy as np

class DamageCalc:
    def __init__(self):
        pass

    def calculate_player_attack(self, player_hp, player_weapon):
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
        """
        Calcula a possibilidade de um acerto crítico.
        
        Args:
            player_hp (int): HP atual do jogador
            player_weapon (int): Poder da arma do jogador
            damage_to_enemy (int): Dano calculado para o inimigo
            
        Returns:
            bool: True se o acerto crítico é possível, False caso contrário
        """
        # Se o jogador está muito fraco em relação à sua arma, não pode dar crítico
        if player_weapon > 0 and player_hp < 0.2 * player_weapon:
            return False

        # Calcula a probabilidade baseada no dano máximo possível
        max_possible_damage = int(0.5 * player_hp) + player_weapon
        damage_percentile = (damage_to_enemy / max_possible_damage) * 100

        # Retorna True se o dano está no top 10% dos danos possíveis
        return damage_percentile >= 90