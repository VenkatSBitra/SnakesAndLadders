import pygame #imports modules 'pygame' and 'random'
import random

class Dice(object): #creates a class

    dice1 = pygame.image.load(r'D_1.png') #loads dice1
    dice2 = pygame.image.load(r'D_2.png') #loads dice2
    dice3 = pygame.image.load(r'D_3.png') #loads dice3
    dice4 = pygame.image.load(r'D_4.png') #loads dice4
    dice5 = pygame.image.load(r'D_5.png') #loads dice5
    dice6 = pygame.image.load(r'D_6.png') #loads dice6
    dice = [dice1, dice2, dice3, dice4, dice5, dice6] #creates a list to hold all the dice.

    def __init__(self):
        pass

    def number(self, gameDisplay):               #defining a function called number.
        for i in range(0, len(self.dice)):
            gameDisplay.blit(self.dice[i], (700,60))
            pygame.display.update()
            pygame.time.delay(100)
        self.num = random.randint(1, 6)
        gameDisplay.blit(self.dice[self.num - 1], (700,60))
        print("dice: "+ str(self.num))
        return self.num



