import pygame
pygame.init()

size = width, height = 800, 600

class Ball:
    def __init__(self, coord, screen):
        self.pos = coord
        self.x, self.y = -200, -200
        self.screen = screen
        self.clock = pygame.time.Clock()

    def run(self, x, y, coord, width, height):
      speed = (x, y)
      speeds_all = [(-200, -200), (200, 200), (200, -200), (-200, 200)]
      if speed == speeds_all[0]:
        if coord[0] <= 0:
          return (200, -200)
        if coord[1] <= 0:
          return (-200, 200)
        else:
          return speed
      elif speed == speeds_all[1]:
        if coord[0] >= width:
          return (-200, 200)
        if coord[1] >= height:
          return (200, -200)
        else:
          return speed
      elif speed == speeds_all[2]:
        if coord[0] >= width:
          return (-200, -200)
        if coord[1] <= 0:
          return (200, 200)
        else:
          return speed
      elif speed == speeds_all[3]:
        if coord[0] <= 0:
          return (200, 200)
        if coord[1] >= height:
          return (-200, -200)
        else:
          return speed

    def draw(self, width, height):
        x, y = self.pos
        print(self.run(self.x, self.y, self.pos, width, height))
        self.x, self.y = self.run(self.x, self.y, self.pos, width, height)
        x += self.x // 60
        y += self.y // 60
        self.clock.tick(60)
        self.pos = (int(x), int(y))
        pygame.draw.circle(self.screen, (255, 255, 255), self.pos, 10)


def menu_sprite():  # download sprite: list with sprite menu
    sprites = []
    for i in range(1, 12):
        sprites.append(pygame.image.load(f'data/menu_{str(i)}.png'))
    return sprites


class Hero:
    def __init__(self, x, y, height, width, speed):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = speed

    def move(self, flag):  # flag - bool, True = вправо, False = влево
        if flag:
            self.x -= self.speed
        else:
            self.x += self.speed

    def draw(self):
        pygame.draw.rect(self.x, self.y, self.height, self.width)


class Enemy:
    def __init__(self, x, y, height, width, speed):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = speed

    def AI(self, x):  # x - координата объекта ball
        if self.x == x:
            return self.x
        elif self.x > x:
            return self.x - self.speed
        elif self.x < x:
            return self.x + self.speed

    def draw(self):
        pygame.draw.rect(self.x, self.y, self.height, self.width)


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
