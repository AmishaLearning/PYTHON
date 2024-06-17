# Any or All

# num = int(input("Enter the number of integers : "))
# integers = list(map(int, input("Enter the integers : ").split()))

# all_positive = all(i > 0 for i in integers)
# any_positive = any(i > 0 for i in integers)

# if all_positive:
#     print(True)
# else:
#     print(False)

# Exceptions

nums = int(input("Enter the number of values : "))
for i in range(nums):
    values = input("Enter the numbers : ").split()
    try:
        division = int(values[0])//int(values[1])
        print(division)
    except Exception as e:
        print("Error Code:",e)
        

# nums = int(input("Enter the number of values: "))

# for i in range(nums):
#     values = input("Enter two numbers separated by space: ").split()

#     try:
#         num1 = int(values[0])
#         num2 = int(values[1])
#         division = num1 / num2
#         print("Result:", division)
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")
#     except ValueError:
#         print("Error: Please enter valid numeric values.")
