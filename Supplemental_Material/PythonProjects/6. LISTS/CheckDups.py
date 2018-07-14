# ask user to supply values for a list

#list1 = [10, 20, 12, 10, 12, 12, 12]
#print(len(list1))
#print(list1.count(12))

# check if an item is a duplicate

list2 = []
userInput = input("enter an integer to continue, and 'x' to stop")

while userInput != 'x':
    val = int(userInput)
    list2.append(val) #adds val to the end of the list
    if list2.count(val) > 1: #checking the number of occurences of val
        print("you entered a duplicate, so I am removing it")
        list2.pop() #removes an item from the end of list
    userInput = input("enter an integer to continue, and 'x' to stop")

print("end of list")
