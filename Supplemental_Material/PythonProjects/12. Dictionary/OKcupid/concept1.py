# code for OKcupid.com
# https://www.youtube.com/watch?v=m9PiPlRuy6E

#1. Get PersonA Questions
#2. Get PersonB Questions
#3. Perform Analysis
#4. Give Compatibility Result
#5. Later on, create a database for each person, and then run compatibility analysis

#create a dictionary for each Person
print("welcome PersonA")
Name1 = input("enter your name")
Age1 = input("enter your age")
Location1 = input("do you live in city or village?")
name="name"
age="age"
location="location"

PersonA = {name: Name1, age: Age1, location: Location1}
print(PersonA)
print()

print("welcome PersonB")
Name1 = input("enter your name")
Age1 = input("enter your age")
Location1 = input("do you live in city or village?")
PersonB = {name: Name1, age: Age1, location: Location1}
print(PersonB)
