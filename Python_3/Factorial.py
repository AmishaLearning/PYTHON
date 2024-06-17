num=int(input("Enter a number : "))
fact=1

if num < 0:
    print("Factorial for {} doesn't exist. ".format(num))
    
if num == 0:
    print("Factorial for {} is {}. ".format(num,fact))
    
if num > 0:
    for i in range(1,num+1):
        fact = fact*i
print("Factorial for {} is {}. ".format(num,fact))