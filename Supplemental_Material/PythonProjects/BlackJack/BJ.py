import random

deck = ['CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK',
        'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK',
        'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK',
        'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK']
dictVal = {'CA':11, 'C2':2, 'C3':3, 'C4':4, 'C5':5, 'C6':6, 'C7':7, 'C8':8, 'C9':9, 'C10':10, 'CJ':10, 'CQ':10, 'CK':10,
           'SA':11, 'S2':2, 'S3':3, 'S4':4, 'S5':5, 'S6':6, 'S7':7, 'S8':8, 'S9':9, 'S10':10, 'SJ':10, 'SQ':10, 'SK':10,
           'DA':11, 'D2':2, 'D3':3, 'D4':4, 'D5':5, 'D6':6, 'D7':7, 'D8':8, 'D9':9, 'D10':10, 'DJ':10, 'DQ':10, 'DK':10,
           'HA':11, 'H2':2, 'H3':3, 'H4':4, 'H5':5, 'H6':6, 'H7':7, 'H8':8, 'H9':9, 'H10':10, 'HJ':10, 'HQ':10, 'HK':10} 

def draw():
    #this randomly draws a card from the deck'
    drawItem = deck[random.randint(0, len(deck)-1)]
    deck.remove(drawItem)
    return(drawItem)

def firstRound():
    pc1 = draw()
    pv1 = dictVal[pc1]
    dc1 = draw()
    dv1 = dictVal[dc1]
    pc2 = draw()
    pv2 = dictVal[pc2]
    dc2 = draw()
    dv2 = dictVal[dc2]
    return pc1, pv1, dc1, dv1, pc2, pv2, dc2, dv2


#main program    
dealerCount = 0
playerCount = 0

pc1, pv1, dc1, dv1, pc2, pv2, dc2, dv2 = firstRound()
print("player's cards are", pc1, " ", pc2)
print("player's total is", pv1+pv2)
print("dealer's cards are", dc1, " ", dc2)
print("dealer's total is ", dv1+dv2)

dealerCount = dv1+dv2
if dealerCount == 22:
    dealerCount = 12
playerCount = pv1+pv2
if playerCount == 22:
    playerCount = 12

if playerCount == 21:
    print("player has BlackJack. GAME OVER!")
    
if dealerCount == 21:
    print("dealer has BlackJack. GAME OVER!")

#asking player to Hit or Stand    
while (playerCount < 22) and (playerCount != 21):
    playerChoice = input("Hit or Stand?")
    if playerChoice in ["Hit", "H", "hit", "h"]:
        card = draw()
        print("player's new card is", card)
        print("player's new card value is", dictVal[card])
        playerCount = playerCount + dictVal[card]
        print("player's new total is", playerCount)
        if playerCount == 21:
            print("player has BlackJack. GAME OVER!")
            break
        if playerCount > 21:
            print("player is BUST. GAME OVER!")
            break
    else:
        break

#dealer automatically Hits if dealerCount < 17
while (dealerCount < 17):
        card = draw()
        print("dealer's new card is", card)
        print("dealer's new card value is", dictVal[card])
        dealerCount = dealerCount + dictVal[card]
        print("dealer's new total is", dealerCount)
        if dealerCount == 21:
            print("dealer has BlackJack. GAME OVER!")
            break
        if dealerCount > 21:
            print("dealer is BUST. GAME OVER!")
            break

if (playerCount < 22) and (playerCount > dealerCount):
    print("player wins!!!!!!!!")
elif (playerCount < 22) and (playerCount == dealerCount):
    print("it is a DRAWWWWW")
else:
    print("dealer wins.....")
    


    
    
    