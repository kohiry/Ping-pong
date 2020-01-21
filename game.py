import pygame
pygame.init()


size = width, height = 600, 600
screen = pygame.display.set_mode(size)

White = (255, 255, 255)
Black = (0, 0, 0)

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_DOWN:
                pass
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pass
    elif keys[pygame.K_RIGHT]:
        pass
    elif keys[pygame.K_A]:
        pass
    elif keys[pygame.K_D]:
        pass
    screen.fill(Black)
    pygame.display.flip()

pygame.quit()
