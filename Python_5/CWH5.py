# for i in range(1,15):
#     if i == 11:
#         continue
#     print("5 X ",i,"=",5*i)
# print("Loop lo chorke nikal gya...break")

# #Break means Loop ko chorke nikal jao
# #Continue means Iteration ko chorke nikal jao

# for i in range(1,15):
#     if i == 11:
#         print("Skip the iteration")
#         continue
#     print("5 X ",i,"=",5*i)
    
    
# i = 0 
# while True:
#     print(i)
#     i = i + 1
#     if i % 10 == 0:
#         break
def CalculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def isgreater(a, b):
    if a > b:
        print("First number is greater")
    else:
        print("Second number is greater or equal")
a = 9
b = 8
CalculateGmean(a, b)
isgreater(a,b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)

c = 7
d = 8
CalculateGmean(c, d)
isgreater(c, d)
# gmean2 = (c*d)/(c+d)
# print(gmean2)