# user enters the word
myWord = input("what's the word you want to check #vowels for?")

# calculate the vowels by looping through each character in the word
print(len(myWord))
print("")

#print each letter in the word
i = 0
while i < len(myWord):
    print(myWord[i])
    i = i + 1

print('')
count = 0 #number of vowels
j = 0 #a local variable to parse thru the loop
while j < len(myWord):
    if (((((myWord[j] == 'a') or (myWord[j] == 'e')) or (myWord[j] == 'i')) or (myWord[j] == 'o')) or (myWord[j] == 'u')):
        count = count + 1
    j = j + 1
        
# print the word
print(count)