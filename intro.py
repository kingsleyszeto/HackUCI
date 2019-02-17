import pygame


class Intro:
    def __init__(self, screen):
        self.screen = screen
        self.start_element = None
        self.index = 0
        self.element_list = ['fire', 'water', 'earth', 'light', 'dark']

    def play_intro(self):
        titles = [pygame.image.load('sprites/start1.png'), pygame.image.load('sprites/start2.png')]
        current_image = titles[0]
        loop = True
        while loop:
            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 510, 500))
            if current_image == titles[0]:
                self.screen.blit(titles[1], (0, 0))
                current_image = titles[1]
                pygame.time.wait(250)
            elif current_image == titles[1]:
                self.screen.blit(titles[0], (0, 0))
                current_image = titles[0]
                pygame.time.wait(250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.instructions()
                    loop = False
            pygame.display.flip()

    def instructions(self):
            loop = True
            while loop:
                self.screen.fill((0, 0, 0))
                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 510, 500))
                self.screen.blit(pygame.image.load('sprites/howtoplay.png'), (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        self.select_element()
                        loop = False
                pygame.display.flip()

    def select_element(self):
            elements = [pygame.image.load('sprites/startelement1.png'), pygame.image.load('sprites/startelement2.png')]
            stick = pygame.image.load('sprites/stick.png')
            current_image = 0
            loop = True
            while loop:
                self.screen.fill((0, 0, 0))
                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 510, 500))
                if current_image == 0:
                    self.screen.blit(elements[1], (0, 0))
                    self.screen.blit(stick, (-65 + 95*self.index, 240))
                    current_image = 1
                    pygame.time.wait(100)
                elif current_image == 1:
                    self.screen.blit(elements[0], (0, 0))
                    self.screen.blit(stick, (-65 + 95*self.index, 240))
                    current_image = 0
                    pygame.time.wait(100)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            if self.index > 0:
                                self.index -= 1
                        elif event.key == pygame.K_RIGHT:
                            if self.index < 4:
                                self.index += 1
                        elif event.key == pygame.K_RETURN:
                            loop = False
                            self.start_element = self.element_list[self.index]
                pygame.display.flip()