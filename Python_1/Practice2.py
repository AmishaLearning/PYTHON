# list1=[1,2,4,6,1,2,3,4,5,6]
# print(list(set(list1)))
# print(list(dict.fromkeys(list1)))


# txt=" hi I am {name} {surname}".format(name="Amisha",surname="Srivastava")
# print(txt)
# txt1=" hi I am {0} {1}".format("Amisha","Srivastava")
# print(txt1)

# list2=["apple","nokia","oneplus","samsung"]
# print([x for x in list2 if "oneplus" in x])
# print([x for x in range(5)])

# import array as arr
# from array import *
# vals=array('i',[5,6,7,8,9])
# print(vals)

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
# x=int(input("enter :"))
# print(fact(x))

#0 1 1 2 3 5 8...
# def fib(x):
#     a=0
#     b=1
#     if x==1:
#         print(a)
#     elif x<0:
#         print("No Chance")
#     else:
#         print(a)
#         print(b)
#         for i in range(2,x):
#             c=a+b
#             a=b
#             b=c
#             if c<100:
#                 print(c)
#             else:
#                 break
        
# fib(6)

# print([i*i for i in range(1,5)])

# def sq():
#     n=1
#     while n<=10:
#         sq=n*n
#         n=n+1
#         print(sq)
# sq()

# str="This is a programming language"
# str1=str.replace(" ","")
# vowels=['a','e','i','o','u']

# dict1={}

# for x in str1:
#     if x in vowels:
#         if x in dict1:
#             dict1[x]=dict1[x]+1
            
#         else:
#             dict1[x]=1

# print(dict1)


# from numpy import *

# m= matrix('1 2 3 ; 2 3 4 ; 3 4 5')
# print(m)

# list1=[1,2,3,4,5,4,2,1]
# print(list(set(list1)))

# class A:
#     def sum(a,b):
#         c=a+b
#         print(c)


# A.sum(2,3)

# a=2
# b=0

# try:
#    print(a/b)
       
# except ZeroDivisionError as e:
#     print("can't do it")
    
    
# finally:
#     print("Something is done")
    
    
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

n= int(input("enter :"))
print(fact(n))