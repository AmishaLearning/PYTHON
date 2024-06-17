#INTERCHANGE FIRST AND LAST

# list1 = [12,34,56,78,43]
# print(list1)
# list1[0], list1[-1] = list1[-1],list1[0]
# print(list1)


# def swap(list):
#     start, *middle, last = list
#     list = [last, *middle, start]
    
#     return list

# newlist = [12, 34, 56, 78]
# print(newlist)
# print(swap(newlist))
    

#SWAP TWO ELEMENTS IN THE LIST

# list2 = [12, 23, 34 ,45, 56, 67 ,78 ,89]
# print("Initial List : ",list2)
# print("Choose the Position 1 and Position 2 which is less than {}. ".format(len(list2)))

# pos1 = int(input("Enter the position 1 : "))
# pos2 = int(input("Enter the position 2 : "))

# list2[pos1], list2[pos2] = list2[pos2], list2[pos1]

# print("Swapped List : ",list2)

#SWAP CHARACTERS IN STRING

# str1 = ['Gfg', 'is', 'best', 'for', 'Geeks']
# print("The Original List is          : ", str1)

# result = [sub.replace('G','-').replace('e', 'G').replace('-', 'e') for sub in str1]
# print("The list after character swap : ", result)

str2 = ["Amisha", "Aarushi", "Arun", "Sheila"]
print("The Original List is          : ",str2)

result2 = [i.replace("A", "B").replace("a", "b") for i in str2]
print("The list after character swap : ",result2)
