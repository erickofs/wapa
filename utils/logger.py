import logging
import os

# Configuração do logging
log_directory = 'logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(log_directory, 'game.log')),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('wapa')
