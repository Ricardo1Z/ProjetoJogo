
import pygame

from rpg.telas import (
    tela_selecao,
    tela_menu,
    clique_menu,
    botoes_menu,
    botao_voltar,
    botoes_selecao
)

from rpg.personagens import personagens_liberados

personagens_selecionados = []

pygame.init()
rodando = True
ALTURA = 720
LARGURA = 1280

tela = pygame.display.set_mode((LARGURA, ALTURA))
clock = pygame.time.Clock()

tela_atual = "menu"

while rodando:
    mouse = pygame.mouse.get_pos()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:

            if tela_atual == 'menu':
                for i, botao_m in enumerate(botoes_menu):
                    if botao_m.collidepoint(evento.pos):
                        if clique_menu[i] == 'sair':
                            rodando = False
                        else:
                            tela_atual = clique_menu[i]

            elif tela_atual == 'selecao':
                if botao_voltar.collidepoint(evento.pos):
                    tela_atual = 'menu'

                else:
                    for i, botao in enumerate(botoes_selecao):
                        if botao.collidepoint(evento.pos):

                            if i >= len(personagens_liberados):
                                break

                            if i in personagens_selecionados:
                                personagens_selecionados.remove(i)

                            elif len(personagens_selecionados) < 4:
                                personagens_selecionados.append(i)

                            break

    if tela_atual == 'menu':
        tela_menu(tela, mouse)

    elif tela_atual == 'selecao':
        tela_selecao(tela, mouse, personagens_selecionados)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
