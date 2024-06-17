# #Polymorphism--one thing can take multiple forms
# #Poly-- Many, Morph--form
# #ways of implementing polymorphism
# #1- Duck Typing
# #2- Operator Overloading
# #3- Method Overloading
# #4- Method Overriding

# #Duck Typing

# class pycharm:
#     def execute(self):
#         print("Compiling")
#         print("Running")
        
# class Myeditor:
#     def execute(self):
#         print("Spell Check")
#         print("Convention Check")
#         print("Compiling")
#         print("Running")     

# class laptop:
#     def code(self,ide):
#         ide.execute()
        
# # ide= pycharm()
# # lap1=laptop()
# # lap1.code(ide)

# ide= Myeditor()
# lap1=laptop()
# lap1.code(ide)


class Bird:

    def intro(self):
        print("There are many types of birds.")
        print("From class Bird")        

    def flight(self):
        print("Most of the birds can fly but some cannot.")
        print("From class Bird")

class sparrow(Bird):

    def flight(self):
        print("Sparrows can fly.")
        print("From class Sparrow")

class ostrich(Bird):

    def flight(self):
        print("Ostriches cannot fly.")
        print("From class Ostrich")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()
print("-------------------------------------")
obj_spr.intro()
obj_spr.flight()
print("-------------------------------------")
obj_ost.intro()
obj_ost.flight()
