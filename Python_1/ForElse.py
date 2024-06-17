#For..Else..
# nums=[12,16,18,20,25]

# for num in nums:
#     if num%5==0:
#         print(num)

# #If we want only the first number then use break
# nums=[12,16,18,20,25]

# for num in nums:
#     if num%5==0:
#         print(num)
#         break

#if none of the number is divisible by 5     
nums = [11, 16, 18, 21, 26]

for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print("Not Found")
