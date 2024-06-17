# n = int(input())

# for i in range(1, n + 1):
#     print(str(i) * i) 
    

# def print_sequence(n):
#     for i in range(1, n + 1):
#         num = i
#         for j in range(i):
#             print(num, end="")
#         print()
        
# print_sequence(5)

#This method checks if all the characters of a string are alphanumeric

# if __name__ == '__main__':
#     s = input()
    
# print(any(c.isalpha() for c in s))
# print(any(c.isalnum() for c in s))
# print(any(c.isdigit() for c in s))
# print(any(c.islower() for c in s))
# print(any(c.isupper() for c in s))


thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))