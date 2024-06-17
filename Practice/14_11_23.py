# # initializing dictionary
# test_dict = {"Geeks": 1, "for": 2, "geeks": 3}
 
# # Printing dictionary
# print("Original dictionary is : " + str(test_dict))
 
# # using in operator to
# # get key and value
# print("Dict key-value are : ")
# for i in test_dict:
#     print(i, test_dict[i])

# code for testing decorator chaining 
def decor1(func):
    print("I am from decor1") 
    def inner(): 
        print("I am from decor 1 inner")
        x = func() 
        return x * x 
    return inner

def decor(func): 
    print("I am from decor")
    def inner(): 
        print("I am from decor inner")
        x = func() 
        return 2 * x 
    return inner


@decor1
@decor
def num(): 
    print("I am from num")
    return 10

@decor
@decor1
def num2():
    print("I am from num2")
    return 10

print(num()) 
print(num2())
