# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# the nth term in Fobonacci series is Fn = F(n-1) + F(n-2)
from timeit import Timer

def FibR(n): #recursive
    if n == 1:
        return 0
    if n == 2:
        return 1
    elif n > 2:
        return (FibR(n-1) + FibR(n-2)) 
    
def FibI(n): #iterative
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
    
#n = int(input("what's the term you want?"))
#print(FibR(n))
#print(FibI(n))

# time1 is the time in seconds it takes for 3 calls to fib(n) 
# and time2 respectively the time for fibi()
# CHECK THE TIMER FUNCTIONS

for i in range(1,41):
	s = "FibR(" + str(i) + ")"
	t1 = Timer(s,"from fibo import fib")
	time1 = t1.timeit(3)
	s = "FibI(" + str(i) + ")"
	t2 = Timer(s,"from fibo import fibi")
	time2 = t2.timeit(3)
	print("n=%2d, fib: %8.6f, fibi:  %7.6f, percent: %10.2f" % (i, time1, time2, time1/time2))
        
