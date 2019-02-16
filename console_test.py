from wizard import Wizard
from random import randint
from game_logic import Game_Logic

GL = Game_Logic()
enemies =  [Wizard('earth', 1)] #, Wizard('water', 1), Wizard('earth', 1)]

you = Wizard('fire', 1)
you.hp = 25
while you.hp > 0:
    print('your hp', you.hp)
    for enemy in enemies:
        print('enemy hps', enemy.hp)

    spell_num = (input('input a spell '))
    GL.check_valid_spell(you, spell_num, enemies[0])

    #you.exec_turn(enemies[0], you.spells[spell_num])

    #you.exec_turn(enemies[randint(0, len(enemies)) - 1], you.spells[randint(0,len(you.spells)) - 1])

    enemy.exec_turn(you, 'burn')

    print()
