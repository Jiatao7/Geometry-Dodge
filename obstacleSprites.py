import pygame, random

class Laser(pygame.sprite.Sprite):
  def __init__(self, score):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.Surface((30, 10))
    self.image = self.image.convert()
    self.image.fill((255, 0, 0))

    directions = ["left", "right"]
    self.direction = random.choice(directions)
    self.step = 5

    self.rect = self.image.get_rect()

    if self.direction == "left":
      self.rect.centerx = 640
    elif self.direction == "right":
      self.rect.centerx = 0
    self.rect.centery = random.randrange(0, 480)
    
    self.speed = 5 + score//300
    if self.speed > 15:
      self.speed = 15

  def update(self):
    if self.direction == "left":
      self.rect.centerx = self.rect.centerx - self.speed
      if self.rect.centerx < 0:
        self.kill()

    elif self.direction == "right":
      self.rect.centerx = self.rect.centerx + self.speed
      if self.rect.centerx > 640:
        self.kill()


class Fireball(pygame.sprite.Sprite):
  def __init__(self, score):
    pygame.sprite.Sprite.__init__(self)
    
    self.image = pygame.Surface((40, 40))
    self.image.fill((0, 0, 0))
    self.image.set_colorkey((0, 0, 0))  

    pygame.draw.circle(self.image, (255, 100, 0), (20, 20), 20, 0)
    self.rect = self.image.get_rect()
    self.rect.centerx = random.randrange(0, 640)
    self.rect.centery = 0

    self.base_speed = 8 + score//400
    if self.base_speed > 20:
      self.base_speed = 20
    self.speed = self.base_speed

  def update(self):
    self.rect.centery = self.rect.centery + self.speed
    if self.rect.centery > 480:
      self.kill()
    elif self.rect.centery > 320:
      self.speed = self.base_speed + 4
    elif self.rect.centery > 160:
      self.speed = self.base_speed + 2


class Spikeball(pygame.sprite.Sprite):
  def __init__(self, score):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.Surface((60, 60))
    self.image.fill((0, 0, 0))
    self.image.set_colorkey((0, 0, 0))

    self.points = ((10, 10), (30, 15), (50, 10), (45, 30), (50, 50), (30, 45), (10, 50), (15, 30)) 
    self.points2 = ((30, 0), (40, 20), (60, 30), (40, 40), (30, 60), (20, 40), (0, 30), (20, 20))
    pygame.draw.polygon(self.image, (120, 120, 120), (self.points), 0)
    pygame.draw.polygon(self.image, (80, 80, 80), (self.points2), 0)

    self.rect = self.image.get_rect()
    self.rect.centerx = random.randrange(0, 640)
    self.rect.centery = 480
    
    directions = ["left", "right"]
    self.direction_x = random.choice(directions)
    self.direction_y = "up"

    self.speed = 5 + score//600
    if self.speed > 10:
      self.speed = 10

  def update(self):
    if self.direction_x == "left":
      self.rect.centerx = self.rect.centerx - self.speed
      if self.rect.centerx < 0:
        self.direction_x = "right"

    elif self.direction_x == "right":
      self.rect.centerx = self.rect.centerx + self.speed
      if self.rect.centerx > 640:
        self.direction_x = "left"
    
    if self.direction_y == "up":
      self.rect.centery = self.rect.centery - self.speed
      if self.rect.centery < 0:
        self.direction_y = "down"

    elif self.direction_y == "down":
      self.rect.centery = self.rect.centery + self.speed
      if self.rect.centery > 480:
        self.kill()
