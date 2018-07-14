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

numPlayers = int(input("enter number of players: "))

def draw():
    #this randomly draws a card from the deck'
    drawItem = deck[random.randint(0, len(deck)-1)]
    deck.remove(drawItem)
    return(drawItem)

def firstRound(): #disrtibute 2 cards to a player
    px = []
    pC = 0
    for y in range(0, 2):
            p1 = draw() #first card given to player
            px.append(p1)
            pC = pC + dictVal[p1]
    return px, pC

for x in range(0, numPlayers):
    print(firstRound())
    
    #store players hands using a dictionary
    #players = {p1: ['C2', 'D3, 'HA'], 