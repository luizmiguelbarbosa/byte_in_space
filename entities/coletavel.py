import pygame

class Coletavel:
    TAM = 30
    def __init__(self, x, y, tipo):
        self.tipo = tipo
        self.rect = pygame.Rect(x, y, self.TAM, self.TAM)

    def desenhar(self, superficie, sprites):
        superficie.blit(sprites[self.tipo], self.rect.topleft)

