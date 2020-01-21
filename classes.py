import pygame
pygame.init()

size = width, height = 800, 600

class Ball:
    def __init__(self, coord, screen):
        self.pos = coord
        self.x, self.y = -100, -100
        self.screen = screen
        self.clock = pygame.time.Clock()

    def run(self, x, y, coord, width, height):
      speed = (x, y)
      speeds_all = [(-100, -100), (100, 100), (100, -100), (-100, 100)]
      if speed == speeds_all[0]:
        if coord[0] <= 0:
          return (100, -100)
        if coord[1] <= 0:
          return (-100, 100)
        else:
          return speed
      elif speed == speeds_all[1]:
        if coord[0] >= width:
          return (-100, 100)
        if coord[1] >= height:
          return (100, -100)
        else:
          return speed
      elif speed == speeds_all[2]:
        if coord[0] >= width:
          return (-100, -100)
        if coord[1] <= 0:
          return (100, 100)
        else:
          return speed
      elif speed == speeds_all[3]:
        if coord[0] <= 0:
          return (100, 100)
        if coord[1] >= height:
          return (-100, -100)
        else:
          return speed

    def draw(self, width, height):
        x, y = self.pos
        self.x, self.y = self.run(self.x, self.y, self.pos, width, height)
        x += self.x / 80
        y += self.y / 80
        self.clock.tick(80)
        self.pos = (int(x), int(y))
        pygame.draw.circle(self.screen, (255, 255, 255), self.pos, 10)


def menu_sprite():  # download sprite: list with sprite menu
    sprites = []
    for i in range(1, 12):
        sprites.append(pygame.image.load(f'data/menu_{str(i)}.png'))
    return sprites
