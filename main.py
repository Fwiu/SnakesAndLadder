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

font1 = pygame.font.SysFont("comicsansms", 25)
font2 = pygame.font.SysFont("comicsansms", 20)

start1 = [225, 560]
start2 = [225, 625]


# rx = 225
# ry = 560


# blx = 225
# bly = 625

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
    diceroll = random.randint(5, 6)
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
    msg1 = font1.render("Player 1", True, (0, 0, 255))
    screen.blit(msg1, [130, 560])
    msg2 = font1.render("Player 2", True, (255, 0, 0))
    screen.blit(msg2, [130, 625])

def rollr():
    msg3 = font2.render("Your Turn", True, (0, 0, 0))
    screen.blit(msg3, [130, 535])

def rollb():
    msg4 = font2.render("Your Turn", True, (0, 0, 0))
    screen.blit(msg4, [130, 600])

# def move_player():




run = True

turn = 'red'

while run:

    back()
    rplayer(start1[0], start1[1])
    bplayer(start2[0], start2[1])
    player()

    if turn == 'red':
        rollr()
    else:
        rollb()


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

            #for Player 1
            if pickNumber() and turn == 'red':
                turn='blue'
                if diceroll == 6 and start1 == True:
                    rx = 300
                    ry = 625
                    turn = 'red'
            #for Player 2
            elif pickNumber() and turn == 'blue':
                turn='red'
                if diceroll == 6 and start2 == True:
                    blx = 300
                    bly = 625
                    turn = 'blue'

    pygame.display.update()
    time.sleep(0.4)

pygame.quit()