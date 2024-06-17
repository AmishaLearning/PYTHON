# Python – Extract elements with Frequency greater than K

# list1 = [1, 2, 3, 5, 1, 2, 5, 1, 3, 2, 4, 6, 7, 8, 9, 5]
# k = 2
# count = 0

# elements = []

# for i in list1:
#     freq = list1.count(i)
    
#     if freq > k and i not in elements:
#         elements.append(i)
        
# print(elements)


# Python – Test if List contains elements in Range

# list2 = [4, 5, 6, 7, 3, 9]
# i, j = 3, 10

# result = True
# for x in list2:
#     if x < i or x >= j:
#         result = False
#         break
# print(f"Does list contains all elements in the range {i} to {j} : {result}")

# Python program to check if the list contains three consecutive common numbers in Python

arr = [1, 1, 1, 64, 23, 64, 22, 22, 22]
size = len(arr)
conse = []
for i in range(size - 2):
	if arr[i] == arr[i + 1] and arr[i + 1] == arr[i + 2]:
		conse.append(arr[i])
  
print(f"List of Three Consecutive common elements is : {conse}")


        