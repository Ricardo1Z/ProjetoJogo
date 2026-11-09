
import random


class Luta:
    def __init__(self, grupo_jogador, grupo_inimigos):
        self.grupo_jogador = grupo_jogador
        self.grupo_inimigos = grupo_inimigos

        self.participantes = grupo_jogador + grupo_inimigos

        self.ordem_turnos = sorted(
            self.participantes,
            key=lambda c: c.velocidade,
            reverse=True
        )

        self.indice_turno = 0
        self.tempo_inimigo = 0
        self.resultado = None

    def combatente_atual(self):
        if self.resultado:
            return None

        if not self.ordem_turnos:
            return None

        return self.ordem_turnos[self.indice_turno]

    def verificar_fim(self):
        jogadores_vivos = any(
            p.vida > 0 for p in self.grupo_jogador
        )

        inimigos_vivos = any(
            i.vida > 0 for i in self.grupo_inimigos
        )

        if not jogadores_vivos:
            self.resultado = "derrota"

        elif not inimigos_vivos:
            self.resultado = "vitoria"

    def avancar_turno(self):
        self.verificar_fim()

        if self.resultado:
            return

        quantidade = len(self.ordem_turnos)

        for _ in range(quantidade):
            self.indice_turno = (
                self.indice_turno + 1
            ) % quantidade

            combatente = self.combatente_atual()

            if combatente and combatente.vida > 0:
                return

    def executar_acao_jogador(self, acao, alvo=None):
        combatente = self.combatente_atual()

        if combatente not in self.grupo_jogador:
            return

        if combatente.vida <= 0:
            return

        if acao == "atacar":
            if alvo not in self.grupo_inimigos:
                return

            if alvo.vida <= 0:
                return

            combatente.atacar(alvo)

        elif acao == "defender":
            combatente.defender()

        else:
            return

        self.avancar_turno()

    def atualizar(self):
        self.verificar_fim()

        if self.resultado:
            return

        combatente = self.combatente_atual()

        if combatente in self.grupo_inimigos:
            self.tempo_inimigo += 1

            # Espera um pouco antes da ação do inimigo
            if self.tempo_inimigo >= 45:
                self.tempo_inimigo = 0

                acao = combatente.escolher_acao()

                if acao == "atacar":
                    alvos = [
                        p for p in self.grupo_jogador
                        if p.vida > 0
                    ]

                    if alvos:
                        alvo = random.choice(alvos)
                        combatente.atacar(alvo)

                elif acao == "defender":
                    combatente.defender()

                elif acao == "fugir":
                    print(f"{combatente.nome} fugiu!")

                    self.grupo_inimigos.remove(combatente)
                    self.ordem_turnos.remove(combatente)

                    if self.indice_turno >= len(self.ordem_turnos):
                        self.indice_turno = 0

                    self.verificar_fim()
                    return

                self.avancar_turno()
        else:
            self.tempo_inimigo = 0




