# # ARMSTRONG NUMBER Three digit 
# # 153 = (1x1x1) + (5x5x5) + (3x3x3) = 153

number = int(input("Enter a number : "))
sum = 0
temp = number

while temp > 0:
    digit = temp % 10
    cube = digit ** 3
    sum = sum + cube
    temp = temp // 10
    
    
if sum == number:
    print("Yes! Its an Armstrong number")
else:
    print("No!! Its not an Armstrong number")  


# number = int(input("Enter a number : "))
# length = len(str(number))
# print("The length of the number is : ",length)
# sum = 0
# temp = number

# while temp > 0:
#     digit = temp % 10
#     cube = digit ** length
#     sum = sum + cube
#     temp //= 10
    
# if sum == number:
#     print("Yes! Its an Armstrong number")
# else:
#     print("No!! Its not an Armstrong number")  
    
# temp //= 10: This is an in-place floor division assignment. 
# It means that the value of temp is updated by performing floor division with 10, 
# and the result is stored back in temp. It effectively removes the last digit of temp.

#num = temp // 10: Here, a new variable num is defined, 
# and it is assigned the value of temp after performing floor division with 10. 
# This operation effectively removes the last digit from temp and stores the result in num