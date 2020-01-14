import pygame
import random
pygame.init()

class obj:
    def __init__(self, x):
        self.x = x
        self.y = 300
        self.speed = 10

    def draw(self, screen):
        pygame.draw.rect(screen, White, (x - 25, y - 25, 50, 50))
        self.x -= self.speed


size = width, height = 600, 600
screen = pygame.display.set_mode(size)

White = (255, 255, 255)
Black = (0, 0, 0)
x = 602
y = 300
width_inside_obj = 100

rects = []

def randoma(x):
    x = x
    print(x)
    n = random.randint(1, 3)
    if n == 3:
        width_inside_obj = 150
    elif n == 2:
        width_inside_obj = 250
    else:
        if random.randint(1, 2) == 2:
            width_inside_obj = 0
        else:
            width_inside_obj = 100

    for i in range(n):
        rects.append(obj(x))
        x += width_inside_obj
    return x

flag = True
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(Black)
    if flag:
        randoma(x)
        flag = False
    for i in rects:
        i.draw(screen)
    pygame.display.flip()

pygame.quit()
