# towers of Hanoi
# The number of moves necessary to move a tower with n disks can be calculated as: 2n - 1 
# The legend and the game "towers of Hanoi" had been conceived by the French mathematician Edouard Lucas in 1883. 

# There is a general rule for moving a tower of size n (n > 1) from the peg S to the peg T:
#1 move a tower of n - 1 discs Dn-1 ... D1 from S to A. Disk Dn is left alone on peg S
#2 move disk Dn to T
#3 move the tower of n - 1 discs Dn-1 ... D1 on A to T, i.e. this tower will be put on top of Disk Dn

source = ([], "source") #starting pole
aux = ([], "aux") #intermediate or auxillary pole
target = ([], "target") #desitnation pole

def fillSource(n):
    i = n
    while i > 0:
        source[0].append(i)
        i = i - 1
    return source

def HanoiMove(n, source, aux, target):
    if n > 0:
        # move tower of size n-1 from source to aux
        HanoiMove(n-1, source, target, aux) # move from source to aux
        
        if len(source[0]) > 0:
            disk = source[0].pop()
            print ("moving " + str(disk) + " from " + source[1] + " to " + target[1])
            target[0].append(disk)
        
        # move tower of size n-1 from helper to target
        HanoiMove(n-1, aux, source, target) # move from aux to target
           
n = int(input("enter number of levels: "))
print(fillSource(n))
HanoiMove(len(source[0]), source, aux, target)