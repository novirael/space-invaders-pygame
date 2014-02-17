import pygame
import GIFImage
from pygame.locals import *
from sys import exit
from random import randint
from math import *

from invaders import Alien
from ship import Ship
from barykady import Barykada

#constants
SW = 900
SH = 600

# variables
lifes = 3
aliens = []
font_duration = 0
explo_duration = 0

count = 0
points = 0

current_level = 1
max_level = 3

level_up = True
load_next_level = True

explosion = False
fail = False
victory = False


# pygame init
pygame.init()
screen = pygame.display.set_mode((SW, SH))

explo1 = pygame.image.load("img/exp.png").convert_alpha()
explo2 = GIFImage.GIFImage("img/wybuch.gif")

# pygame mixer init
pygame.mixer.init()
boom_sound = pygame.mixer.Sound("boom.wav")
boom_sound.play()
clock = pygame.time.Clock()

######## auxiliary functions  ########

def delete_bad(G):               # is deleting sprites off screen
   for s in G.sprites():
      if s.y < 0 or s.y > SH:
         G.remove(s)

def czekaj(time, wait):
   if wait > 0:
      wait -= 1
   else:
      wait = time
   return wait

def check_game_conditions():   # is checking game conditions
   global victory, fail
   for i in invaders:
      if i.y > 450:
         fail = True
         return False
   if lifes < 1:
      fail = True
      return False
   if current_level == max_level:
      victory = True
      return False
   return True
def load_next_level(level):
   global rockets
   for r in rockets:
      rockets.remove(r)
   draw_barykady()
   draw_invaders(level)


def reset_ship():
   my_ship.x = SW/2

# create groups of sprites
rockets = pygame.sprite.Group()
bombs = pygame.sprite.Group()
invaders = pygame.sprite.Group()
barykady = pygame.sprite.Group()
lbarykad = []

# draw barykady
def draw_barykady():
   global lbarykad, barykady
   for i in range(16):
      lbarykad.append(Barykada((160 + 5 * i, 490)))
   for i in range(16):
      lbarykad.append(Barykada((410 + 5 * i, 490)))
   for i in range(16):
      lbarykad.append(Barykada((660 + 5 * i, 490)))
   for i in range(20):
      lbarykad.append(Barykada((150 + 5 * i, 495)))
   for i in range(20):
      lbarykad.append(Barykada((400 + 5 * i, 495)))
   for i in range(20):
      lbarykad.append(Barykada((650 + 5 * i, 495)))
   for i in range(24):
      lbarykad.append(Barykada((140 + 5 * i, 500)))
   for i in range(24):
      lbarykad.append(Barykada((390 + 5 * i, 500)))
   for i in range(24):
      lbarykad.append(Barykada((640 + 5 * i, 500)))
   for i in range(28):
      lbarykad.append(Barykada((130 + 5 * i, 505)))
   for i in range(28):
      lbarykad.append(Barykada((380 + 5 * i, 505)))
   for i in range(28):
      lbarykad.append(Barykada((630 + 5 * i, 505)))
   barykady = pygame.sprite.Group(lbarykad)

# Alien( left_top_knap_pos, bullets,nr_of_monster)
# nr_of_monster: 0,1 - green; 2,3 - purple; 4,5 - yellow;

def draw_invaders(level): # is creating list of invaders
   global aliens, invaders
   if level == 1:
      aliens = []
      for i in range(10):
         aliens.append(Alien((90 + 70 * i, 50), bombs, 0 ))
      for i in range(10):
         aliens.append(Alien((90 + 70 * i, 100), bombs, 2 ))
      for i in range(10):
         aliens.append(Alien((90 + 70 * i, 150), bombs, 4 ))
      for i in range(10):
         aliens.append(Alien((90 + 70 * i, 200), bombs, 1 ))
      invaders = pygame.sprite.Group(aliens)
   if level == 2:
      aliens = []
      for i in range(9):
         aliens.append(Alien((120 + 70 * i, 50), bombs, 5+0 ))
      for i in range(10):
         aliens.append(Alien((90 + 70 * i, 100), bombs, 5+2 ))
      for i in range(9):
         aliens.append(Alien((120 + 70 * i, 150), bombs, 5+4 ))
      for i in range(10):
         aliens.append(Alien((90 + 70 * i, 200), bombs, 5+1 ))
      for i in range(9):
         aliens.append(Alien((120 + 70 * i, 250), bombs, 5+3 ))
      for i in range(10):
         aliens.append(Alien((90 + 70 * i, 300), bombs, 5+0 ))
      invaders = pygame.sprite.Group(aliens)


my_ship = Ship( (SW/2,SH-50), rockets)

# font init
pygame.font.init()
font1 = pygame.font.SysFont("arial", 20)
font2 = pygame.font.SysFont("arial", 20)
font2.set_bold(True)


def font_update():
   if check_game_conditions():
      zycia_t = "LEVEL " + str(current_level)  + "    LIFES: " + str(lifes) + "    POINTS: " + str(points)
      zycia = font1.render(zycia_t, True, (255,255,255) )
      screen.blit( zycia, (5,5) )

   if victory:
      wygrana_t = "CONGRATZ! YOU WON"
      punkty_t = "SCORE: " + str(points)
      wygrana = font2.render(wygrana_t, True, (255,255,255) )
      punkty = font1.render(punkty_t, True, (255,255,255) )
      size_win = wygrana.get_size()
      size_score = punkty.get_size()
      screen.blit( wygrana, ( (SW-size_win[0])/2, (SH-size_win[1])/2 - 20) )
      screen.blit( punkty, ( (SW-size_score[0])/2, (SH-size_score[1])/2 + 20) )

   if fail:
      przegrana_t = "GAME OVER"
      punkty_t = "SCORE: " + str(points)
      przegrana = font2.render(przegrana_t, True, (255,255,255) )
      punkty = font1.render(punkty_t, True, (255,255,255) )
      size_fail = przegrana.get_size()
      size_score = punkty.get_size()
      screen.blit( przegrana, ( (SW-size_fail[0])/2, (SH-size_fail[1])/2 - 20) )
      screen.blit( punkty, ( (SW-size_score[0])/2, (SH-size_score[1])/2 + 20) )

   if level_up and not victory:
      poziom_t = "LEVEL " + str(current_level)
      poziom = font2.render(poziom_t, True, (180,180,180) )
      size_level = poziom.get_size()
      screen.blit( poziom, ( (SW-size_level[0])/2, (SH-size_level[1])/2) )


########### start game ##########

draw_barykady()
draw_invaders(1) #for level 1

while True:
    clock.tick(30)

    #from invaders import *
    #from ship import *
    #from kula import *

    # events
    for event in pygame.event.get():
       if event.type == QUIT:
          pygame.font.quit()
          pygame.display.quit()
          exit()

    # fill screen
    screen.fill((0,0,0))

    # update fonts
    font_update()
    font_duration = czekaj(50, font_duration)
    print font_duration
    # my ship navigation
    pressed_keys = pygame.key.get_pressed()
    my_ship.drive(pressed_keys)

    # check game conditions
    if check_game_conditions() == True:

       # when level up?
       if len(invaders) == 0:
          level_up = True
          current_level += 1
          if not victory:
             load_next_level(current_level)

       # show font
       if font_duration == 0:
          level_up = False

       # show ship
       if explo_duration == 0 and explosion:
          explosion = False
          reset_ship()


       # check collide for bombs and my ship
       for b in bombs:
          if pygame.sprite.collide_rect(b, my_ship):
             my_ship.hit()
             bombs.remove(b)
             explosion = True
             lifes -= 1
             #boom_sound.play()

       # check collide for allien and my rocket
       for r in rockets:
          for i in invaders:
             if pygame.sprite.collide_rect(r, i):
                rockets.remove(r)
                invaders.remove(i)
                count += 1
                points = count * 40
                screen.blit(explo1, (i.x-30, i.y-22) )
                #boom_sound.play()
                break

       # check collide for bomb and barykady
       if pygame.sprite.groupcollide(bombs, barykady, True,True):
          boom_sound.play()

       if pygame.sprite.groupcollide(rockets, barykady, True,True):
          boom_sound.play()

       # update and draw my ship
       if not explosion:
          my_ship.update()
          my_ship.draw(screen)
       else:
          rect = pygame.Rect(0, 0, 60, 45)
          rect.centerx = my_ship.x
          rect.centery = my_ship.y
          explo2.render(screen, (rect.left,rect.top) )
          for b in bombs:
             bombs.remove(b)
          explo_duration = czekaj(50, explo_duration)

       # update invaders
       invaders.update(screen, explosion)

       # update and draw bullets
       bombs.update()
       rockets.update()
       bombs.draw(screen)
       rockets.draw(screen)

       # update barykady
       barykady.update()
       barykady.draw(screen)

       # remove bullets off the screen
       delete_bad(rockets)
       delete_bad(bombs)

    # update display
    pygame.display.update()

