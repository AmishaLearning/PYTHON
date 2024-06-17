#APPROACH 1
num = int(input("Enter a number : "))
for i in range(1,11):
    print("{} X {} = {} ".format(num, i, num * i))
    
# #APPROACH 2 
# num1 = int(input("Enter a number : "))

# for i in range(1,11):
#     z = i
#     i = i * num1
#     print("{} X {} = {} ".format(num1, z, i))
    
# #APPROACH 3 USING while loop

# num2 = int(input("Enter a number : "))
# i = 1

# while i <= 10:
#     print("{} X {} = {} ".format(num2, i, num2 * i))
#     i = i + 1