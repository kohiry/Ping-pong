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
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Objects:  # class for weapon, food, clothes
    pass

class Sound:  # class for downloa and play sound
    def __init__(self):
        r'''
        шаблон загрузки аудиофайлов

        self.sound = {'die_sound': pygame.mixer.Sound(r'Sound\die.ogg'),
                      'jump_sound': pygame.mixer.Sound(r'Sound\jump.ogg'),
                      'score_sound': pygame.mixer.Sound(r'Sound\score.ogg')}
        '''
        pass
