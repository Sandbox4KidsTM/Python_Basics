#general solution of a quadratic equation: SIMPLE

quad = input("enter a stadard quadratic equation ")
print(quad)

if (quad.find("x^2") == -1):
    print("this is NOT a quadratic equation")
else:
    print("this IS a quadtratic equation")
    terms = quad.split(" ")
    print(terms)
    for item in terms:
        if 'x^2' in item:
            a = item
            print(a)

