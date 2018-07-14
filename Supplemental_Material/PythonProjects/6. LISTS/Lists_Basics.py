s = "Hello"
c = ["H", 123, 12.34, "Hellow"]

print(s)
print(type(s))
print(type(s[1]))
print(c)
print(type(c))

print(c.remove(c[2]))
print(c)


for char in s:
    print(char)
    
print('')

for i in range(0, len(s)):
    print(s[i])
    