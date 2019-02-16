class Wizard():
    elements = {'water': 'fire', 'fire': 'earth', 'earth': 'water', 'light': 'dark', 'dark': 'light'}
    game_spells = {'ambustum': 'fire', 'macerari': 'water', 'planicia': 'earth', 'opscurum': 'dark',
                   'illustris': 'light', 'confervo': 'heal'}  ###
    spell_to_text = {'fire': 'Burn', 'water': 'Soak', 'earth': 'Sand', 'dark': 'Shadow', 'light': 'Light',
                     'heal': 'heal'}
    aoe_to_text = {'fire': 'Explosion', 'water': 'Flood', 'earth': 'Earthquake', 'dark': 'Requiem',
                   'light': 'Solar Flare'}
    game_prefixes = {'ledo magis hosti': 'multi'}

    def __init__(self, element, level, text_box, max_hp = 20, is_main = False):
        self.element = element
        self.level = level
        self.is_main = is_main

        self.max_hp = max_hp + level*5        #subject to change
        self.hp = self.max_hp
        self.damage = 5 + level*5    #subject to change
        self.defense = 3 + level*5   #subject to change


        self.energy = 0

        self.text_box = text_box


        self.xp_worth = 5 * level

    def exec_turn(self, target, spell):
        if spell == 'confervo':
            if self.hp + 10 > self.max_hp:
                heal = self.max_hp - self.hp
            else:
                heal = 25
            self.hp += heal
            self.text_box.change_console('Zalvin casts heal! +' + str(heal) + ' HP')
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
            if self.is_main: self.text_box.change_console('Zalvin casts ' + Wizard.spell_to_text[Wizard.game_spells[spell]] + '!')

    def mistake(self):
        self.hp -= 5
        self.text_box.change_console('Zalvin bit his tongue! - 5HP')

    def exec_aoe(self, target, spell):
        if spell == 'confervo':
            if target.hp + 3 > target.max_hp:
                target.hp += target.max_hp - target.hp
            else:
                target.hp += 3
            self.text_box.change_console('You healed the enemy. Nice.')

        else:
            if Wizard.elements[Wizard.game_spells[spell]] == target.element:
                damage = int(2 * self.damage - self.defense) * 0.3
            elif Wizard.elements[target.element] == Wizard.game_spells[spell]:
                damage = int((2 * self.damage - self.defense) // 4) * 0.3
            elif Wizard.game_spells[spell] == target.element:
                damage = int(((2 * self.damage - self.defense) // 2) * 0.8) * 0.3
            else:
                damage = int((2 * self.damage - self.defense) // 2) * 0.3
            target.hp -= damage
            if self.is_main: self.text_box.change_console(
                'Zalvin casts ' + Wizard.aoe_to_text[Wizard.game_spells[spell]] + '!')

    def set_element(self, new_element):
        self.element = Wizard.game_spells[new_element]



