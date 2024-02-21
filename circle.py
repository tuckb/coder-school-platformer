#imports
import pygame

#circle class settings
class Circle(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.moving_right = False
    self.moving_left = False
    self.jumping = False
    self.image = pygame.image.load('Images/BallGuy.png')
    self.image = pygame.transform.scale(self.image, (50,50))
    self.rect = self.image.get_rect()
    self.rect.x = 275
    self.rect.y = 230
    self.velocity_y = 0
    self.onGround = False

  #updating game/inputs
  def update(self):

    #making ball move right
    if self.moving_right is True:
      self.rect.x += 1

    #making ball move left
    if self.moving_left is True:
      self.rect.x -= 1

    #making ball jump
    if self.jumping is True and self.rect.y > self.maxJump:
      self.rect.y -= self.velocity_y

    #making ball fall
    if self.onGround is False:
      self.velocity_y = 2
    else:
      self.maxJump = self.rect.y - 100
      #print(self.maxjump)
    #print(self.velocity_y)
      
    