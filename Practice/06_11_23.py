# class something:
#     def __init__(self, name, number):
#         self.name = name
#         self.number = number
        
#     def details(self):
#         #pass
#         print(f"My name is {self.name} and my number is {self.number}. ")
#         pass        
# # If some content is there in the function then there is no meaning of pass
# obj = something("Amisha", 9876543210)
# obj.details()        

# __str__

class MyClass:
    def __init__(self, value):
        self.value = value

    # def details(self):
    #     return f"MyClass instance with value: {self.value}"
    
    def __str__(self):
        return f"MyClass instance with value: {self.value}"    

obj = MyClass(42)
print(obj)  # This will call the __str__ method and print the custom string representation.
# print(obj.details())
