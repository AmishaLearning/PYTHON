str1 = "Automation and Testing"
vowels = ['a', 'e', 'i', 'o','u']

str2 = str1.replace(" ","")
print(str2.lower())

dict1 = {}

for i in str1:
    if i in vowels:
        if i in dict1:
            dict1[i] = dict1[i] +1
         
        else:
            dict1[i] = 1        
print(dict1)

# from collections import Counter   
# str1 = "Testing python programming Language"
# x = input("Enter the alphabet you want to find occurrance of :")
# dic = Counter(str1)
# print("'{}' has occurred {} times. ".format(x,dic[x]) )


#USING DICTIONARY

a = "Harry Potter And The Prisoner Of Azkaban"
vowels = "aeiou"
a = a.casefold()
print(a)

count = {}.fromkeys(vowels, 0)
print(count)
for char in a:
    if char in count:
        count[char] = count[char] + 1
print(count)        

# USING LIST AND DICTIONARY COMPREHENSION

# a = "Harry Potter And The Prisoner Of Azkaban"
# vowels = "aeiou"
# a = a.casefold()

# count = {key:sum([1 for char in a if char == key])for key in vowels}

# print(count)