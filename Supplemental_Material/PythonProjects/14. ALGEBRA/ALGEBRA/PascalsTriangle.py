# Pascal's Triangle

n = int(input("enter the level number: "))
print(n)

list1 = [1]
list2 = [1, 1]

i = 0
while i < n:
    j = 0
    while j <= i:
        list2.append(j)
        j = j + 1   
    list1.append(list2)
    i = i + 1
    
print(list1)