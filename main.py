import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Snakes And Ladders")

#background
backimg = pygame.image.load("assets/background.jpg")
stage = pygame.image.load("assets/snakes-and-ladder.png")
roll = pygame.image.load("assets/roll.png")
dicebackground = pygame.image.load("assets/dicebackground.png")
# arrow = pygame.image.load("assets/arrow.png")

#players
rl = pygame.image.load("assets/player1.png")
bl = pygame.image.load("assets/player2.png")

#size and location
backimg = pygame.transform.smoothscale(backimg, (1280, 720))
stage = pygame.transform.smoothscale(stage, (670, 670))
roll = pygame.transform.smoothscale(roll, (200, 200))
dicebackground = pygame.transform.smoothscale(dicebackground, (300, 300))
# arrow = pygame.transform.smoothscale(arrow, (50, 50))
rl = pygame.transform.smoothscale(rl, (50, 50))
bl = pygame.transform.smoothscale(bl, (50, 50))



#button
button = pygame.Rect(1140, 600, 100, 100)

player1 = pygame.font.SysFont("comicsansms", 25)
player2 = pygame.font.SysFont("comicsansms", 25)

rx = 225
ry = 560


blx = 225
bly = 625

def back():
    screen.blit(backimg, (0, 0))
    screen.blit(stage, (277, 25))
    screen.blit(dicebackground, (1090, 550))
    screen.blit(roll, (1100, 540))
    # screen.blit(arrow, (10, 90))

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

def player():
    msg1 = player1.render("Player 1", True, (0, 0, 255))
    screen.blit(msg1, [130, 560])
    msg2 = player2.render("Player 2", True, (255, 0, 0))
    screen.blit(msg2, [130, 625])

run = True
while run:

    back()
    rplayer(rx, ry)
    bplayer(blx, bly)
    player()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button.collidepoint(mouse_pos):
                pickNumber()
                dice, diceroll = pickNumber()
                dice = pygame.transform.smoothscale(dice, (150, 150))
                screen.blit(dice, (1000, 420))
                print(diceroll)
    pygame.display.update()
    time.sleep(0.8)

pygame.quit()