from combatentes import Combatente

class Inimigo(Combatente):
    def __init__(self, nome, vida, ataque, defesa, velocidade, prob_ataque):
        super().__init__(nome, vida, ataque, defesa, velocidade)
        self.prob_ataque = prob_ataque 


slime = Inimigo("Slime de Código", 30, 8, 2, 1, 80)
inseto = Inimigo("Inseto Bugado", 45, 12, 4, 2, 60)
aranha = Inimigo("Aranha de Firewall", 35, 15, 3, 3, 80) # FUGIR
goblin = Inimigo("Goblin de Sintaxe", 25, 10, 1, 4, 75) # FUGIR
golem = Inimigo("Golem de Erro de Compilação", 150, 22, 12, 1, 40) 
doppelganger = Inimigo("Plágiador de Código", 100, 20, 6, 2, 50) # FUGIR
virus = Inimigo("Vírus Corrompido", 120, 18, 5, 2, 80)
dragao = Inimigo("Dragão do Infinito", 250, 28, 10, 1, 95)
compilador = Inimigo("Compilador Supremo", 300, 25, 14, 1, 95)
bug_original = Inimigo("Bug Original", 500, 35, 12, 1, 95)