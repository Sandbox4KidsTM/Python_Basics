import random
import time

#each insult should have one adjective and one noun
list_one = ["sniggering", "limping", "gibbering"] #adjective
list_two = ["manakin", "snotbinder", "blizzard-fish", "mugawump"] #noun


while True:
    magicWord = input("What's the magic word?")
    if magicWord == 'sorry':
        break
     print(list_two[random.randint(0,3)] + " " + list_two[random.randrange(0,3)])
