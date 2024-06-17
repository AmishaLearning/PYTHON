# import this

# RUN_INDENTED = True

# message = "running unindented"

# if RUN_INDENTED:
#     message = "running indented"  
# print(message)

# def my_function():
#     greet = "Hello"
#     return greet

# print(my_function())

# STRINGS

# greet = "Hello World"
# extended_greet = "Hello World, " + "this is a long string"

# name = "John"
# intruption = f"Hello {name}"

# greet_formal = "Hello {}"
# formatted = greet_formal.format(name)

# print(intruption, formatted)
# print(formatted.upper())
# print(formatted.lower())
# print(formatted.replace("John", "Paul"))

# LISTS

# NAMES = ["John", "Paul", "George", "Ringo"]
# AGES = [20, 21, 22, 23]

# JOHN = NAMES[0]
# PAUL = NAMES[1]

# JOHN_PAUL = NAMES[:2]
# GEORGE_RINGO = NAMES[2:]
# REVERSE = NAMES[::-1]
# EVERY_OTHER = NAMES[::2]

# print(JOHN_PAUL)
# print(GEORGE_RINGO)
# print(REVERSE)
# print(EVERY_OTHER)

# print(sum(AGES))
# print(min(AGES))
# print(max(AGES))

# LOOPS

# NAMES = ["John", "Paul", "George", "Ringo"]
# AGES = [20, 21, 22, 23]

# i = 0
# while i < len(NAMES):
#     print([NAMES[i], AGES[i]])
#     i +=1
    
# for name in NAMES:
#     print(name)
    
# for name, age in zip(NAMES, AGES):
#     print(f"{name} {age}")
    
# for name in reversed(NAMES):
#     print(name)
    
# for i in range(5):
#     print(i)
    
# # ENUMERATE

# for i, name in enumerate(NAMES):
#     print(f"{i} {name}")

# ELSE / IF / ELIF

# import os

# DEVELOPMENT = "developemnt"
# PRODUCTION = "production"
# STAGING = "staging"
# CODE_SPACE = "code_space"
# LOCAL = "local"

# current_env = os.environ.get("ENV_NAME", DEVELOPMENT)# allows to take the environment I am running on

# if current_env == DEVELOPMENT:
#     print("Developemnt Environment")
# elif current_env == PRODUCTION:
#     print("Production Environment")
# elif current_env == STAGING:
#     print("Staging Environment")
# elif current_env in [CODE_SPACE, LOCAL]:
#     print("Codespace or Local Environment")
# else:
#     print("Unknown Environment")

# Reading CSV file

# import csv
# from pprint import pprint

# EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

# EINSTEIN = {
#     "birthplace": "Germany",
#     "name": "Albert",
#     "surname": "Einstein",
#     "born": "1879-03-14",
#     "category": "physics",
#     "motivation": "for his services to Theoretical Physics...",
# }

# with open("laureates_trial.csv", "r") as f:
#     reader = csv.DictReader(f)
#     laureates_trial = list(reader)
    
# for laureate in laureates_trial:
#     if laureate["surname"] == "Einstein":
#         pprint(laureate)
#         break

# Making Calculations

# import csv
# from pprint import pprint
# from datetime import datetime

# EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

# EINSTEIN = {
#     "birthplace": "Germany",
#     "name": "Albert",
#     "surname": "Einstein",
#     "born": "1879-03-14",
#     "category": "physics",
#     "motivation": "for his services to Theoretical Physics...",
# }

# with open("laureates_trial.csv", "r") as f:
#     reader = csv.DictReader(f)
#     laureates_trial = list(reader)
    
# for laureate in laureates_trial:
#     if laureate["surname"] == "Einstein":
#         pprint(laureate)
#         print("=====================")
#         year_date = datetime.strptime(laureate["year"], "%Y")
#         born_date = datetime.strptime(laureate["born"], "%Y-%m-%d")
#         print("Age : ", year_date.year - born_date.year)
#         break
        
# CSV to JSON

# import csv
# import json
# from pprint import pprint

# EINSTEIN = {
#     "birthplace": "Germany",
#     "name": "Albert",
#     "surname": "Einstein",
#     "born": "1879-03-14",
#     "category": "physics",
#     "motivation": "for his services to Theoretical Physics...",
# }

# einstein_json = json.dumps(EINSTEIN)
# back_to_dict = json.loads(einstein_json)
# print(einstein_json)
# pprint(back_to_dict)

# with open("laureates_trial.csv", "r") as f:
#     reader = csv.DictReader(f)
#     laureates = list(reader)

# with open("laureates_trial.json", "w") as f:
#     json.dump(laureates, f, indent=2)

# Challenge 

import csv
import json
from pprint import pprint

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

einstein_json = json.dumps(EINSTEIN)
back_to_dict = json.loads(einstein_json)
print(einstein_json)
pprint(back_to_dict)

# FOR GETTING NAMES ONLY
# laureates_name = []

# with open("laureates_trial.csv", "r") as f:
#     csv_reader = csv.reader(f)
#     column_data = [row[0] for row in csv_reader]
#     laureates_name.extend(column_data[1:])
    
# laureates_name_beginning_A = []

# for name in laureates_name:
#     if name[0] == "A":
#         laureates_name_beginning_A.append(name)
# print("Starting with A :", laureates_name_beginning_A)
# # print(len(laureates_name_beginning_A))

# with open("laureates_beginning_A.json", "w") as f:
#     json.dump(laureates_name_beginning_A, f, indent=2)

# FOR GETTING EVERY DETAILS OF PERSON WHOSE NAME STARTS WITH A

# laureates_beginning_with_a = []

# with open("laureates_trial.csv", "r") as f:
#     reader = csv.DictReader(f)
#     laureates = list(reader)
    
# for lareate in laureates:
#     if lareate['name'][0] == "A":
#         laureates_beginning_with_a.append(lareate)

# with open("laureates_all_details.json", "w") as f:
#     json.dump(laureates_beginning_with_a, f, indent=2)