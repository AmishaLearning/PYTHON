# x=int(input("Enter the value of x : "))
# y=int(input("Enter the value of y : "))
# z=int(input("Enter the value of z : "))
# n=int(input("Enter the value of n : "))

# list1= ([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if x+y+z!=n])
# print(list1)

# n=int(input("Enter the value of n : "))
# arr=list(map(int, input("Enter the array : ").split()))

# sortedlist=sorted(arr,reverse=True)

# print("The runner up is {} ".format(sortedlist[1]))

# n=int(input("Enter the value of N : "))
# arr=list(map(int, input("Enter the array : ").split()))

# maxi=max(arr)
# print("The maximum value is : ",maxi)

# runner=max([i for i in arr if i!=maxi])
# print("The runner-up is : ", runner)

# list1=[]

# range_value = int(input())

# for i in range(range_value):
#         name = input()
#         score = float(input())
#         list1.append((name,score))
        
# list1.sort()

# second_lowest_score = sorted(set([score for i , score in list1]))[1]
# second_lowest_names = sorted([name for name, score in list1 if score == second_lowest_score])

# for name in second_lowest_names:
#     print(name)
     
     
# tuple1=int(input())
# tuple2=list()
# for i in range(tuple1):
#     number=input()
#     tuple2.append(number)

   
# z=tuple(tuple2)
# x=hash(z)
# print(x)
        
# n = int(input("Enter the number of integers: "))
# numbers = input("Enter the space-separated integers: ").split()

# # Convert the list of strings to a tuple of integers
# t = tuple(map(int, numbers))

# # Compute and print the hash value of the tuple
# print(hash(t))

# str1 = str(input("Enter the String : "))
# str2 = ""

# for i in str1:
#     if i.islower():
#         str2 += i.upper()
#     elif i.isupper():
#         str2 += i.lower()
#     else:
#         str2 += i
# print(str2)        

# str1 = str(input("Enter the String : "))

# str2=''.join([i.upper() if i.islower() else i.lower() if i.isupper() else i for i in str1])
# print(str2)

# def split_and_join(line):
#     line= line.replace(" ","-")
#     return line

# if __name__ == '__main__':
#     line = str(input())
#     result = split_and_join(line)
#     print(result)


# def print_full_name(first_name, last_name):
#     first_name = first_name
#     last_name = last_name
#     print("Hello {} {} ! you just delved into python".format(first_name , last_name))

# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)


#Without replacing character

# def mutate_string(string, position, character):
#     l = list(string)
    
#     string = l.insert(position,character)
#     string2 = ''.join(l)
    
#     return string2

# #with replacing character

# # def mutate_string(string, position, character):
# #     l = list(string)
# #     print(l)
# #     l[position] = character
# #     string = ''.join(l)
    
# #     return string  
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)


