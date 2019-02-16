import pygame


class Spellbook:
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(50, 100, 410, 300)
        self.font = pygame.font.SysFont(None, 30)
        self.fire = self.font.render('Fire: i touched the stove once and it burned me', False, (0, 0, 0))
        self.water = self.font.render('Water: water is wet and non breathable', False, (0, 0, 0))
        self.earth = self.font.render('Earth: is flat cuz otherwise we\'d fall off', False, (0, 0, 0))
        self.dark = self.font.render('Dark: racial segregation is a serious problem', False, (0, 0, 0))
        self.light = self.font.render('Light: ow i looked into the sun my retinas', False, (0, 0, 0))
        self.heal = self.font.render('Heal: the US government prevents me from proper insurance', False, (0, 0, 0))
        self.spellbook = [self.fire, self.water, self.earth, self.dark, self.light, self.heal]

    def open(self, screen):
        pygame.draw.rect(screen, (245, 222, 179), self.rect)
        height = 100
        for text in self.spellbook:
            screen.blit(text, (50, height))
            height += 30