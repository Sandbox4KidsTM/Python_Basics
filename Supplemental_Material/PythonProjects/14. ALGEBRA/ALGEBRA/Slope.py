#calculates the slope of a line

equation = input("enter the equation, space after each term: ")
print(equation)
terms = equation.split(" ")
print(terms)

varTerms = []

for item in terms:
    if item == " ":
        terms.remove(item)

print(terms)

for item in terms:
    if 'x' in item:
        varTerms.append(item)
        
print(varTerms)

lhs, rhs = varTerms[0].split('x')
print("slope is", lhs)