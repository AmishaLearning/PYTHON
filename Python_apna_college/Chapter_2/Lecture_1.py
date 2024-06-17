# Strings

# print("---------------------------------------------------------")
# str1 = "Hello World!"
# str2 = 'Hello World!'
# str3 = '''Hello World!'''

# # Next line
# str1 = "Hi!\nAmisha"
# print(str1)

# # Tab
# str2 = "Hello \tWorld!"
# print(str2)

# print("-----------------------------Concatination----------------------------")
# str1 = "Hi!" 
# str2 = "Amisha"
# print(str1 + str2)

# print("--------------------------length----------------------------")

# print(len(str2))

# print("----------------------------Indexing-----------------------------")

# str3 = "Amisha_Srivastava"
# print(str3[0])

# print("----------------------------Slicing-----------------------------")

# str4 = "Amisha_Srivastava"
# print(str4[0:6])
# print(str4[6:len(str4)])
# print(str4[6:])
# print(str4[:5])
# print(str4[:-5])

# print("----------------------------String Functions-----------------------------")

# str5 = "i am from studying python from ApnaCollege"
# print(str5.endswith("ege"))
# print(str5.capitalize())
# print(str5)
# str5 = str5.capitalize()
# print(str5)
# print(str5.replace("a", "B"))
# print(str5.find("am"))
# print(str5.find("Z"))
# print(str5.count("a"))
# print(str5.count("from"))
 
# print("--------------------------Conditional Statement-------------------------------")

# marks = float(input("Enter the marks : "))
# if marks >= 90:
#     print("Grade : A")
# elif marks >= 80 and marks < 90:
#     print("Grade : B")
# elif marks >= 70 and marks < 80:
#     print("Grade : C")
# else:
#     print("Grade : D ")
    
print("-----------------------------Nesting----------------------------")

age = int(input("Enter Age : "))
if (age >= 18):
    if (age >=80):
        print("Cannot Drive")
    else:
        print("Can Drive")
else:
    print("Cannot Drive")