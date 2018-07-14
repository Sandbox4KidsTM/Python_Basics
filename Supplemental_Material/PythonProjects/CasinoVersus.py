import random


cw = 0
vw = 0

j = 0
while j < 1000: #played for j number of days
    
    casino = 10000
    venkat = 100
    
    i = 0
    while i < 1000:
        toss = random.randint(0,1)
        if toss == 0:
            casino = casino + 1
            venkat = venkat -1
            if venkat <= 0:
                break
        if toss == 1:
            venkat = venkat + 1
            casino = casino - 1
            if casino <= 0:
                break
        i = i + 1
    
    if venkat <= 0:
       cw = cw + 1
    elif casino <= 0:
        vw = vw + 1
    else:
        print()
    
    j = j + 1

print("casino wins: ", cw)
print("venkat wins: ", vw)
    
