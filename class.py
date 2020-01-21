import pygame
import random
pygame.init()


class Hero:  # класс объекты которого все нпс игры
    def __init__(self, x, y, speed, damage, stamina):
        self.x = x
        self.y = y
        self.damage = damage
        self.speed = speed
        self.stamina = stamina
        self.clock = pygame.time.Clock()

    def draw(self, screen):
        # шаблон отрисовок картинки
        # screen.blit(pygame.image.load('data/obstacle_1.png'), (self.x, self.y))
        pass


class Zombie:  # class for zombie
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.damage = 2
        self.speed = speed
        self.clock = pygame.time.Clock()

    def draw(self, screen):
        # шаблон отрисовок картинки
        # screen.blit(pygame.image.load('data/obstacle_1.png'), (self.x, self.y))
        pass


class Building:  # class for objects in game: buildings
    pass


class Objects:  # class for weapon, food, clothes
    pass

class Sound:
    def __init__(self):
        r'''
        шаблон загрузки аудиофайлов

        self.sound = {'die_sound': pygame.mixer.Sound(r'Sound\die.ogg'),
                      'jump_sound': pygame.mixer.Sound(r'Sound\jump.ogg'),
                      'score_sound': pygame.mixer.Sound(r'Sound\score.ogg')}
        '''




'''
size = width, height = 800, 310
screen = pygame.display.set_mode(size)
pygame.display.set_caption('tamplate game')

running = True
clock = pygame.time.Clock()
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_E]: # инвентарь
        pass
    pygame.display.update()
pygame.quit()
'''
