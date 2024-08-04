import pygame
import sys


class Image:
    def __init__(self) -> None:

        self.images = []
        for i in range(0,118):
            self.image = pygame.image.load(f"t2x2/{i}.gif")
            self.images.append(self.image)
        self.image_rect = self.image.get_rect()

        self.loop = 0

        self.loop += 1           
        if self.loop >= 117:
            self.loop = 0

        self.screen.blit(self.images[self.loop], self.image_rect)
