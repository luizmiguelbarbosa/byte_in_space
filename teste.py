import pygame
from pygame.locals import *
from sys import exit
from moviepy.editor import VideoFileClip
import numpy as np

pygame.init()

largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura), RESIZABLE)
pygame.display.set_caption("Byte in Space")

icone = pygame.image.load('assets/imagens/icone_janela.png')
pygame.display.set_icon(icone)

# Carregar vídeo com moviepy
cutscene = VideoFileClip("videos/cutscene_1.mp4")

def exibir_video():
    global largura, altura, tela
    clock = pygame.time.Clock()
    
    for frame in cutscene.iter_frames(fps=24, dtype="uint8"):  # lê os frames
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == VIDEORESIZE:
                largura, altura = event.w, event.h
                tela = pygame.display.set_mode((largura, altura), RESIZABLE)

        frame_surface = pygame.surfarray.make_surface(np.rot90(frame))  # Corrige a orientação
        frame_surface = pygame.transform.scale(frame_surface, (largura, altura))
        tela.blit(frame_surface, (0, 0))
        pygame.display.update()
        clock.tick(24)

def exibir_menu():
    # Coloque aqui sua função de menu normalmente
    print("Mostrar menu...")

# Executar vídeo e depois o menu
exibir_video()
exibir_menu()
