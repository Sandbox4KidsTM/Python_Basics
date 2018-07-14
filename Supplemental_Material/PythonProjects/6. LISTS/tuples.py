tuple1 = ("banana", 3.2, 7)
print(tuple1)
print(type(tuple1))
#tuple1.reverse() #reverse(), pop(), remove(), clear() etc. are not allowed
#tuple is NOT mutable
print(tuple1)

list1 = ["orange", 2.7, 3]
print(list1)
list1.reverse() #list is revered in place i.e. it is mutable
print(list1)
list1.clear()
print(list1)

#type dir(tuple) to get a list of all the methods associated with tuple
#type dir(list) to get a list of all the methods associated with list

