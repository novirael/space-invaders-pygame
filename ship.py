import pygame
from pygame.locals import *
from sys import exit
from random import randint,choice
from math import *
from kula import Bullet
from pygame.constants import *

my_ship_tex = 'img/s0.png'

my_ship_position = (0,0)
my_ship_fire_speed = (0,-8)
my_ship_fire_positions = (0,0)

class Ship(pygame.sprite.Sprite):
  
  def __init__(self, pos, bullets):
     pygame.sprite.Sprite.__init__(self)
     self.x, self.y = pos
     self.dx = 0
     self.image = pygame.Surface( (100,50) )
     self.image = pygame.image.load(my_ship_tex)
     self.rect = self.image.get_rect()
     self.rect.centerx = self.x
     self.rect.centery = self.y
     self.bullets = bullets
     self.wait = 0
     
  def update(self):
     global my_ship_position
     self.x += self.dx
     if self.x > 900-50:
        self.x = 50
     if self.x < 50:
        self.x = 900-50
     my_ship_position = (self.x, self.y)
     self.rect.centerx = self.x
     self.rect.centery = self.y
     if self.wait > 0: self.wait -= 1       
     
     
  def fire(self):
     global my_ship_fire_positions
     if self.wait == 0:
        vx = my_ship_fire_speed[0]
        vy = my_ship_fire_speed[1]
        bullet = Bullet( (self.rect.centerx + 3 * vx, self.rect.centery + 3 *vy), vx, vy)
        self.bullets.add(bullet)
        my_ship_fire_positions = (self.rect.centerx + 3 * my_ship_fire_speed[0]
                                       , self.rect.centery + 3 *my_ship_fire_speed[1])
        self.wait = 10
        
  def hit(self):
     1
     #self.image.fill( (choice([0,100,250]), choice([0,100,250]), choice([0,100,250])))
     
  def drive(self,key_pressed):
     self.dx = 0
     if key_pressed[K_LEFT] and key_pressed[K_LALT]: self.dx = -20
     elif key_pressed[K_RIGHT] and key_pressed[K_LALT]: self.dx = +20 
     elif key_pressed[K_LEFT]: self.dx = -10
     elif key_pressed[K_RIGHT]: self.dx = +10
     if key_pressed[K_SPACE]: self.fire()
      
     
  def draw(self, screen):
     screen.blit(self.image, (self.rect.left,self.rect.top) )   

