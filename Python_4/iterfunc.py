# nums = [1, 2, 3, 4, 5, 6, 7]

# iterate = iter(nums)
# print(iterate.__next__())
# print(iterate.__next__())
# print(iterate.__next__())
# print(iterate.__next__()) 

# String = "Amisha Srivastava"

# iterate1 = iter(String)
# print(iterate1.__next__())
# print(iterate1.__next__())
# print(next(iterate1))

class Fantastic_Five:
    def __init__(self):
        self.num = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <= 5:
            Value = self.num
            self.num += 1
            return Value
            
        else:
            raise StopIteration
        
FF = Fantastic_Five()

for i in FF:
    print(i)