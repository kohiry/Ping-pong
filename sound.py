class Sound:  # class for downloa and play sound
    def __init__(self):
        self.sound = {'die_sound': pygame.mixer.Sound(r'Sound\die.ogg'),
                      'jump_sound': pygame.mixer.Sound(r'Sound\jump.ogg'),
                      'score_sound': pygame.mixer.Sound(r'Sound\score.ogg')}
