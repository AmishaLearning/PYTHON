# print(type("shirt"))
# print(dir("shirt"))
# print(id("shirt"))
# print(id("pants"))

# class Jeans:
#     def __init__(self, waist, length, color):
#         self.waist = waist
#         self.length = length
#         self.color = color
#         self.wearing = False
        
#     def put_on(self):
#         print(f"Putting on {self.waist}x{self.length} {self.color} jeans.")
#         self.wearing = True
    
#     def take_off(self):
#         print(f"Taking off {self.waist}x{self.length} {self.color} jeans.")
#         self.wearing = False

# my_jeans = Jeans(31, 32, "Blue")
# print(type(my_jeans))
# print(dir(my_jeans))

# my_jeans.put_on()
# print(my_jeans.wearing)
# my_jeans.take_off()
# print(my_jeans.wearing)

# class Shirt:
#     def __init__(self):
#         self.clean = True
#     def make_dirty(self):
#         self.clean = False
#     def make_clean(self):
#         self.clean = True
        
# red = Shirt()
# crimson = red
# print(id(red))
# print(id(crimson))

# print(red.clean)
# print(crimson.clean)

# red.make_dirty()
# print(red.clean)
# print(crimson.clean)
# print(red is crimson)

# crimson = Shirt()
# print(id(red))
# print(id(crimson))

# print(crimson.clean)
# print(red.clean)
# red.make_clean()
# print(red.clean)
# print(crimson.clean)

# MUTABLE AND NON-MUTABLE OBJECTS

# LISTS - Mutable

# closet = ['shirt', 'hat', 'pants', 'jacket', 'socks']
# print(closet)
# print(id(closet))
# closet.remove('hat')
# print(closet)
# print(id(closet))

# STRINGS - Immutable

# words = "Your're wearing that"
# print(id(words))
# words = words + " because you look great!"
# print(words)
# print(id(words))