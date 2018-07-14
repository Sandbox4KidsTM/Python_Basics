import random #import library to generate random numbers
import time #import library to wait before action

list_one = ["sniggering", "limping", "gibbering", "ham-fisted", "boasting", "gib-faced", "snooty", "snooty", "bouncing", "creeping"]
list_two = ["manakin", "snotbinder", "blizzard-fish", "mugawump", "blunder-bus", "stingbum", "thunderpuss", "barryphant", "bar-fly", "shabbaroon" ]

#list_one is for adjectives
#list_two is for nouns
#insults typically take the form: adjective + noun

insult_one = random.randrange(0, 9)
insult_two = random.randrange(0, 10)

print("Hello, welcome to the B.I.G, (Boris Insult Generator)")
time.sleep(1)
print("")
your_name = input("What is your name? ")
print("")
time.sleep(0.5)
print("Boris is thinking of an insult....")
print("")
time.sleep(2)
print(your_name)
print("")
time.sleep(0.7)
print("Boris says that you are a", list_one[insult_one], list_two[insult_two])

time.sleep(10)
