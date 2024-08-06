import pygame
import sys


class Image:
    def __init__(self, path) -> None:
        self.images = []
        self.image = pygame.image.load(f"{path}/{1}.gif")
        self.images.append(self.image)
        # for i in range(0):

        # self.loop = 0

    def get(self):
        # self.loop += 1           
        # if self.loop >= 117:
        #     self.loop = 0
        return self.images[0]
