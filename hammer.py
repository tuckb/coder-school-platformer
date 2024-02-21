import pygame

class Hammer(pygame.sprite.Sprite):

  def __init__(self):
    super().__init__()
    self.image = pygame.image.load('Images/HammerTime.png')
    self.image = pygame.transform.scale(self.image, (60, 95))

    self.rect = self.image.get_rect()
    self.rect.x = 275
    self.rect.y = 30