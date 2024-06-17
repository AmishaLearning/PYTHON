# list1 = [3, 5, 6, "Harry", True]

# if "Harry" in list1:
#     print("Yes")
# else:
#     print("No")
    
# if "arry" in "Harry":
#     print("Yes")
# else:
#     print("No")
    
# lst = [i*i for i in range(4)]
# print(lst)

# lst2 = [i*i for i in range(10) if i % 2 == 0]
# print(lst2)

#ONE ELEMENT TUPPLE

tup = (1,)
tup2 = (1)
print(type(tup2), tup2)
print(type(tup), tup)

tup3 = (1, 43, 13, 65 ,"Harry", True)
for i in tup3:
    print(i)
    
if "Harry" in tup3:
    print("Yes")
else:
    print("No")