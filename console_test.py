import pygame
from textbox import TextBox
from wizard import Wizard
from game_logic import Game_Logic
from spellbook import Spellbook
from intro import Intro
from gameover import game_over

def run_game():
    background = pygame.image.load('sprites/background.png')
    background_red = pygame.image.load('sprites/darkbackground.png')
    background_dark_red = pygame.image.load('sprites/dyingbackground.png')

    pygame.init()
    GL = Game_Logic()
    screen = pygame.display.set_mode((510,500))
    screen.fill((125,125,125))
    spellbook = Spellbook(screen)
    pygame.display.flip()
    pygame.display.set_caption('Wizards')
    icon = pygame.image.load('sprites/logo.png')
    icon2 = pygame.image.load('sprites/logo1.png')
    pygame.display.set_icon(icon)
    current_icon = icon
    prev_char_animation = pygame.time.get_ticks() #Used for getting time between character animation movements
    prev_time = pygame.time.get_ticks()  #Used for getting time between minion attacks
    text_box = TextBox(screen)

    intro = Intro(screen)
    intro.play_intro()

    round = 1

    character_party = [Wizard(intro.start_element, 5, text_box, 140, True)]            #player's party (index always 0 unless we extend on game)
    #enemy_party = [Wizard('earth', 1, text_box), Wizard('water', 1, text_box), Wizard('fire',1, text_box), Wizard('dark',1, text_box), Wizard('light',1, text_box)]       #Max size for party is 5
    enemy_party = []
    current_pics = [0, 24, 12, 16, 8]                       #for animation purposes
    wizard_element_pic = 0
    target_num = 0                                         #index of what enemy to target

    shifting = False                                        #is the shift key being held


    difficulty_scaling = 1                                  #current loop, used for difficulty scaling

    attacking_ani = [False, 0]                                   #for animation

    while True: