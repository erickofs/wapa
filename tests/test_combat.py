import unittest
from events.damage_calc import DamageCalc
from entities.player import Player
from entities.enemies import Enemy
from entities.boss import Boss

class TestCombat(unittest.TestCase):
    def setUp(self):
        self.damage_calc = DamageCalc()
        self.player = Player()
        self.enemy = Enemy()
        self.boss = Boss()

    def test_player_attack(self):
        """Test if player attack calculation is within expected range"""
        damage = self.damage_calc.calculate_player_attack(self.player.hp, self.player.weapon)
        self.assertGreaterEqual(damage, int(0.1 * self.player.hp))
        self.assertLessEqual(damage, int(0.5 * self.player.hp) + self.player.weapon)

    def test_enemy_attack(self):
        """Test if enemy attack calculation is within expected range"""
        damage = self.damage_calc.calculate_enemy_attack(self.enemy.hp)
        self.assertGreaterEqual(damage, int(0.1 * self.enemy.hp))
        self.assertLessEqual(damage, int(0.5 * self.enemy.hp))

    def test_defense_calculation(self):
        """Test if defense calculation is within expected range"""
        defense = self.damage_calc.calculate_defense(self.player.hp, self.player.armor)
        min_defense = int(0.1 * self.player.hp)
        max_defense = int(0.3 * self.player.hp) + int(0.75 * self.player.armor)
        self.assertGreaterEqual(defense, min_defense)
        self.assertLessEqual(defense, max_defense)

if __name__ == '__main__':
    unittest.main()
