# # print("------------------------------Question_1------------------------------")

# # with open("C:/Users/Misha/Desktop/Python/Python_apna_college/Chapter_7/practice.txt", "w") as f:
# #     f.write("Hi everyone\nwe are learning File I/O\nusing Java\nI like programming in Java")
    
# # with open("C:/Users/Misha/Desktop/Python/Python_apna_college/Chapter_7/practice.txt", "r") as f:
# #     data = f.read()
# #     print(data)
    
# # print("--------------------------------Question_2--------------------------------")

# # with open("C:/Users/Misha/Desktop/Python/Python_apna_college/Chapter_7/practice.txt", "r") as f:
# #     data = f.read()
# #     print(data)
# # new_data = data.replace("Java", "Python")
# # print(new_data)  

# # with open("C:/Users/Misha/Desktop/Python/Python_apna_college/Chapter_7/practice.txt", "w") as f:
# #     f.write(new_data)

# # print("--------------------------------Question_3--------------------------------")

# # def check_for_word():
# #     with open("C:/Users/Misha/Desktop/Python/Python_apna_college/Chapter_7/practice.txt", "r") as f:
# #         data = f.read()
        
# #     if "learning" in data:
# #         print("Yes!! I found the word learning in data")
# #     else:
# #         print("Oops!! There is no work as leaning in data")
        
# # check_for_word()

# # print("--------------------------------Question_4--------------------------------")

# # def check_for_line():
# #     with open("C:/Users/Misha/Desktop/Python/Python_apna_college/Chapter_7/practice.txt", "r") as f:
# #         line_number = 1
# #         for line in f.readlines():
# #             if "learning" in line:
# #                 print("Yes!! I found the word learning in data")
# #                 print(f"The word is found in line number '{line_number}' and the line was '{line}'")
# #                 return
# #             line_number += 1
# #         print(-1)
# # check_for_line()

# print("--------------------------------Question_5--------------------------------")

# def check_for_even():
#     with open("C:/Users/Misha/Desktop/Python/Python_apna_college/Chapter_7/practice_1.txt", "r") as f:
#         data = f.read()
#         print(data)
        
#         # num = ""
#         # for i in range(len(data)):
#         #     if(data[i] == ","):
#         #         print(int(num))
#         #         num = ""
#         #     else:
#         #         num += data[i]
        
#         count = 0                
#         nums = data.split(",")
#         for value in nums:
#             if(int(value) % 2 == 0):
#                 count += 1
#     print(count)
# check_for_even()
                 