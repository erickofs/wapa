# motion.py

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
        |  \_/  | 
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
