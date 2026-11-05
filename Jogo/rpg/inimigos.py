from combatentes import Combatente
import random

class Inimigo(Combatente):
    def __init__(self, nome, vida_maxima, vida, ataque, defesa, velocidade, prob_ataque):
        super().__init__(nome, vida_maxima, vida, ataque, defesa, velocidade)
        self.prob_ataque = prob_ataque 

    def escolher_acao(self):
        return random.choices([
        'atacar', 'defender'],
        weights=[self.prob_ataque, 
        100 - self.prob_ataque])[0]



class Slime(Inimigo):
    def escolher_acao(self):
        return 'atacar'


class Inseto(Inimigo):
    def escolher_acao(self):
        if self.vida <= self.vida_maxima * 0.3:
            return random.choices([
        'atacar', 'defender'],
        weights=[0, 100])[0]
        else:
            return super().escolher_acao()


class Aranha(Inimigo):
    def escolher_acao(self):
        if self.vida <= self.vida_maxima * 0.2:
            return random.choices([
            'atacar', 'defender', 'fugir'    
            ], weights=[60, 0, 40])[0]
        else:
            return super().escolher_acao()



class Goblin(Inimigo):
    def escolher_acao(self):
        if self.vida <= self.vida_maxima * 0.6:
            return random.choices([
            'atacar', 'defender', 'fugir'
            ], weights=[70, 0, 30])[0]
        else:
            return super().escolher_acao()


class Golem(Inimigo):
    def escolher_acao(self):
        if self.vida <= self.vida_maxima * 0.4:
            return random.choices(
            ['atacar', 'defender'],
            weights=[10, 90])[0]
        else:
            return super().escolher_acao() 


class Doppelganger(Inimigo):
    def escolher_acao(self):
        if self.vida <= self.vida_maxima * 0.5:
            return random.choices([
            'atacar', 'defender', 'fugir'
            ], weights=[50, 30, 20])[0]
        else:
            return super().escolher_acao()

class Virus(Inimigo):
    def escolher_acao(self):
        if self.vida >= self.vida_maxima * 0.45:
            return random.choices([
        'atacar', 'defender'],
        weights=[100, 0])[0]
        else:
            return super().escolher_acao()


class Dragao(Inimigo):
    def escolher_acao(self):
        if self.vida >= self.vida_maxima * 0.6:
            return random.choices([
        'atacar', 'defender'],
        weights=[75, 25])[0]
        else:
            return super().escolher_acao()

class Compilador(Inimigo):
    def escolher_acao(self):
        if self.vida >= self.vida_maxima * 0.5:
            return random.choices([
        'atacar', 'defender'],
        weights=[70, 30])[0]
        else:
            return super().escolher_acao()

class BugOriginal(Inimigo):
    def escolher_acao(self):
        if self.vida >= self.vida_maxima * 0.5:
            return random.choices([
        'atacar', 'defender'],
        weights=[100, 0])[0]
        else:
            return super().escolher_acao()


slime = Slime("Slime de Código", 30, 30, 8, 2, 1, 100)
inseto = Inseto("Inseto Bugado", 45, 45, 12, 4, 2, 60)
aranha = Aranha("Aranha de Firewall", 35, 35, 15, 3, 3, 80) # FUGIR
goblin = Goblin("Goblin de Sintaxe", 40, 1, 10, 1, 4, 75) # FUGIR
golem = Golem("Golem de Erro de Compilação", 150, 150, 22, 12, 1, 40) 
doppelganger = Doppelganger("Plágiador de Código", 100, 100, 20, 6, 2, 50) # FUGIR
virus = Virus("Vírus Corrompido", 120, 120, 18, 5, 2, 80)
dragao = Dragao("Dragão do Infinito", 250, 250, 28, 10, 1, 95)
compilador = Compilador("Compilador Supremo", 300, 300, 25, 14, 1, 95)
bug_original = BugOriginal("Bug Original", 500, 500, 35, 12, 1, 95)