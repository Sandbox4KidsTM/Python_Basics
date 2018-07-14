# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 07:52:12 2017

@author: Sandbox999
"""

# single quotes
print('this is an example of print function')

# double quotes
print("another example of print function")

# three single quotes
print('''three single quotes''')

# three double quotes
print("""three double quotes""")

#cannot mix single & double quotes
#print('starts with single and ends with double")

#use double quotes to allow use of single quotes as apostrophe
# you can encase one single quote in two double quotes
# you can also encase one double quote in two single quotes
print("we're the champions")

#you can also use the escape character \ to encase one single into two double quotes
# escape character lets you "espace" the default behavior of the character it precedes
print('we\'re are going to the store')

#concatenate using either comma or plus sign
#comma automatically adds a plus sign
print('hello',"world")
print('hello'+"world")

print('hi',5) #prints hi 5
#print('hi'+5) #throws an error as it cannot convert int 5 into string to perform concatenation 
print('hi'+str(5))
#print(int('Hi')+5) #ValueError: invalid literal for int() with base 10: 'Hi'
print(int('8')+5) #string '8' is converted to int 8
print(float('8.65')+5)