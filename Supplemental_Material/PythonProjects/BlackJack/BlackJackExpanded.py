# code for BlackJack Game
#version1: single player against dealer, 1 deck of cards, A is always 1, full deck at the beginning of each round

# how to play BlackJack : https://www.youtube.com/watch?v=VB-6MvXvsKo

import random

#data
#deck >> List or Dictionary
deck = ['CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK',
        'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK',
        'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK',
        'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK']
dictVal = {'CA':1, 'C2':2, 'C3':3, 'C4':4, 'C5':5, 'C6':6, 'C7':7, 'C8':8, 'C9':9, 'C10':10, 'CJ':10, 'CQ':10, 'CK':10,
           'SA':1, 'S2':2, 'S3':3, 'S4':4, 'S5':5, 'S6':6, 'S7':7, 'S8':8, 'S9':9, 'S10':10, 'SJ':10, 'SQ':10, 'SK':10,
           'DA':1, 'D2':2, 'D3':3, 'D4':4, 'D5':5, 'D6':6, 'D7':7, 'D8':8, 'D9':9, 'D10':10, 'DJ':10, 'DQ':10, 'DK':10,
           'HA':1, 'H2':2, 'H3':3, 'H4':4, 'H5':5, 'H6':6, 'H7':7, 'H8':8, 'H9':9, 'H10':10, 'HJ':10, 'HQ':10, 'HK':10} 
dealerCount = 0
playerCount = 0

#functions
# draw()

def draw():
    #this randomly draws a card from the deck'
    drawItem = deck[random.randint(0, len(deck)-1)]
    deck.remove(drawItem)
    return(drawItem)

def firstRound(dC = 0, pC = 0):
    #firstRound() is for dealer to distribute cards 2 cards to player and 2 to self
    drawnCard = draw()
    p1 = draw() #first card given to player
    pC = pC + dictVal[drawnCard]
    drawnCard = draw()
    d1 = draw()
    dC = dC + dictVal[drawnCard]
    drawnCard = draw()
    p2 = draw() #second card given to player
    pC = pC + dictVal[drawnCard]
    drawnCard = draw()
    d2 = draw()
    dC = dC + dictVal[drawnCard]
    return dC, pC, p1, d1, p2, d2
    
# result()
# trackTurns()
# countPlayer()
# countDealer()
# resetList() >> List/Dictionary gets continually adjusted as you remove cards

print('welcome to BlackJack')
turn = 1    #0 for dealer and 1 for player
dealerCount = 0
playerCount = 0
print("dealer count is", dealerCount)
print("player count is", playerCount)

dealerCount, playerCount, p1, d1, p2, d2 = firstRound(dealerCount, playerCount)
print("player's first card is", p1)
print("player's second card is", p2)
print("playerCount after firstRound is", playerCount)

print("dealer's first card is", d1)
print("dealer's second card is", d2)
print("dealerCount after firstRound is", dealerCount) #later on hide the second card
if playerCount == 21:
    print("player WINS BLACKJACK. Game Over.")
if dealerCount == 21:
    print("dealer WINS BLACKJACK. Game Over.")

turn = 1 #player's turn
while (turn == 1) and ((playerCount != 21) or (dealerCount != 21)):
    playerChoice = input("do you want to Hit or Stand?")
    if playerChoice in ["hit", "Hit", "H", "h"]:
        drawnCard = draw()
        print("drawn card is", drawnCard)
        if playerCount < 11 and drawnCard in ['CA', 'SA', 'HA', 'DA']:
            playerCount = playerCount + dictVal[drawnCard] + 10
        else:
            playerCount = playerCount + dictVal[drawnCard]
        print("playerCount after a Hit is", playerCount)
        if playerCount == 21:
            print("player WINS")
            break
        if playerCount > 21:
            print("player is bust")
            break
        turn = 1
    if playerChoice in ["stand", "Stand", 's', "S"]:
        turn = 0 #dealer's turn 
        #dealer is forced to hit, if the dealer's first 2 cards total 16 or less
        while dealerCount <= 16:
            print("dealer to serve a card")
            drawnCard = draw()
            print("drawn card is", drawnCard)
            
            if dealerCount < 12 and drawnCard in ['CA', 'SA', 'HA', 'DA']:
                dealerCount = dealerCount + dictVal[drawnCard] + 10
            else:
                dealerCount = dealerCount + dictVal[drawnCard]
                
            print("dealerCount after a Hit is", dealerCount)
            if dealerCount == 21:
                print("dealer WINS")
                break
            if dealerCount > 21:
                print("dealer is bust")
                break
    
print("end of player's turns and dealer's turns")
if (playerCount > dealerCount) and (playerCount < 22):
    print("player WINS")
elif (playerCount == dealerCount) and (playerCount < 22):
    print("PUSH i.e. player and dealer are equal")
elif (playerCount < dealerCount) and (dealerCount >= 22):
    print("player WINS")
else:
    print("dealer WINS")