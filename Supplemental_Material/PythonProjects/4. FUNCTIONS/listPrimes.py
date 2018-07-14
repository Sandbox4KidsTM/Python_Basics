
def checkPrime(checkInt):
    j = 2
    numFactors = 0
    while j <= checkInt:
        if ((checkInt%j) != 0):
            numFactors = numFactors + 1
        j = j + 1
    return(numFactors)

n = int(input("what's the upper limit?"))
i = 2
while i <= n:
    if checkPrime(i) != 0:
        print(checkPrime(i))
    i = i+1


#ask user to type upper limit (n)
# then for values 2 to n, check if the value is prime: se checkPrime()
# print all prime numbers between 2 and n