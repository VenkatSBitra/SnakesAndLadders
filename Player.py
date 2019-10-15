import pygame
from Dice import *

global ladder
global snake

ladder = [[3, 51], [6, 27], [20, 70], [36, 55], [63, 95], [68, 98]]
snake = [[34, 1], [25, 5], [47, 19], [65, 52], [87, 57], [91, 61], [99, 69]]

class Player(object):
    def __init__(self, num, token, name):
        self.num = num
        self.name = name
        self.x_player = 0
        self.y_player = 0
        self.token = token
        self.moveCount = 0
        self.numSnake = 0
        self.numLadder = 0
        self.numSix = 0
        
    def move(self, diceval):
        self.num = self.num + diceval
        for i in range(0, len(ladder)):
            if ladder[i][0] == self.num:
                self.num = ladder[i][1]
                self.numLadder += 1
        for i in range(0, len(snake)):
            if snake[i][0] == self.num:
                self.num = snake[i][1] 
                self.numSnake += 1
        if self.num > 100:
            self.num = self.num - diceval
        if self.num % 10 == 0:
            self.x_player = 576
            self.y_player = 700 - (((self.num // 10)) * 64)
        else:
            self.x_player = 64 * ((self.num % 10) - 1)
            self.y_player = 700 - (((self.num // 10) + 1) * 64)
        
        self.moveCount += 1
        print(self.name + ": " + str(self.num) + " " + str(self.numLadder) + " " + str(self.numSnake) + " " + str(self.numSix) + " " + str(self.moveCount))
        

    def draw(self, gameDisplay):
        gameDisplay.blit(self.token, (self.x_player, self.y_player))




