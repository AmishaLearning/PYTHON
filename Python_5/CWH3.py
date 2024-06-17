# time = int(input("Enter the time in 24hr pattern : "))
# name = input("Enter a name : ")

# if time < 12 :
#     print("Hello {} Good Morning !!".format(name))
    
# elif time >= 12 and time <= 16 :
#     print("Hello {} Good Afternoon !!".format(name))
    
# elif time > 16 and time < 22:
#     print("Hello {} Good Evening !!".format(name))
    
# else: 
#     print("Hello {} Good Night !!".format(name))
    
import time

timestamp = int(time.strftime("%H"))
print("The time is : ",timestamp)

if (timestamp) < 12 :
    print("Good Morning!!")
elif (timestamp) >= 12 and timestamp <= 16 :
    print("Good Afternoon !!")
elif (timestamp) > 16 and (timestamp) <= 22:
    print("Good Evening !!")
else:
    print("Good Night !!")