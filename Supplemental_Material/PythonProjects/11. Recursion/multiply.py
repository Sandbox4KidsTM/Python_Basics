def multStd(first, second):
    return first*second

# 4 * 3
# 4 + 4 + 4
# add 'a' to itself 'b' times

# product = 0, when second = 3
# product = 0 + first, wjem second = 2

def multIter(first, second):
    product = 0
    while second > 0:
        product = product + first
        second = second - 1
    return product

def multRecur(first, second):
    if second > 0:
       second = second - 1
       return first + multRecur(first, second)
    else:
       return 0
    
a = int(input("enter first number"))
b = int(input("enter second number"))

print(multStd(a, b))
print(multIter(a, b))
print(multRecur(a, b))
