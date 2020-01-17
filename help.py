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
