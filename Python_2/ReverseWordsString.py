str1="Welcome To Python Programing"
print("The Original String is : ",str1) 

str2 = str1.split(" ")
print("The Original List      : ",str2)

str2.reverse()
print("The Reversed List      : ",str2)

str3=' '.join(str2)
print("The Reversed String is : ",str3)
