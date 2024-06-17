# a = 'py' 'thon'
# print(a)

# word = 'Python'
# x='J' + word[1:]
# print(x)


# a, b = 0, 1
# num = int(input("Enter a number : "))
# while a <= num:
#     print(a)
#     a, b = b , a+b
      
      
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            print("***")
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
