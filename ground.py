#imports
import pygame

#ground class settings
class Ground(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load('Images/GrassPlat.png')
    self.image = pygame.transform.scale(self.image, (1290,100))
    self.rect = self.image.get_rect()
    #self.rect.x = 
    self.rect.y = 550
    