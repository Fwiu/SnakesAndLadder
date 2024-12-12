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

tiles1 = [300, 625]
TILES = {
    1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
}

POS_TILE = []
# POS_TILE[] = {1, 2}

SNAKES = {
        27: 8,
        34: 7,
        29: 3,
        69: 31,
        72: 36,
        77: 46,
        80: 41,
        96: 48,
        98: 79,
    }

LADDERS = {
    4: 16,
    6: 25,
    12: 49,
    20: 40,
    38: 88,
    58: 62,
    71: 93,
    78: 84,
    86: 95,
    }


LAST_TILES = 100



# rx = 225
# ry = 560


# blx = 225
# bly = 625

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

    def font_player():
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

    def move_player(self, player_i):
        prev_pos = self.players[player_i]
        new_pos = prev_pos + self.pickNumber()

        if new_pos >= self.LAST_TILES:
            self.winner = player_i
            new_pos = self.LAST_TILES
        elif new_pos in self.SNAKES:
            new_pos = self.SNAKES[new_pos]
        elif new_pos in self.LADDERS:
            new_pos = self.LADDERS[new_pos]
        
        self.players[player_i] = new_pos

    #move player
    def move_players(self):
        for player_i in range(self.n_players):
            self.move_player(player_i)
            if self.winner is not None: # done with game
                break

    def play_game(self):
        while self.winner is None:
            self.turn += 1
            self.move_players()
        return f"Player #{self.winner+1} Wins!"

    run = True

    font_turn = 'blue'

    while run:

        back()
        rplayer(start1[0], start1[1])
        bplayer(start2[0], start2[1])
        font_player()

        if font_turn == 'blue':
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


                

                if pickNumber() and font_turn == 'blue':
                        font_turn = 'red'
                elif pickNumber() and font_turn == 'red':
                        font_turn = 'blue'

                

                # #for Player 1
                # if pickNumber() and turn == 'red':
                #     turn='blue'
                #     if diceroll == 6 and start1 == True:
                #         tiles1
                #         turn = 'red'
                # #for Player 2
                # elif pickNumber() and turn == 'blue':
                #     turn='red'
                #     if diceroll == 6 and start2 == True:
                #         blx = 300
                #         bly = 625
                #         turn = 'blue'
        
        pygame.display.update()
        time.sleep(0.4)
    
pygame.quit()