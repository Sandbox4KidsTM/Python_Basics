#calculate modulus without using modulus function
#repeated subtraction

def modMe(dividend, divisor):
    if divisor == 0:
        return "Shaqtin' a Fool! Divisor cannot be zero!!"
    if dividend > divisor:
        dividend = dividend - divisor
        return modMe(dividend, divisor)
    if dividend < divisor:
        return dividend

dividendE = int(input("what's the dividend?"))
divisorE = int(input("what's the divisor?"))
print(modMe(dividendE, divisorE))