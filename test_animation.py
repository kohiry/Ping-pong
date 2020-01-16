import pygame
import os
pygame.init()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()

size = width, height = 800, 310
screen = pygame.display.set_mode(size)

# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()

def addsprite(art):
    print(1)
    # создадим спрайт
    sprite = pygame.sprite.Sprite()
    # определим его вид
    sprite.image = pygame.image.load(f'data/{art}.png')
    # и размеры
    sprite.rect = sprite.image.get_rect(bottomright=(50, 70))
    # добавим спрайт в группу
    all_sprites.add(sprite)
    sprite.rect.x = 50
    sprite.rect.y = 240



image_surf = pygame.image.load('data/background1.bmp')
image_rect = image_surf.get_rect(bottomright=(800, 310))
screen.blit(image_surf, image_rect)
addsprite('hero')

all_sprites.draw(screen)
pygame.display.update()

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
