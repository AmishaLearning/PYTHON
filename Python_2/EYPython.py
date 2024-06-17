#Printing Uncommon from both the lists

# list1 = ["apple","orange","banana"]
# list2 = ["orange","apple","grapes"]

# list3 = set(list1)
# list4 = set(list2)

# list5 = list3.difference(list4)

# print(list(list5))

# list1 = ["apple","orange","banana"]
# list2 = ["orange","apple","grapes"]

# uncommon = []

# for i in list1:
#     if i not in list2:
#         uncommon.append(i)      
# print(uncommon)
    
# Printing Bigrams
    
# str1 = "Ram is a good boy"
# str2 = str1.split()
# list2 = []

# print(str2)

# for i in range(len(str2) - 1):
#     list1 = str2[i], str2[i + 1]
#     list3 = tuple(list1)
#     list2.append(list3)
    
# print(list2)
    
# # Printing Trigrams

# str1 = "Ram is a good boy"
# str2 = str1.split()
# list2 = []

# print(str2)

# for i in range(len(str2) - 2):
#     list1 = str2[i], str2[i + 1], str2[i + 2]
#     list3 = tuple(list1)
#     list2.append(list3)
    
# print(list2)

nums = int(input("Enter the number of inputs : "))
list1 = []
       
for i in range(nums):
    n = int(input("Enter the numbers : "))
    list1.append(n)  
    
list1.sort()
print(list1)

def even_num(num):
    for num in range(len(list1)):
        if num % 2 == 0:
            return True, list1[num]   
        else:
            return None, list1[num]
        
result = even_num(n)
print(result)
        