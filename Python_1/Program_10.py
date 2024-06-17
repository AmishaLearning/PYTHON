#Python Lists
mylist = ["apple", "mango", "cherry"]
print(mylist)
print(mylist[1])
print(len(mylist))

list1 = ["apple", "mango", "cherry"]
list2 = [1, 3, 5, 7, 9]
list3 = [True, False, True]
print(type(list1))

list4 = list(("apple", "mango", "banana", "kiwi", "pomegranate", "grapes"))
print(list4)

print(list4[-1])
print(list4[0:2])
print(list4[:4])
print(list4[-4:-1])

if "apple" in list4:
    print("Yes!")
    
#Change item value
list4[3] = "Anar"
print(list4)
#Change range of values

list4[1:3] = ["Angoor", "cherry"]
print(list4)

list4[1:3] = ["watermelon"]
print(list4)

list4.insert(2,"blueberry")
print(list4)
list4.append("orange")
print(list4)

list4.extend(list1)
print(list4)
list4.remove("apple")
print(list4)
print(list4.pop(0))
del list4[1]
print(list4)
# print(list4.clear())

for x in list4:
    print(x)
for i in range(len(list4)):
    print(list4[i])
    
list5=["blue","white","red"]
i=0
while i < len(list5):
    print(list5[i])
    i=i+1
    
[print(x)for x in list5]

list6=["nokia","oneplus","n-apple","samsung"]
newlist=[]

for x in list6:
    if "n" in x:
        newlist.append(x)
print(newlist)

newlist1=[x for x in list6 if "n" in x]
print(newlist1)

newlist2 = [x for x in list6 if x!= "n-apple"]
print(newlist2)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist.sort(reverse=True)
print(thislist)
