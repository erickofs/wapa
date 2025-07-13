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
        """
        Move o jogador na direção especificada se possível.
        
        Args:
            direction (str): Direção do movimento ('north', 'south', 'east', 'west')
            
        Returns:
            tuple: Nova posição (x, y) do jogador
        
        Raises:
            MovementError: Se a direção é inválida ou o movimento não é possível
        """
        from utils.exceptions import MovementError

        if direction not in ['north', 'south', 'east', 'west']:
            raise MovementError(f"Invalid direction: {direction}")

        x, y = self.player.position
        initial_position = (x, y)

        try:
            if direction == 'north' and x > 0:
                x -= 1
            elif direction == 'south' and x < 7:
                x += 1
            elif direction == 'west' and y > 0:
                y -= 1
            elif direction == 'east' and y < 7:
                y += 1
            else:
                print(f"Cannot move {direction}, edge of the map.")

        new_position = (x, y)
        return new_position  # Retorna a nova posição calculada
