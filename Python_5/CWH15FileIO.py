
# If the file doesn't exist then write mode will create a file
# f = open('C:/Users/Misha/Desktop/Python/Python_2/Python_3/Python_4/Python_5/myfile2', 'w')
# print(f)

# text = f.read()
# print(text)
# f.close()

# f = open('C:/Users/Misha/Desktop/Python/Python_2/Python_3/Python_4/Python_5/myfile', 'rb')
# print(f)

# # data_to_append = "Heyy!! Same here nice to see you"
# # f.write(data_to_append)

# text = f.read()
# print(text)
# f.close()

# with open('C:/Users/Misha/Desktop/Python/Python_2/Python_3/Python_4/Python_5/myfile','a') as f:
#     f.write("Hey I am inside with")

#Readline method
#Reading text line by line


# f = open('C:/Users/Misha/Desktop/Python/Python_2/Python_3/Python_4/Python_5/myfile','r')
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         print(line, type(line))
#         break
    
  
# f = open('C:/Users/Misha/Desktop/Python/Python_2/Python_3/Python_4/Python_5/myfile2','r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Marks of Student {i} in Maths is : {m1}")
#     print(f"Marks of Student {i} in Science is : {m2}")
#     print(f"Marks of Student {i} in SST is : {m3}")
    
    
#Writelines()
# f = open('C:/Users/Misha/Desktop/Python/Python_2/Python_3/Python_4/Python_5/myfile2','a')
# lines = ['line 1\n','line 2\n','line 3\n']
# f.writelines(lines)
# f.close()

# f = open('C:/Users/Misha/Desktop/Python/Python_2/Python_3/Python_4/Python_5/myfile2','r')
# # lines = ['line 1\n','line 2\n','line 3\n']
# text = f.read()
# print(text)
# f.close()

#Seek and tell functions are used to work with file objects and their position within.
#Seek func allows to move the current position toa specific point
#Tell func returns the current position within the file, in bytes

# with open('C:/Users/Misha/Desktop/Python/Python_2/Python_3/Python_4/Python_5/myfile3', 'r') as f:
#     print(type(f))
#     #Move to the 10th byte in the file
#     f.seek(10)
#     #Read the next 5 bytes
#     print(f.tell())
#     data = f.read(5)
#     print(data)

#Truncate(): 
with open('C:/Users/Misha/Desktop/Python/Python_2/Python_3/Python_4/Python_5/myfile4','w') as f:
    f.write("Hello World!")
    # f.truncate(5)
with open('C:/Users/Misha/Desktop/Python/Python_2/Python_3/Python_4/Python_5/myfile4', 'r') as f:
    print(f.read())