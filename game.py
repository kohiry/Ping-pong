import pygame
import random
import help
pygame.init()


size = width, height = 600, 600
screen = pygame.display.set_mode(size)

hero_sprite, background = help.hero_sprites()
game_sound = help.download_sound()
x, y = 20, 240

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
    screen.fill(Black)
    pygame.display.flip()

pygame.quit()
