import pygame

class Character(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.Surface((40, 40))
    self.image = self.image.convert()
    self.image.fill((0, 0, 255))

    self.rect = self.image.get_rect()
    self.rect.centerx = 320
    self.rect.centery = 240

    self.invincible_duration = 0

  def update(self):
    self.rect.center = pygame.mouse.get_pos()
    if self.invincible_duration > 0:
      self.invincible_duration = self.invincible_duration - 1
      if self.invincible_duration == 0:
        self.lose_powerup()
  
  def powerup(self, powerup):
    if powerup == "invincibility":
      self.image.fill((255, 255, 0))
      self.invincible_duration = 300

  def lose_powerup(self):
    self.image.fill((0, 0, 255))

  def return_invincibility(self):
    return self.invincible_duration
    


class Heart(pygame.sprite.Sprite):
  def __init__(self, size, center):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.image.load("heart.png")
    self.image = pygame.transform.scale(self.image, (size))
    self.rect = self.image.get_rect()
    self.rect.center = center


class Score(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)      
    self.font = pygame.font.SysFont("Arial", 30)
    self.text = 0
    self.color = (255, 255, 255)    
    self.score = 0

  def change_score(self, score):
    self.score = score

  def update(self):
    self.text = str(self.score)
    self.image = self.font.render(self.text, 1, self.color)
    self.rect = self.image.get_rect()
    self.rect.right = 630
    self.rect.top = 10
