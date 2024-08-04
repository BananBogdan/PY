import pygame
import sys
from image import *


class Box:
    def __init__(self, screen, width, height, color, speed):

        Image()
        self.speed = speed
        self.color = color  # KAKI!!!!!!!!!!!!!!!!
        self.screen = screen
        self.screen_width = width
        self.screen_height = height

        self.width = 400
        self.height = 100

        self.box_up = False
        self.box_down = False
        self.box_right = False
        self.box_left = False

        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)

        self.image = pygame.transform.scale(self.image, (self.box_arr[0].width, self.box_arr[0].height ))
        self.image_rect.x = self.image.get_rect()
        self.image_rect.y = self.image.get_rect()

        self.image_rect.x = self.box_arr[0].x
        self.image_rect.y = self.box_arr[0].y
        

    def move_box(self):
        if self.box_up == True and self.y > 0:
            self.image_rect.y -= self.speed
        if self.box_down == True and self.y < self.screen_height - self.height:
            self.image_rect.y += self.speed
        if self.box_right == True and self.x < self.screen_width - self.width:
            self.image_rect.x += self.speed
        if self.box_left == True and self.x > 0:
            self.image_rect.x -= self.speed


    def rectCeate(self):
         self.screen.blit(self.image, self.image_rect)
    


