# n=int(input("Enter a Number: "))

# if n%2!=0:
#     print("Weird")
    
# elif n%2==0 and n in range(2,6):
#     print("Not Weird")

# elif n%2==0 and n in range(6,21):
#     print("Weird")

# elif n%2==0 and n>20:
#     print("Not Weird")

# def is_leap(year):
#     leap = True
#     if year%400==0 or year%100!=0 and year%4==0:
#         return leap
   
#     else:
#         return not leap
   
# year=int(input())
# print(is_leap(year))

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year=int(input())
print(is_leap_year(year))



# def num(n):
#     for i in range(1,n+1):
#         print(i,end="")
   
# n=int(input())
# num(n)    


