import pygame
import random

class Dice(object):

    dice1 = pygame.image.load(r'D_1.png')
    dice2 = pygame.image.load(r'D_2.png')
    dice3 = pygame.image.load(r'D_3.png')
    dice4 = pygame.image.load(r'D_4.png')
    dice5 = pygame.image.load(r'D_5.png')
    dice6 = pygame.image.load(r'D_6.png')
    dice = [dice1, dice2, dice3, dice4, dice5, dice6]

    def __init__(self):
        pass

    def number(self, gameDisplay):
        for i in range(0, len(self.dice)):
            gameDisplay.blit(self.dice[i], (700,60))
            pygame.display.update()
            pygame.time.delay(100)
        self.num = random.randint(1, 6)
        gameDisplay.blit(self.dice[self.num - 1], (700,60))
        print("dice: "+ str(self.num))
        return self.num



