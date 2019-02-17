import pygame
from textbox import TextBox
from wizard import Wizard
from game_logic import Game_Logic
from spellbook import Spellbook
from intro import Intro
from gameover import game_over

def run_game():
    pygame.init()
    background = pygame.image.load('sprites/ant1.png')                     #for animation purposes
    screen = pygame.display.set_mode((510,500))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        screen.blit(background, (0,0) )
        pygame.display.flip()


run_game()