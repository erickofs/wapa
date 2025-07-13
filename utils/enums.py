from enum import Enum, auto

class EventType(Enum):
    """
    Enum para representar os diferentes tipos de eventos no jogo.
    """
    NOTHING = 0
    ENEMY = 1
    WEAPON = 2
    ARMOR = 3

    @classmethod
    def from_int(cls, value: int):
        """
        Converte um valor inteiro para o tipo de evento correspondente.
        """
        for event_type in cls:
            if event_type.value == value:
                return event_type
        return cls.NOTHING
