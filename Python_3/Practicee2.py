# def count_substring(string, sub_string):
#     count = 0
#     start_index = 0

#     while True:
#         index = string.find(sub_string, start_index)
#         if index == -1:
#             break
#         count += 1
#         start_index = index + len(sub_string)

#     return count

# if __name__ == '__main__':
#     string = input("Enter the original string: ")
#     sub_string = input("Enter the substring to count: ")

#     count = count_substring(string, sub_string)
#     print("Total occurrences:", count)
    
    
def find_substring(string, sub_string):
    count = 0
    start_index = 0

    while True:
        index = string.find(sub_string, start_index)
        if index == -1:
            break
        count += 1
        start_index = index + 1

    return count

if __name__ == '__main__':
    string = input("Enter the original string: ")
    sub_string = input("Enter the substring to find: ")

    occurrence_indices = find_substring(string, sub_string)
    print(occurrence_indices)