#user supplies list; computer checks for duplicate items

#1 ask user for list
numList = []

print("to stop entering more numbers, press '0' ")
entry = int(input("enter a natural number"))
while entry != 0:
    entry = int(input("enter another natural number or enter '0' to stop"))
    if numList.count(entry) == 1:
        print("that item is already in the list; type of")
    else:
        numList.append(entry)
print(numList)