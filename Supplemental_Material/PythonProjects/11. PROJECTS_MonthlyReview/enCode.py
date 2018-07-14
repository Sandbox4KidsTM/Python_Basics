# user enters the word to encrypt

# computer parses thru each letter in the word, and changes 'a' to '@'

oldWord = input("what's the word you want to encode?")
newWord = ''


j = 0 #a local variable to parse thru the loop
while j < len(oldWord):
    if (oldWord[j] == 'a'):
        newWord = newWord + '@'
    elif (oldWord[j] == 'e'):
        newWord = newWord + '3'
    elif (oldWord[j] == 'i'):
        newWord = newWord + '!'
    elif (oldWord[j] == 'o'):
        newWord = newWord + '0'
    elif (oldWord[j] == 'u'):
        newWord = newWord + 'U'
    else:
        newWord = newWord + oldWord[j]
    j = j + 1
        
# print the new word
print(newWord)