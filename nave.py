import pygame
from bullet import Bullet

class Nave(pygame.sprite.Sprite):
    def __init__(self, screen_largura, screen_altura, speed, delay): #delay de tiros
        super().__init__()
        self.largura = screen_largura
        self.altura = screen_altura
        self.speed = speed
        
        sprite_nave = pygame.image.load("C:/Users/mique/byte_in_space/imagens/sprite_nave.png")
        self.image = pygame.transform.scale(sprite_nave, (75, 75))
        self.rect = self.image.get_rect(midbottom = (self.largura/2, self.altura))

        self.bullets_group = pygame.sprite.Group()
        self.bullet_ready = True
        self.bullet_time = 0
        self.bullet_delay = delay
        
    def Atirar(self):
        disparo = Bullet(tipo=0, posicao=self.rect.center, screen_altura=self.altura, speed=12)#esse speed é o da bala, diferente do self.speed
        self.bullets_group.add(disparo)
        self.bullet_time = pygame.time.get_ticks()

    def inputs_usuario(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
        
        if keys[pygame.K_z] and self.bullet_ready:
            self.bullet_ready = False
            self.Atirar()

    def update(self): #atualizado por frame. Chamado por grupo
        self.inputs_usuario()
        self.constrain_mov()
        self.bullets_group.update()
        self.recarregar_disparo()
    
    def recarregar_disparo(self):
        if not self.bullet_ready:
            atual = pygame.time.get_ticks()
            if atual - self.bullet_time >= self.bullet_delay:
                self.bullet_ready = True
    
    def constrain_mov(self):
        if self.rect.right > self.largura:
            self.rect.right = self.largura
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.altura:
            self.rect.bottom = self.altura
        

