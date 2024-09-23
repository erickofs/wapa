#events.py

import random
import numpy as np
import time
from motion import Motion
from board import Board

class Events:
    def __init__(self, player, board):
        self.motion = Motion()
        self.board = board
        self.player = player

    def process_event(self, position):
        event = self.board.get_event(position)
        self.board.mark_position_explored(position)

        if event == 0:
            print(self.motion.nothing_happens())
            print(self.motion.no_enc_desc())
        elif event == 1:
            print(self.motion.enemy_encounter()) 
            self.player.hp = self.fight_enemy(self.player.hp, self.player.weapon, self.player.armor)
            if self.player.hp > 20:
                print("You feel a sense of foreboding... the enemies are becoming stronger as you gain power.")
        elif event == 2:
            self.player.weapon = self.get_weapon(self.player.weapon, self.player.hp)
        elif event == 3:
            self.player.armor = self.get_armor(self.player.armor, self.player.hp)
        else:
            print(self.motion.nothing_happens())

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

    def fight_enemy(self, player_hp, player_weapon, player_armor):
        max_hp = 100
        probability = max(0.6, min(0.95, player_hp / max_hp))

        # Garante que o valor mínimo para a vida do inimigo seja sempre positivo e dentro de um intervalo adequado
        min_enemy_hp = max(5, player_hp - 10)
        max_enemy_hp = max(min_enemy_hp + 1, player_hp - 1)

        if random.random() < probability:
            enemy_hp = random.randint(player_hp + 1, player_hp + 10)
        else:
            enemy_hp = random.randint(min_enemy_hp, max_enemy_hp)

        initial_enemy_hp = enemy_hp
        print(self.motion.ene_enc_desc())
        print(f"The enemy has {enemy_hp} HP!")

        while enemy_hp > 0 and player_hp > 0:
            action = input("Do you want to (attack) or (defend)? ").lower()
            if action == "attack":
                damage_to_enemy = self.calculate_damage(player_hp, player_weapon)
                enemy_hp -= damage_to_enemy
                print(f"You strike the enemy for {damage_to_enemy} damage! Enemy HP is now {enemy_hp}.")
                if enemy_hp <= 0:
                    break  # Inimigo derrotado

                damage_to_player = self.calculate_enemy_attack(enemy_hp)
                player_hp -= damage_to_player
                print(f"The enemy strikes back, dealing {damage_to_player} damage to you! Your HP is now {player_hp}.")
            elif action == "defend":
                defense_value = self.calculate_defense(player_hp, player_armor)
                damage_to_player = max(0, self.calculate_enemy_attack(enemy_hp) - defense_value)
                player_hp -= damage_to_player
                print(f"The enemy strikes, but you reduce the damage! Your HP is now {player_hp}.")
            else:
                print("Invalid action. The enemy takes advantage and strikes!")
                damage_to_player = self.calculate_enemy_attack(enemy_hp)
                player_hp -= damage_to_player
                print(f"The enemy strikes back, dealing {damage_to_player} damage to you! Your HP is now {player_hp}.")

        if player_hp > 0:
            print("You have defeated the enemy! You feel a sense of relief and gain strength.")
            player_hp += initial_enemy_hp  # Recupera HP baseado na HP inicial do inimigo derrotado
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
        max_weapon_quality = max(2, int(0.2 * player_hp))  
        weapon_quality = random.randint(1, max_weapon_quality)
        print(self.motion.wea_enc_desc())

        if player_weapon == 0 or weapon_quality > player_weapon:
            print(f"You upgrade your weapon from power {player_weapon} to {weapon_quality}.")
            return weapon_quality
        else:
            print("You leave the weapon behind.")
            return player_weapon

    def get_armor(self, player_armor, player_hp):
        max_armor_quality = max(2, int(0.2 * player_hp))
        armor_quality = random.randint(1, max_armor_quality)
        print(self.motion.arm_enc_desc())

        if player_armor == 0 or armor_quality > player_armor:
            print(f"You upgrade your armor from quality {player_armor} to {armor_quality}.")
            return armor_quality
        else:
            print("You leave the armor behind.")
            return player_armor

    def display_introduction(self):
        intro_text = self.motion.intro_text()
        for line in intro_text.split('\n'):
            print(line)
            time.sleep(0.05)

    def display_revived_message(self):
        revived_text = self.motion.revived_text()
        for line in revived_text.split('\n'):
            print(line)
            time.sleep(0.05)