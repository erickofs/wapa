class Event():
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def execute(self, block):
        block.add_event(self)
    
    def __repr__(self):
        return f"Evento(nome={self.name})"

class RainEvent(Event):
    def __init__(self):
        super().__init__("Chuva", "O bloco está molhado.")
    
    def execute(self, block):
        super().execute(block)
        print("Choveu no bloco")
