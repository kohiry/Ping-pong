import pygame
import random
pygame.init()

class obj:
    def __init__(self, x):
        self.x = x
        self.y = 300
        self.speed = 1
        self.clock = pygame.time.Clock()

    def run(self):
        self.clock.tick(300)
        if self.x > 0:
            self.x -= self.speed
            return False
        else:
            return True

    def draw(self, screen):
        pygame.draw.rect(screen, White, (self.x - 25, self.y - 25, 50, 50))
        if self.run():
            return True


size = width, height = 600, 600
screen = pygame.display.set_mode(size)

White = (255, 255, 255)
Black = (0, 0, 0)
x = 602
y = 300

rects = []

def randoma(x):
    n = random.randint(1, 5)
    if n == 1:
        rects.append(obj(x))
    elif n == 2:
        for i in range(n):
            rects.append(obj(x))
            x += 300
    elif n == 3:
        for i in range(n):
            rects.append(obj(x))
            x += 200
    elif n == 4:
        for i in range(2):
            rects.append(obj(x))
            x += 50
    elif n == 5:
        for i in range(3):
            rects.append(obj(x))
            x += 50




flag = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            rects.clear()
            randoma(x)

    screen.fill(Black)
    if flag:
        randoma(x)
        flag = False
        print(rects)
    for i in rects:
        if i.draw(screen):
            del rects[rects.index(i)]
            if len(rects) == 0:
                randoma(x)
    pygame.display.flip()

pygame.quit()
