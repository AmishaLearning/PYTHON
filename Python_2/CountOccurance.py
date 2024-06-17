#APPROACH 1
list1 = [1, 3, 4, 2, 1, 3, 1, 2, 1, 2, 1]
x = int(input("Enter the number you want to count : "))
count = 0

for i in list1:
    if i == x:
        count = count + 1
        
print("The number {} appears {} times.".format(x, count))

#APPROACH 2 USING  count() method

# list2=[12,34,45,12,34,12,99,12]
# y=int(input("Enter the number you want to count :"))

# print("The number of times {} occurred is {}.".format(y,list2.count(y)))

#APPROACH 3 USING counter() method

# from collections import Counter
# list3=[21,43,21,54,21,65,21,76,21]
# x=int(input())
# dic=Counter(list3)# used to count each and every elements occurrance
# print("The number of times {} occurred is {}.".format(x,dic[x]))