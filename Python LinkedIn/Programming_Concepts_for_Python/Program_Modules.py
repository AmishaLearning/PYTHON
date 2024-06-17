# MODULES : Refers to a single python script which contains a handfull of functions and classes related to same task

# import random
# print(random.randint(1, 20))
# # If we have specified the entire module we have to specify random everytime we are using the randit function
# from random import randint
# print(randint(1, 20))
# print(random.random())

# from random import random
# print(random())

# import random as rand
# print(rand.randint(1, 20))

# PACKAGES : A collection of several modules which are also related to same type of task

import urllib.request
print(urllib.request.urlopen("http://www.google.com"))
print(urllib.__path__)
