import pygame
import sys
from image import *


class Box:
    def __init__(self, screen, width, height, speed):

        self.speed = speed
        self.screen = screen
        self.screen_width = width
        self.screen_height = height

        self.box_up = False
        self.box_down = False
        self.box_right = False
        self.box_left = False

        self.image = Image('t2x2')

        #self.image = pygame.transform.scale(self.image, (self.box_arr[0].width, self.box_arr[0].height ))

        self.rect = self.image.images[0].get_rect()

        self.rect.x = (self.screen_width / 2) - (self.rect.width / 2)
        self.rect.y = (self.screen_height / 2) - (self.rect.height / 2)


        

    def move_box(self):
        if self.box_up == True and self.rect.y > 0:
            self.rect.y -= self.speed
        if self.box_down == True and self.rect.y < self.screen_height - self.rect.height:
            self.rect.y += self.speed
        if self.box_right == True and self.rect.x < self.screen_width - self.rect.width:
            self.rect.x += self.speed
        if self.box_left == True and self.rect.x > 0:
            self.rect.x -= self.speed


    def rectCeate(self):
         self.screen.blit(self.image.get(), self.rect)
    


