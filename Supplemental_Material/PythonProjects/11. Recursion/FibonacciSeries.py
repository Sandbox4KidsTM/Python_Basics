#Fn = F(n-1) + F(n-2)
#Fn = 0 when n = 0, and Fn = 1 when n = 1
#print first n Fibonacci Series

def Fib(num):
    FibArray = []
    if num == 1:
        FibArray = [0]
        return FibArray
    elif num == 2:
        FibArray = [0, 1]
        return FibArray
    else:
        FibArray = ???
        return Fib(num-1) + Fib(num-2)
    
n = int(input("enter the number of items in Fibonacci series you want"))
print(Fib(n))