import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Snakes And Ladders")

#background
backimg = pygame.image.load("assets/background.jpg")
stage = pygame.image.load("assets/snakes-and-ladder.png")
arrow = pygame.image.load("assets/arrow.png")

#players
rl = pygame.image.load("assets/player1.png")
bl = pygame.image.load("assets/player2.png")

#size and location
backimg = pygame.transform.smoothscale(backimg, (1280, 720))
stage = pygame.transform.smoothscale(stage, (720, 720))
arrow = pygame.transform.smoothscale(arrow, (50, 50))
rl = pygame.transform.smoothscale(rl, (50, 50))
bl = pygame.transform.smoothscale(bl, (50, 50))

#button
button = pygame.Rect(100, 500, 400, 400)


rx = 100
ry = 251

blx = 100
bly = 362

def back():
    screen.blit(backimg, (0, 0))
    screen.blit(stage, (277, 0))
    screen.blit(arrow, (10, 90))

def rplayer(x, y):
    screen.blit(rl, (x, y))

def bplayer(x, y):
    screen.blit(bl, (x, y))

def pickNumber():
    diceroll = random.randint(1, 6)
    if diceroll==1:
        dice = pygame.image.load("assets/Dice1.png")
    elif diceroll==2:
        dice = pygame.image.load("assets/Dice2.png")
    elif diceroll==3:
        dice = pygame.image.load("assets/Dice3.png")
    elif diceroll==4:
        dice = pygame.image.load("assets/Dice4.png")
    elif diceroll==5:
        dice = pygame.image.load("assets/Dice5.png")
    elif diceroll==6:
        dice = pygame.image.load("assets/Dice6.png")

    return(dice, diceroll)

run = True
while run:

    back()
    rplayer(rx, ry)
    bplayer(blx, bly)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button.collidepoint(mouse_pos):
                pickNumber()
                dice, diceroll = pickNumber()
                screen.blit(dice, (50, 60))
                print(diceroll)
    pygame.display.update()
    # time.sleep(1.3)

pygame.quit()