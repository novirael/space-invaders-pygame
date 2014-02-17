import pygame
from pygame.locals import *
from sys import exit
from random import randint,choice
from math import *


class Barykada(pygame.sprite.Sprite):
  def __init__(self, pos):
     pygame.sprite.Sprite.__init__(self)
     self.x, self.y = pos
     self.image = pygame.Surface( (100,50) )
     self.image = pygame.Surface( (5,5) )
     self.image.fill( (80,0,0) )
     self.rect = pygame.Rect(0, 0, 5, 5)
     self.rect.centerx = self.x
     self.rect.centery = self.y

  def update(self):
     self.rect.centerx = self.x
     self.rect.centery = self.y
     #position = (self.x, self.y)
     
  def draw(self, screen):
     screen.blit(self.image, (self.rect.left,self.rect.top) )
