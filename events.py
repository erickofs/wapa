import random
import numpy as np

class Events:
    def calculate_damage(self, player_hp, player_weapon):
        # Dano é um valor aleatório entre 10% e 50% do HP do jogador + 100% do valor da arma
        damage = random.randint(int(0.1 * player_hp), int(0.5 * player_hp)) + player_weapon
        return damage

    def calculate_enemy_attack(self, enemy_hp):
        # Dano do inimigo é entre 10% e 50% do HP do inimigo
        damage = random.randint(int(0.1 * enemy_hp), int(0.5 * enemy_hp))
        return damage

    def calculate_defense(self, player_hp, player_armor):
        # Defesa é 10% a 30% do HP do jogador + 10% a 30% do valor da armadura
        hp_defense = random.randint(int(0.1 * player_hp), int(0.3 * player_hp))
        armor_defense = random.randint(int(0.1 * player_armor), int(0.3 * player_armor))
        return hp_defense + armor_defense

    def fight_enemy(self, player_hp, player_weapon, player_armor):
        max_hp = 100  # Definindo um HP máximo teórico do jogador
        min_prob = 0.6  # Probabilidade mínima de encontrar inimigo mais forte (60%)
        max_prob = 0.95  # Probabilidade máxima de encontrar inimigo mais forte (95%)
        
        probability = min_prob + (max_prob - min_prob) * (player_hp / max_hp)

        if random.random() < probability:
            enemy_hp = random.randint(player_hp + 1, player_hp + 10)
        else:
            enemy_hp = random.randint(max(5, player_hp - 10), player_hp - 1)

        initial_enemy_hp = enemy_hp  # Guardando o HP inicial do inimigo para a recompensa
        encounter_description = [
            "A shadowy figure emerges from the mist, revealing a fierce opponent.",
            "You hear a growl, and suddenly a wild beast leaps out from the underbrush.",
            "The ground trembles as a massive creature blocks your path, its eyes glowing with malice."
        ]
        encounter = random.choice(encounter_description)
        print(encounter)
        print(f"The enemy has {enemy_hp} HP!")

        surprise_attack_occurred = False  # Controle para o ataque surpresa
        enemy_has_attacked = False  # Controle para verificar se o inimigo já atacou

        while enemy_hp > 0 and player_hp > 0:
            if not surprise_attack_occurred and not enemy_has_attacked and random.random() < 0.3:
                # 30% de chance de o inimigo realizar um ataque surpresa, uma vez por encontro
                print("The enemy launches a surprise attack!")
                damage_to_player = self.calculate_enemy_attack(enemy_hp)
                player_hp -= damage_to_player
                print(f"The enemy strikes you for {damage_to_player} damage! Your HP is now {player_hp}.")
                surprise_attack_occurred = True
                enemy_has_attacked = True  # Marcar que o inimigo já atacou
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
                        
                        if damage_to_enemy >= percentiles[1]:
                            enemy_hp -= damage_to_enemy  # Reduzir o HP do inimigo mesmo em ataques críticos
                            print(f"Critical hit! You deal {damage_to_enemy} damage and get to attack again!")
                        elif damage_to_enemy <= percentiles[0]:
                            print(f"The enemy dodges your attack and counterattacks!")
                            damage_to_player = self.calculate_enemy_attack(enemy_hp)
                            player_hp -= damage_to_player
                            print(f"The enemy strikes back, dealing {damage_to_player} damage to you! Your HP is now {player_hp}.")
                            enemy_has_attacked = True  # Marcar que o inimigo já atacou
                            break
                        else:
                            enemy_hp -= damage_to_enemy  # Reduzir o HP do inimigo para ataques normais
                            print(f"You strike the enemy for {damage_to_enemy} damage! Enemy HP is now {enemy_hp}.")
                            if enemy_hp > 0:  # Somente atacar se o inimigo ainda estiver vivo
                                damage_to_player = self.calculate_enemy_attack(enemy_hp)
                                percentiles_enemy = np.percentile(range(int(0.1 * enemy_hp), int(0.5 * enemy_hp) + 1), [10, 90])

                                if damage_to_player >= percentiles_enemy[1]:
                                    print(f"Critical hit! The enemy deals {damage_to_player} damage and attacks again!")
                                    player_hp -= damage_to_player
                                    print(f"The enemy strikes again, dealing {damage_to_player} damage to you! Your HP is now {player_hp}.")
                                elif damage_to_player <= percentiles_enemy[0]:
                                    print(f"You dodge the enemy's attack and counterattack!")
                                    damage_to_enemy = self.calculate_damage(player_hp, player_weapon)
                                    enemy_hp -= damage_to_enemy
                                    print(f"You strike back, dealing {damage_to_enemy} damage! Enemy HP is now {enemy_hp}.")
                                else:
                                    player_hp -= damage_to_player
                                    print(f"The enemy strikes back, dealing {damage_to_player} damage to you! Your HP is now {player_hp}.")
                                enemy_has_attacked = True  # Marcar que o inimigo já atacou
                    elif action == "defend":
                        print("You brace yourself for the enemy's attack, reducing the damage.")
                        defense_value = self.calculate_defense(player_hp, player_armor)
                        damage_to_player = max(0, self.calculate_enemy_attack(enemy_hp) - defense_value)
                        player_hp -= damage_to_player
                        print(f"The enemy strikes back, dealing {damage_to_player} damage to you! Your HP is now {player_hp}.")
                        enemy_has_attacked = True  # Marcar que o inimigo já atacou
                    else:
                        print("Invalid action. The enemy takes advantage and strikes!")
                        damage_to_player = self.calculate_enemy_attack(enemy_hp)
                        player_hp -= damage_to_player
                        print(f"The enemy strikes back, dealing {damage_to_player} damage to you! Your HP is now {player_hp}.")
                        enemy_has_attacked = True  # Marcar que o inimigo já atacou
        
        if player_hp > 0:
            print("You have defeated the enemy! You feel a sense of relief and gain strength.")
            player_hp += initial_enemy_hp  # Jogador ganha o HP inicial do inimigo como recompensa
            print(f"You gain {initial_enemy_hp} HP from your victory! Your HP is now {player_hp}.")
        else:
            print("The enemy has defeated you... Your journey ends here.")
        
        return player_hp

    def fight_boss(self, player_hp, player_weapon, player_armor):
        boss_hp = 500 + int(player_hp * 2)
        print("\nA massive figure looms before you... it's the BOSS!")
        print(f"The boss has {boss_hp} HP!")

        while boss_hp > 0 and player_hp > 0:
            action = input("Do you want to (attack) or (defend)? ").lower()
            if action == "attack":
                damage_to_boss = self.calculate_damage(player_hp, player_weapon)
                boss_hp -= damage_to_boss
                print(f"You strike the boss for {damage_to_boss} damage! Boss HP is now {boss_hp}.")
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
            player_hp += 50  # Recompensa por derrotar o boss
        else:
            print("The boss has defeated you... Your journey ends here.")
        
        return player_hp

    def get_weapon(self, player_weapon, player_hp):
        max_weapon_power = int(0.2 * player_hp)
        weapon_power = random.randint(1, max_weapon_power)
        
        weapon_discovery = [
            "You stumble upon a hidden cache buried beneath some ancient ruins.",
            "In the remains of an old battlefield, you find a weapon glinting in the sunlight.",
            "While exploring a forgotten armory, you come across a well-crafted blade."
        ]
        discovery = random.choice(weapon_discovery)
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

        armor_discovery = [
            "You find a suit of armor, gleaming despite the years it has been abandoned.",
            "Hidden in the shadows of a cave, you discover a set of armor left by a long-lost warrior.",
            "In a dusty corner of an old fortress, you uncover a piece of armor still in good condition."
        ]
        discovery = random.choice(armor_discovery)
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