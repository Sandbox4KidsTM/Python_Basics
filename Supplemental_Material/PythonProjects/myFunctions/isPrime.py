#check if a number is prime

def isItPrime(x):
    isPrime = True
    i = 2
    while i < x:
        if (x % i == 0):
            #print("num is NOT a prime")
            isPrime = False
            break
        else:
            i = i + 1
    return isPrime
