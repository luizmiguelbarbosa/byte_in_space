import pygame
from pygame.locals import *
from config import *
from entities.inimigo import Inimigo
from sys import exit


def processar_eventos(estado):
    for event in pygame.event.get():
        # Sair do jogo
        if event.type == QUIT:
            pygame.quit()
            exit()

        # Clique do mouse 
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            if not estado["jogo_rodando"] and not estado["game_over"]:
                if estado["botao_start"].collidepoint(event.pos):
                    iniciar_jogo(estado)
                elif estado["botao_diffcuty"].collidepoint(event.pos):
                    print("Dificuldade")
                elif estado["botao_credits"].collidepoint(event.pos):
                    print("Mostrar créditos")

        # Teclas
        elif event.type == KEYDOWN:
            # MENU → iniciar com espaço
            if event.key == K_SPACE and not estado["jogo_rodando"] and not estado["game_over"]:
                iniciar_jogo(estado)

            # JOGO → disparar tiros com z
            if event.key == K_z and estado["jogo_rodando"] and not estado["game_over"]:
                disparar_tiro(estado)


def iniciar_jogo(estado):
    pygame.mixer.music.stop()
    pygame.mixer.music.load('assets/musicas/musica_start.mp3')
    pygame.mixer.music.play(-1)
    estado["jogo_rodando"] = True
    estado["mostrar_texto_fase"] = True
    estado["tempo_inicio_fase"] = pygame.time.get_ticks()
    estado["inimigos"].clear()
    estado["coletaveis"].clear()
    estado["tiros"].clear()
    estado["contagem_coletaveis"] = {'computador': 0, 'circuito': 0, 'dados': 0}
    estado["imune_ate"] = 0
    estado["turbo_ate"] = 0
    estado["furia_ate"] = 0

    for _ in range(QUANT_INIMIGOS_INICIO):
        estado["inimigos"].append(
            Inimigo(estado["largura"], estado["altura"], estado["sprite_inimigo"])
        )


def disparar_tiro(estado):
    agora = pygame.time.get_ticks()
    centro_tiro = estado["nave_x"] + (NAVE_LARGURA // 2) - 2
    if agora < estado["furia_ate"]:
        estado["tiros"].extend([
            [centro_tiro - 12, estado["nave_y"]],
            [centro_tiro, estado["nave_y"]],
            [centro_tiro + 12, estado["nave_y"]],
        ])
    else:
        estado["tiros"].append([centro_tiro+22, estado["nave_y"]])
    estado["som_tiro"].play()


def criar_botoes(largura, altura):
    botao_start = pygame.Rect(largura * 0.4, altura * 0.45, largura * 0.25, altura * 0.1)
    botao_diffcuty = pygame.Rect(largura * 0.4, altura * 0.6, largura * 0.25, altura * 0.1)
    botao_credits = pygame.Rect(largura * 0.4, altura * 0.75, largura * 0.25, altura * 0.1)
    return botao_start, botao_diffcuty, botao_credits
