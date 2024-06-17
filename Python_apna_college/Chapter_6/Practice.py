# print("---------------------------------Question_1--------------------------------")

# def len_list(list1):
#     print(len(list1))
#     # return len(list1)

# list1 = [1, 3, 5, 7, 9]
# len_list(list1)

# print("---------------------------------Question_2--------------------------------")

# def elements(list2):
#     for i in list2:
#         print(i, end = " ")
#     # return i
    
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# elements(list2)

# print("---------------------------------Question_3--------------------------------")

# n = int(input("Enter a number : "))
# i = 1

# def fact(n):
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i
#         i += 1
#     print(factorial)
#     # return factorial
# n = int(input("Enter a number : "))
# fact(n)

# print("--------------------------------Question_4--------------------------------")

# def usd_inr(amount):
#     usd = amount * 83.503853
#     print(amount, "USD =", usd, "INR" )
#     # return usd

# amount = float(input("Enter amount(INR): "))
# usd_inr(amount)

# print("--------------------------------Question_5--------------------------------")

# def odd_even(number):
#     if number % 2 == 0:
#         print("The number is Even")
#     else:
#         print("The number is Odd")
        
# number = int(input("Enter a number : "))
# odd_even(number)

# print("--------------------------------Question_6--------------------------------")

# def sum_natural(n):
#     if (n == 0):
#         return 0
#     else:
#         return n + sum_natural(n - 1) 
    
# sum = sum_natural(5)   
# print(sum)

print("--------------------------------Question_7--------------------------------")

def print_list(list1, index = 0):
    if (index == len(list1)):
        return 
    else:
        print(list1[index])
        print_list(list1, index + 1)

list1 = [4, 3, 8, 6, 9, 10]
print_list(list1)