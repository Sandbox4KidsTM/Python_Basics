#n! = n * (n-1)!

def fac(gogo):
    if gogo < 1:
        return 1
    else:
        return gogo*fac(gogo-1)

n = int(input("enter a number: "))
print(fac(n))    
