# motion.py
import random

class Motion:
    def nothing_happens(self):
        return """
         ~~~~~~~
       ~~~     ~~~
      ~~  The wind ~~
     ~~    is howling  ~~
       ~~~         ~~~
         ~~~~~~~~
        """

    def enemy_encounter(self):
        return """
         .-'''''-.
        /  .-=-.  \\
       /  /_=_-.\  \\
      /'`-[_=_-]`'-\\
      `'-.   '"` .-'`
          `''''`
        """

    def surprise_attack(self):
        return """
          .-'''-.
         /   _   \\
        |  /_\\  | 
        |  \\_/  | 
         \\     / 
          `~~~`
        """

    def enemy_attack(self):
        return """
           /|
          / |
         /  |
        /   |  The enemy strikes!
        \\   |
         \\  |
          \\ |
           \\|
        """

    def enemy_critical_attack(self):
        return """
           /|
          / |    **
         /  |   ****
        /   |  The enemy lands a 
        \\   |   critical hit!
         \\  |   ****
          \\ |    **
           \\|
        """

    def player_attack(self):
        return """
         |\\
         | \\   
         |  \\  
         |   \\  You strike the enemy!
         |   /
         |  /
         | /
         |/
        """

    def player_critical_attack(self):
        return """
         |\\
         | \\    **
         |  \\  ****
         |   \\ You land a
         |   / critical hit!
         |  /  ****
         | /    **
         |/
        """

    def player_dodge(self):
        return """
         \\
          \\   You dodge the attack and counterattack!
           \\
          O
         /|
         / \\
        """

    def enemy_dodge(self):
        return """
           O
          /|
          / \\  The enemy dodges your attack and counterattacks!
        """

    def player_victory(self):
        return """
          \\O/
           |    You Win!
          / \\
        """

    def enemy_defeated(self):
        return """
           X
          /|\\
           |
          / \\
         // \\\\
        """

    def game_over(self):
        return """
        _____   ____   ____
       /     \\ |  __| |  __|
      |  () ()|| |__  | |__
       \\  ^  / |____| |____|
        |||||
        |||||
        """

    def intro_text(self):
        return """
        ------------------------------------------------------------
                           WARRIOR'S PATH
        ------------------------------------------------------------

        Welcome, warrior!

        The world is in turmoil, and legends speak of a path leading to
        great power and riches. Many have sought it, but none have returned.

        You are now on this path, armed with nothing but your courage.
        Monsters roam, and ancient secrets lie hidden, waiting for you.

        Will you survive and uncover the secrets of the Warrior's Path,
        or will you become another lost soul in its trials?

        Your journey begins now...

        ------------------------------------------------------------
        """

    def revived_text(self):
        return """
        ------------------------------------------------------------
                           WARRIOR'S PATH
        ------------------------------------------------------------

        As your vision fades and darkness consumes you, a warm light
        suddenly envelops your soul. The Divinity of Adventurers has
        seen your determination and granted you another chance.

        Your spirit is revived, your wounds healed, and you are once
        again placed at the start of the path.

        Go forth, brave warrior. Your journey continues...

        ------------------------------------------------------------
        """
    def boss_defeated(self):
        return """
        ------------------------------------------------------------
                           WARRIOR'S PATH
        ------------------------------------------------------------

        As the dust settles and the echoes of battle fade, you stand
        victorious over the fallen boss. The path to power and riches
        is now open to you, and the world will remember your name.

        Congratulations, brave warrior. You have conquered the Warrior's Path!

        ------------------------------------------------------------
        """
    def ene_enc_desc(self):
        encounter_description = [
            "A shadowy figure emerges from the mist, revealing a fierce opponent.",
            "You hear a growl, and suddenly a wild beast leaps out from the underbrush.",
            "The ground trembles as a massive creature blocks your path, its eyes glowing with malice.",
            "A band of marauders surrounds you, weapons drawn and eyes filled with greed.",
            "A dark presence looms before you, its form shifting and changing with malevolent intent.",
            "A horde of undead creatures emerges from the darkness, their moans echoing in the stillness."
        ]
        return random.choice(encounter_description)
    def wea_enc_desc(self):
        weapon_description = [
            "You find a weapon lying on the ground, its blade gleaming in the sunlight.",
            "A mysterious weapon appears before you, pulsing with hidden power.",
            "A weapon of legend reveals itself to you, promising strength and victory.",
            "You stumble upon a hidden cache buried beneath some ancient ruins.",
            "In the remains of an old battlefield, you find a weapon glinting in the sunlight.",
            "While exploring a forgotten armory, you come across a well-crafted blade."
        ]
        return random.choice(weapon_description)
    def arm_enc_desc(self):
        armor_description = [
            "A suit of armor lies abandoned, its metal still shining despite the passage of time.",
            "You discover a set of armor hidden in a secret chamber, its enchantments still active.",
            "An ancient suit of armor reveals itself to you, offering protection and strength.",
            "A fallen warrior's armor lies before you, a testament to battles long past.",
            "In the depths of a forgotten dungeon, you find a suit of armor untouched by time.",
            "A set of armor crafted by master artisans beckons to you, offering protection and power.",
            "You find a suit of armor, gleaming despite the years it has been abandoned.",
            "Hidden in the shadows of a cave, you discover a set of armor left by a long-lost warrior.",
            "In a dusty corner of an old fortress, you uncover a piece of armor still in good condition."
        ]
        return random.choice(armor_description)
    def no_enc_desc(self):
        nothing_description = [
            "The wind whispers through the trees, carrying the scent of adventure.",
            "The path stretches out before you, inviting you to explore its mysteries.",
            "The world is quiet, as if holding its breath in anticipation of your next move.",
            "You feel a sense of peace and tranquility, surrounded by the beauty of nature.",
            "The sun shines down on you, warming your spirit and filling you with hope.",
            "The sound of birdsong fills the air, a melody of life and vitality.",
            "You take a moment to rest and reflect, grateful for the chance to continue your journey."
        ]
        return random.choice(nothing_description)
    def boss_intro(self):
        boss_description = [
            "A massive figure looms before you, its eyes filled with ancient wisdom and power.",
            "The ground shakes as the boss approaches, its form wreathed in shadow and flame.",
            "A legendary creature stands in your path, its presence commanding respect and fear.",
            "The boss reveals itself, a being of immense strength and dark intent.",
            "You face the final challenge, a foe unlike any you have encountered before.",
            "The boss's eyes lock onto yours, a silent challenge passing between you."
        ]
        return random.choice(boss_description)

    def boss_dodge_message(self):
        boss_dodge = [
            "The boss moves with unnatural speed, dodging your attack effortlessly.",
            "You strike, but the boss's reflexes are too quick, and it evades your blow.",
            "Your attack is swift and precise, but the boss anticipates your move and sidesteps it.",
            "The boss's movements are fluid and graceful, allowing it to avoid your strike with ease."
        ]
        return random.choice(boss_dodge)
