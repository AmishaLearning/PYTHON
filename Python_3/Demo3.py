class A:
    def __init__(self,private,protected):
        self.__private = private
        self._protected = protected
        
obj_A = A(10,20)

# print(obj_A.__private)
print(obj_A._A__private)