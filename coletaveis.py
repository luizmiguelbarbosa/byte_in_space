import pygame

class Coletavel:
    TAM = 30

    def __init__(self, x, y, tipo):
        # tipo deve ser 'computador', 'circuito' ou 'dados'
        self.tipo = tipo
        self.rect = pygame.Rect(x, y, self.TAM, self.TAM)

    def desenhar(self, superficie):
        # desenha usando sprite específico do tipo
        superficie.blit(sprite_coletaveis[self.tipo], self.rect.topleft)