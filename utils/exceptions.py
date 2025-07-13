class GameError(Exception):
    """Classe base para exceções do jogo"""
    pass

class InvalidActionError(GameError):
    """Exceção lançada quando uma ação inválida é tentada"""
    pass

class MovementError(GameError):
    """Exceção lançada quando um movimento inválido é tentado"""
    pass

class EquipmentError(GameError):
    """Exceção lançada quando há problemas com equipamentos"""
    pass
