# #Number Palindrome
# num = 123
# num1 = str(num)
# print(num1[::-1])

# num = 123

# remainder1 = num % 10
# print(remainder1)

# quotient1 = num // 10
# print(quotient1)

# remainder2 = quotient1 % 10
# print(remainder2)

# quotient2 = quotient1 // 10
# print(quotient2)


# a = 123 % 10
# print(a)
# b = 123 // 10
# # print(b)
# c = b % 10
# print(c)
# d = b // 10
# print(d)
 
def reverse_num(number):
    reversed_number = 0
    
    while number > 0:
        obtained_first = number % 10
        reversed_number = reversed_number * 10 + obtained_first
        number = number // 10
        
    return reversed_number
    
print(reverse_num(123))
        


 


    