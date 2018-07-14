# code for BlackJack Game
#version1: single player against dealer, 1 deck of cards, A is always 1, full deck at the beginning of each round

import random

#data
#deck >> List or Dictionary
deck = ['CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK']
dictVal = { 'CA':1, 'C2':2, 'C3':3, 'C4':4, 'C5':5, 'C6':6, 'C7':7, 'C8':8, 'C9':9, 'C10':10, 'CJ':10, 'CQ':10, 'CK':10} 
dealerCount = 0
playerCount = 0

#functions
# draw()

def draw():
    #this randomly draws a card from the deck'
    drawItem = deck[random.randint(0, len(deck)-1)]
    deck.remove(drawItem)
    return(drawItem)

# result()
# trackTurns()
# countPlayer()
# countDealer()
# resetList() >> List/Dictionary gets continually adjusted as you remove cards

print('welcome to BlackJack')
print(dealerCount)
print(playerCount)

while (dealerCount < 21 and playerCount < 21):
    turn = 0 #o for dealer and 1 for player
    if turn == 0:
        drawnCard = draw()
        print("card drawn is: ", drawnCard)
        dealerCount = dealerCount + dictVal[drawnCard] 
        print(dealerCount)
        if dealerCount == 21:
            print("dealer WINS")
            break
        if dealerCount > 21:
            print("dealer bust")
            break

    turn = 1 #o for dealer and 1 for player
    if turn == 1:
        drawnCard = draw()
        print("card drawn is: ", drawnCard)
        playerCount = playerCount + dictVal[drawnCard] 
        print(playerCount)
        if playerCount == 21:
            print("player WINS")
            break
        if playerCount > 21:
            print("player bust")
            break
