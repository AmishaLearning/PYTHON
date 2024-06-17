#BINARY SEARCH
#All values should be sorted

pos =-1

def search(list1,n):
    l=0
    u=len(list1)-1
        
    while l<=u:
        mid=(l+u)//2#integer divisoion
        if list1[mid]==n:
            globals()['pos']=mid   
            return True
        else:
            if list1[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
list1=[4,7,8,12,45,99,102,702,10987,56666]
n=10
if search(list1,n):
    print("Found at ",pos+1)
else:
    print("Not Found") 