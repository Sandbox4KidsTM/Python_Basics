# https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2

# MATH FUNCTIONS in Python: https://docs.python.org/3.2/library/math.html

#all key methods related to string manipulation

message = "Hello World"
print(message[0:3]) #including lower limit, but not including upper limit

print(message.lower()) #prints lower case
print(message.upper()) #prints uppoer case

print(message.count('l')) #counts the number of occurances of substring 'l'
print(message.find('World')) #prints index of first occurance of substring 'l'
print(message.find('bobo')) #prints -1, if substring is not found

print(message.casefold())

message = message.replace('World', 'Universe')
print(message)