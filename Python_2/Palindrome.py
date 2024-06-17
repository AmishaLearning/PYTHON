#APPROACH 1
word = str(input("Enter the word : "))

if word[0 : : ] == word[ : : -1]:
    print("Yes! It's a Palindrome")
else:
    print("No! It's not Palindrome")

# #APPROACH 2
# word=str(input("Enter the Word : "))
# x=word[::]
# y=word[::-1]

# if x==y:
#     print("Yes! It's a Palindrome")
# else:
#     print("No! It's not Palindrome")