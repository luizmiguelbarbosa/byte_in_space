import pygame
from pygame.locals import *
import cv2  # Para a cutscene
from config import *
from entities.coletavel import Coletavel
from entities.eventos import processar_eventos
from entities.update import atualizar
from entities.render import renderizar, desenhar_menu, desenhar_game_over

pygame.init()
pygame.mixer.init()
pygame.font.init()

# Configurações iniciais
largura = LARGURA
altura = ALTURA
tela = pygame.display.set_mode((largura, altura))  # Sem redimensionamento
pygame.display.set_caption("Byte in Space")
icone = pygame.image.load('assets/imagens/icone_janela.png')
pygame.display.set_icon(icone)

imagem_menu_original = pygame.image.load('assets/imagens/imagem_menu.png')
imagem_menu = pygame.transform.scale(imagem_menu_original, (largura, altura))

cenario_original = pygame.image.load('assets/imagens/cenario1.png').convert()
cenario = pygame.transform.scale(cenario_original, (largura, altura))

def criar_botoes(largura, altura):
    botao_start = pygame.Rect(largura * 0.4, altura * 0.45, largura * 0.25, altura * 0.1)
    botao_diffcuty = pygame.Rect(largura * 0.4, altura * 0.6, largura * 0.25, altura * 0.1)
    botao_credits = pygame.Rect(largura * 0.4, altura * 0.75, largura * 0.25, altura * 0.1)
    return botao_start, botao_diffcuty, botao_credits

botao_start, botao_diffcuty, botao_credits = criar_botoes(largura, altura)

# Estado do jogo
estado = {
    "largura": largura,
    "altura": altura,
    "tela": tela,
    "icone": icone,
    "imagem_menu_original": imagem_menu_original,
    "imagem_menu": imagem_menu,
    "cenario_original": cenario_original,
    "cenario": cenario,
    "cenario_y1": 0,
    "cenario_y2": -altura,
    "velocidade_cenario": VELOCIDADE_BASE_CENARIO * (altura / ALTURA_BASE),
    "botao_start": botao_start,
    "botao_diffcuty": botao_diffcuty,
    "botao_credits": botao_credits,
    "jogo_rodando": False,
    "mostrar_texto_fase": False,
    "tempo_inicio_fase": 0,
    "sprite_nave": pygame.transform.scale(pygame.image.load('assets/imagens/sprite_nave.png'), (NAVE_LARGURA, NAVE_ALTURA)),
    "nave_x": largura // 2 - NAVE_LARGURA//2,
    "nave_y": altura - 80,
    "velocidade_nave": VELOCIDADE_NAVE_BASE,
    "velocidade_nave_base": VELOCIDADE_NAVE_BASE,
    "tiros": [],
    "som_tiro": pygame.mixer.Sound('assets/musicas/tiro.mp3'),
    "velocidade_tiro": VELOCIDADE_TIRO,
    "sprite_inimigo": pygame.transform.scale(pygame.image.load('assets/imagens/sprite_inimigo.png'), (60, 60)),
    "inimigos": [],
    "coletaveis": [],
    "velocidade_coletavel": VELOCIDADE_COLETAVEL,
    "y_max_inimigo": altura // 2,
    "intervalo_spawn_inimigo": INTERVALO_SPAWN_INIMIGO,
    "tempo_ultimo_inimigo": pygame.time.get_ticks(),
    "fonte_fase": pygame.font.SysFont(None, 60),
    "texto_fase": pygame.font.SysFont(None, 60).render('Fase 1', True, (255, 255, 255)),
    "contagem_coletaveis": {'computador': 0, 'circuito': 0, 'dados': 0},
    "imune_ate": 0,
    "turbo_ate": 0,
    "furia_ate": 0,
    "sprite_coletaveis": {
        'computador': pygame.transform.scale(pygame.image.load('assets/imagens/computador.png'), (Coletavel.TAM, Coletavel.TAM)),
        'circuito': pygame.transform.scale(pygame.image.load('assets/imagens/circuito.png'), (Coletavel.TAM, Coletavel.TAM)),
        'dados': pygame.transform.scale(pygame.image.load('assets/imagens/dados.png'), (Coletavel.TAM, Coletavel.TAM)),
    },
    "game_over": False,
    "tempo_game_over": 0,
    "fonte_game_over": pygame.font.SysFont(None, 80),
    "texto_game_over": pygame.font.SysFont(None, 80).render('GAME OVER', True, (255, 0, 0)),
    "fonte_item": pygame.font.SysFont(None, 30),
    "musica_fase1": 'assets/musicas/musica_start.mp3',
}

clock = pygame.time.Clock()

# --- Variáveis da cutscene ---
cutscene_ativa = True
cutscene_video = cv2.VideoCapture('assets/videos/cutscene1.mp4')

# Loop principal
while True:
    clock.tick(FPS)

    if cutscene_ativa:
        ret, frame = cutscene_video.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], "RGB")
            tela.blit(pygame.transform.scale(frame, (largura, altura)), (0, 0))
            pygame.display.update()
        else:
            # Se o vídeo acabar
            cutscene_ativa = False
            cutscene_video.release()
            pygame.mixer.music.load('assets/musicas/musica_jogo.mp3')
            pygame.mixer.music.play(-1)

        # Eventos de pulo/cancelamento da cutscene
        for event in pygame.event.get():
            if event.type == QUIT:
                cutscene_video.release()
                pygame.quit()
                exit()
            if event.type in (KEYDOWN, MOUSEBUTTONDOWN):
                cutscene_ativa = False
                cutscene_video.release()
                pygame.mixer.music.load('assets/musicas/musica_jogo.mp3')
                pygame.mixer.music.play(-1)

    else:
        processar_eventos(estado)
        atualizar(estado)

        if estado["game_over"]:
            desenhar_game_over(estado)
            if pygame.time.get_ticks() - estado["tempo_game_over"] >= 2000:
                estado["game_over"] = False
                estado["jogo_rodando"] = False
        elif estado["jogo_rodando"]:
            renderizar(estado)
        else:
            desenhar_menu(estado)

        pygame.display.update()
