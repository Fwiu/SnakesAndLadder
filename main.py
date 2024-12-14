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
bl = pygame.image.load("assets/player1.png")
rl = pygame.image.load("assets/player2.png")

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

# start1 = [225, 560]
# start2 = [225, 625]

# tiles1 = [300, 625]
# TILES = {
#     [225, 560], [300, 625], 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
# }

# POS_TILE = {
#     [TILES[0] = '123, 123'],
#     [TILES[1]],
#     [TILES[3]],
#     [TILES[4]],
#     [TILES[5]],
#     }

# SNAKES = {
#         27: 8,
#         34: 7,
#         29: 3,
#         69: 31,
#         72: 36,
#         77: 46,
#         80: 41,
#         96: 48,
#         98: 79,
#     }

# LADDERS = {
#     4: 16,
#     6: 25,
#     12: 49,
#     20: 40,
#     38: 88,
#     58: 62,
#     71: 93,
#     78: 84,
#     86: 95,
#     }


# LAST_TILES = 100



rx = 225
ry = 560


blx = 225
bly = 625

class SnakesAndLadders:
    
    def __init__(self, n_players):
        self.n_players = 2
        self.players = n_players
        self.turn = 0
        self.winner = None 

    def back():
        screen.blit(backimg, (0, 0))
        screen.blit(stage, (277, 25))
        screen.blit(dicebackground, (1090, 550))
        screen.blit(roll, (1100, 540))
        # screen.blit(arrow, (10, 90))

    # def players(self, rplayer, bplayer):
    #     self.rplayer = rplayer
    #     self.bplayer = bplayer

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

    def font_player():
        msg1 = font1.render("Player 1", True, (255, 0, 0))
        screen.blit(msg1, [130, 560])
        msg2 = font1.render("Player 2", True, (0, 0, 255))
        screen.blit(msg2, [130, 625])

    def rollr():
        msg3 = font2.render("Your Turn", True, (0, 0, 0))
        screen.blit(msg3, [130, 535])

    def rollb():
        msg4 = font2.render("Your Turn", True, (0, 0, 0))
        screen.blit(msg4, [130, 600])

    # def move_player(self, player_i):
    #     prev_pos = self.players[player_i]
    #     new_pos = prev_pos + self.pickNumber()

    #     if new_pos >= self.LAST_TILES:
    #         self.winner = player_i
    #         new_pos = self.LAST_TILES
    #     elif new_pos in self.SNAKES:
    #         new_pos = self.SNAKES[new_pos]
    #     elif new_pos in self.LADDERS:
    #         new_pos = self.LADDERS[new_pos]
        
    #     self.players[player_i] = new_pos

    #move player
    # def move_players(self):
    #     for player_i in range(self.n_players):
    #         self.move_player(player_i)
    #         if self.winner is not None: # done with game
    #             break

    # def play_game(self):
    #     while self.winner is None:
    #         self.turn += 1
    #         self.move_players()
    #     return f"Player #{self.winner+1} Wins!"

    run = True

    turn = 'red'

    while run:

        back()
        rplayer(rx, ry)
        bplayer(blx, bly)
        font_player()

        if turn == 'blue':
            rollb()
        else:
            rollr()


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
                # if pickNumber() and turn == 'blue':
                #     turn = 'red'
                #     if 
                # elif pickNumber() and turn == 'red':
                #     turn = 'blue'

                #for Player 1
                    #row 1
                if pickNumber() and turn == 'red':
                    turn='blue'
                    if diceroll in range (1, 6) and rx == 225 and ry == 560:
                        rx = 300
                        ry = 625
                        turn = 'red'
                    elif rx in range (300, 625) and diceroll != 6 and (ry == 625 or ry == 497 or ry == 369 or ry == 241 or ry == 113):
                        rx = rx + (64*diceroll)
                    elif rx in range (300, 625) and diceroll == 6 and (ry == 625 or ry == 497 or ry == 369 or ry == 241 or ry == 113):
                        rx = rx + (64*diceroll)
                        turn = 'red'
                    elif rx == 300 and diceroll != 6 and (ry == 625 or ry == 497 or ry == 369 or ry == 241 or ry == 113):
                        rx = rx + (64*diceroll)
                    elif rx == 300 and diceroll == 6 and (ry == 625 or ry == 497 or ry == 369 or ry == 241 or ry == 113):
                        rx = rx + (64*diceroll)
                        ry = ry - 64
                        turn = 'red'
                    elif rx == 620 and diceroll <= 4 and (ry == 625 or ry == 497 or ry == 369 or ry == 241 or ry == 113): #7
                        rx = rx + (64*diceroll)
                    elif rx == 620 and diceroll >= 4 and diceroll != 6 and (ry == 625 or ry == 497 or ry == 369 or ry == 241 or ry == 113):
                        rx = rx + (64*diceroll)
                        ry = ry - 64
                    elif rx == 620 and diceroll == 6 and (ry == 625 or ry == 497 or ry == 369 or ry == 241 or ry == 113):
                        rx = rx + (64*4) - (64*(diceroll-5))
                        ry = ry - 64
                        turn = 'red'
                    elif rx == 684 and diceroll <= 3 and (ry == 625 or ry == 497 or ry == 369 or ry == 241 or ry == 113): #8
                        rx = rx+(64*diceroll)
                    elif rx == 684 and diceroll >= 3 and diceroll != 6 and (ry == 625 or ry == 497 or ry == 369 or ry == 241 or ry == 113):
                        rx = rx + (64*3) - (64*(diceroll-4))
                        ry = ry - 64
                    elif rx == 684 and diceroll == 6 and (ry == 625 or ry == 497 or ry == 369 or ry == 241 or ry == 113):
                        rx = rx + (64*3) - (64*(diceroll-4))
                        ry = ry - 64
                        turn = 'red'
                    elif rx == 748 and diceroll <= 2 and (ry == 625 or ry == 497 or ry == 369 or ry == 241 or ry == 113): #9
                        rx = rx+(64*diceroll)
                    elif rx == 748 and diceroll >= 2 and diceroll != 6 and (ry == 625 or ry == 497 or ry == 369 or ry == 241 or ry == 113):
                        rx = rx + (64*2) - (64*(diceroll-3))
                        ry = ry - 64
                    elif rx == 748 and diceroll == 6 and (ry == 625 or ry == 497 or ry == 369 or ry == 241 or ry == 113):
                        rx = rx + (64*2) - (64*(diceroll-3))
                        ry = ry - 64
                        turn = 'red'
                    elif rx == 812 and diceroll == 1 and (ry == 625 or ry == 497 or ry == 369 or ry == 241 or ry == 113): #10
                        rx = rx+(64*diceroll)
                    elif rx == 812 and diceroll >= 1 and diceroll != 6 and (ry == 625 or ry == 497 or ry == 369 or ry == 241 or ry == 113):
                        rx = rx + (64*1) - (64*(diceroll-2))
                        ry = ry - 64
                    elif rx == 812 and diceroll == 6 and (ry == 625 or ry == 497 or ry == 369 or ry == 241 or ry == 113):
                        rx = rx + (64*1) - (64*(diceroll-2))
                        ry = ry - 64
                        turn = 'red'
                    elif rx >= 876 and diceroll != 6 and (ry == 625 or ry == 497 or ry == 369 or ry == 241 or ry == 113):
                        rx = rx - (64*(diceroll-1))
                        ry = ry - 64
                    elif rx == 876 and diceroll == 6 and (ry == 625 or ry == 497 or ry == 369 or ry == 241 or ry == 113):
                        rx = rx - (64*(diceroll-1))
                        ry = ry - 64

                    #row 2
                    elif rx > 556 and rx <= 876 and (ry == 561 or ry == 433 or ry == 305 or ry == 177 or ry == 49) and diceroll != 6:
                        rx = rx - (64*diceroll)
                    elif rx > 556 and rx <= 876 and (ry == 561 or ry == 433 or ry == 305 or ry == 177 or ry == 49) and diceroll == 6:
                        rx = rx - (64*diceroll)
                    elif rx > 620 and rx <= 876 and (ry == 561 or ry == 433 or ry == 305 or ry == 177 or ry == 49) and diceroll != 6:
                        rx = rx - (64*diceroll)
                    elif rx > 620 and rx <= 876 and (ry == 561 or ry == 433 or ry == 305 or ry == 177 or ry == 49) and diceroll == 6:
                        rx = rx - (64*diceroll)
                        turn = 'red'
                    elif rx == 620 and (ry == 561 or ry == 433 or ry == 305 or ry == 177 or ry == 49) and diceroll != 6:
                        rx = rx - (64*diceroll)
                    elif rx == 620 and (ry == 561 or ry == 433 or ry == 305 or ry == 177 or ry == 49) and diceroll == 6:
                        rx = rx - (64*5)
                        ry = ry - 64
                        turn = 'red'
                    elif rx == 556 and (ry == 561 or ry == 433 or ry == 305 or ry == 177 or ry == 49) and diceroll <= 5:
                        rx = rx - (64*diceroll)
                    elif rx == 556 and (ry == 561 or ry == 433 or ry == 305 or ry == 177 or ry == 49) and diceroll == 5:
                        rx = rx - (64*4) + (49*(diceroll-5))
                        ry = ry - 64 
                    elif rx == 556 and (ry == 561 or ry == 433 or ry == 305 or ry == 177 or ry == 49) and diceroll == 6:
                        rx = rx - (64*4) + (49*(diceroll-5))
                        ry = ry - 64 
                        turn = 'red'
                    elif rx == 492 and (ry == 561 or ry == 433 or ry == 305 or ry == 177 or ry == 49) and diceroll <= 4:
                        rx = rx - (64*diceroll)
                    elif rx == 492 and (ry == 561 or ry == 433 or ry == 305 or ry == 177 or ry == 49) and diceroll >= 4 and diceroll != 6:
                        rx = rx - (64*3) + (64*(diceroll-4))
                        ry = ry - 64
                    elif rx == 492 and (ry == 561 or ry == 433 or ry == 305 or ry == 177 or ry == 49) and diceroll == 6:
                        rx = rx - (64*3) + (64*(diceroll-4))
                        ry = ry - 64
                        turn = 'red'
                    elif rx == 428 and (ry == 561 or ry == 433 or ry == 305 or ry == 177 or ry == 49) and diceroll < 3:
                        rx = rx - (64*diceroll)
                    elif rx == 428 and (ry == 561 or ry == 433 or ry == 305 or ry == 177 or ry == 49) and diceroll >= 3 and diceroll != 6:
                        rx = rx - (64*2) + (64*(diceroll-3))
                        ry = ry - 64
                    elif rx == 428 and (ry == 561 or ry == 433 or ry == 305 or ry == 177 or ry == 49) and diceroll == 6:
                        rx = rx - (64*2) + (64*(diceroll-3))
                        ry = ry - 64
                        turn = 'red'
                    elif rx == 364 and (ry == 561 or ry == 433 or ry == 305 or ry == 177 or ry == 49) and diceroll < 2:
                        rx = rx - (64*diceroll)
                    elif rx == 364 and (ry == 561 or ry == 433 or ry == 305 or ry == 177 or ry == 49) and diceroll >= 2 and diceroll != 6:
                        rx = rx - 64 + (64*(diceroll-2))
                        ry = ry - 64
                    elif rx == 364 and (ry == 561 or ry == 433 or ry == 305 or ry == 177 or ry == 49) and diceroll == 6:
                        rx = rx - 64 + (64*(diceroll-2))
                        ry = ry - 64
                        turn = 'red'
                    elif rx == 300 and (ry == 561 or ry == 433 or ry == 305 or ry == 177 or ry == 49) and diceroll != 6:
                        rx = rx + (64*(diceroll-1))
                        ry = ry - 64
                    elif rx == 300 and (ry == 561 or ry == 433 or ry == 305 or ry == 177 or ry == 49) and diceroll == 6:
                        rx = rx + (64*(diceroll-1))
                        ry = ry - 64
                        turn = 'red'
                    
                    #for final row
                    elif ry == 49 and (rx == 812 or rx == 876) and diceroll != 6:
                        rx = rx - (64*diceroll)
                        turn = 'red'
                    elif ry == 49 and (rx == 812 or rx == 876) and diceroll == 6:
                        rx = rx - (64*diceroll)
                        turn = 'red'
                    elif ry == 49 and rx == 684 and diceroll <5:
                        rx = rx - (64*diceroll)
                    elif ry == 49 and rx == 684 and diceroll == 5:
                        rx = rx - (64*diceroll)
                    # elif ry == 49 and rx == 

                    

                #for Player 2
                    #row 1
                elif pickNumber() and turn == 'blue':
                    turn='red'
                    if diceroll in range (1, 6) and blx == 225 and bly == 625:
                        blx = 300
                        bly = 625
                        turn = 'blue'
                    elif blx in range (300, 625) and diceroll != 6 and (bly == 625 or bly == 497 or bly == 369 or bly == 241 or bly == 113):
                        blx = blx + (64*diceroll)
                    elif blx in range (300, 625) and diceroll == 6 and (bly == 625 or bly == 497 or bly == 369 or bly == 241 or bly == 113):
                        blx = blx + (64*diceroll)
                        turn = 'red'
                    elif blx == 300 and diceroll != 6 and (bly == 625 or bly == 497 or bly == 369 or bly == 241 or bly == 113):
                        blx = blx + (64*diceroll)
                    elif blx == 300 and diceroll == 6 and (bly == 625 or bly == 497 or bly == 369 or bly == 241 or bly == 113):
                        blx = blx + (64*diceroll)
                        bly = bly - 64
                        turn = 'red'
                    elif blx == 620 and diceroll <= 4 and (bly == 625 or bly == 497 or bly == 369 or bly == 241 or bly == 113): #7
                        blx = blx + (64*diceroll)
                    elif blx == 620 and diceroll >= 4 and diceroll != 6 and (bly == 625 or bly == 497 or bly == 369 or bly == 241 or bly == 113):
                        blx = blx + (64*diceroll)
                        bly = bly - 64
                    elif blx == 620 and diceroll == 6 and (bly == 625 or bly == 497 or bly == 369 or bly == 241 or bly == 113):
                        blx = blx + (64*4) - (64*(diceroll-5))
                        bly = bly - 64
                        turn = 'red'
                    elif blx == 684 and diceroll <= 3 and (bly == 625 or bly == 497 or bly == 369 or bly == 241 or bly == 113): #8
                        blx = blx+(64*diceroll)
                    elif blx == 684 and diceroll >= 3 and diceroll != 6 and (bly == 625 or bly == 497 or bly == 369 or bly == 241 or bly == 113):
                        blx = blx + (64*3) - (64*(diceroll-4))
                        bly = bly - 64
                    elif blx == 684 and diceroll == 6 and (bly == 625 or bly == 497 or bly == 369 or bly == 241 or bly == 113):
                        blx = blx + (64*3) - (64*(diceroll-4))
                        bly = bly - 64
                        turn = 'red'
                    elif blx == 748 and diceroll <= 2 and (bly == 625 or bly == 497 or bly == 369 or bly == 241 or bly == 113): #9
                        blx = blx+(64*diceroll)
                    elif blx == 748 and diceroll >= 2 and diceroll != 6 and (bly == 625 or bly == 497 or bly == 369 or bly == 241 or bly == 113):
                        blx = blx + (64*2) - (64*(diceroll-3))
                        bly = bly - 64
                    elif blx == 748 and diceroll == 6 and (bly == 625 or bly == 497 or bly == 369 or bly == 241 or bly == 113):
                        blx = blx + (64*2) - (64*(diceroll-3))
                        bly = bly - 64
                        turn = 'red'
                    elif blx == 812 and diceroll == 1 and (bly == 625 or bly == 497 or bly == 369 or bly == 241 or bly == 113): #10
                        blx = blx+(64*diceroll)
                    elif blx == 812 and diceroll >= 1 and diceroll != 6 and (bly == 625 or bly == 497 or bly == 369 or bly == 241 or bly == 113):
                        blx = blx + (64*1) - (64*(diceroll-2))
                        bly = bly - 64
                    elif blx == 812 and diceroll == 6 and (bly == 625 or bly == 497 or bly == 369 or bly == 241 or bly == 113):
                        blx = blx + (64*1) - (64*(diceroll-2))
                        bly = bly - 64
                        turn = 'red'
                    elif blx >= 876 and diceroll != 6 and (bly == 625 or bly == 497 or bly == 369 or bly == 241 or bly == 113):
                        blx = blx - (64*(diceroll-1))
                        bly = bly - 64
                    elif blx == 876 and diceroll == 6 and (bly == 625 or bly == 497 or bly == 369 or bly == 241 or bly == 113):
                        blx = blx - (64*(diceroll-1))
                        bly = bly - 64

                    #row 2
                    elif blx > 556 and blx <= 876 and (bly == 561 or bly == 433 or bly == 305 or bly == 177 or bly == 49) and diceroll != 6:
                        blx = blx - (64*diceroll)
                    elif blx > 556 and blx <= 876 and (bly == 561 or bly == 433 or bly == 305 or bly == 177 or bly == 49) and diceroll == 6:
                        blx = blx - (64*diceroll)
                    elif blx > 620 and blx <= 876 and (bly == 561 or bly == 433 or bly == 305 or bly == 177 or bly == 49) and diceroll != 6:
                        blx = blx - (64*diceroll)
                    elif blx > 620 and blx <= 876 and (bly == 561 or bly == 433 or bly == 305 or bly == 177 or bly == 49) and diceroll == 6:
                        blx = blx - (64*diceroll)
                        turn = 'red'
                    elif blx == 620 and (bly == 561 or bly == 433 or bly == 305 or bly == 177 or bly == 49) and diceroll != 6:
                        blx = blx - (64*diceroll)
                    elif blx == 620 and (bly == 561 or bly == 433 or bly == 305 or bly == 177 or bly == 49) and diceroll == 6:
                        blx = blx - (64*5)
                        bly = bly - 64
                        turn = 'red'
                    elif blx == 556 and (bly == 561 or bly == 433 or bly == 305 or bly == 177 or bly == 49) and diceroll <= 5:
                        blx = blx - (64*diceroll)
                    elif blx == 556 and (bly == 561 or bly == 433 or bly == 305 or bly == 177 or bly == 49) and diceroll == 5:
                        blx = blx - (64*4) + (49*(diceroll-5))
                        bly = bly - 64 
                    elif blx == 556 and (bly == 561 or bly == 433 or bly == 305 or bly == 177 or bly == 49) and diceroll == 6:
                        blx = blx - (64*4) + (49*(diceroll-5))
                        bly = bly - 64 
                        turn = 'red'
                    elif blx == 492 and (bly == 561 or bly == 433 or bly == 305 or bly == 177 or bly == 49) and diceroll <= 4:
                        blx = blx - (64*diceroll)
                    elif blx == 492 and (bly == 561 or bly == 433 or bly == 305 or bly == 177 or bly == 49) and diceroll >= 4 and diceroll != 6:
                        blx = blx - (64*3) + (64*(diceroll-4))
                        bly = bly - 64
                    elif blx == 492 and (bly == 561 or bly == 433 or bly == 305 or bly == 177 or bly == 49) and diceroll == 6:
                        blx = blx - (64*3) + (64*(diceroll-4))
                        bly = bly - 64
                        turn = 'red'
                    elif blx == 428 and (bly == 561 or bly == 433 or bly == 305 or bly == 177 or bly == 49) and diceroll < 3:
                        blx = blx - (64*diceroll)
                    elif blx == 428 and (bly == 561 or bly == 433 or bly == 305 or bly == 177 or bly == 49) and diceroll >= 3 and diceroll != 6:
                        blx = blx - (64*2) + (64*(diceroll-3))
                        bly = bly - 64
                    elif blx == 428 and (bly == 561 or bly == 433 or bly == 305 or bly == 177 or bly == 49) and diceroll == 6:
                        blx = blx - (64*2) + (64*(diceroll-3))
                        bly = bly - 64
                        turn = 'red'
                    elif blx == 364 and (bly == 561 or bly == 433 or bly == 305 or bly == 177 or bly == 49) and diceroll < 2:
                        blx = blx - (64*diceroll)
                    elif blx == 364 and (bly == 561 or bly == 433 or bly == 305 or bly == 177 or bly == 49) and diceroll >= 2 and diceroll != 6:
                        blx = blx - 64 + (64*(diceroll-2))
                        bly = bly - 64
                    elif blx == 364 and (bly == 561 or bly == 433 or bly == 305 or bly == 177 or bly == 49) and diceroll == 6:
                        blx = blx - 64 + (64*(diceroll-2))
                        bly = bly - 64
                        turn = 'red'
                    elif blx == 300 and (bly == 561 or bly == 433 or bly == 305 or bly == 177 or bly == 49) and diceroll != 6:
                        blx = blx + (64*(diceroll-1))
                        bly = bly - 64
                    elif blx == 300 and (bly == 561 or bly == 433 or bly == 305 or bly == 177 or bly == 49) and diceroll == 6:
                        blx = blx + (64*(diceroll-1))
                        bly = bly - 64
                        turn = 'red'
        pygame.display.update()
        time.sleep(0.6)
    
pygame.quit()