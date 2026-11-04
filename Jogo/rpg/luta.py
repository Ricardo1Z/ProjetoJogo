from inimigos import *
from personagens import *
import random

inimigos_disponiveis = {
    'slime': slime,
    'inseto': inseto,
    'aranha': aranha,
    'goblin': goblin,
    'golem': golem,
    'clone': doppelganger,
    'virus': virus,
    'dragao': dragao,
    'compilador': compilador,
    'bug_original': bug_original
    }

personagens_liberados = [
    guerreiro,
    mago,
    ladino,
    paladino
]

grupo_inimigos = [slime, inseto, goblin]
grupo_jogador = []

grupo_jogador.append(guerreiro)

class Luta():
    def __init__(self, grupo_jogador, grupo_inimigos):
        self.grupo_jogador = grupo_jogador
        self.grupo_inimigos = grupo_inimigos

        self.participantes = grupo_jogador + grupo_inimigos


    def ordenar_turnos(self):    
        self.ordem_turnos = sorted(
    self.participantes, 
    key=lambda c: c.velocidade,
    reverse=True
    )
        return self.ordem_turnos


    def rodada(self):
        while (any(personagem.vida > 0 for personagem in self.grupo_jogador)
               and
               any(inimigo.vida > 0 for inimigo in self.grupo_inimigos)):
            self.ordenar_turnos()
            for combatente in self.ordem_turnos:
                if not any(personagem.vida > 0 for personagem in self.grupo_jogador):
                    break

                if not any(inimigo.vida > 0 for inimigo in self.grupo_inimigos):
                    break

                if combatente.vida <= 0:
                    continue


                if combatente in self.grupo_jogador:
                    print(f'Turno do {combatente.nome}')
                    if combatente.defendendo:
                        combatente.remover_defesa()

                    comando = input('Digite uma ação: ')

                    if '(' in comando and ')' in comando:
                        partes = comando.split('(')
                        alvo = partes[1].replace(')', '')
                        acao = partes[0]

                    else:
                        acao = comando.replace('()', '')
                        alvo = None

                    if acao == 'defender':
                        combatente.defender()

                    elif acao == 'atacar':
                        inimigo = inimigos_disponiveis.get(alvo)
                        if inimigo is not None:
                            if inimigo in self.grupo_inimigos:
                                combatente.atacar(inimigo)
                            else:
                                print('Esse inimigo não está na luta!')
                        else:
                            print('Inimigo não encontrado')

                    else:
                        print('Comando não reconhecido!')


                elif combatente in self.grupo_inimigos:
                    print(f'Turno do {combatente.nome}')

                    if combatente.defendendo:
                        combatente.remover_defesa()

                    acao = random.choices(
                    ['atacar', 'defender'],
                    weights=[
                    combatente.prob_ataque,
                    100 - combatente.prob_ataque
                    ])[0]
                    if acao == 'atacar':
                        alvo = self.escolher_alvo()
                        if alvo:
                            combatente.atacar(alvo)

                    elif acao == 'defender':
                        combatente.defender()

        if not any(personagem.vida > 0 for personagem in self.grupo_jogador):
            print('Você Perdeu!')
        elif not any(inimigo.vida > 0 for inimigo in self.grupo_inimigos):
            print('Você venceu!!!')

    def escolher_alvo(self):
        personagens_vivos = [
            personagem for personagem in self.grupo_jogador
            if personagem.vida > 0
        ]
        if personagens_vivos:
            alvo = random.choice(personagens_vivos)
            return alvo

        return None
    
luta = Luta(grupo_jogador, grupo_inimigos)

