x = 5

def random():
    global x
    x = 10
    print(f"This is Local value inside function = {x}")
    
print(f"This is Global before setting global in function = {x}")
random()
print(f"Global value after setting global in function = {x}")