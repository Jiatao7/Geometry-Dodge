import pygame

class Text(pygame.sprite.Sprite):
  def __init__(self, message, size, color, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.text = message
    self.font = pygame.font.SysFont("Arial", size)
    self.color = color
    self.image = self.font.render(self.text, 1, self.color)
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)


class Button(pygame.sprite.Sprite):
  def __init__(self, message, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((200, 50))
    self.image.fill((100, 100, 100))
    self.font = pygame.font.SysFont("Arial", 30)
    self.text = self.font.render(message, True, (255, 255, 255))
    self.image.blit(self.text, (10, 10))
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
  
  def check(self, mouse):
        return self.rect.collidepoint(mouse)
