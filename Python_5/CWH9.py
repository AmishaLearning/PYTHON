#Recursion and SET

# def factorial(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n - 1)

# n = int(input("Enter the number to find its factorial : "))    
# print(f"The factorial of {n} is {factorial(n)}")

# def fibonacci(n):
#     a = 0
#     if n <= 0: 
#         print("Fibonacci not possible")
        
#     elif n == 1:
#         print(a)
        
#     else:
#         b = 1
#         print(a, end = " ")
#         print(b, end = " ")
#         for i in range(n):
#             c = a + b
#             a = b
#             b = c
#             print(c, end = " ")
# n = int(input("Enter range of fibonacci : "))
# fibonacci(n)

# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n - 1) + fibo(n - 2)
    
# n = int(input("Enter the length of Fibonacci Series : "))

# if n <= 1:
#     print("Fibonacci Series not possible. ")
# else:
#     for i in range(n):
#         print(fibo(i),end=" ")

# #Set Methods
# name = set()
# print(type(name))

s1 = {1, 2, 5, 6}
s2 = {3, 6 ,7}
#UNION AND UNION UPDATE

# print(s1.union(s2))
# print("Not updated value :",s1)
# # print(s1)# s1 and s2 are not updated remains same
# #To update s1 or s2
# s1.update(s2)
# print("Updated value :",s1,s2)

#INTERSECTION AND INTERSECTION UPDATE
# print(s2.intersection(s1))
# s2.intersection_update(s1)
# print(s2)

#SYMMERTIC DIFFERENCE
#remove value of (A intersection B) from values of (A union B)
#The values which are not common in the two sets

cities1 = {"Raebareli", "Lucknow", "Delhi", "Chandigarh"}
cities2 = {"Bangalore", "Chandigarh", "Raebareli"}

# cities3 = cities1.symmetric_difference(cities2)
# print(cities3)
# cities2.symmetric_difference_update(cities1)
# print(cities2)

#DIFFERENCE AND DIFFERENCE UPDATE
#prints values which are present in that particular set only

# cities4 = cities1.difference(cities2)
# print(cities4)

#DISJOINT SETS
#intersection of two sets is zero
# print(cities1.isdisjoint(cities2))

#ISSUPERSET()
#if all items of one set are present in the another set
# cities5 = {"Chandigarh", "Raebareli"}
# print(cities2.issuperset(cities5))
# #ISSUBSET()
# #items of original set are present in another set
# print(cities5.issubset(cities2))

#ADD
#used to add a value to a set
# cities1.add("Kurukshetra")
# print(cities1)

#UPDATE
#used to add more than one item (example above)

#REMOVE/DISCARD
#main difference between both is, if a value is not present and we try to delete it
#then, remove() method will show error but discard() will not

# print(cities1.remove("Bangalore"))
# cities1.discard("Bangalore")
# print(cities1)
# cities1.remove("Raebareli")
# print(cities1)

#pop()

# item = cities2.pop()
# print(cities2)
# print(item)

#del
#can delete an entire set

# del cities1
# print(cities1)

#clear()
#its used to clear all the elements in set, it inturn returns an empty set
# cities1.clear()
# print(cities1)

if "Raebareli" in cities1:
    print("Yes")
else:
    print("No")