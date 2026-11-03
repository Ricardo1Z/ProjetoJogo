from combatentes import Combatente

class Inimigo(Combatente):
    pass


slime = Inimigo("Slime de Código", 30, 8, 2, 1)
inseto = Inimigo("Inseto Bugado", 45, 12, 4, 2)
aranha = Inimigo("Aranha de Firewall", 35, 15, 3, 3)
goblin = Inimigo("Goblin de Sintaxe", 25, 10, 1, 4)
golem = Inimigo("Golem de Erro de Compilação", 150, 22, 12, 1)
doppelganger = Inimigo("Plágiador de Código", 100, 20, 6, 2)
virus = Inimigo("Vírus Corrompido", 120, 18, 5, 2)
dragao = Inimigo("Dragão do Infinito", 250, 28, 10, 1)
compilador = Inimigo("Compilador Supremo", 300, 25, 14, 1)
bug_original = Inimigo("Bug Original", 500, 35, 12, 1)