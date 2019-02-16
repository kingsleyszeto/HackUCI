class Wizard():
    elements = {'water': 'fire', 'fire': 'earth', 'earth': 'water', 'light': 'dark', 'dark': 'light'}
    game_spells = {'burn': 'fire', 'soak': 'water', 'wood': 'earth', 'requiem': 'dark', 'bright': 'light', 'heal' : 'heal'}
    game_prefixes = {'multi'}

    def __init__(self, element, level, text_box, is_main = False):
        self.element = element
        self.level = level
        self.is_main = is_main

        self.max_hp = 20 + level*5        #subject to change
        self.hp = self.max_hp
        self.damage = 5 + level*5    #subject to change
        self.defense = 3 + level*5   #subject to change
        self.spells = ['burn']
        self.prefixes = ['multi']

        self.energy = 0

        self.text_box = text_box

        if is_main:
            self.spells.append('heal')

        self.xp_worth = 5 * level

    def exec_turn(self, target, spell):
        if spell == 'heal':
            if self.hp + 10 > self.max_hp:
                self.hp += self.max_hp - self.hp
            else:
                self.hp += 10
        else:
            if Wizard.elements[Wizard.game_spells[spell]] == target.element:
                damage = int(2 * self.damage - self.defense)
            elif Wizard.elements[target.element] == Wizard.game_spells[spell]:
                damage = int((2 * self.damage - self.defense) // 4)
            elif Wizard.game_spells[spell] == target.element:
                damage = int(((2 * self.damage - self.defense)//2)  * 0.8)
            else:
                damage = int((2 * self.damage - self.defense) // 2)
            target.hp -= damage
            if self.is_main: self.text_box.change_console('Zalvin casts ' + spell + '! ' + str(damage) + ' DMG')
    def mistake(self):
        self.hp -= 5
        self.text_box.change_console('Zalvin bit his tongue! - 5HP')

    def exec_aoe(self, target, spell):
        if spell == 'heal':
            if self.hp + 3 > self.max_hp:
                self.hp += self.max_hp - self.hp
            else:
                self.hp += 3

        elif Wizard.elements[Wizard.game_spells[spell]] == target.element:
            target.hp -= int(2 * self.damage - self.defense) * 0.2
            print('super effective')
        elif Wizard.elements[target.element] == Wizard.game_spells[spell]:
            target.hp -= int((2 * self.damage - self.defense) // 4) * 0.2
            print('not every effective')
        elif Wizard.game_spells[spell] == target.element:
            target.hp -= int(((2 * self.damage - self.defense) // 2) * 0.8) * 0.2
            print('same element attack penalty')
        else:
            target.hp -= int((2 * self.damage - self.defense) // 2) * 0.2



