n = int(input("enter the level number: "))

list1 = [1]
list2 = [1, 1]

if n == 0:
    print(list1) #(a+b)^0 = 1
if n == 1:
    print(list2) #(a+b)^1 = 2

if n > 1:
    clevel = 2 #current level in the Pascal's Tree
    print(list1)
    print(list2)
    while  clevel <= n:
        list1 = list(list2) #convert to a list
        l2 = len(list2)
        list2[0] = 1
        i = 1
        while i < l2:
            list2[i] = list1[(i-1)] + list1[i]
            i = i + 1
        list2.append(1) #append 1 at the end of the list
        print(list2)
        clevel += 1