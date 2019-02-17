ele_list = {'dark': 'P', 'earth': 'G', 'water': 'W', 'fire': 'R', 'light': 'Y'}
type = 'earth'
listpics = [exec('pygame.image.load("sprites/{element}atk.png")'.format(element = type, number = num + 1)),
            exec('pygame.image.load("sprites/{color_letter}ombieAttack.png"'.format(color_letter = Game_Logic.ele_list[type])),
            exec('pygame.image.load("sprites{color_letter}BlobAttack.png"'.format(color_letter = Game_Logic.ele_list[type]))]
print(listpics)