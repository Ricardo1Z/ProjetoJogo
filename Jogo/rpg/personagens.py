from .combatentes import Combatente

class Personagem(Combatente):
    def __init__(self, nome, vida_maxima, vida, ataque, defesa, velocidade,):
        super().__init__(nome, vida_maxima, vida, ataque, defesa, velocidade)

#PERSONAGENS
guerreiro = Personagem('Python', 100, 100, 15, 8, 3)
mago = Personagem('Java', 80, 80, 25, 7, 2)
ladino = Personagem('JavaScript', 90, 90, 20, 6, 5)
paladino = Personagem('C#', 150, 150, 10, 10, 1)

personagens_liberados = [
    guerreiro,
    mago,
    ladino,
    paladino
]