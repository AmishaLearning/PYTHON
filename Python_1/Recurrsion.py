#Recurrsion-- Calling a function from itself
#By default the recurrsion limit is 1000
import sys

sys.setrecursionlimit(2000)#Used for setting recurrsion limit on ur own
print(sys.getrecursionlimit())#default limit 
i=0
def greet():
    global i
    i+=1
    print("Hello People!! ", i)
    greet()
greet()
