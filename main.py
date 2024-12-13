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

start1 = [225, 560]
start2 = [225, 625]

tiles1 = [300, 625]
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
                    if diceroll == 6 and rx == 225 and ry == 560:
                        rx = 300
                        ry = 625
                        turn = 'red'
                    elif rx in range (300, 625) and diceroll != 6 and bly == 625:
                        rx = rx + (64*diceroll)
                    elif rx in range (300, 625) and diceroll == 6 and bly == 625:
                        rx = rx + (64*diceroll)
                        turn = 'red'
                    elif rx == 625 and diceroll != 6 and ry == 560:
                        rx = rx + (64*diceroll)
                    elif rx == 625 and diceroll == 6 and ry == 560:
                        rx = rx + (64*diceroll)
                        ry = ry - 64
                        turn = 'red'
                    elif rx == 689 and diceroll <= 4 and ry == 560: #7
                        rx = rx + (64*diceroll)
                    elif rx == 689 and diceroll >= 4 and diceroll != 6 and ry == 560:
                        rx = rx + (64*diceroll)
                        ry = ry - 64
                    elif rx == 689 and diceroll == 6 and ry == 560:
                        rx = rx + (64*4) - (64*(diceroll-5))
                        ry = ry - 64
                        turn = 'red'
                    elif rx == 753 and diceroll <= 3 and ry == 560: #8
                        rx = rx+(64*diceroll)
                    elif rx == 753 and diceroll >= 3 and diceroll != 6 and ry == 560:
                        rx = rx + (64*3) - (64*(diceroll-4))
                        ry = ry - 64
                    elif rx == 753 and diceroll == 6 and ry == 560:
                        rx = rx + (64*3) - (64*(diceroll-4))
                        ry = ry - 64
                        turn = 'red'
                    elif rx == 817 and diceroll <= 2 and ry == 560: #9
                        rx = rx+(64*diceroll)
                    elif rx == 817 and diceroll >= 2 and diceroll != 6 and ry == 560:
                        rx = rx + (64*2) - (64*(diceroll-3))
                        ry = ry - 64
                    elif rx == 817 and diceroll == 6 and ry == 560:
                        rx = rx + (64*2) - (64*(diceroll-3))
                        ry = ry - 64
                        turn = 'red'
                    elif rx == 881 and diceroll == 1 and ry == 560: #10
                        rx = rx+(64*diceroll)
                    elif rx == 881 and diceroll >= 1 and diceroll != 6 and ry == 560:
                        rx = rx + (64*1) - (64*(diceroll-2))
                        ry = ry - 64
                    elif rx == 881 and diceroll == 6 and ry == 560:
                        rx = rx + (64*1) - (64*(diceroll-2))
                        ry = ry - 64
                        turn = 'red'
                    elif rx >= 945 and diceroll != 6 and ry == 560:
                        rx = rx - (64*(diceroll-1))
                        ry = ry - 64
                    elif rx == 945 and diceroll == 6 and ry == 560:
                        rx = rx - (64*(diceroll-1))
                        ry = ry - 64


                #for Player 2
                    #row 1
                elif pickNumber() and turn == 'blue':
                    turn='red'
                    if diceroll == 6 and blx == 225 and bly == 625:
                        blx = 300
                        bly = 625
                        turn = 'blue'
                    elif blx in range (300, 625) and diceroll != 6 and bly == 625:
                        blx = blx+(64*diceroll)
                    elif blx in range (300, 625) and diceroll == 6 and bly == 625:
                        blx = blx+(64*diceroll)
                        turn = 'blue'
        pygame.display.update()
        time.sleep(0.4)
    
pygame.quit()