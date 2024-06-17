#LINEAR SEARCH

pos =-1

def search(list1,n):
    i=0
    
    while i<len(list1):
        if list1[i]==n:
            globals()['pos']=i   
            return True
        i=i+1
    
    return False
list1=[5,8,4,6,9,2]
n=9
if search(list1,n):
    print("Found at ",pos+1)
else:
    print("Not Found") 

