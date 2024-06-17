# Swapping two values
a=5
b=6

# temp=a
# a=b
# b= temp
# print(a)
# print(b)

# a=a+b   #a=5+6=11
# b=a-b   #b=11-6=5
# a=a-b   #a=11-5=6
# print(a)
# print(b)

#XOR

# a=a^b   #a=0101(5)^0110(6)=0011(3) wherever bits are different 1 in output so a=3
# b=a^b   #b=0011(3)^0110(6)= 0101(5)
# a=a^b   #a=0011(3)^0101(5)=0110(6)
# print(a)#6
# print(b)#5

a,b=b,a
print(a)
print(b)