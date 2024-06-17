# Pass List in a Function

def count(lst):
    even=0
    odd=0
    
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even, odd
        
lst=[20,25,14,16,19,24,28,47,26]

even,odd=count(lst)
# print(even)
# print(odd)

print("Even : {} and Odd : {}".format(even,odd))

def name(names):
    a=0
    b=0
    for i in names:
        if len(i)>=5:
            a+=1
        else:
            b+=1
    return a,b
            
names=['qwerty','uiop','asdf','ghjkl','zxcvb','vbnm','qazxs','qwasdf','zxcvsdfg','tyhjlknm']
a,b=name(names)
print("Length grater than 5 :{} and length less than 5 : {}".format(a,b))