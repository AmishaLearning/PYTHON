#GENERATORS

def topten():
    
    yield 1#This will make the function as a generator
    yield 2
    yield 3
    yield 4 
    yield 5

values=topten()
print(values.__next__())
print(values.__next__())

for i in values:
    print(i)

#Perfect Square

# def sqr():
#     n=1
#     while n<=10:
#         sq=n*n
#         yield sq
#         n += 1
        
# values1=sqr()
# for i in values1:
#     print(i)