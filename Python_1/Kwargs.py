# Keyworded Variable Length Arguments

def person(name,*data):
    print(name)
    print(data) 

person('Rose', 24,'Bangalore',9876543210)

def person(name,**data):#** menas we are passing multiple arguments but with the help of keywords
    print(name)
    for i,j in data.items():
        print(i,j) 

person('Rose', age=24,city='Bangalore',mob=9876543210)