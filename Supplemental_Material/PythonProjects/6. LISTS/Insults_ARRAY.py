#random insult generator using Arrays of Strings

import random

column1 = ["artless", "bawdy"]
column2 = ["base-court", "bat-folwing", "chocolate-fudge"]
column3 = ["apple-john", "baggage", "banana", "pineapple"]

#list_one = ["sniggering", "limping", "gibbering", "ham-fisted", "boasting", "gib-faced", "snooty", "snooty", "bouncing", "creeping"]
#list_two = ["manakin", "snotbinder", "blizzard-fish", "mugawump", "blunder-bus", "stingbum", "thunderpuss", "barryphant", "bar-fly", "shabbaroon" ]

print("Thou " + column1[random.randint(0,1)] + " " + column2[random.randint(0,2)] + " " + column3[random.randint(0,3)]), 