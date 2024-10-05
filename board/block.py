class Block():
    def __init__(self, position):
        self.position = position 
        self.events = []       
    
    def add_event(self, event):
        self.events.append(event)
    
    def __repr__(self):
        return f"Bloco(posicao={self.position})"