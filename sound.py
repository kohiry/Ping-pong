import pygame
pygame.init()


size = width, height = 600, 600
screen = pygame.display.set_mode(size)

White = (255, 255, 255)
Black = (0, 0, 0)

def download():
    return {'die_sound': pygame.mixer.Sound(r'Sound\die.ogg'),
            'jump_sound': pygame.mixer.Sound(r'Sound\jump.ogg'),
            'score_sound': pygame.mixer.Sound(r'Sound\score.ogg')}


sound = download()
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            sound['die_sound'].play()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                sound['jump_sound'].play()
            elif event.key == pygame.K_DOWN:
                sound['score_sound'].play()
    screen.fill(Black)
    pygame.display.flip()

pygame.quit()
