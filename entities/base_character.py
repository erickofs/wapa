import random

class BaseCharacter():
    def __init__(self):
        self.hp = 0
        self.weapon = 0
        self.armor = 0
        self.damage = 0
        self.attack_crit_chance = 0.0
        self.attack_crit_damage = 1.5
        self.defense_crit_chance = 0
        self.defense_crit = 1.35

    def attack(self, critical=False):
        attack = self.damage + self.weapon
        if critical:
            return attack*self.attack_crit_damage
        return attack

    def defend(self, critical=False):
        defense = self.hp + self.armor
        if critical:
            return defense*self.defense_crit_chance
        return defense

