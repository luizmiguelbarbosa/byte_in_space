import pygame
from config import *

#função chamada na main para desenhar/renderizar todos os objetos, seja via métodos internos do próprio objeto, seja
#via extração de rect e métodos do próprio pygame. Chamada por interação do lopping principal
def renderizar(estado):
    tela = TELA

    # Cenário
    tela.blit(estado["cenario"], (0, estado["cenario_y1"]))
    tela.blit(estado["cenario"], (0, estado["cenario_y2"]))

    # Texto Fase
    if estado["mostrar_texto_fase"]:
        agora = pygame.time.get_ticks()
        if agora - estado["tempo_inicio_fase"] <= 2000:
            texto_rect = estado["texto_fase"].get_rect(center=(estado["largura"] // 2, estado["altura"] // 2))
            tela.blit(estado["texto_fase"], texto_rect)
        else:
            estado["mostrar_texto_fase"] = False

    #DESENHA A NAVE VIA MÉTODO BLIT E COORDENADAS DA NAVE, JUNTO A SEU SPRITE
    tela.blit(estado["sprite_nave"], (estado["nave_x"], estado["nave_y"]))

    #DESENHA O ESCUDO, QUANDO POSSÍVEL/NECESSÁRIO
    if pygame.time.get_ticks() < estado["imune_ate"]:
        rect_nave = pygame.Rect(estado["nave_x"], estado["nave_y"], NAVE_LARGURA, NAVE_ALTURA)
        pygame.draw.rect(tela, (0, 200, 255), rect_nave.inflate(10, 10), 3, border_radius=6)

    #DESENHA OS TIROS, DE COORDENADAS ARMAZENADAS EM ESTADO["TIROS"], VIA RECT
    tiro_byte = pygame.image.load("assets/lasers/11(c).png")
    for tiro in estado["tiros"]:
        tela.blit(pygame.transform.rotate(pygame.transform.scale(tiro_byte, (20, 5)), 90),(tiro[0], tiro[1]))

    #DESENHA OS INIMIGOS CHAMANDO O MÉTODO DESENHAR DE CADA OBJETO ARMAZENADO NO ARRAY ESTADO["INIMIGOS"]
    for inimigo in estado["inimigos"]:
        inimigo.desenhar(tela)
    
    #DESENHA AS MENSAGENS A PARTIR DO ARRAY ESTADO["MENSAGENS"], DONDE CADA ELEMENTO É UM ARRAY DA FORMA: [MSG_PONTO, RECT]
    estado["mensagens"].draw(tela)

    # Coletáveis
    for c in estado["coletaveis"]:
        c.desenhar(tela, estado["sprite_coletaveis"])

    # HUD
    fonte_item = pygame.font.SysFont(None, 30)
    fonte_pont = pygame.font.SysFont(None, 30)

    texto_e = fonte_item.render(f'Computadores: {estado["contagem_coletaveis"]["computador"]}', True, (0, 200, 255))
    texto_t = fonte_item.render(f'Circuitos: {estado["contagem_coletaveis"]["circuito"]}', True, (255, 200, 0))
    texto_f = fonte_item.render(f'Dados: {estado["contagem_coletaveis"]["dados"]}', True, (255, 80, 80))

    texto_pont = fonte_item.render(f'Objetivo: {estado["pontuacao"]}/{MAX_PONTUACAO}', True, (255, 255, 255))

    x_hud, y_hud = 10, 10
    tela.blit(texto_e, (x_hud, y_hud))
    tela.blit(texto_t, (x_hud, y_hud + texto_e.get_height() + 4))
    tela.blit(texto_f, (x_hud, y_hud + texto_e.get_height() + texto_t.get_height() + 8))
    
    #DESENHAR PONTUAÇÃO
    tela.blit(texto_pont, (LARGURA - texto_pont.get_width() - 10, 30))

def desenhar_menu(estado):
    TELA.blit(estado["imagem_menu"], (0, 0))

def desenhar_game_over(estado):
    tela = TELA
    tela.blit(estado["cenario"], (0, 0))
    texto = estado["texto_game_over"]
    tela.blit(texto, (estado["largura"] // 2 - texto.get_width() // 2,
                      estado["altura"] // 2 - texto.get_height() // 2))

def desenhar_game_win(estado):
    tela = TELA
    tela.blit(estado["cenario"], (0, 0))
    texto = estado["texto_venceu"]
    tela.blit(texto, (estado["largura"] // 2 - texto.get_width() // 2,
                      estado["altura"] // 2 - texto.get_height() // 2))
    