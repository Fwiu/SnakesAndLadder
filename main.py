import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((650, 500))
pygame.display.set_caption("Snakes And Ladders")

#background
backimg = pygame.image.load("assets/snakes-and-ladder.jpg")
stage = pygame.image.load("assets/snakes-and-ladder.jpg")

backimg = pygame.transform.smoothscale(backimg, (400, 350))

bx = 150
by = 5

#players
rl = pygame.image.load("assets/player1.png")
bl = pygame.image.load("assets/player2.png")

rx = 100
ry = 251

blx = 100
bly = 251

def back():
    screen.blit(backimg, (0, 0))
    screen.blit(backimg, (bx, by))

def rplayer(x, y):
    screen.blit(rl, (x, y))

def bplayer(x, y):
    screen.blit(bl, (x, y))

back()
rplayer(rx, ry)
bplayer(blx, bly)
pygame.display.update()
pygame.quit()
