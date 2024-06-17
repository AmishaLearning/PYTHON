# 1
# Python Logical Operators: And, Or, Not:
# What is a Boolean?
# isRaining = True
# isSunny = False

# # Logical Operators -> Special Operators for Booleans

# # AND
# # true and true --> true
# # false and true --> false
# # true and false --> false
# # false and false --> false

# if isRaining and isSunny:
#     print("We might see a Rainbow")
# # OR
# # true and true --> true
# # false and true --> true
# # true and false --> true
# # false and false --> false

# if isRaining or isSunny:
#     print("It might be rainy or it might be sunny")
# # NOT
# # true --> false
# # false --> true

# if not isRaining:
#     print("It must be raining")

# ages = [12, 18, 39, 87, 7, 2]
# for age in ages:
#     isAdult = age > 17
#     if not isAdult:
#         print(f"Being {age} does not make you an adult")
#     else:
#         print(f"Being {age} makes you an adult")

# 2
# Python Comparison Operators
# TIPS:
# == --> is equal to
# <= --> is less than or equal to
# >= --> is greater than or equal to
# < --> is less than
# > --> is greater than

# < --> is less than
# print(10 < 75)
# print(75 < 10)

# if 10 < 75:
#     print("The bigger number is bigger")

# # == --> is equal to
# kitten = 10
# tiger = 75

# if kitten < tiger:
#     print("The kitten weighs less than the tiger")

# # < --> is less than
# mouse = 1
# if mouse < kitten and mouse < tiger:
#     print("The mouse weighs the least")

# #False --> 0
# #True --> 1
# # > --> is greater than
# print(False > True)

# # Looking for first mismatched letter
# # A - Z --> 1 - 26
# # > --> is greater than
# print("Jennifer" > "Jenny")

# # A - Z --> 1 - 26
# # <= --> is less than or equal to
# print('a' <= 'b')

# 3

# Calculating Length
# len() --> returns length

# firstName = "Taylor"
# print(len(firstName))
# lastName = "Swift"
# print(len(lastName))
# firstName.__len__()

# ages = [0, 11, 43, 12, 10]
# print(len(ages))
# i = 0
# for i in range(0, len(ages)):
#     print(ages[i])

# print(len(["bob", "mary", "sam"]))

# candyCollection = {"bob" : 10, "mary" : 7, "sam" : 18}
# print(len(candyCollection))

# 4 
# Range -> range instance that holds all nums counting by one between 0 and first input
# List -> lists numbers from the inputted tuple

# numberedContestants = range(30)

# print(list(numberedContestants))

# for c in list(numberedContestants):
#     print("Contestant " + str(c) + " is here")

# luckyWinners = range(7, 30, 5)

# print(list(luckyWinners))

# 5
# Minimum and Maximum
# playerOneScore = 10
# playerTwoScore = 4
# print(min(playerOneScore, playerTwoScore))
# print(min(0, 12, -19))

# print(min("Kathryn", "Katie"))# kathryn is the o/p cz h comes before i
# print(min("Angela", "Bob"))

# print(max(playerOneScore, playerTwoScore))
# playerThreeScore = 14
# print(max(playerThreeScore, playerTwoScore, playerOneScore))
# print(max("Kathryn", "Katie"))

# 6
# Python Rounding, Absolute Value, and Exponents

# round()
# myGPA = 3.6
# print(round(myGPA))
# amountOfSalt = 1.4
# print(round(amountOfSalt))

# apple = -1.2
# print(round(apple))
# google = -1.6
# print(round(google))

# # abs()
# distanceAway = -13
# print(abs(distanceAway))
# lengthOfRootInGround = -2.5
# print(abs(lengthOfRootInGround))

# # pow()
# chanceOfTails = 0.5
# inARowTails = 3
# print(pow(chanceOfTails, inARowTails))

# chanceOfOne = .167
# inARowOne = 2
# print(pow(chanceOfOne, inARowOne))

# 7
 # Least to Greatest
# pointsInaGame = [0, -10, 15, -2, 1, 12]
# sortedGame = sorted(pointsInaGame)
# print(sortedGame)

# # Alphabetically
# children = ["Sue", "Jerry", "Linda"]
# print(sorted(children))
# print(sorted(["Sue", "jerry", "linda"]))

# # Key Parameters
# print(sorted("My favorite child is Linda".split(), key=str.upper))
# print(sorted(pointsInaGame, reverse=True))

# leaderBoard = {231: "CKL", 123:"ABC", 432:"JKC"}
# print(sorted(leaderBoard, reverse=True))
# print(leaderBoard.get(432))
# print(leaderBoard[432])

# students = [ ('alice', 'B', 12), ('eliza', 'A', 16), ('tae', 'C', 15)]
# print(sorted(students, key=lambda student:student[0]))# sorting on the basis of name
# print(sorted(students, key=lambda student:student[1]))# sorting on the basis of grade
# print(sorted(students, key=lambda student:student[2]))# sorting on the basis of age

# 8
# r = range(0, 30)
# print(type(r))
# print(type(10))
# print(type('a'))
# print(type("Hi there"))

# class Car:
#     pass

# class Truck(Car):
#     pass
# # type doesn't consider inheritance
# c = Car()
# convert = Car()
# t = Truck()
# print(type(c))
# print(type(t))
# print(type(c) == type(t))
# print(type(c) == type(convert))

# print(isinstance(c, Car))
# print(isinstance(t, Car))# isinstance accounts for inheritance

# if isinstance(r, range):
#     print(list(r))

# 9
# Math Module Part I
# import math

# # Constants
# print(math.pi)
# print(math.e)

# print(math.nan)# nan : not a number
# print(math.inf)
# print(-math.inf)

# # Trigonometry
# obst_direction = math.cos(math.pi / 4)
# print(obst_direction)
# print(math.sin(math.pi / 4))

# # Ceiling and Floor
# cookies = 10.3
# candy = 7
# print(math.ceil(cookies))
# print(math.ceil(candy))

# age = 47.9
# otherAge = 47
# print(math.floor(age))
# print(math.floor(otherAge))

# 10
# Math Module Part 2
# import math

# # Factorial & Square Root
# print(math.factorial(3))
# print(math.sqrt(64))

# # Greatest Common Denominator GCD
# print(math.gcd(52, 8))
# print(math.gcd(8, 52))

# print(8/52)
# print(2/13)

# # Degrees and Radians
# print(math.radians(360))
# print(math.pi * 2)
# print(math.degrees(math.pi * 2))

# 11
# Random Module
# import random

# # Random Numbers
# print(random.random())
# decider = random.randrange(2)
# if decider == 0:
#     print("HEADS")
# else:
#     print("TAILS")
# print(decider)

# print("You rolled a " + str(random.randrange(1, 7)))

# # Random Choices
# lotteryWinners = random.sample(range(100), 5)
# print(lotteryWinners)

# possiblePets = ["cat", "dog", "fish"]
# print(random.choice(possiblePets))

# cards = ["Jack", "Queen", "King", "Ace"]
# random.shuffle(cards)
# print(cards)

# 12
# Statistics Module
# import statistics
# import math

# agesData = [10, 13, 14, 12, 11, 10, 11, 10, 15]

# print(statistics.mean(agesData))
# print(statistics.mode(agesData))
# print(statistics.median(agesData))
# print(sorted(agesData))

# print(statistics.variance(agesData))# average of the squared difference from the mean
# print(statistics.stdev(agesData))# sqrt of variance
# print(math.sqrt(statistics.variance(agesData)))

# 13
