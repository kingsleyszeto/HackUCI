class Wizard():
    elements = {'water': 'fire', 'fire': 'earth', 'earth': 'water', 'light': 'dark', 'dark': 'light'}
    game_spells = {'burn': 'fire', 'soak': 'water', 'wood': 'earth', 'requiem': 'dark', 'bright': 'light', 'heal' : 'heal'}
    game_prefixes = {'multi'}

    def __init__(self, element, level, is_main = False):
        self.element = element
        self.level = level
        self.is_main = is_main

        self.max_hp = 20 + level*5        #subject to change
        self.hp = self.max_hp
        self.damage = 5 + level*5    #subject to change
        self.defense = 3 + level*5   #subject to change
        self.spells = ['burn']

        self.energy = 0


        if is_main:
            self.spells.append('heal')

        self.xp_worth = 5 * level

    def exec_turn(self, target, spell):
        if spell == 'heal':
            if self.hp + 10 > self.max_hp:
                self.hp += self.max_hp - self.hp
            else:
                self.hp += 10

        elif Wizard.elements[Wizard.game_spells[spell]] == target.element:
            target.hp -=  int( 2 * self.damage - self.defense)
            print('super effective')
        elif Wizard.elements[target.element] == Wizard.game_spells[spell]:
            target.hp -= int((2 * self.damage - self.defense) // 4)
            print('not every effective')
        elif Wizard.game_spells[spell] == target.element:
            target.hp -= int(((2 * self.damage - self.defense)//2)  * 0.8)
            print('same element attack penalty')
        else:
            target.hp -= int((2 * self.damage - self.defense) // 2)






