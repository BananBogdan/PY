import pygame
import sys
from image import *

class Cart:
    def __init__(self,height,screen):
        self.height = height
        self.screen = screen
        self.image = Image('cart').get()
        self.image = pygame.transform.scale(self.image, (200,300))
        self.rect = self.image.get_rect()
        self.rect.y = self.height - 300
        self.rect.x = 300
    def blit(self):
        self.screen.blit(self.image, self.rect)
