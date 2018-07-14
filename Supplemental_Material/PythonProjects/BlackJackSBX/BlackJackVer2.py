import random

#create a deck of cards

#C is for Clubs suit
deck = ['CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 
        'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK']

deckVal = { 'CA':1, 'C2':2, 'C3':3, 'C4':4, 'C5':5, 'C6':6, 'C7':7, 
        'C8':8, 'C9':9, 'C10':10, 'CJ':10, 'CQ':10, 'CK':10}

#draw a card and remove it from the deck
def draw():
    drawnCard = deck[random.randint(0, len(deck)-1)]
    deck.remove(drawnCard)
    return drawnCard, deckVal[drawnCard]

def dealFirstRound():
    pc = 0
    dc = 0
    p1c, p1v = draw()
    pc = pc + p1v
    
    d1c, d1v = draw()
    dc = dc + d1v
    
    p2c, p2v = draw()
    pc = pc + p2v
    
    d2c, d2v = draw()
    dc = dc + d2v
    
    return p1c, p1v, d1c, d1v, p2c, p2v, d2c, d2v, pc, dc

print(dealFirstRound())