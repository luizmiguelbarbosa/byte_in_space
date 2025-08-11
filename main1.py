import pygame
from sys import exit
from inimigos_byte import Enemy

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Space Invaders")

clock = pygame.time.Clock()

#GRUPO DE OBJETOS ENEMY
enemies_group = pygame.sprite.Group()

while True:
    #HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    #UPDATING
    

    #DRAWING
    screen.fill((29, 29, 27))



    pygame.display.update()
    clock.tick(60)


