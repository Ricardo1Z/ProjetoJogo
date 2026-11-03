class Combatente:
    def __init__(self, nome, vida, ataque, defesa, velocidade):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade

    def verificar_vida(self):
        if self.vida <= 0:
            print(f'O {self.nome} foi derrotado!!!')

    def atacar(self, alvo):
        if self.vida > 0 and alvo.vida > 0:
            dano_real = max(1, self.ataque - alvo.defesa)
            alvo.vida = max(0, alvo.vida - dano_real)
            print(f'{self.nome} atacou {alvo.nome} e causou {dano_real} de dano!')
            print(f'{alvo.nome} tem de {alvo.vida} vida restante!')
            return dano_real
        elif alvo.vida == 0:
            print(f'O {alvo.nome} já está derrotado!!!')
        else:
            print(f'O {self.nome} está derrotado e não pode agir!')
