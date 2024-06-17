num = int(input("Enter a number : "))
list1 = []

for i in range(2,num+1):
    if num % i == 0:
        list1.append(i)
print("The factores of {} are {}. ".format(num,list1))