string = "Harry Potter and the Goblet of Fire"

a = string.split()
print(a)

for i in range(len(a)):
    a[i] = a[i].lower()

a.sort()    
print(a)
