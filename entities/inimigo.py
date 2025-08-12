import pygame
from random import randint

class Inimigo:
    def __init__(self, largura, altura, sprite):
        self.x = randint(0, largura - 40)
        self.y = randint(-200, -40)
        self.sprite = sprite
        self.altura_tela = altura

    def atualizar(self):
        self.y += 1

    def desenhar(self, tela):
        tela.blit(self.sprite, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, 75, 75)
