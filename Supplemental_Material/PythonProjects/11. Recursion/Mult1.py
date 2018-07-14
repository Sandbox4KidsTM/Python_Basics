
def multU(a, b): #usual multiplication
    product = a*b
    return product

def multR(a, b):
    if b > 1:
        b = b - 1
        return a + multR(a, b)
    if b == 1:
        return a

one = int(input("enter first number"))
two = int(input("enter second number"))

print(multU(one, two))
print(multR(one, two))

