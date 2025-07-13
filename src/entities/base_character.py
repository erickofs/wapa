import random

class BaseCharacter():
    """
    Classe base para todos os personagens do jogo.
    
    Attributes:
        hp (int): Pontos de vida do personagem
        weapon (int): Poder da arma equipada
        armor (int): Poder da armadura equipada
        damage (int): Dano base do personagem
        attack_crit_chance (float): Chance de acerto crítico (0.0 a 1.0)
        attack_crit_damage (float): Multiplicador de dano crítico
        defense_crit_chance (float): Chance de defesa crítica (0.0 a 1.0)
        defense_crit (float): Multiplicador de defesa crítica
    """
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
        """
        Calcula o dano de ataque do personagem.
        
        Args:
            critical (bool): Se True, aplica dano crítico
            
        Returns:
            float: Valor do dano calculado
        """
        attack = self.damage + self.weapon
        if critical:
            return attack * self.attack_crit_damage
        return attack

    def defend(self, critical=False):
        """
        Calcula a defesa do personagem.
        
        Args:
            critical (bool): Se True, aplica defesa crítica
            
        Returns:
            float: Valor da defesa calculada
        """
        defense = self.hp + self.armor
        if critical:
            return defense * self.defense_crit_chance
        return defense

