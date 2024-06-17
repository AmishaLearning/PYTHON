list1=["geeks","for","geeks","again","geeks","for","geeks"]
word="geeks"
n=3

count=0

for i in range(0,len(list1)-1):
    if list1[i] == word:
        count = count+1
        if count == n:
            del list1[i]
print(list1)