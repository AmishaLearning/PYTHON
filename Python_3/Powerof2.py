# for i in range(0,int(input("Enter the value of powers : "))):
#     i=2**i
#     print(i,end=" ")


nterms = int(input("Enter the number of terms : "))

result = list(map(lambda x : 2 ** x, range(nterms+1)))
#map function goes inside every iteration
print(result)

for i in range(nterms+1):
    print("The value of 2 raised to the power {} is {}. ".format(i,result[i]))
