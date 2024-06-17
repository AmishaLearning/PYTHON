#APPROACH 1
# a=10
# b=20

# print("The Old Value of 'a' is :",a)
# print("The Old Value of 'b' is :",b)

# a,b=b,a

# print("The New Value of 'a' is :",a)
# print("The New Value of 'b' is :",b)

#APPROACH 2

a=input("Enter value of 'a' :")
b=input("Enter value of 'b' :")

print("The Old Value of 'a' is :",a)
print("The Old Value of 'b' is :",b)

temp=b
b=a
a=temp

print("The New Value of 'a' is :",a)
print("The New Value of 'b' is :",b)
