import pygame
#0 - projetil; 1- missil; 2 - laser
class Bullet(pygame.sprite.Sprite):
    def __init__ (self, tipo, posicao, screen_altura, speed):
        super().__init__()
        if(tipo == 0):
            self.image = pygame.Surface((4, 15))
            self.image.fill((0, 0, 255))
        elif(tipo == 1):
            self.image = pygame.Surface((4, 15))
            self.image.fill((255, 0, 0))
        elif(tipo == 2):
            self.image = pygame.Surface((4, 15))
            self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center = posicao)
        self.altura = screen_altura
        self.speed = speed
    
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y > self.altura + 15 or self.rect.y < 0:
            self.kill()