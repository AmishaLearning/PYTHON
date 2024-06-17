# num = int(input("Enter a number: "))
# count = 0

# if num > 1:
#     for i in range(1,num + 1):
#         if (num % i) == 0:
#             count = count + 1
#     if count == 2:
#         print("Number is Prime")
#     else:
#         print("Number is Not Prime")

num1=int(input("Enter a number : "))

if num1 == 1:
    print("{} is not a Prime Number ".format(num1))
    
if num1 > 1:
    for i in range(2,num1):
        if num1 % i == 0:
            print("{} is not a Prime Number ".format(num1))
            break
    else:
        print("{} is a Prime Number ".format(num1))