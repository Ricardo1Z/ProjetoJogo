import pygame
LARGURA = 1280
ALTURA = 720
tela = pygame.display.set_mode((LARGURA, ALTURA))


#BOTÕES
botoes_selecao = [
pygame.Rect(100, 160, 220, 220),
pygame.Rect(388, 160, 220, 220),
pygame.Rect(670, 160, 220, 220),
pygame.Rect(956, 160, 220, 220),
pygame.Rect(100, 434, 220, 220),
pygame.Rect(388, 434, 220, 220),
pygame.Rect(670, 434, 220, 220),
pygame.Rect(956, 434, 220, 220)
]

botoes_menu = [
pygame.Rect(185, 340, 310, 80),
pygame.Rect(160, 442, 365, 82),
pygame.Rect(215, 540, 250, 80)
]

clique_menu = [
    'selecao',
    'opcao',
    'sair'
]

botao_voltar = pygame.Rect(10, 650, 170, 65)

#IMAGENS
menu = pygame.image.load('jogo/assets/sprites/tela_menu.png').convert()
selecao = pygame.image.load('jogo/assets/sprites/tela_selecao.png').convert()
cursor_vertical = pygame.image.load('jogo/assets/sprites/cursor.png').convert_alpha()
cursor = pygame.image.load("jogo/assets/sprites/cursor2.png").convert_alpha()

#REDISIONAMENTO
menu = pygame.transform.scale(menu, (LARGURA, ALTURA))
selecao = pygame.transform.scale(selecao,(LARGURA, ALTURA))
cursor = pygame.transform.scale(cursor, (32, 32))


def tela_menu(tela, mouse):
    tela.blit(menu, (0,0))

    for botao_m in botoes_menu:
        if botao_m.collidepoint(mouse):
            tela.blit(cursor, (botao_m.left - 35, botao_m.centery - 16))

def tela_selecao(tela, mouse):

    tela.blit(selecao, (0,0))
    for botao in botoes_selecao:
        if botao.collidepoint(mouse):
            tela.blit(cursor_vertical, (botao.right - 120, botao.centery - 155))