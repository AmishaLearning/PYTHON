#APPROACH 1 USING find()
#find() method finds the first occurrence of the specified value
#find() returns -1 if the value is not found

str1="welcome to python programming"
sub_str=str(input("Enter the Sub String you want to find : "))

# print(str1.find(sub_str))# gives the starting position where the string started

if (str1.find(sub_str) == -1):
    print("The Sub String is not present")
else:
    print("The Sub String is present")