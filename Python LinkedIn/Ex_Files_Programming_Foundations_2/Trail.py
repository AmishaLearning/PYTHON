# LIST
# city1 = "Tokyo"
# city2 = "Dakar"
# city3 = "Mumbai"
# city4 = "Buenos Aires"

# cities = [
#     "Tokyo",
#     "Dakar",
#     "Mumbai",
#     "Buenos Aires",
# ]

# print(cities[0])

# DICTIONARY

# California state symbols
# state_bird = 'California quail'
# state_animal = 'Grizzly bear'
# state_flower = 'California poppy'
# state_fruit = 'Avocado'

# california_symbols = {
#     'bird'   : "California quail",
#     'animal' : 'Grizzly bear',
#     'flower' : 'California poppy',
#     'fruit'  : 'Avocado'
# }

# print(california_symbols['bird'])

# Challenge Collections

# Nearest stars to Earth
# star1 = 'Sol'
# star2 = 'Alpha Centauri'
# star3 = 'Barnard'
# star4 = 'Wolf 359'

# # Highest peak on each tectonic plate
# African = 'Kilimanjaro'
# Antarctic = 'Vinson'
# Australian = 'Puncak Jaya'
# Eurasian = 'Everest'
# North_American = 'Denali'
# Pacific = 'Mauna Kea'
# South_American = 'Aconcagua'

# stars = ['Sol', 'Alpha Centauri', 'Barnard', 'Wolf 359']
# print(stars[3])

# peaks = {
#     'African'        : 'Kilimanjaro',
#     'Antarctic'      : 'Vinson',
#     'Australian'     : 'Puncak Jaya',
#     'Eurasian'       : 'Everest',
#     'North_American' : 'Denali',
#     'Pacific'        : 'Mauna Kea',
#     'South_American' : 'Aconcagua' 
# }

# print(peaks['Pacific'])

# LOOP

# spices = ['salt', 'pepper', 'cumin', 'turmeric']

# for spice in spices:
#     print(spice)
# print("No more boring omlettes!!")

# While

# i = 5
# print("Counting to 100 by fives : ")
# while i <= 100:
#     print(i)
#     i += 5
# print("List Complete!!")

# Challenege Loop

# fruits = ['apples', 'bananas', 'dragon fruit', 'mangos', 'nectarines',
#     'pears']

# print("Our Fruit Selection : ")

# for fruit in fruits:
#     print(fruit)
    
# import testmoduletrail

# testmoduletrail.mul(10, 5)

# Strings

# value = input("Enter a number : ")
# print(value + " is my favourite number")
# print("When you multiply it by 10, this is what you get : ")

# value_int = int(value)
# print(value_int * 10)

# String Methods

# first_name = 'malala'
# last_name = 'yousafzai'
# note = 'award : Nobel Peace Prize'

# first_name_cap = first_name.capitalize()
# last_name_cap = last_name.capitalize()

# print(first_name_cap)
# print(last_name_cap)

# # Finding Text

# award_location = note.find('award : ') # find method return the location of start of the text
# print(award_location)

# award_text = note[7:]
# print(award_text)

# Regex

# import re

# five_digit_zip = '98101'
# nine_digit_zip = '98101-0003'
# phone_number = '234-567-8901'

# five_digit_expression = r'\d{5}' # 5 occurences of digit
# print(re.search(five_digit_expression, five_digit_zip))
# print(re.search(five_digit_expression, nine_digit_zip))
# print(re.search(five_digit_expression, phone_number))

# Challenge Strings

# miles = input("Enter a distance in miles : ")
# kilometers_value = float(miles) * 1.609344

# print(f"Miles value {miles} in kilometers is {kilometers_value}")

# Input / output with files

# infile = open('valuestrail.txt', 'rt')
# outfile = open('values-totaled.txt', 'wt')
# print('Processing Input')

# sum = 0
# for line in infile:
#     sum += int(line)
#     print(line.rstrip(), file = outfile)
# print('\nTotal: ' + str(sum), file = outfile)
# outfile.close()
# print('Output Complete')

# Challenge Debugging

# Find error 

# def plant_recommendation(care):
#     if care = 'low':
#         print('aloe')
#     elif care == 'medium':
#         print('pothos')
#     elif care == 'medium':
#         print('orchid')

# plant_rec('low')
# plant_recommendation('medium')
# plant_recommendation('high')

# def plant_recommendation(care):
#     if care == 'low':
#         print('aloe')
#     elif care == 'medium':
#         print('pothos')
#     elif care == 'high':
#         print('orchid')

# plant_recommendation('low')
# plant_recommendation('medium')
# plant_recommendation('high')

# OOP

# flips = ['heads', 'tails', 'tails', 'heads', 'tails']

# print(flips.count('heads'))
# print(flips.pop())

# CLASS

# class Attendee:
#     'Common base class for all attendees'

#     def __init__(self, name, tickets):
#         self.name = name
#         self.tickets = tickets

#     def displayAttendee(self):
#         print('Name : {}, Tickets: {}'.format(self.name, self.tickets))

#     def addTicket(self):
#         self.tickets += 1
#         print('{} tickets increased to {}'.format(self.name, self.tickets))

# Attendee1 = Attendee('B.Giles', 2)
# Attendee2 = Attendee('J. Ortega', 1)

# Attendee2.addTicket()
# Attendee2.addTicket()

# Attendee1.displayAttendee()
# Attendee2.displayAttendee()

