from base_character import BaseCharacter

class Player(BaseCharacter):
    def __init__(self, x=0, y=0): 
        super().__init__()
        self.hp = 10
        self.damage = 5
        self.attack_crit_damage = 1.5
        self.defense_crit = 1.35
        self.position = (x, y)