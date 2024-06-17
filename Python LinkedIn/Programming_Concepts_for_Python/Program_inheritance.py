# INHERITANCE

# class Vehicle:
#     def __init__(self, color, manufacturer):
#         self.color = color
#         self.manufacturer = manufacturer
#         self.gas = 4
        
#     def drive(self):
#         if self.gas > 0:
#             self.gas -= 1
#             print(f"The {self.color} {self.manufacturer} goes VROOOM!!!")
#         else:
#             print(f"The {self.color} {self.manufacturer} sputters out of gas...")
            
# class Car(Vehicle):
#     def radio(self):
#         print("Rocking Tunes!")
        
#     def window(self):
#         print("Ahh...Fresh Air")
        
# class Motorcycle(Vehicle):
#     def helmet(self):
#         print("Helmet on - nice and safe!")
        
# my_car = Car('red', 'Mercedes')
# my_mc = Motorcycle('silver', 'Harley')
# my_car.drive()
# my_mc.drive()
# my_car.radio()
# my_car.window()
# my_mc.helmet()
# my_mc.window()

# OVERRIDDING

class Vehicle:
    def __init__(self, color, manufacturer):
        self.color = color
        self.manufacturer = manufacturer
        self.gas = 4
        
    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print(f"The {self.color} {self.manufacturer} goes VROOOM!!!")
        else:
            print(f"The {self.color} {self.manufacturer} sputters out of gas...")
            
class Car(Vehicle):
    def radio(self):
        print("Rocking Tunes!")
        
    def window(self):
        print("Ahh...Fresh Air")
        
class Motorcycle(Vehicle):
    def helmet(self):
        print("Helmet on - nice and safe!")
        
class ElectricCar(Car):
    def drive(self):
        print(f"The {self.color} {self.manufacturer} goes SSHHH!!!")
        
my_ecar = ElectricCar('White', 'Nissan')
my_ecar.window()
my_ecar.radio()
my_ecar.drive()
print(my_ecar.gas)
