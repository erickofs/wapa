from base_character import BaseCharacter

class Boss(BaseCharacter):
    def __init__(self):
        self.hp = 100
        self.damage = 50
        self.crit_damage = 1.5
        self.defense_crit = 1.35
