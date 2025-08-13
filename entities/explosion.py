import pygame 
from config import TELA

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.index = 0
    
        explosion_frames = []
        for i in range(1, 5):  
            img = pygame.image.load(f"assets/imagens/Explosion/explosion{i}.png")
            img = pygame.transform.scale(img, (64, 64))  # Ajusta tamanho
            explosion_frames.append(img)
        self.frames = explosion_frames
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.frame_delay = 5  # esse numero define o numero de frames por imagem
        self.counter = 0
    
    def update(self): #visto que isso é chamado por frame
        self.counter += 1
        if self.counter >= self.frame_delay:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.frames):
                self.kill()  # Remove explosão quando terminar
            else:
                self.image = self.frames[self.index]