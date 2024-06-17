# Functions 

# def make_omelette():
#     print("Mixing the Ingredients")
#     print("Pouring the mixture")
#     print("Cooking the first side")
#     print("Flipping it")
#     print("Cooking the other side\n")
#     omelette = "A Tasty Omelette!!"
#     return omelette

# barron_breakfast = make_omelette()
# olivia_breakfast = make_omelette()
# print(f"Barron is having {barron_breakfast}\n")
# print(f"Olivia is having {olivia_breakfast}\n")

# def make_omelette():
#     print("Mixing the Ingredients")
#     print("Pouring the mixture")
#     print("Cooking the first side")
#     print("Flipping it")
#     print("Cooking the other side\n")
#     omelette = "A Tasty Omelette!!"
#     return omelette

# def make_pancake():
#     print("Mixing the Ingredients")
#     print("Pouring the mixture")
#     print("Cooking the first side")
#     print("Flipping it")
#     print("Cooking the other side\n")
#     pancake = "A Delicious Pancake!!"
#     return pancake
    
# barron_breakfast = make_omelette()
# olivia_breakfast = make_pancake()
# print(f"Barron is having {barron_breakfast}\n")
# print(f"Olivia is having {olivia_breakfast}\n")

# def mix_and_cook():
#     print("Mixing the Ingredients")
#     print("Greasing the Fry pan")
#     print("Pouring the mixture")
#     print("Cooking the first side")
#     print("Flipping it")
#     print("Cooking the other side\n")
    
# def make_omelette():
#     mix_and_cook()
#     omelette = "A Tasty Omelette!"
#     return omelette

# def make_pancake():  
#     mix_and_cook()
#     pancake = "A Delicious Pancake!!" 
#     return pancake

# # make breakfast for two
# barron_breakfast = make_omelette()
# olivia_breakfast = make_pancake()
# print(f"Barron is having {barron_breakfast}\n")
# print(f"Olivia is having {olivia_breakfast}\n")

# Modifying Functions

# def mix_and_cook():
#     print("Mixing the Ingredients")
#     print("Greasing the Fry pan")
#     print("Pouring the mixture")
#     print("Cooking the first side")
#     print("Flipping it")
#     print("Cooking the other side\n")
    
# def make_omelette(ingredient):# Ingredient is a parameter: a variable name that we use inside a function to access the value which is passed as an argument.
#     mix_and_cook()
#     omelette = f"A {ingredient} Omelette!"
#     return omelette

# def make_pancake():  
#     mix_and_cook()
#     pancake = "A Delicious Pancake!!" 
#     return pancake

# # make breakfast for two
# barron_breakfast = make_omelette("Bacon") # Ingredient is an argument: when passed as an input value.
# olivia_breakfast = make_omelette("Spam")
# print(f"Barron is having {barron_breakfast}\n")
# print(f"Olivia is having {olivia_breakfast}\n")

# Modifying functions with more than one input

# def mix_and_cook():
#     print("Mixing the Ingredients")
#     print("Greasing the Fry pan")
#     print("Pouring the mixture")
#     print("Cooking the first side")
#     print("Flipping it")
#     print("Cooking the other side\n")
    
# def make_omelette(ingredient):# Ingredient is a parameter: a variable name that we use inside a function to access the value which is passed as an argument.
#     mix_and_cook()
#     omelette = f"A {ingredient} Omelette!"
#     return omelette

# # Function that has ability to add any number of ingredients
# def make_fancy_omelette(*ingredients):# * tells python to accept any number of arguments. All the inputs are combined as a TUPLE
#     mix_and_cook()
#     omelette = f"A Fancy omelette with {len(ingredients)} ingredients!"
#     return omelette        

# def make_pancake():  
#     mix_and_cook()
#     pancake = "A Delicious Pancake!!" 
#     return pancake

# # make breakfast for two
# barron_breakfast = make_omelette("Bacon") # Ingredient is an argument: when passed as an input value."
# olivia_breakfast = make_fancy_omelette("Sausage", "Onion", "Pepper", "Spinach", "Mushroom", "Tomato", "Goat Cheese")
# print(f"Barron is having {barron_breakfast}\n")
# print(f"Olivia is having {olivia_breakfast}\n")

# Local and Global Variable

# def mix_and_cook():
#     print("Mixing the Ingredients")
#     print("Greasing the Fry pan")
#     print("Pouring the mixture")
#     print("Cooking the first side")
#     print("Flipping it")
#     print("Cooking the other side\n")
    
# def make_omelette(ingredient):# Ingredient is a parameter: a variable name that we use inside a function to access the value which is passed as an argument.
#     mix_and_cook()
#     omelette = f"A {ingredient} Omelette!"
#     return omelette

# def make_pancake():  
#     mix_and_cook()
#     pancake = f"A Delicious {ingredient} Pancake!!" 
#     return pancake

# # make breakfast for two
# barron_breakfast = make_omelette("Bacon") # Ingredient is an argument: when passed as an input value.
# print(ingredient)# only exists inside the make_omelette function
# olivia_breakfast = make_pancake("Spam")
# print(f"Barron is having {barron_breakfast}\n")
# print(f"Olivia is having {olivia_breakfast}\n")

# GLobal SCOPE

# cheese = "Cheddar"

# def mix_and_cook():
#     print("Mixing the Ingredients")
#     print("Greasing the Fry pan")
#     print("Pouring the mixture")
#     print("Cooking the first side")
#     print("Flipping it")
#     print("Cooking the other side\n")
    
# def make_omelette():# Ingredient is a parameter: a variable name that we use inside a function to access the value which is passed as an argument.
#     mix_and_cook()
#     omelette = f"A {cheese} Omelette!"
#     return omelette

# def make_pancake():  
#     mix_and_cook()
#     pancake = f"A Delicious {cheese} Pancake!!" 
#     return pancake

# # make breakfast for two
# barron_breakfast = make_omelette() # Ingredient is an argument: when passed as an input value.
# olivia_breakfast = make_pancake()
# print(f"Barron is having {barron_breakfast}\n")
# print(f"Olivia is having {olivia_breakfast}\n")

# SAME NAME FOR LOCAL AND GLOBAL SCOPE

# cheese = "Cheddar"

# def mix_and_cook():
#     print("Mixing the Ingredients")
#     print("Greasing the Fry pan")
#     print("Pouring the mixture")
#     print("Cooking the first side")
#     print("Flipping it")
#     print("Cooking the other side\n")
    
# def make_omelette():
#     cheese = "Swiss"
#     mix_and_cook()
#     omelette = f"A {cheese} Omelette!"# Searches the value of cheese locally first
#     return omelette

# def make_pancake():  
#     mix_and_cook()
#     pancake = f"A Delicious {cheese} Pancake!!" 
#     return pancake

# print(f"***The Global cheese is {cheese}***")
# barron_breakfast = make_omelette() 
# print(f"***The Global cheese is {cheese}***")
# olivia_breakfast = make_pancake()
# print(f"***The Global cheese is {cheese}***")

# print(f"Barron is having {barron_breakfast}\n")
# print(f"Olivia is having {olivia_breakfast}\n")

# IF WE REALLY WANT THE LOCAL VALUE TO BE PRINTED THEN FOLLOW THE STEPS

# cheese = "Cheddar"

# def mix_and_cook():
#     print("Mixing the Ingredients")
#     print("Greasing the Fry pan")
#     print("Pouring the mixture")
#     print("Cooking the first side")
#     print("Flipping it")
#     print("Cooking the other side\n")
    
# def make_omelette():
#     global cheese
#     cheese = "Swiss"
#     mix_and_cook()
#     omelette = f"A {cheese} Omelette!"# Searches the value of cheese locally first
#     return omelette

# def make_pancake():  
#     mix_and_cook()
#     pancake = f"A Delicious {cheese} Pancake!!" 
#     return pancake

# print(f"***The Global cheese is {cheese}***")
# barron_breakfast = make_omelette() 
# print(f"***The Global cheese is {cheese}***")
# olivia_breakfast = make_pancake()
# print(f"***The Global cheese is {cheese}***")

# print(f"Barron is having {barron_breakfast}\n")
# print(f"Olivia is having {olivia_breakfast}\n")

# swapping the order of the function being called
# cheese = "Cheddar"

# def mix_and_cook():
#     print("Mixing the Ingredients")
#     print("Greasing the Fry pan")
#     print("Pouring the mixture")
#     print("Cooking the first side")
#     print("Flipping it")
#     print("Cooking the other side\n")
    
# def make_omelette():
#     global cheese
#     cheese = "Swiss"
#     mix_and_cook()
#     omelette = f"A {cheese} Omelette!"# Searches the value of cheese locally first
#     return omelette

# def make_pancake():  
#     mix_and_cook()
#     pancake = f"A Delicious {cheese} Pancake!!" 
#     return pancake

# print(f"***The Global cheese is {cheese}***")
# barron_breakfast = make_pancake() 
# print(f"***The Global cheese is {cheese}***")
# olivia_breakfast = make_omelette()
# print(f"***The Global cheese is {cheese}***")

# print(f"Barron is having {barron_breakfast}\n")
# print(f"Olivia is having {olivia_breakfast}\n")


