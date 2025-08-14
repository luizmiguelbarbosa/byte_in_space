import pygame
from config import *
class Nave(pygame.sprite.Sprite):
    def __init__(self, vel_base):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('assets/imagens/sprite_nave.png'), (NAVE_LARGURA, NAVE_ALTURA))
        self.rect = pygame.Rect(estado["nave_x"]+10, estado["nave_y"]+20, NAVE_LARGURA-20, NAVE_ALTURA-35) #RECT USADO PARA COLISÃO E MOVIMENTO
        self.speed = vel_base
    def desenhar(self):
        TELA.blit(self.image, (self.rect.x, self.rect.y))
    
    
    def update(self):
        #DEFINIÇÃO DA VELOCIDADE
        global estado
        agora = pygame.time.get_ticks()
        self.speed = self.speed * (2 if agora < estado["turbo_ate"] else 1)
        
        #MOVIMENTO
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.rect.x -= self.speed
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.rect.x += self.speed
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.rect.y -= self.speed
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.rect.y += self.speed

        #LIMITES DE TELA
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > LARGURA - NAVE_LARGURA:
            self.rect.x = LARGURA - NAVE_LARGURA
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > ALTURA - NAVE_ALTURA:
            self.rect.y = ALTURA - NAVE_ALTURA
        
        