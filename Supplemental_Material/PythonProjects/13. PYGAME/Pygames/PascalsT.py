n = int(input("# of levels?: "))

X = [1]
Y = [1,1]

if n == 0:
    print(X)
if n == 1:
    print(X)
    print(Y)
    
if n > 1:
    cLevel = 2 #tracks current level
    print(X)
    print(Y)
    while cLevel <= n:
        X = list(Y) #copy list Y into list X
        lY = len(Y) #current length of Y
        Y[0] = 1
        i = 1
        while i < lY:
            Y[i] = X[i-1] + X[i]
            i = i + 1
        Y.append(1)
        print(Y)
        cLevel = cLevel + 1