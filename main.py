import pygame, random, menuSprites, characterSprites, obstacleSprites
pygame.init()

def main():
  object = open("highscore.txt")
  highscore = int(object.read())
  object.close()

  screen = pygame.display.set_mode((640, 480))
  pygame.display.set_caption("Geometry Dodge")

  background = pygame.Surface(screen.get_size())
  background.fill((0, 0, 0))
  screen.blit(background, (0, 0))

  title = menuSprites.Text("Geometry Dodge", 60, (0, 0, 255), 320, 60)
  playButton = menuSprites.Button("Play", 320, 200)
  highscoreButton = menuSprites.Button("Highscore", 320, 280)
  exitButton = menuSprites.Button("Exit", 320, 360)
  allSprites = pygame.sprite.OrderedUpdates(title, playButton, highscoreButton, exitButton)

  keepGoing = True
  clock = pygame.time.Clock()
  
  while keepGoing:
    clock.tick(30)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        keepGoing = False
        
      if event.type == pygame.MOUSEBUTTONUP:
        if playButton.check(pygame.mouse.get_pos()):
          while True:
            score = play()
            if score > highscore:
              highscore = score
              save_highscore(highscore)
            restart = endScreen(score)
            if restart == False:
              break

        elif highscoreButton.check(pygame.mouse.get_pos()):
          highscoreScreen(highscore)
        elif exitButton.check(pygame.mouse.get_pos()):
          keepGoing = False

    allSprites.clear(screen, background)
    allSprites.draw(screen)
    
    pygame.display.flip()
   
  pygame.quit()        


def play():
  lives = 3
  score = 0

  screen = pygame.display.set_mode((640, 480))
  pygame.display.set_caption("Geometry Dodge")

  background = pygame.Surface(screen.get_size())
  background.fill((0, 0, 0))
  screen.blit(background, (0, 0))

  character = characterSprites.Character()
  score_label = characterSprites.Score()
  hearts = []
  for i in range(3):
    hearts.append(characterSprites.Heart((40, 40), (i * 50 + 30, 30)))
  lasers = []
  fireballs = []
  spikeballs = []
  extrahearts = []

  characterGroup = pygame.sprite.OrderedUpdates(character, score_label, hearts)
  obstacleGroup = pygame.sprite.OrderedUpdates(lasers, fireballs, spikeballs)
  extraheartsGroup = pygame.sprite.OrderedUpdates(extrahearts)

  clock = pygame.time.Clock()
  gameOver = False

  while gameOver == False:
    clock.tick(30)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
    
    if score % (15 - score//1000) == 10:
      lasers.append(obstacleSprites.Laser(score))
      obstacleGroup.add(lasers[-1])
    if score > 1000 and score % 80 == 40:
      for i in range(2):
        lasers.append(obstacleSprites.Laser(score))
        obstacleGroup.add(lasers[-1])    
    if score % 100 == 50:
      fireballs.append(obstacleSprites.Fireball(score))
      obstacleGroup.add(fireballs[-1])   
    if score % 400 == 200:
      spikeballs.append(obstacleSprites.Spikeball(score))
      obstacleGroup.add(spikeballs[-1])

    if pygame.sprite.spritecollide(character, obstacleGroup, True):
      lives = lives - 1
      hearts[-1].kill()
      hearts.pop(-1)
      if lives == 0:
        gameOver = True
        return score
      
    if lives < 3 and score % 50 == 25 and random.randint(1, 20) == 20:
      extrahearts.append(characterSprites.Heart((30, 30), (random.randint(80, 560), random.randint(80, 400))))
      extraheartsGroup.add(extrahearts[-1])
      characterGroup.add(extrahearts[-1])

    if pygame.sprite.spritecollide(character, extraheartsGroup, True):
      for h in extrahearts:
        h.kill()
      hearts.append(characterSprites.Heart((40, 40), (lives * 50 + 30, 30)))
      characterGroup.add(hearts[-1])
      lives = lives + 1

    score = score + 1
    score_label.change_score(score)

    characterGroup.clear(screen, background)   
    characterGroup.update()
    characterGroup.draw(screen)
    obstacleGroup.clear(screen, background)
    obstacleGroup.update()
    obstacleGroup.draw(screen)
    pygame.display.flip()


def endScreen(score):
  screen = pygame.display.set_mode((640, 480))
  pygame.display.set_caption("Geometry Dodge")

  background = pygame.Surface(screen.get_size())
  background.fill((0, 0, 0))
  screen.blit(background, (0, 0))

  text1 = menuSprites.Text("Game Over", 50, (255, 0, 0), 320, 60)
  text2 = menuSprites.Text("Score: " + str(score), 30, (255, 255, 255), 320, 120)
  restartButton = menuSprites.Button("Restart", 320, 240)
  menuButton = menuSprites.Button("Menu", 320, 320)
  allSprites = pygame.sprite.OrderedUpdates(text1, text2, restartButton, menuButton)

  keepGoing = True
  clock = pygame.time.Clock()
  
  while keepGoing:
    clock.tick(30)

    allSprites.clear(screen, background)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        keepGoing = False
      if event.type == pygame.MOUSEBUTTONUP:
        if restartButton.check(pygame.mouse.get_pos()):
          return True
        elif menuButton.check(pygame.mouse.get_pos()):
          return False

    allSprites.draw(screen) 
    pygame.display.flip()


def highscoreScreen(highscore):
  screen = pygame.display.set_mode((640, 480))
  pygame.display.set_caption("Geometry Dodge")

  background = pygame.Surface(screen.get_size())
  background.fill((0, 0, 0))
  screen.blit(background, (0, 0))
  
  text = menuSprites.Text("Highscore: " + str(highscore), 50, (255, 255, 255), 320, 60) 
  menuButton = menuSprites.Button("Menu", 320, 200)
  allSprites = pygame.sprite.OrderedUpdates(text, menuButton)
  
  keepGoing = True
  clock = pygame.time.Clock()
  
  while keepGoing:
    clock.tick(30)

    allSprites.clear(screen, background)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        keepGoing = False
      if event.type == pygame.MOUSEBUTTONUP:
        if menuButton.check(pygame.mouse.get_pos()):
          return False

    allSprites.draw(screen) 
    pygame.display.flip()


def save_highscore(highscore):
  object = open("highscore.txt", "w")
  object.write(str(highscore))
  object.close()

main()

              