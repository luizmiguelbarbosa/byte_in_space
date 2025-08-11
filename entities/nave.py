import pygame
from config import NAVE_LARGURA, NAVE_ALTURA, VELOCIDADE_NAVE_BASE

class Nave:
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.largura = NAVE_LARGURA
        self.altura = NAVE_ALTURA
        self.sprite = sprite
        self.velocidade = VELOCIDADE_NAVE_BASE

    def mover(self, teclas, largura_tela, altura_tela):
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.x -= self.velocidade
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.x += self.velocidade
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.y -= self.velocidade
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.y += self.velocidade
        self.x = max(0, min(self.x, largura_tela - self.largura))
        self.y = max(0, min(self.y, altura_tela - self.altura))

    def desenhar(self, tela):
        tela.blit(self.sprite, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)
