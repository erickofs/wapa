import keyboard

class Movements:
    def __init__(self, player):
        self.player = player

    def key_listener(self):
        # Aguarda até que uma tecla válida seja pressionada
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                key = event.name
                if key == 'up':
                    return 'north'
                elif key == 'down':
                    return 'south'
                elif key == 'left':
                    return 'west'
                elif key == 'right':
                    return 'east'

    def move(self, direction):
        x, y = self.player.position  # Obtém a posição atual do jogador
        initial_position = (x, y)  # Salva a posição inicial

        if direction == 'north':
            if x > 0:
                x -= 1
            else:
                print("Cannot move north, edge of the map.")
        elif direction == 'south':
            if x < 7:
                x += 1
            else:
                print("Cannot move south, edge of the map.")
        elif direction == 'west':
            if y > 0:
                y -= 1
            else:
                print("Cannot move west, edge of the map.")
        elif direction == 'east':
            if y < 7:
                y += 1
            else:
                print("Cannot move east, edge of the map.")

        new_position = (x, y)
        return new_position  # Retorna a nova posição calculada
