import pygame
import GIFImage
from pygame.locals import *
from sys import exit
from random import randint,choice
from math import *
from kula import Bullet


monster_tex = ['img/green1.gif','img/green2.gif',
               'img/purple1.gif','img/purple2.gif',
               'img/yellow1.gif', 'img/yellow2.gif',
               'img/green11.gif','img/green22.gif',
               'img/purple11.gif','img/purple22.gif',
               'img/yellow11.gif', 'img/yellow22.gif']

aliens_position = (0,0)
aliens_fire_speed = [0,6] # vx, vy

class Alien(pygame.sprite.Sprite):
  
  def __init__(self, pos, bullets, n):
     pygame.sprite.Sprite.__init__(self)
     self.x, self.y = pos
     self.states = [ (1,0), (0,1), (-1,0), (0,1) ]
     self.state = 0
     self.state_lens = [40,10,40,10]
     self.state_len = self.state_lens[self.state]
     self.image = pygame.Surface ( (60,45) )
     self.image = GIFImage.GIFImage(monster_tex[n])
     self.rect = pygame.Rect(0, 0, 60, 45)
     self.rect.centerx = self.x
     self.rect.centery = self.y
     self.bullets = bullets

  def update(self, screen, explosion):
     global aliens_position
     dx,dy = self.states[self.state]
     if not explosion:
       self.x += 2*dx
       self.y += dy
       aliens_position = (self.x, self.y)
       self.rect.centerx = self.x
       self.rect.centery = self.y
       self.state_len -= 1
       if self.state_len < 0:
         self.state += 1
         if self.state > 3:
           self.state = 0
         self.state_len = self.state_lens[self.state]
       if randint(0,800) == 0:
         self.fire()
     self.image.render(screen, (self.rect.left,self.rect.top) )
     
  def fire(self):
     #print 'inside fire def'
     vx = aliens_fire_speed[0]
     vy = aliens_fire_speed[1]
     bullet = Bullet( (self.rect.centerx + 3 * vx, self.rect.centery + 3 *vy), vx, vy)
     self.bullets.add(bullet)
  
