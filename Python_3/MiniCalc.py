print("~~~~~~~~~~~~~~MINI CALCULATOR~~~~~~~~~~~~~~~~~")

num1 = float(input("Enter the First number : "))
num2 = float(input("Enter the Second number : "))

print("The List of Operations are :\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")

choice = int(input("Enter ur choice as 1, 2, 3 or 4 : "))

if choice == 1 :
    print("Addition of numbers {} and {} = {}. ".format(num1,num2,num1+num2))
elif choice == 2 :
    print("Subtraction of numbers {} and {} = {}. ".format(num1,num2,num1-num2))
elif choice == 3:
    print("Multiplication of numbers {} and {} = {}. ".format(num1,num2,num1*num2))
elif choice == 4:
    print("Division of numbers {} and {} = {}. ".format(num1,num2,num1/num2))
else: 
    print("Error!! Invalid Input")
