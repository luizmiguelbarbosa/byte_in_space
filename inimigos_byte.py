import pygame

from bullet import Bullet

class Enemy(pygame.sprite.Sprite): #a classe que vai defenir as propriedades gerais de inimigos do byte
    #ATRIBUTOS/FIELDS DE QUALQUER INSTÂNCIA DE ENEMY
    def __init__ (self, tipo, posicao, speed,  y_max_inimigo): #INICIA O CONSTRUTOR DA CLASSE.
        super().__init__()
        imagem_enemy = pygame.image.load(f"C:/Users/mique/byte_in_space/imagens/inimigo{tipo}.png")
        self.image = pygame.transform.scale(imagem_enemy, (40, 40))
        self.rect = self.image.get_rect(topleft = posicao) #POSIÇÃO É UMA TUPLA (X,Y)
        self.vida = True
        self.speed = speed
        self.y_max = y_max_inimigo
    
    def constrain_mov(self):
        if self.rect.bottom > self.y_max:
            self.rect.bottom = self.y_max
    def update(self):
        self.rect.y -= self.speed
        self.constrain_mov()

