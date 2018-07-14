# http://level1wiki.wikidot.com/syntax-error

# import randomly # ModuleNotFoundError: No module named 'randomly'

import random #warning: module imported but not used

#r = random.randint(10) #TypeError: randint() missing 1 required positional argument: 'b'
r = random.randint(1, 6) #it was expecting 2 variables: min and max

#printe(r) # NameError: name 'printe' is not defined
print(r)



