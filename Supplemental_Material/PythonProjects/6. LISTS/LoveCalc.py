# Love Calculator

def crt1Func(strA, strB):
    if (((len(strA) - len(strB)) > 2) or (len(strB) - len(strA)) > 2):
        return 0 
    else:
        return 75 #returns 75 (weightage is 75% for this criteria)

#if the names both have an even amount of characters
def crt2Func(name1,name2):
    variable = 0
    variable2 = 0
    if(len(name1)%2 == 0):
        variable+=1
    if(len(name2)%2 == 0):
        variable2+=1
    if(variable == variable2):
       return 25 #returns 25 (weightage is 25% for this criteria)
    else:
        return 0
        
# ask user to enter 2 names
str1 = input("enter your name")
str2 = input("enter your friend's name")

print(crt1Func(str1, str2) + crt2Func(str1, str2))