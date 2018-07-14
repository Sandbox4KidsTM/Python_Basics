'''
Sam attackes Paul and deals a 9 damage
Paul is down to 10 health
Sam/Paul wins if the opponent has negative health
Each warrior has sword and sheild
Attacks are randomized
'''

# Warrior & Battle Class

# Warrior Attributes: names, health, and attack and block maximums
# Warrior Capabilities: attack and block random amounts

# Attack random() * max Attack + 0.5
# Block random() * max Block + 0.5
# random() gives a value between 0.0 and 1.0

#Battle Class loops until 1 warrior dies
#Warriors will each get a turn to attack each other

# Function gets 2 warriors
# First warrior attacks the Second warrior

import random
import math

class Warrior:
    
    def __init__(self, name="Warrior", health=0, attackMax, blockMax):
        self.name = name
        self.health = health
        self.attackMax = attackMax
        self.blockMax = blockMax

    def attack(self):
        attackAmt = self.attackMax = self.attackMax * (random.random() + 0.5)
        return attackAmt
    
    def block(self):
        blockAmt = self.blockMax = self.blockMax * (random.random() + 0.5)
        return blockAmt
    
class Battle:
    
    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                #player1 wins
                print("Game is OVER")
                break
            
            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                #player2 wins
                print("Game is OVER")
                break
    