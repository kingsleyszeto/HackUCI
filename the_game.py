import pygame
from textbox import TextBox
from wizard import Wizard
from game_logic import Game_Logic
from spellbook import Spellbook
import time

def run_game():
    background = pygame.image.load('sprites/bkg.png')
    background_red = pygame.image.load('sprites/bkgred.png')
    background_dark_red = pygame.image.load('sprites/bkgdarkred.png')
    background_light = pygame.image.load('sprites/bkglight.png')
    pygame.init()
    GL = Game_Logic()
    screen = pygame.display.set_mode((510,500))
    screen.fill((125,125,125))
    spellbook = Spellbook(screen)
    pygame.display.flip()
    pygame.display.set_caption('Wizards')
    icon = pygame.image.load('sprites/logo.png')
    pygame.display.set_icon(icon)

    prev_time = pygame.time.get_ticks()                     #Used for getting time between minion attacks
    text_box = TextBox(screen)

    round = 1

    character_party = [Wizard('dark', 5, text_box, 140, True)]            #player's party (index always 0 unless we extend on game)
    enemy_party = [Wizard('earth', 1, text_box), Wizard('water', 1, text_box), Wizard('fire',1, text_box), Wizard('dark',1, text_box), Wizard('light',1, text_box)]       #Max size for party is 5

    current_pics = [0, 24, 12, 16, 8]                       #for animation purposes
    wizard_element_pic = 0
    target_num = 2                                          #index of what enemy to target

    shifting = False                                        #is the shift key being held

    while True:
        #print(pygame.time.get_ticks()) -> use if statements to do constant attacking

        screen.fill((0,0,0))
        if character_party[0].hp > character_party[0].max_hp*0.4:
            screen.blit(background, (0, 0))
        elif character_party[0].hp > character_party[0].max_hp*0.2:
            screen.blit(background_red, (0,0))
        else:
            screen.blit(background_dark_red, (0,0))
        GL.update_HP_bar(screen, character_party[0])
        GL.update_enemy_HP_bar(screen, enemy_party)
        GL.update_screen(screen, character_party, enemy_party, current_pics, target_num, wizard_element_pic)     #animates all characters


        screen.blit(icon, (150, 250) )                                      #player character


        for i in range(len(current_pics)):
            current_pics[i] = current_pics[i] + 2 if current_pics[i] <= 27 else 0   # for animation

        wizard_element_pic = wizard_element_pic + 2 if wizard_element_pic <= 27 else 0

        text_box.update(screen)

        if shifting:
            spellbook.open(screen)

        #pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key != pygame.K_LSHIFT:            #checks to see if target needs to be changed or if user is typing
                spell = text_box.input(event)
                new_index = GL.key_LR(event, target_num, enemy_party)
                if new_index != None:
                    target_num = new_index
                    print('new target num', target_num)
                if spell != None:
                    if spell.count(' ') >= 1:
                        GL.check_valid_prefix_spell(character_party[0], spell.rpartition(' ')[0], spell.rpartition(' ')[2], enemy_party, target_num)
                    else:
                        GL.check_valid_spell(character_party[0], spell, enemy_party[target_num])
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
                shifting = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_LSHIFT:
                shifting = False



        #game attempt
        if pygame.time.get_ticks() - prev_time > 5000:  #checks if 5 seconds have passed (for first level) then all units attack, attacking animation NOT IMPLEMENTED YET
            prev_time = pygame.time.get_ticks()
            GL.ai_constant_attack(screen, enemy_party, character_party[0])
            screen.fill((0, 0, 0))
            screen.blit(background_red, (0, 0))
            GL.update_HP_bar(screen, character_party[0])
            GL.update_enemy_HP_bar(screen, enemy_party)
            GL.update_screen_attacking(screen, character_party, enemy_party, current_pics, target_num, wizard_element_pic)
            text_box.update(screen)
            screen.blit(icon, (150, 250))
            if shifting:
                spellbook.open(screen)
            print(character_party[0].hp)
        pygame.display.flip()
        pygame.time.wait(40)


        #if not GL.health_is_gt_0(character_party[0]):   #checks if the main character has health greater than 0, breaks loop if less than 0
         #   break

        if GL.all_enemies_dead(enemy_party):
            round += 1
            enemy_party = GL.new_enemies(round, text_box)

        print(character_party[0].hp)
        print(target_num)

        print('len', len(enemy_party))
run_game()
