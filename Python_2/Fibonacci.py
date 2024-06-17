
n=int(input("Enter the range of Fibonacci Series: "))
a=0

if n<0:
    print("Fibonacci Series Not Possible")

elif n == 1:
    print(a)
    
else: 
    if n>0:
        b=1
        print(a, end=" ")
        print(b, end=" ")
        for i in range(2,n):
            c=a+b          
            a=b
            b=c
            print(c, end=" ")
            