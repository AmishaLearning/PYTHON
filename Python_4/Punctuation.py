punc = '''!()-@[]{};:'".\,<>/?#%^$*_~'''
string = input("Enter a string : ")

empty_string = ""

for i in string:
    if i not in punc:
        empty_string = empty_string + i
    
print(empty_string)
        

        