import random
import numpy as np

class Events:
    def __init__(self, motion):
        self.motion = motion

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
        if player_weapon == 0 and crit_probability >= 50:
            return False

        if player_hp <= 2:
            return False

        return True

    def fight_enemy(self, player_hp, player_weapon, player_armor):
        max_hp = 100
        min_prob = 0.6
        max_prob = 0.95
        
        probability = min_prob + (max_prob - min_prob) * (player_hp / max_hp)

        if random.random() < probability:
            enemy_hp = random.randint(player_hp + 1, player_hp + 10)
        else:
            enemy_hp = random.randint(max(5, player_hp - 10), player_hp - 1)

        initial_enemy_hp = enemy_hp
        print(self.motion.ene_enc_desc())  # Correção: Remover `self`
        print(f"The enemy has {enemy_hp} HP!")

        surprise_attack_occurred = False
        enemy_has_attacked = False

        while enemy_hp > 0 and player_hp > 0:
            if not surprise_attack_occurred and not enemy_has_attacked and random.random() < 0.3:
                print(self.motion.surprise_attack())
                damage_to_player = self.calculate_enemy_attack(enemy_hp)
                player_hp -= damage_to_player
                print(f"The enemy strikes you for {damage_to_player} damage! Your HP is now {player_hp}.")
                surprise_attack_occurred = True
                enemy_has_attacked = True
                action = input("You can only (defend) now: ").lower()
                if action == "defend":
                    print("You brace yourself for the enemy's next attack, reducing the damage.")
                    defense_value = self.calculate_defense(player_hp, player_armor)
                    damage_to_player = max(0, self.calculate_enemy_attack(enemy_hp) - defense_value)
                    player_hp -= damage_to_player
                    print(f"The enemy strikes again, dealing {damage_to_player} damage to you! Your HP is now {player_hp}.")
                else:
                    print("Invalid action. The enemy takes advantage and strikes!")
                    damage_to_player = self.calculate_enemy_attack(enemy_hp)
                    player_hp -= damage_to_player
                    print(f"The enemy strikes again, dealing {damage_to_player} damage to you! Your HP is now {player_hp}.")
            else:
                while enemy_hp > 0 and player_hp > 0:
                    action = input("Do you want to (attack) or (defend)? ").lower()
                    if action == "attack":
                        damage_to_enemy = self.calculate_damage(player_hp, player_weapon)
                        percentiles = np.percentile(range(int(0.1 * player_hp), int(0.5 * player_hp) + player_weapon + 1), [10, 90])

                        if self.critical_hit_possible(player_hp, player_weapon, damage_to_enemy) and damage_to_enemy >= percentiles[1]:
                            enemy_hp -= damage_to_enemy
                            print(self.motion.player_critical_attack())
                        elif damage_to_enemy <= percentiles[0]:
                            print(self.motion.enemy_dodge())
                            damage_to_player = self.calculate_enemy_attack(enemy_hp)
                            player_hp -= damage_to_player
                            print(f"The enemy strikes back, dealing {damage_to_player} damage to you! Your HP is now {player_hp}.")
                            enemy_has_attacked = True
                            break
                        else:
                            enemy_hp -= damage_to_enemy
                            print(f"You strike the enemy for {damage_to_enemy} damage! Enemy HP is now {enemy_hp}.")
                            if enemy_hp > 0:
                                damage_to_player = self.calculate_enemy_attack(enemy_hp)
                                percentiles_enemy = np.percentile(range(int(0.1 * enemy_hp), int(0.5 * enemy_hp) + 1), [10, 90])

                                if damage_to_player >= percentiles_enemy[1]:
                                    print(self.motion.enemy_critical_attack())
                                    player_hp -= damage_to_player
                                    print(f"The enemy strikes again, dealing {damage_to_player} damage to you! Your HP is now {player_hp}.")
                                elif damage_to_player <= percentiles_enemy[0]:
                                    print(self.motion.player_dodge())
                                    damage_to_enemy = self.calculate_damage(player_hp, player_weapon)
                                    enemy_hp -= damage_to_enemy
                                    print(f"You strike back, dealing {damage_to_enemy} damage! Enemy HP is now {enemy_hp}.")
                                else:
                                    player_hp -= damage_to_player
                                    print(f"The enemy strikes back, dealing {damage_to_player} damage to you! Your HP is now {player_hp}.")
                                enemy_has_attacked = True
                    elif action == "defend":
                        print("You brace yourself for the enemy's attack, reducing the damage.")
                        defense_value = self.calculate_defense(player_hp, player_armor)
                        damage_to_player = max(0, self.calculate_enemy_attack(enemy_hp) - defense_value)
                        player_hp -= damage_to_player
                        print(f"The enemy strikes back, dealing {damage_to_player} damage to you! Your HP is now {player_hp}.")
                        enemy_has_attacked = True
                    else:
                        print("Invalid action. The enemy takes advantage and strikes!")
                        damage_to_player = self.calculate_enemy_attack(enemy_hp)
                        player_hp -= damage_to_player
                        print(f"The enemy strikes back, dealing {damage_to_player} damage to you! Your HP is now {player_hp}.")
                        enemy_has_attacked = True
        
        if player_hp > 0:
            print("You have defeated the enemy! You feel a sense of relief and gain strength.")
            player_hp += initial_enemy_hp
            print(f"You gain {initial_enemy_hp} HP from your victory! Your HP is now {player_hp}.")
        else:
            print("The enemy has defeated you... Your journey ends here.")
        
        return player_hp

    def fight_boss(self, player_hp, player_weapon, player_armor):
        boss_hp = int(player_hp * 2) + random.randint(int(0.3 * player_hp), int(0.5 * player_hp)) 
        print(self.motion.boss_intro())
        print(f"The boss has {boss_hp} HP!")

        while boss_hp > 0 and player_hp > 0:
            action = input("Do you want to (attack) or (defend)? ").lower()
            if action == "attack":
                damage_to_boss = self.calculate_damage(player_hp, player_weapon)
                percentiles = np.percentile(range(int(0.1 * player_hp), int(0.5 * player_hp) + player_weapon + 1), [10, 90])

                if self.critical_hit_possible(player_hp, player_weapon, damage_to_boss) and damage_to_boss >= percentiles[1]:
                    boss_hp -= damage_to_boss
                    print(self.motion.player_critical_attack())
                elif damage_to_boss <= percentiles[0]:
                    print(self.motion.boss_dodge_message())
                    damage_to_player = self.calculate_enemy_attack(boss_hp)
                    player_hp -= damage_to_player
                    print(f"The boss strikes back, dealing {damage_to_player} damage to you! Your HP is now {player_hp}.")
                else:
                    boss_hp -= damage_to_boss
                    print(f"You strike the boss for {damage_to_boss} damage! Boss HP is now {boss_hp}.")
                    if boss_hp > 0:
                        damage_to_player = self.calculate_enemy_attack(boss_hp)
                        percentiles_enemy = np.percentile(range(int(0.1 * boss_hp), int(0.5 * boss_hp) + 1), [10, 90])

                        if damage_to_player >= percentiles_enemy[1]:
                            print(self.motion.enemy_critical_attack())
                            player_hp -= damage_to_player
                            print(f"The boss strikes again, dealing {damage_to_player} damage to you! Your HP is now {player_hp}.")
                        elif damage_to_player <= percentiles_enemy[0]:
                            print(self.motion.player_dodge())
                            damage_to_boss = self.calculate_damage(player_hp, player_weapon)
                            boss_hp -= damage_to_boss
                            print(f"You strike back, dealing {damage_to_boss} damage! Boss HP is now {boss_hp}.")
                        else:
                            player_hp -= damage_to_player
                            print(f"The boss strikes back, dealing {damage_to_player} damage to you! Your HP is now {player_hp}.")
            elif action == "defend":
                print("You brace yourself for the boss's attack, reducing the damage.")
                defense_value = self.calculate_defense(player_hp, player_armor)
                damage_to_player = max(0, self.calculate_enemy_attack(boss_hp) - defense_value)
                player_hp -= damage_to_player
                print(f"The boss strikes back, dealing {damage_to_player} damage to you! Your HP is now {player_hp}.")
            else:
                print("Invalid action. The boss takes advantage and strikes!")
                damage_to_player = self.calculate_enemy_attack(boss_hp)
                player_hp -= damage_to_player
                print(f"The boss strikes back, dealing {damage_to_player} damage to you! Your HP is now {player_hp}.")

        if player_hp > 0:
            print("You have defeated the boss! You feel a surge of power.")
            player_hp += 50
        else:
            print("The boss has defeated you... Your journey ends here.")
        
        return player_hp

    def get_weapon(self, player_weapon, player_hp):
        max_weapon_power = int(0.2 * player_hp)
        weapon_power = random.randint(1, max_weapon_power)
        discovery = self.motion.wea_enc_desc()  # Correção: Remover `self`
        print(discovery)

        if player_weapon == 0:
            print(f"You currently have no weapon. You decide to wield this new weapon with power {weapon_power}.")
            return weapon_power
        elif weapon_power > player_weapon:
            print(f"The weapon you find is much better than your current one. You upgrade your weapon from power {player_weapon} to {weapon_power}.")
            return weapon_power
        else:
            print(f"Despite your discovery, the weapon is not stronger than what you already possess. You leave it behind.")
            return player_weapon

    def get_armor(self, player_armor, player_hp):
        max_armor_quality = int(0.2 * player_hp)
        armor_quality = random.randint(1, max_armor_quality)
        discovery = self.motion.arm_enc_desc()  # Correção: Remover `self`
        print(discovery)

        if player_armor == 0:
            print(f"You currently have no armor. You decide to equip this new armor with quality {armor_quality}.")
            return armor_quality
        elif armor_quality > player_armor:
            print(f"The armor you find is superior to your current one. You upgrade from armor quality {player_armor} to {armor_quality}.")
            return armor_quality
        else:
            print(f"After inspecting the armor, you realize it offers no better protection than your current gear. You decide to leave it.")
            return player_armor
