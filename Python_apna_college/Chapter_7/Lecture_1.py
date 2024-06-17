# print("--------------------------Reading a File------------------------")

# # If file is not in the same folder then we need to give the complete file path.

# f = open("C:/Users/Misha/Desktop/Python/Python_apna_college/Chapter_7/demo.txt", "r")
# # data = f.read()
# # print(data)
# # print(type(data))
# # f.close() 


# # data1 = f.read(5) # reads first 5 characters from the file
# # print(data1)
# # f.close()

# data2 = f.readlines()
# print(data2)
# f.close()

# print("------------------------------Writing a File ------------------------------")

# f = open("C:/Users/Misha/Desktop/Python/Python_apna_college/Chapter_7/demo.txt", "w")
# f.write("I want to learn Javascript Tomorrow....1234")
# f.close()

# f = open("C:/Users/Misha/Desktop/Python/Python_apna_college/Chapter_7/demo.txt", "a")
# f.write("\nThen I'll move to ReactJS")
# f.close()

# print("-------------------------r+ mode------------------------")

# f = open("C:/Users/Misha/Desktop/Python/Python_apna_college/chapter_7/sample.txt", "r+") # Overwrites text from the starting in the file..
# f.write("Lapinoz")
# print(f.read()) # the pointer will be at the position where lapinoz was written
# f.close()

# print("----------------------------w+----------------------------")

# f = open("C:/Users/Misha/Desktop/Python/Python_apna_college/Chapter_7/sample.txt", "w+")
# print(f.read()) # no data will be there as the file gets truncated with this command
# f.write("ABCDEFG")
# f.close()

# print("------------------------------a+--------------------------")

# f = open("C:/Users/Misha/Desktop/Python/Python_apna_college/Chapter_7/demo.txt", "a+")
# print(f.read()) # no data will be there as the pointer is at the end 
# f.write("Ishq Mitaye Haye Haye")
# f.close()

# print("--------------------------------with syntax--------------------------------")

# with open("C:/Users/Misha/Desktop/Python/Python_apna_college/Chapter_7/sample_1.txt", "r") as f:
#     data = f.read()
#     print(data)
#     # no need to close the file as with will automatically close the file for us
    
# with open("C:/Users/Misha/Desktop/Python/Python_apna_college/chapter_7/sample_1.txt", "w") as f:
#     f.write("These people deleted my previous data")
    
print("------------------------------Deleting a file------------------------------")

import os
os.remove("C:/Users/Misha/Desktop/Python/Python_apna_college/chapter_7/sample_1.txt")