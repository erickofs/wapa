from base_character import BaseCharacter

class Enemy(BaseCharacter):
    def __init__(self):
        super().__init__()
        self.hp = 10
        self.damage = 5
        self.attack_crit_damage = 1.5
        self.defense_crit = 1.35


