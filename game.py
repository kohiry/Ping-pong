import pygame
import classes
pygame.init()


size = width, height = 800, 600
screen = pygame.display.set_mode(size)

White = (255, 255, 255)
Black = (0, 0, 0)
list_balls = []
bol = False

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            list_balls.append(classes.Ball(event.pos, screen))
            bol = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pass
    elif keys[pygame.K_RIGHT]:
        pass
    elif keys[pygame.K_a]:
        pass
    elif keys[pygame.K_d]:
        pass
    screen.fill(Black)
    if bol:
        for i in list_balls:
            i.draw(width, height)
    pygame.display.flip()

pygame.quit()
