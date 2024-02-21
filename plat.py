import pygame

class Platform(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load('Images/GrassPlat.png')
    self.image = pygame.transform.scale(self.image,(150,35))
    
    self.rect = self.image.get_rect()
    self.rect.x = 225
    self.rect.y = 150