import pygame
import sys


class Box:
    def __init__(self, screen, width, height, color, speed):
        self.speed = speed
        self.color = color
        self.screen = screen
        self.width = width
        self.height = height

        self.width = 100
        self.height = 100

        self.box_up = False
        self.box_down = False
        self.box_right = False
        self.box_left = False

        self.x = (800 / 2) - (self.width / 2)
        self.y = (600 / 2) - (self.height / 2)

    def move_box(self):
        if self.box_up == True and self.y > 0:
            self.y -= self.speed
        if self.box_down == True and self.y < 500:
            self.y += self.speed
        if self.box_right == True and self.x < 700:
            self.x += self.speed
        if self.box_left == True and self.x > 0:
            self.x -= self.speed

    def rectCeate(self):
        self.rect = pygame.draw.rect(
            self.screen, self.color, (self.x, self.y, self.width, self.height)
        )

