import pygame
from Player import *

pygame.init()

gameDisplay = pygame.display.set_mode((900,700))

pygame.display.set_caption("Snakes and Ladders")

clock = pygame.time.Clock()

retry = True
crashed = False

board = pygame.image.load(r"snakes_ladders.png")
token1 = pygame.image.load(r"token1.png")
token2 = pygame.image.load(r"token2.png")
blank = pygame.image.load(r"empty.png")

player1 = Player(0, token1, "Player 1")
player2 = Player(0, token2, "Player 2")

dice = Dice()
move = True

fontP = pygame.font.SysFont("Times New Roman", 45, True)

gameDisplay.blit(board, (0, 60))

while not crashed:
        
    pygame.draw.rect(gameDisplay, (255, 64, 64), (700, 500, 100, 50))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos[0] > 700 and mouse_pos[0] < 800 and mouse_pos[1] > 500 and mouse_pos[1] < 550:
        if pygame.mouse.get_pressed() == (True, False, False):
            #pygame.time.delay(100)
            if move:
                num = dice.number(gameDisplay)
                player1.move(num)
                gameDisplay.blit(board, (0,60))
                player1.draw(gameDisplay)
                if player2.num != 0:
                    player2.draw(gameDisplay)
                if num == 6:
                    move = True
                    player1.numSix += 1
                else:
                    move = False
            else:
                num = dice.number(gameDisplay)
                player2.move(num)
                gameDisplay.blit(board, (0,60))
                player1.draw(gameDisplay)
                player2.draw(gameDisplay)
                if num == 6:
                    move = False
                    player2.numSix += 1
                else:
                    move = True
    pygame.display.update()
    if player1.num == 100 or player2.num == 100:
        if player1.num == 100:
            print(player1.name + " wins!!")
            crashed = True
        else:
            print(player2.name + " wins!!")
            crashed = True

pygame.quit()
quit()

