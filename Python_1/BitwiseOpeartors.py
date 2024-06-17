#Bitwise Operator- Complement. And, Or, XOR, Left Shift, Right Shift
#Compliment(~)
print(~12)#-13 is the answer
#00001100(12)---(~12)--11110011

#-13--2's Compliment--(1's Complement +1)
#00001101(13)--1's Complement--11110010--2's Compliment--11110011(-13)

print(~45)#Answer is -46
# 00101101(45)--(~45)--1's Complement--11010010--2's Complement
#00101101+1--00101110(-46)

print(12&13)#12--00001100
            #13--00001101
            #----00001100(AND means Multiplication)
print(12|13)#12--00001100
            #13--00001101
            #----00001101
print(25&30)#24

#XOR--odd number of 1's= 1 in o/p(^)
print(12^13)#12--00001100
            #13--00001101
            #----00000001
print(25^30)#7

#Left Shift
print(10<<2)#initially--1010.000
            #left shift--101000.00--40
print(10>>2)#initially--1010.00
            #right shift--10.100(2)