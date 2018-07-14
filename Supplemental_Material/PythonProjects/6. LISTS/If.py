

myName = input("what's your name?")
if 'ick' in myName:
    myIndex = myName.find('ick') #gets the index of the substring
    print(myIndex)
    subS = myName[0 : myIndex] #gets the substring
    print(subS)
    print(subS+'Prick')