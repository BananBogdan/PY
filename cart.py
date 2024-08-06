import pygame
import sys
from image import *

class Cart:
    def __init__(self,image,rect):

        self.image = Image('cart').get()
        self.image = pygame.transform.scale(self.image, (200,300))
        self.rect = self.image.get_rect()
        self.rect.y = self.height - 300
        self.rect.x = 300
        self.screen.blit(self.image, self.rect)