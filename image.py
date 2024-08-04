import pygame
import sys


class Image:
    def __init__(self) -> None:

        self.images = []
        for i in range(0,118):
            self.image = pygame.image.load(f"t2x2/{i}.gif")
            self.images.append(self.image)

        self.loop = 0

    def get(self):
        self.loop += 1           
        if self.loop >= 117:
            self.loop = 0
        return self.images[self.loop]
