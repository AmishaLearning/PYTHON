arr=[55,4,3,66,77,88]

#Finding Max
max=arr[0]

for i in range(1,len(arr)):
    if arr[i]>max:
        max=arr[i]
        
print("The Maximum Number is : ", max)

#Finding Min
min=arr[0]

for i in range(1,len(arr)):
    if arr[i]<min:
        min=arr[i]
       
print("The Minimum NUmber is : ",min)