# Warrior's Path

[Português](#português) | [English](#english)

## English
### Conception

Hello and welcome to my first game project

The intention of this game is to replicate the gameplay style of Hero Wars Ads, [like this one](https://www.youtube.com/shorts/xjK5IMZxYQ8) on a text-based game. In the moment I'm writing this, I have intentions of expanding this game to become a full text-based classic RPG, but for now, I believe this game is on a satisfactory state.

### Game description

This game is text-based, with 3 main mechanics:

- Movement
- Fighting enemies/boss
- Picking armor/weapon

Right now, the game's logic is:

- The game takes place in a 8x8 board and everytime you start a match, you'll start in a random position of the board.
- Your initial status will always be the same
- Your enemies will grow stronger as you grow stronger
- The boss is at a random position at the board (yes, you can find it on the first move. You'll probabilly die)
- You beat the boss, you beat the game
  
 Fun fact:

 I have never defeated the boss (neither will force test this, it's fun discovering what are the outcomes of my coding)

### Installation

I coded this on Python 3.10, try at least using this. 
If you wish, you can try older version since this doesn't have that much of imports
 
1. Cloning Repo
```
  git clone https://github.com/erickofs/wapa.git
```
2. Installing Requirements
```
pip install -r requirements.txt
```
3. Starting the game

Run the script with the command:
``` 
python wapa.py
```
to execute game

### Controls
- Use arrows keys to move
- Input choices/decisions when prompted to (becareful with your input on battles, a wrong one can cost your run)

### Contribution
For coding
  - Fork this repository.
  - Create a branch for your feature (git checkout -b feature/NewFeature).
  - Commit your changes (git commit -m 'Add new feature').
  - Push to the branch (git push origin feature/NewFeature).
  - Open a Pull Request.

For Testing
  - Follow [Installation](###Installation) guide and run the game. If you encounter a bug, open an Issue

### License
Huh? What is that?

-------

## Português

### Concepção

Olá e bem-vindo ao meu primeiro projeto de jogo!

A intenção deste jogo é replicar o estilo de gameplay dos anúncios do Hero Wars, [como este](https://www.youtube.com/shorts/xjK5IMZxYQ8), em um jogo baseado em texto. No momento em que estou escrevendo isso, tenho a intenção de expandir este jogo para se tornar um RPG clássico completo baseado em texto, mas por enquanto, acredito que este jogo está em um estado satisfatório.

### Descrição do Jogo

Este jogo é baseado em texto, com 3 mecânicas principais:

- **Movimento**
- **Combate contra inimigos/boss**
- **Coleta de armadura/arma**

Atualmente, a lógica do jogo é:

- O jogo ocorre em um tabuleiro 8x8 e toda vez que você inicia uma partida, começará em uma posição aleatória do tabuleiro.
- Seu status inicial será sempre o mesmo.
- Seus inimigos ficarão mais fortes conforme você se fortalece.
- O chefe está em uma posição aleatória no tabuleiro (sim, você pode encontrá-lo na primeira jogada. Você provavelmente morrerá).
- Você derrota o chefe, você vence o jogo.
  
**Curiosidade:**

Nunca derrotei o chefe (nem pretendo testar isso, é divertido descobrir quais são os resultados do meu código).

### Instalação

Eu codifiquei isso no Python 3.10, tente pelo menos usar esta versão. 
Se quiser, você pode tentar versões mais antigas, já que não tem lá muitas importações.
 
1. **Clonar o Repositório**
    ```
    git clone https://github.com/erickofs/wapa.git
    ```
2. **Instalar Requisitos**
    ```
    pip install -r requirements.txt
    ```
3. **Iniciar o Jogo**
    Execute o script com o comando:
    ```
    python wapa.py
    ```
    para executar o jogo.

### Controles
- Use as **teclas de seta** para mover.
- Insira escolhas/decisões quando solicitado (cuidado com sua decisão nas batalhas, uma errada pode custar sua run).

### Contribuição
**Para Coding:**
1. Faça um **fork** deste repositório.
2. Crie uma branch para sua feature:
    ```bash
    git checkout -b feature/NovaFeature
    ```
3. Faça **commit** das suas mudanças:
    ```bash
    git commit -m 'Adiciona nova feature'
    ```
4. Envie para a branch:
    ```bash
    git push origin feature/NovaFeature
    ```
5. Abra um **Pull Request**.

**Para Testes:**
1. Siga o guia de [Instalação](#instalação) e execute o jogo.
2. Se você encontrar um bug, abra uma **Issue**.

### Licença
Huh? O que é isso?
