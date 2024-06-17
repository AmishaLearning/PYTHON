# """Have the function ArrayChallenge(strArr) take the array of strings stored in strArr, 
# which will only contain two strings of equal length that represent binary numbers, and return a
# final binary string that performed the bitwise OR operation on both strings. A bitwise OR operation
# places a 0 in the new string where there are zeroes in both binary strings, otherwise it places a 1 in 
# that spot. For example: if strArr is ["1001", "0100"] then your program should return the string 1101 """


# def ArrayChallenge(strArr):
#   result = ""
#   for i in range(len(strArr[0])):
#     if strArr[0][i] == "0" and strArr[1][i] == "0":
#       result += "0"
#     else: 
#       result += "1"
#   return result

# print(ArrayChallenge(input()))

# def ArrayChallenge(strArr):
#   result = ""
#   for i in range(len(strArr[0])):
#     if strArr[0][i] == "0" and strArr[1][i] == "0":
#       result += "0"
#     else: 
#       result += "1"
#   return result

# input_strings = ["10011", "01111"]
# output = ArrayChallenge(input_strings)
# print(output)

# """Have the function MathChallenge(num) return the string yes if the number given is part of the Fibonacci sequence. 
# This sequence is defined by: Fn = Fn-1 + Fn-2, which means to find Fn you add the previous two numbers up. 
# The first two numbers are 0 and 1, then comes 1, 2, 3, 5 etc. If num is not in the Fibonacci sequence, return the string no."""

# def MathChallenge(num):
#   if num < 0:
    
#     return "no"
#   a, b = 0, 1

#   while a <= num:

#     if a == num:
#       return "yes"
#     a, b = b, a + b
  
#   return "no"
  
# # keep this function call here 
# print(MathChallenge(input()))


# Did in coderbyte
def MathChallenge(num):
  
  if num < 0:
    return "no"
  a, b = 0, 1

  while b < num:
    a, b = b, a + b
  
  return "yes" if b == num else "no"

# keep this function call here 
print(MathChallenge(input()))

