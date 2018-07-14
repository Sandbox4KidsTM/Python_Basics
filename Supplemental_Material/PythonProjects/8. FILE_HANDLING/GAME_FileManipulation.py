#Snakes & Ladders Game using File Manipulation

#Snakes & Ladders: using a Text File
#Roll the dice i.e. random values from 1 to 6
#Move the Pointer
#If the current Position is a Vowel, jump 5 steps forward.
#If the current Position is a Consonant, jump 5 steps backward.
#You win if you reach the end of the file in x moves.

fileVar = open("C:\\Sandbox Files\\Programming\\Python3\\PythonProjects\\8. FILE_HANDLING\\Snakes.txt", 'w+')
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
for item in list1:
    fileVar.write(item)

fileVar.seek(2, 0) #number of values to skip, and the position info
print(fileVar.tell())
fileCont = fileVar.read(3) #values to read
print(fileCont)

