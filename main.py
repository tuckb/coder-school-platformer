

#imports
import sys
import pygame
from pygame.locals import QUIT
from ground import Ground
from circle import Circle
from plat import Platform
from hammer import Hammer

#screen size
pygame.init()
WIDTH = 1290
HEIGHT = 650
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

#classes
c = Circle()
g = Ground()
p = Platform()
h = Hammer()

#putting classes in the screen
all_sprites = pygame.sprite.Group()
all_sprites.add(g,c)

#title of game
pygame.display.set_caption("Tuck's pretty platformer")

#game loop
while True:
  
  #checking if we're on the ground or not
  if not pygame.sprite.collide_rect(c, g):
    c.rect.y += c.velocity_y
    c.onGround = False
  else:
    print(c.onGround)
    c.onGround = True
    c.jumping = False
    c.velocity_y = 0
    

  #adding key inputs
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.KEYDOWN:

      #key(d) inputs
      if event.key == pygame.K_d:
        #print("Move right")
        c.moving_right = True
      
      #key(a) inputs
      if event.key == pygame.K_a:
        #print("Move left")
        c.moving_left = True
        
      #key(w) inputs / jumping inputs
      if event.key == pygame.K_w:
        if pygame.sprite.collide_rect(c,g):
          c.jumping = True
          c.velocity_y = 50
    
    #adding the ability to check when keys are let up
    elif event.type == pygame.KEYUP:

      #checking key(d) is up
      if event.key == pygame.K_d:
        c.moving_right = False

      #checking key(a) is up
      if event.key == pygame.K_a:
        c.moving_left = False

      #checking key(w) is up
      if event.key == pygame.K_w:
        c.jumping = False

  #screen color
  SCREEN.fill((100,180,255))

  #updating screen
  all_sprites.update()
  all_sprites.draw(SCREEN)
  pygame.display.update()
