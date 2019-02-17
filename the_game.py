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

    pygame.mixer.init()
    dungeon_music = pygame.mixer.Sound('audio/dungeon.wav')
    dungeon_music.play()

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
        time_counter = pygame.time.get_ticks() - prev_time

        if GL.all_enemies_dead(enemy_party):
            screen.blit(background, (0, 0))
            if current_icon == icon:
                screen.blit(current_icon, (155, 255))
            if current_icon == icon2:
                screen.blit(current_icon, (155, 255))
            pygame.display.flip()
            time_counter = pygame.time.get_ticks()
            GL.update_screen(screen, character_party, enemy_party, current_pics, target_num, wizard_element_pic)
            if len(enemy_party) > 0:
                round += 1
            if pygame.time.get_ticks() - prev_char_animation > 300:
                prev_char_animation = pygame.time.get_ticks()
                if current_icon == icon:
                    screen.blit(icon2, (155, 255))  # player character
                    current_icon = icon2
                else:
                    screen.blit(icon, (155, 255))
                    current_icon = icon
            else:
                if current_icon == icon:
                    screen.blit(current_icon, (155, 255))
                if current_icon == icon2:
                    screen.blit(current_icon, (155, 255))
            text_box.update(screen)

            if shifting:
                spellbook.open(screen)

            enemy_party = GL.new_enemies(round, text_box, difficulty_scaling)
            screen.blit(background, (0, 0))
            if current_icon == icon:
                screen.blit(current_icon, (155, 255))
            if current_icon == icon2:
                screen.blit(current_icon, (155, 255))
            pygame.display.flip()

            for i in range(30):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                pygame.display.flip()
                GL.spawn_enemies(screen, enemy_party, current_pics, i//6)

            target_num = 0 if len(enemy_party) == 1 else target_num if target_num < len(enemy_party) else GL.LR_change(target_num, enemy_party)
            screen.blit(GL.boxes[current_pics[1] // 15], (target_num * 100, 55))
            GL.update_screen(screen, character_party, enemy_party, current_pics, target_num, wizard_element_pic)

            if difficulty_scaling < 3:
                difficulty_scaling = round//5 + 1



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

        if pygame.time.get_ticks() - prev_char_animation > 300:
            prev_char_animation = pygame.time.get_ticks()
            if current_icon == icon:
                screen.blit(icon2, (155, 255))  #player character
                current_icon = icon2
            else:
                screen.blit(icon, (155, 255) )
                current_icon = icon
        else:
            if current_icon == icon:
                screen.blit(current_icon, (155, 255))
            if current_icon == icon2:
                screen.blit(current_icon, (155, 255))


        for i in range(len(current_pics)):
            current_pics[i] = current_pics[i] + 2 if current_pics[i] <= 27 else 0   # for animation

        wizard_element_pic = wizard_element_pic + 2 if wizard_element_pic <= 27 else 0

        text_box.update(screen)

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
                if spell != None:
                    if spell.count(' ') == 1 and spell.split()[0] == 'praestituo' and spell.split()[1] in Wizard.game_spells and spell.split()[1] != 'confervo':
                        character_party[0].set_element(spell.split()[1])
                    elif spell.count(' ') >= 1:
                        GL.check_valid_prefix_spell(character_party[0], spell.rpartition(' ')[0], spell.rpartition(' ')[2], enemy_party, target_num)
                    else:
                        GL.check_valid_spell(character_party[0], spell, enemy_party[target_num])
                    GL.update_enemy_HP_bar(screen, enemy_party)
                    if not GL.health_is_gt_0(enemy_party[target_num]) and not GL.all_enemies_dead(enemy_party):
                        target_num = GL.LR_change(target_num, enemy_party)
                        screen.blit(GL.boxes[current_pics[1] // 15], (target_num * 100, 55))
                    if not GL.health_is_gt_0(enemy_party[target_num]):
                        GL.update_screen(screen, character_party, enemy_party, current_pics, target_num, wizard_element_pic)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
                shifting = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_LSHIFT:
                shifting = False

        # game attempt

        if time_counter > 8000:  # checks if 5 seconds have passed (for first level) then all units attack, attacking animation NOT IMPLEMENTED YET
            prev_time = pygame.time.get_ticks()
            GL.ai_constant_attack(screen, enemy_party, character_party[0])
            screen.fill((0, 0, 0))
            screen.blit(background_red, (0, 0))
            GL.update_HP_bar(screen, character_party[0])
            GL.update_enemy_HP_bar(screen, enemy_party)
            attacking_ani = [True, pygame.time.get_ticks()]
            screen.blit(icon, (155, 255))
            if shifting:
                spellbook.open(screen)
            text_box.update(screen)
        else:
            GL.update_enemy_atk_bar(screen, enemy_party, time_counter)


        if attacking_ani[0] and pygame.time.get_ticks() - attacking_ani[1] < 750:
            GL.update_screen_attacking(screen, character_party, enemy_party, current_pics, target_num, wizard_element_pic, spellbook, shifting)

        if shifting:
            spellbook.open(screen)

        pygame.display.flip()

        if GL.all_enemies_dead(enemy_party):
            screen.blit(background, (0, 0))
            if current_icon == icon:
                screen.blit(current_icon, (155, 255))
            if current_icon == icon2:
                screen.blit(current_icon, (155, 255))
            pygame.display.flip()

        if not GL.health_is_gt_0(character_party[0]):   #checks if the main character has health greater than 0, breaks loop if less than 0
            dungeon_music.stop()
            violins = pygame.mixer.Sound('audio/sad_violin.wav')
            violins.play()
            game_over(screen, round)

run_game()
