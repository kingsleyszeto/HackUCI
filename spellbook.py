import pygame

class Spellbook:
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(50, 100, 410, 300)
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.fire = self.font.render('Fire: ambustum', False, (0, 0, 0))
        self.water = self.font.render('Water: macerari', False, (0, 0, 0))
        self.earth = self.font.render('Earth: planicia', False, (0, 0, 0))
        self.dark = self.font.render('Dark: opscurum', False, (0, 0, 0))
        self.light = self.font.render('Light: illustris', False, (0, 0, 0))
        self.heal = self.font.render('Heal: confervo', False, (0, 0, 0))
        self.multi = self.font.render('Multi: ledo magis hosti', False, (0,0,0))
        self.change = self.font.render('Change: praestituo', False, (0,0,0))
        self.spellbook = [self.fire, self.water, self.earth, self.dark, self.light, self.heal]
        self.prefixes = [self.multi, self.change]

    def open(self, screen):
        pygame.draw.rect(screen, (245, 222, 179), self.rect)
        height = 100
        screen.blit(self.font.render('Spells', False, (0, 0, 0)), (50, height))
        height += 25
        for text in self.spellbook:
            screen.blit(text, (50, height))
            height += 25
        height += 25
        screen.blit(self.font.render('Prefixes', False, (0, 0, 0)), (50, height))
        height += 25
        for text in self.prefixes:
            screen.blit(text, (50, height))
            height += 25