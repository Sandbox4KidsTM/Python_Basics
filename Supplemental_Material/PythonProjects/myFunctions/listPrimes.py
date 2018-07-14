n = int(input("enter the upper limit"))

j = 2
while j < n:
    if isItPrime(j) == True:
        print(j)
    else:
        pass
    j = j + 1