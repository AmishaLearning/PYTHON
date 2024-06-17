#APPROACH 1

# str1="welcome to python programming"
# print(len(str1))

#APPROACH 2 Using loop
# str2="welcome to python programming"
# count=0

# for i in str2:
#     count=count+1
# print("The Length of String is : ",count)

#APPROACH 3 Using while loop and slicing
# str3="welcome to python programming"
# counter=0

# while str3[counter:]:
#     counter=counter+1
# print("The Length of String is : ",counter)

#APPROACH 4 Using join and count
str4="welcome to python programming"
random_str="X"
# print((random_str).join(str4))
# print((random_str).join(str4).count(random_str))
print("The Length of the String is : ",((random_str).join(str4).count(random_str))+1)