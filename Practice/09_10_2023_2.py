# HACKER EARTH 

# FAVOURITE SINGER

# number_songs = int(input("Enter the number of songs : "))
# songs = list(map(int, input("Enter the songs : ").split()))

# dict1 = {}

# for i in songs:
#     if i in dict1 :
#         dict1[i] += 1
#     else:
#         dict1[i] = 1

# max_count = max(dict1.values())

# max_keys = []
# for key, value in dict1.items():
#     if value == max_count:
#         max_keys.append(key)
# print(len(max_keys))

# MAXIMUM BORDERS 

number_t = int(input("Enter the number of test cases : "))

for num in range(number_t):
    rows, columns = list(map(int, input("Enter the number of Rows and Columns : ").split()))

    list_count = []

    for i in range(rows):
        string = input("Enter string : ")
        count = 0
        if len(string) == columns:
            for char in string:
                if char == "#":
                    count += 1
            list_count.append(count)
    print(max(list_count))