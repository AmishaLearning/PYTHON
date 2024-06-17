#If Statement
if False:
    print("I'm Right")
print("Bye")# Outside of the if loop

x = 8
r = x % 2
if r == 0:
    print("Even")
if r == 1:
    print("Odd")
    
#for efficient coding we use if else
x = 9
r = x % 2
if r == 0:
    print("Even")
else:
    print("Odd")
    
#If inside if(Nested if)
x = 4
r = x % 2
if r == 0:
    print("Even")
    if x > 5:
        print("Yes! its greater than 5")
    else:
        print("No! its not greater than 5")
else:
    print("Odd")

#if...even if x value is found to be 2 it will check for all other ifs so to remove that er use elif
x = 2
if x == 1:
    print("ONE")
if x == 2:
    print("TWO")
if x == 3:
    print("THREE")
if x == 4:
    print("FOUR")
    
#elif
x = 5
if x == 1:
    print("ONE")
elif x == 2:
    print("TWO")
elif x == 3:
    print("THREE")
elif x == 4:
    print("FOUR")
else:
    print("Wrong Input")

#Assignment 1    
x = 5
if x > 0:
    print("Positive Number")
else:
    print("Negative Number")
    
#Assignment 2
a = int(input("Enter 1st Value :"))
b = int(input("Enter 2nd Value :"))
c = int(input("Enter 3rd Value :"))

print(max(a,b,c))