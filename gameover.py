import pygame


def game_over(screen, round, score=0):
    while True:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 30)
        text1 = font.render('You survived ' + str(round-1) + ' rounds', False, (255, 255, 255))
        text2 = font.render('Score: ' + str(score), False, (255, 255, 255))
        screen.blit(pygame.image.load('sprites/deadscreen.png'), (0, 0))
        screen.blit(text1, (150, 200))
        #screen.blit(text2, (200, 230))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                pygame.quit()
                quit()
        pygame.display.flip()