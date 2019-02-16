from random import randint
from wizard import Wizard
import pygame




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
        self.water_en = [pygame.image.load('sprites/wateren1.png'), pygame.image.load('sprites/wateren2.png')]
        self.earth_en = [pygame.image.load('sprites/earthen1.png'), pygame.image.load('sprites/earthen2.png')]
        self.light_en = [pygame.image.load('sprites/lighten1.png'), pygame.image.load('sprites/lighten2.png')]
        self.dark_en = [pygame.image.load('sprites/darken1.png'), pygame.image.load('sprites/darken2.png')]
        self.boxes = [pygame.image.load('sprites/RedBox1.png'), pygame.image.load('sprites/RedBox2.png')]

    def check_valid_spell(self, m_c, spell, target):
        if spell in m_c.spells:
            m_c.exec_turn(target, spell)
            print(True)
        else:
            m_c.mistake()

    def check_valid_prefix_spell(self, m_c, prefix, spell, targets, target):
        if spell in m_c.spells and prefix in m_c.prefixes:
            m_c.exec_turn(targets[target], spell)
            if prefix == 'multi':
                for target in targets:
                    m_c.exec_turn(target, spell)
            print(True)
        else:
            m_c.mistake()

    def ai_constant_attack(self, enemy_party, m_c):
        for enemy in enemy_party:
            self.ai_choose_spell(enemy, m_c)

    def ai_choose_spell(self, enemy, m_c):                              #add healing
        enemy.exec_turn(m_c, enemy.spells[randint(0, len(enemy.spells)  - 1)] )

    def health_is_gt_0(self, unit):
        if unit.hp > 0:
            return True
        return False

    def all_enemies_dead(self, enemy_party):
        return all([not self.health_is_gt_0(enemy) for enemy in enemy_party])

    def new_enemies(self, level, text_box):
            return [Wizard([element for element in Game_Logic.elements][randint(0,4)], level // 2,text_box) for i in range(5)]



    def update_screen(self, screen, character_party, enemy_party, current_pics, target_num, wizard_element_pic): #animation
          #may move into settings
        exec("screen.blit(self.{element}_pics[wizard_element_pic // 15], (275, 220))".format(element=character_party[0].element))
        for i in range(len(enemy_party)):
            if self.health_is_gt_0(enemy_party[i]):
                exec("screen.blit(self.{element}_pics[current_pics[i] // 15], ( i * 100 + 25, 55))".format(element = enemy_party[i].element))
                exec("screen.blit(self.{element}_en[current_pics[i]//15], (i*100 + 10, 95))".format(element = enemy_party[i].element))
        screen.blit(self.boxes[current_pics[1] // 15], (target_num * 100,55))

    def key_LR(self, event, target_num, enemy_party):    #moves the target and red box
        tn = target_num
        if event.key == pygame.K_RIGHT:
            tn += 1
            if tn > 4:
                tn = 0
            while(not self.health_is_gt_0(enemy_party[tn])):
                tn += 1
                if tn > 4:
                    tn = 0
            return tn
        elif event.key == pygame.K_LEFT:
            tn -= 1
            if tn < 0:
                tn = 4
            while (not self.health_is_gt_0(enemy_party[tn])):
                tn -= 1
                if tn < 0:
                    tn = 4
            return tn

    def gen_new_level(self, level_num, enemy_party): #returns a new enemy party list when the one in the current level has died
        for i in range(5):
            enemy_party.append(Wizard([element for element in Game_Logic.elements][randint(0,4)], level_num // 2))
        return enemy_party

    def update_HP_bar(self, screen, m_c):
        m_c_hp = m_c.hp
        HP_bar = pygame.Rect((50, 450 - 5*m_c_hp), (15, m_c_hp*5))
        screen.fill((255, 100, 100), HP_bar)








