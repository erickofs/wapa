import random
from player import Player

class Enemy:
    def __init__(self, player):
        self.player = player


    def enemy_hp_calc(self, player_hp):
        player_hp = self.player.hp
        max_hp = 100
        probability = max(0.6, min(0.95, player_hp / max_hp))

        # Garante que o valor mínimo para a vida do inimigo seja sempre positivo e dentro de um intervalo adequado
        min_enemy_hp = max(5, player_hp - 10)
        max_enemy_hp = max(min_enemy_hp + 1, player_hp - 1)

        if random.random() < probability:
            enemy_hp = random.randint(player_hp + 1, player_hp + 10)
        else:
            enemy_hp = random.randint(min_enemy_hp, max_enemy_hp)

        return enemy_hp
    
    
