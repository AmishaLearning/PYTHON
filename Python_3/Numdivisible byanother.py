# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number : "))

# if a % b == 0:
#     print("The first number {} is divisible by the second number {}. ".format(a,b))
    
# elif b % a == 0:
#     print("The second number {} is divisible by the first number {}. ".format(b,a))
    
# else:
#     print("The numbers are not divisible by each other")

#FOR LOOP AND CONDITIONAL STATEMENTS
    
# num = int(input("Enter a number : "))
# rangereq = int(input("Enter the range for divisibility check : "))

# print("The Numbers which are divisible by {} in the range from 1 to {} are : ".format(num, rangereq))

# list1=[]

# for i in range(1,rangereq):
#     if i % num == 0:
#         list1.append(i)
# print(list1)

#USING lambda function AND filter() function

list2 = [12,23,36,48,56,60,78,89]

result = list(filter(lambda x : x % 12 == 0 , list2))

print("The numbers which are divisible by 12 are ",result)