import pygame
pygame.init()

size = width, height = 800, 600


class Ball:
    def __init__(self, coord, screen, width):
        self.pos = coord
        self.x, self.y = -400, -400
        self.screen = screen
        self.width = width
        self.clock = pygame.time.Clock()

    def run(self, x, y, coord, width, height):
      speed = (x, y)
      speeds_all = [(-400, -400), (400, 400), (400, -400), (-400, 400)]
      if speed == speeds_all[0]:
        if coord[0] <= 0:
          return speeds_all[2]
        if coord[1] <= 0:
          return speeds_all[3]
        else:
          return speed
      elif speed == speeds_all[1]:
        if coord[0] >= width:
          return speeds_all[3]
        if coord[1] >= height:
          return speeds_all[2]
        else:
          return speed
      elif speed == speeds_all[2]:
        if coord[0] >= width:
          return speeds_all[0]
        if coord[1] <= 0:
          return speeds_all[1]
        else:
          return speed
      elif speed == speeds_all[3]:
        if coord[0] <= 0:
          return speeds_all[1]
        if coord[1] >= height:
          return speeds_all[0]
        else:
          return speed

    def draw(self, width, height):
        x, y = self.pos
        self.x, self.y = self.run(self.x, self.y, self.pos, width, height)
        x += self.x // 60
        y += self.y // 60
        self.clock.tick(60)
        self.pos = (int(x), int(y))
        pygame.draw.circle(self.screen, (255, 255, 255), self.pos, self.width)


def transforms(sprite, width, height):
    for i in range(len(sprite)):
        sprite[i] = pygame.transform.scale(sprite[i], (width, height))

def menu_sprite():  # download sprite: list with sprite menu
    sprites = []
    for i in range(1, 12):
        sprites.append(pygame.image.load(f'data/menu_{str(i)}.png').convert())
    return sprites


class Hero:
    def __init__(self, x, y, height, width, speed):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = speed
        self.color = (255, 255, 255)

    def move(self, flag):  # flag - bool, True = вправо, False = влево
        if flag:
            self.y -= self.speed
        else:
            self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.height, self.width))


class Enemy:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = speed
        self.color = (255, 255, 255)
        self.clock = pygame.time.Clock()

    def AI(self, y, display_height):  # y - координата объекта ball

        if self.y + (self.height // 2) > y and self.y >= 0:
            self.y -= self.speed // 60
        elif self.y + (self.height // 2) < y and self.y <= display_height - self.height:
            self.y += self.speed // 60
        self.clock.tick(60)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


class DrawBackground:
    def __init__(self):
        self.jump = 160
        self.width = 10
        self.height = 120
        self.text_y = 10

        self.score = {'enemy':'0', 'hero':'0'}

        font = pygame.font.Font(None, 70)
        White = (255, 255, 255)
        self.enemy_txt = font.render(self.score['enemy'], 1, (255, 255, 255))
        self.hero_txt = font.render(self.score['hero'], 1, (255, 255, 255))

    def change_score(self, who, score):
        if who == 'enemy' or who == 'hero':
            self.score[who] = score
        else:
            print('Неверные даны данные')

    def draw(self, x, Dheight, screen):
        # отрисовка поля
        for i in range(0, Dheight, self.jump):  # отрисовка разграничивающих полос на поле
            pygame.draw.rect(screen, (255, 255, 255), (x - self.width//2, i,\
                             self.width, self.height))

        # отрисовка счёта
        screen.blit(self.enemy_txt, (x // 2 - self.enemy_txt.get_width() // 2, self.text_y))  # 1/4 ширины
        screen.blit(self.hero_txt, ((x + x // 2) - self.hero_txt.get_width() // 2, self.text_y))  # 3/4


class Sound:  # class for downlod and play sound
    def __init__(self):
        self.sound = {'die_sound': pygame.mixer.Sound(r'Sound\die.ogg'),
                      'jump_sound': pygame.mixer.Sound(r'Sound\jump.ogg'),
                      'score_sound': pygame.mixer.Sound(r'Sound\score.ogg')}

    def play_die(self):
        sound['die_sound'].play()

    def play_jump(self):
        sound['jump_sound'].play()

    def play_score(self):
        sound['score_sound'].play()


'''
background = DrawBackground()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    background.draw(width//2, height, screen)
    pygame.display.flip()

pygame.quit()
'''
