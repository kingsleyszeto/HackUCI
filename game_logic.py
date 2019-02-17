from random import randint
from wizard import Wizard
import pygame
import time




class Game_Logic:
    game_spells = {'burn': 'fire', 'soak': 'water', 'wood': 'earth', 'requiem': 'dark', 'bright': 'light',
                   'heal': 'heal'}
    prefix = {'explosive': 'aoe'}
    elements = {'water': 'fire', 'fire': 'earth', 'earth': 'water', 'light': 'dark', 'dark': 'light'}


    def __init__(self):
        self.fire_pics = [pygame.image.load('sprites/smallfire1.png'), pygame.image.load('sprites/smallfire2.png')]
        self.water_pics = [pygame.image.load('sprites/smallwater1.png'), pygame.image.load('sprites/smallwater2.png')]
        self.earth_pics = [pygame.image.load('sprites/smallleaf1.png'), pygame.image.load('sprites/smallleaf2.png')]
        self.light_pics = [pygame.image.load('sprites/smalllight1.png'), pygame.image.load('sprites/smalllight2.png')]
        self.dark_pics = [pygame.image.load('sprites/smalldark1.png'), pygame.image.load('sprites/smalldark2.png')]
        self.fire_en = [pygame.image.load('sprites/fireen1.png'), pygame.image.load('sprites/fireen2.png')]
        self.fire_en_atk = pygame.image.load('sprites/fireenatk.png')
        self.fire_en_dead = pygame.image.load('sprites/fireendead.png')
        self.water_en = [pygame.image.load('sprites/wateren1.png'), pygame.image.load('sprites/wateren2.png')]
        self.water_en_atk = pygame.image.load('sprites/waterenatk.png')
        self.water_en_dead = pygame.image.load('sprites/waterendead.png')
        self.earth_en = [pygame.image.load('sprites/earthen1.png'), pygame.image.load('sprites/earthen2.png')]
        self.earth_en_atk = pygame.image.load('sprites/earthenatk.png')
        self.earth_en_dead = pygame.image.load('sprites/earthendead.png')
        self.light_en = [pygame.image.load('sprites/lighten1.png'), pygame.image.load('sprites/lighten2.png')]
        self.light_en_atk = pygame.image.load('sprites/lightenatk.png')
        self.light_en_dead = pygame.image.load('sprites/lightendead.png')
        self.dark_en = [pygame.image.load('sprites/darken1.png'), pygame.image.load('sprites/darken2.png')]
        self.dark_en_atk = pygame.image.load('sprites/darkenatk.png')
        self.dark_en_dead = pygame.image.load('sprites/darkendead.png')
        self.boxes = [pygame.image.load('sprites/RedBox1.png'), pygame.image.load('sprites/RedBox2.png')]

    def check_valid_spell(self, m_c, spell, target):
        if spell in m_c.game_spells:
            m_c.exec_turn(target, spell)
            print(True)
        else:
            m_c.mistake()

    def check_valid_prefix_spell(self, m_c, prefix, spell, targets, target_num):
        if spell in m_c.game_spells and prefix in Wizard.game_prefixes:
            m_c.exec_turn(targets[target_num], spell)
            if prefix == 'ledo magis hosti':
                for target in targets:
                    m_c.exec_aoe(target, spell)
            print(True)
        else:
            m_c.mistake()

    def ai_constant_attack(self, screen, enemy_party, m_c):
        for count, enemy in enumerate(enemy_party):
            self.ai_choose_spell( enemy, m_c)

    def ai_choose_spell(self, enemy, m_c):
        if enemy.element is 'fire':
            spell = 'ambustum'
        elif enemy.element is 'water':
            spell = 'macerari'
        elif enemy.element is 'earth':
            spell = 'planicia'
        elif enemy.element is 'light':
            spell = 'opscurum'
        elif enemy.element is 'dark':
            spell = 'illustris'
        if self.health_is_gt_0(enemy):
            enemy.exec_turn(m_c, spell)

    def health_is_gt_0(self, unit):
        if unit.hp > 0:
            return True
        return False

    def all_enemies_dead(self, enemy_party):
        return all([not self.health_is_gt_0(enemy) for enemy in enemy_party])

    def new_enemies(self, level, text_box, difficulty_scaling):
            return [Wizard([element for element in Game_Logic.elements][randint(0,4)], level // 2,text_box) for i in range(randint(0, difficulty_scaling))]



    def update_screen(self, screen, character_party, enemy_party, current_pics, target_num, wizard_element_pic): #animation
          #may move into settings
        exec("screen.blit(self.{element}_pics[wizard_element_pic // 15], (277, 224))".format(element=character_party[0].element))
        for i in range(len(enemy_party)):
            if self.health_is_gt_0(enemy_party[i]):
                exec("screen.blit(self.{element}_pics[current_pics[i] // 15], ( i * 100 + 25, 55))".format(element = enemy_party[i].element))
                exec("screen.blit(self.{element}_en[current_pics[i]//15], (i*100 + 10, 95))".format(element = enemy_party[i].element))
            else:
                exec("screen.blit(self.{element}_en_dead, (i*100 + 10, 95))".format(element=enemy_party[i].element))
        screen.blit(self.boxes[current_pics[1] // 15], (target_num * 100,55))

    def update_screen_attacking(self, screen, character_party, enemy_party, current_pics, target_num, wizard_element_pic): #animation
          #may move into settings
        exec("screen.blit(self.{element}_pics[wizard_element_pic // 15], (277, 224))".format(element=character_party[0].element))
        for i in range(len(enemy_party)):
            if self.health_is_gt_0(enemy_party[i]):
                exec("screen.blit(self.{element}_pics[current_pics[i] // 15], ( i * 100 + 25, 55))".format(element = enemy_party[i].element))
                exec("screen.blit(self.{element}_en_atk, (i*100 + 10, 95))".format(element = enemy_party[i].element))
            else:
                exec("screen.blit(self.{element}_en_dead, (i*100 + 10, 95))".format(element=enemy_party[i].element))
        pygame.display.update()

        screen.blit(self.boxes[current_pics[1] // 15], (target_num * 100,55))

    def key_LR(self, event, target_num, enemy_party):    #moves the target and red box
        tn = target_num
        if event.key == pygame.K_RIGHT:
            tn += 1
            if tn > len(enemy_party) - 1:
                tn = 0
            while(not self.health_is_gt_0(enemy_party[tn])):
                tn += 1
                if tn > len(enemy_party) - 1:
                    tn = 0
            return tn
        elif event.key == pygame.K_LEFT:
            tn -= 1
            if tn < 0:
                tn = len(enemy_party) - 1
            while (not self.health_is_gt_0(enemy_party[tn])):
                tn -= 1
                if tn < 0:
                    tn = len(enemy_party) - 1
            return tn

    def gen_new_level(self, level_num, enemy_party): #returns a new enemy party list when the one in the current level has died
        for i in range(5):
            enemy_party.append(Wizard([element for element in Game_Logic.elements][randint(0,4)], level_num // 2))
        return enemy_party

    def update_HP_bar(self, screen, m_c):
        m_c_hp = m_c.hp
        HP_bar = pygame.Rect((50, 450 - 200*(m_c_hp/m_c.max_hp)), (15, 200*(m_c_hp/m_c.max_hp)))
        screen.fill((255, 100, 100), HP_bar)

    def update_enemy_HP_bar(self, screen, enemy_party):
        for i in range(len(enemy_party)):
            if self.health_is_gt_0(enemy_party[i]):
                exec("screen.fill((255,100,100), pygame.Rect(( i * 100 + 30, 200), (({enemy}.hp/{enemy}.max_hp) * 40, 6)))".format(enemy = 'enemy_party[i]'))

    def spawn_enemies(self, screen, enemy_party, current_pics, row):
        for i in range(len(enemy_party)):
            exec("screen.blit(self.{element}_pics[current_pics[i] // 15], ( i * 100 + 25, 55), (0,0,100,row*10) )".format(
                element=enemy_party[i].element))
