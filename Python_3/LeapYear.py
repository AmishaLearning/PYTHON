year=int(input("Enter a Year : "))

if (year % 400 == 0) and (year % 100 == 0):
    print("{} is a Leap Year ".format(year))
    
elif (year % 4 == 0) and (year % 100 != 0):
    print("{} is a Leap Year ".format(year))
    
else:
    print("{} is not a Leap Year ".format(year))