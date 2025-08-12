import pygame
from config import *

def renderizar(estado):
    tela = estado["tela"]

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

    # Nave
    tela.blit(estado["sprite_nave"], (estado["nave_x"], estado["nave_y"]))

    # Aura ESCUDO
    if pygame.time.get_ticks() < estado["imune_ate"]:
        rect_nave = pygame.Rect(estado["nave_x"], estado["nave_y"], NAVE_LARGURA, NAVE_ALTURA)
        pygame.draw.rect(tela, (0, 200, 255), rect_nave.inflate(10, 10), 3, border_radius=6)

    # Tiros
    for tiro in estado["tiros"]:
        pygame.draw.rect(tela, (255, 0, 0), (tiro[0], tiro[1], 4, 10))

    # Inimigos
    for inimigo in estado["inimigos"]:
        inimigo.desenhar(tela)

    # Coletáveis
    for c in estado["coletaveis"]:
        c.desenhar(tela, estado["sprite_coletaveis"])

    # HUD
    fonte_item = estado["fonte_item"]

    texto_e = fonte_item.render(f'Computadores: {estado["contagem_coletaveis"]["computador"]}', True, (0, 200, 255))
    texto_t = fonte_item.render(f'Circuitos: {estado["contagem_coletaveis"]["circuito"]}', True, (255, 200, 0))
    texto_f = fonte_item.render(f'Dados: {estado["contagem_coletaveis"]["dados"]}', True, (255, 80, 80))

    x_hud, y_hud = 10, 10
    tela.blit(texto_e, (x_hud, y_hud))
    tela.blit(texto_t, (x_hud, y_hud + texto_e.get_height() + 4))
    tela.blit(texto_f, (x_hud, y_hud + texto_e.get_height() + texto_t.get_height() + 8))

def desenhar_menu(estado):
    estado["tela"].blit(estado["imagem_menu"], (0, 0))

def desenhar_game_over(estado):
    tela = estado["tela"]
    tela.blit(estado["cenario"], (0, 0))
    texto = estado["texto_game_over"]
    tela.blit(texto, (estado["largura"] // 2 - texto.get_width() // 2,
                      estado["altura"] // 2 - texto.get_height() // 2))
