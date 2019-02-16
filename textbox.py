import pygame


class TextBox:
    def __init__(self, screen):
        self.rect = pygame.Rect(0, 450, 510, 50)
        self.console = pygame.Rect(0, 0, 510, 50)
        self.font = pygame.font.SysFont(None, 50)
        self.text = ''
        self.console_message = 'oh no the magic men are here :('
        self.screen = screen
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.text_words = self.font.render(self.text, False, self.white)

    def input(self, event):
        if event.key != pygame.K_RIGHT and event.key != pygame.K_LEFT:
            if event.key == pygame.K_RETURN:
                print(self.text)
                spell = self.text
                self.text = ''
                return spell
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif self.text_words.get_width() < 470:
                self.text += event.unicode

    def change_console(self, text):
        self.console_message = text

    def update(self, screen):
        self.text_words = self.font.render(self.text, False, self.white)
        pygame.draw.rect(screen, self.black, self.rect)
        pygame.draw.rect(screen, self.black, self.console)
        screen.blit(self.text_words, (10, 455))
        screen.blit(self.font.render(self.console_message, False, self.white), (10, 5))