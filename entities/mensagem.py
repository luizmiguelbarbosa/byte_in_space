import pygame
pygame.font.init()

class Mensagem(pygame.sprite.Sprite):
    def __init__(self, texto, cor, X_enemy, Y_enemy): # X e Y são coordenadas do vértice superior esquerdo
        super().__init__()
        fonte = pygame.font.Font("assets/fontes/arcade/ARCADE.TTF", 35)
        msg_ponto = fonte.render(texto, False, cor)
        self.image = msg_ponto
        self.rect = pygame.rect.Rect(X_enemy+2,Y_enemy+15, 60, 44)
        self.alpha = 255 #alpha trata-se da transparência da imagem
    
       
    def update(self):
        if self.alpha > 0:
            self.alpha -= 5
            self.image.set_alpha(self.alpha)

        self.rect.y -= 3
        if self.alpha <= 0:
            self.kill()

        
