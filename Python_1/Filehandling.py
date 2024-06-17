#File Handling

#Reading data
# f= open('Mydata.txt','r')
# print(f.readline(), end="")
# print(f.readline())#there is sapce in output because print itself gives us result in new line and in the data also there is start of new line

#Writing Data
# f= open('Mydata.txt','r')
# # f1=open('abc','w')#If no such file is there it will create the file on it's own
# f1=open('abc','a')#Used for adding values in the file
# f1.write(" Something")

# #Copy everthing from Mydata and paste to abd

# for data in f:
#    f1.write(data) 
   
   
#priting data of an image
#Read image file in binary format
f=open('Amisha_Photo.jpg','rb')#rb means read binary
f1=open('Mypic.jpg','wb')

for i in f:
    f1.write(i)
