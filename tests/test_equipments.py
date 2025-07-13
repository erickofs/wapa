import unittest
from entities.player import Player
from events.equipments import Weapon, Armor
from motion import Motion

class TestEquipments(unittest.TestCase):
    def setUp(self):
        self.motion = Motion()
        self.weapon = Weapon(self.motion)
        self.armor = Armor(self.motion)
        self.player = Player()

    def test_weapon_quality(self):
        """Test if weapon quality is within expected range"""
        quality = self.weapon.weapon_quality(self.player.weapon, self.player.hp)
        max_quality = max(2, int(0.2 * self.player.hp))
        self.assertGreaterEqual(quality, 1)
        self.assertLessEqual(quality, max_quality)

    def test_armor_quality(self):
        """Test if armor quality is within expected range"""
        quality = self.armor.get_armor(self.player.armor, self.player.hp)
        max_quality = max(2, int(0.2 * self.player.hp))
        self.assertGreaterEqual(quality, 1)
        self.assertLessEqual(quality, max_quality)

if __name__ == '__main__':
    unittest.main()
