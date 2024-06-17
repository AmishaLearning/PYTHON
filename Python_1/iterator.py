#Iterators

# nums=[5,6,3,4,9]

# # for i in nums:
# #     print(i)
    
# it =iter(nums)#converts list to iterator
# print(it.__next__())
# print(it.__next__())

# print(next(it))

#Creating Own Class

class TopTen:
    def __init__(self):
        self.num=1
        
    def __iter__(self):#Gives object of the method
        return self
    
    def __next__(self):#gives the next value 
        
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration#Only way to stop a for loop is raise 
    
values= TopTen()
# print(values.__next__())
# print(values.__next__())


for i in values:
    print(i)
