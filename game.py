import pygame
import random
pygame.init()


size = width, height = 800, 310
screen = pygame.display.set_mode(size)
pygame.display.set_caption('tamplate game')

class Zombie:  # class for zombie
    def __init__(self):
        self.x = 0
        self.y = 220
        self.speed = 10
        self.clock = pygame.time.Clock()

    def run(self):
        self.clock.tick(300)
        if self.x > 0:
            self.x -= self.speed
            return False
        else:
            return True

    def draw(self, screen):
        screen.blit(pygame.image.load('data/obstacle_1.png'), (self.x, self.y))
        if self.run():
            return True


class Sound:
    def __init__(self):
        self.sound = {'die_sound': pygame.mixer.Sound(r'Sound\die.ogg'),
                      'jump_sound': pygame.mixer.Sound(r'Sound\jump.ogg'),
                      'score_sound': pygame.mixer.Sound(r'Sound\score.ogg')}


White = (0, 0, 0)

x_rect = 850
y_rect = 300

zombies = []


def random_for_move_obstacles(x):  # function for spawn random obstacles
    n = random.randint(2, 6)


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
