def NaturalNumSum(n):
    if n <= 1:
        return n
    else:
        return n + NaturalNumSum(n-1)

n=int(input("Enter a number : "))

if n <= 0:
    print("Enter a Positive Number!!")
else:
    print("The sum of First {} natural numbers is {}. ".format(n,NaturalNumSum(n)))
    
