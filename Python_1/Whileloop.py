#While Loop
# i=1#initialization
# while i<=5:#condition
#     print("Amisha")
#     i=i+1#increment/decrement

# j=5
# while j>=1:
#     print("Something", j)
#     j=j-1
    
# j=1

# while j<=5:
#     print("Something ",end="")
#     i=1
#     while i<=4:
#         print("rocks ",end="")
#         i=i+1
#     j=j+1
#     print()
#First the inner while loop will be completed then the outer one

# i=1
# while i<=4:
#     j=1
#     while j<=4:
#         print("# ", end="")
#         j=j+1
#     print("# ")    
#     i=i+1

i=1
a=1

while i<=100:
    if a%3 == 0 or a%5 ==0:
        a=a+1
    else:
        print(a)
        a=a+1
    i=i+1
