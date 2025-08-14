import pygame
from config import ALTURA
class Bullet(pygame.sprite.Sprite):
    def __init__(self, speed, x, y):
        super().__init__()
        sprite = pygame.image.load("assets/lasers/14(c).png")
        self.image = pygame.transform.rotate(pygame.transform.scale(sprite, (20, 5)), -90)
        self.rect = self.image.get_rect(center = (x, y))
        self.speed = speed
    
    def update(self):
        self.rect.y += self.speed
        if(self.rect.y) > ALTURA:
            self.kill()