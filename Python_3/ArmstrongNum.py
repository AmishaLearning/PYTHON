# ARMSTRONG NUMBER
# 153 = (1x1x1) + (5x5x5) + (3x3x3) = 153

number = int(input("Enter the number : "))
sum = 0
temp = number


digit1 = temp % 10

print("First digit for armstrong : ",digit1)

cube = digit1 ** 3

sum = sum + cube
print("Sum after 1st cube : ",sum) # 27

number2 = temp // 10
print("Now number is : ",number2)

digit2 = number2 % 10
print("Second digit for armstrong : ",digit2)

cube2 = digit2 ** 3
sum2 = sum + cube2

print("Sum after 2nd cube : ",sum2)

digit3 = number2 // 10
print("The last digit is : ",digit3)

cube3 = digit3 ** 3
sum3 = sum2 + cube3

print("The final sum is : ",sum3)

if sum3 == number:
    print("Yes! Its an Armstrong number")
else:
    print("No!! Its not an Armstrong number")    

