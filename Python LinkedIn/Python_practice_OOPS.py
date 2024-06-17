# Class and Class Objects

# class Cake:
#     def __init__(self, kind, price, slices):
#         self.kind = kind
#         self.price = price
#         self.slices = slices
        
#     def describe(self):
#         return f"The {self.kind} cake costs ${self.price} and is divided into {self.slices} slices."
    
# spice_cake = Cake("spice", 18, 8)
# chocolate_cake = Cake("chocolate", 24, 6)

# print(spice_cake.describe())
# print(chocolate_cake.describe())

# ADD METHOD TO CLASS

# class Cake:
#     def __init__(self, kind, price, slices):
#         self.kind = kind
#         self.price = price
#         self.slices = slices
          
        
#     def describe(self):
#         return f"The {self.kind} cake costs ${self.price} and is divided into {self.slices} slices."
    
#     def sell(self, count):
#         if count <= 0:
#             return f"Cannot sell zero or negative slices!"
#         elif count > self.slices:
#             return f"Cannot sell more slices than we have ({self.slices})!"
#         else:
#             remaining_slices = self.slices - count
#             self.slices = remaining_slices  
#             return f"This cake has {remaining_slices} slices remaining."
    
# spice_cake = Cake("spice", 18, 8)
# chocolate_cake = Cake("chocolate", 24, 6)

# # print(spice_cake.describe())
# # print(chocolate_cake.describe())
# # print(spice_cake.sell(6))
# # print(spice_cake.sell(4))

# print(spice_cake.sell(5))
# print(spice_cake.sell(4))
# print(chocolate_cake.sell(-1))
# print(chocolate_cake.sell(0))

# Refactor a Class

class item:
    def __init__(self, item_type, price):
        self.item_type = item_type
        self._price = price

class Cake(item):
    def __init__(self, kind, price, slices):
        super().__init__("cake", price)
        self.kind = kind
        self._price = price
        self.slices = slices
        
spice_cake = Cake("spice", 11.45, 8)
chocolate_cake = Cake("Chocolate", 12.67, 6)

