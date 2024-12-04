import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Snakes And Ladders")

run = True
while run:
    #background
    backimg = pygame.image.load("assets/background.jpg")
    stage = pygame.image.load("assets/snakes-and-ladder.png")
    arrow = pygame.image.load("assets/arrow.png")
    #players
    rl = pygame.image.load("assets/player1.png")
    bl = pygame.image.load("assets/player2.png")

    backimg = pygame.transform.smoothscale(backimg, (1280, 720))
    stage = pygame.transform.smoothscale(stage, (720, 720))
    arrow = pygame.transform.smoothscale(arrow, (50, 50))
    rl = pygame.transform.smoothscale(rl, (50, 50))
    bl = pygame.transform.smoothscale(bl, (50, 50))


    rx = 100
    ry = 251

    blx = 100
    bly = 362

    def bck():
        screen.blit(backimg, (0, 0))
        screen.blit(stage, (277, 0))
        screen.blit(arrow, (10, 90))

    def rplayer(x, y):
        screen.blit(rl, (x, y))

    def bplayer(x, y):
        screen.blit(bl, (x, y))

    bck()
    rplayer(rx, ry)
    bplayer(blx, bly)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()