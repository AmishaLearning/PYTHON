# #Python Strings
# print("Hello")
# print('Hello People')
# a="Hello World"
# print(a)

# b="""The date today is 20 April 2023,
# the time now is 00:51 am"""
# print(b)

# c="Hello, World!"
# print(c[1])

# for x in "banana":
#     print(x)

# print(len(c))

# txt="The Best things in life are free!"
# print("free" in txt)

# if "free" in txt:
#     print("Yes! 'Free' is present in the text.")

# print("Amisha" not in txt)

# if "Amisha" not in txt:
#     print("No 'Amisha' is not there in the text")
    
# #Slicing Strings
# d="Hello , World!"
# print(d[1:5])

# #Slice from start
# print(d[:5])

# #Slice to the End
# print(d[2:])

# #Negative Indexing
# print(d[-5:-2])

#Modify Strings
e=" Amisha, Srivastava"
# print(e.upper())
# print(e.lower())

# #Remove whitesapce
# print(e.strip())

# #Replace String
# print(e.replace("A","M"))

#Split String
print(e.split(","))


# #Concatenate Strings
# f="Hello"
# g="World"
# print(f+g)
# print(f+" "+g)

# #Format Strings
# age=36
# txt="My name is John, I am {}"
# print(txt.format(age))

# #Format() method can be used unlimited times 
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))

# myorder1= "I want {2} pieces of item {0} for {1} dollars."
# print(myorder1.format(quantity, itemno, price))

# #Escape Characters
# txt1= "We are the so-called \"Vikings\" from the North"
# print(txt1)

# #Single Quote
# txt3='It\'s Me'
# print(txt3)

# #Backslash
# txt4="This will insert one \\(backslash)."
# print(txt4)

# #New Line
# txt5="Hello\nWorld"
# print(txt5)

# #Carriage Return
# txt6="Hello\rWorld!"
# print(txt6)

# #Tab 
# txt7="Hello\tWorld"
# print(txt7)

# #Backspace
# txt8="Hello \bWorld"
# print(txt8)

# #Form Feed
# txt9="Hello \fWorld"
# print(txt9)

# #Octal Value
# txt10="\110\145\154\154\157"
# print(txt10)

# #Hexa VAlue
# txt11= "\x48\x65\x6c\x6c\x6f"
# print(txt11)