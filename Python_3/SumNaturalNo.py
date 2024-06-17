num = int(input("Enter the value : "))

if num < 0:
    print("Sum not possible as it's not a natural number.")
    
else:
    original_num = num
    sum = 0
    while num > 0:
        sum += num
        num -= 1
        
    print("The sum of First {} natural numbers is {}. ".format(original_num, sum)) 

#The issue with the code was that the variable 'num' is being decremented inside the while loop, and then its value is being used to display
#the result at the end. This will cause the output to display as if the value of 'num' is 0, regardless of the user input.