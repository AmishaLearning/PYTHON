# word_to_digit = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4,
#                  "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}

# string = "nine eight seven six five four three two one zero"
# string_split = string.split()
# print(string_split)

# if len(string_split) == 10:
#     for i in range(len(string_split)):
#         if string_split[i] in word_to_digit:
#             string_split[i] = word_to_digit[string_split[i]]
                
# result = int("".join(map(str, string_split)))
# print(result)


word_to_digit = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4,
                 "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}

string = "five eight double two double two four eight five six"
string_split = string.split()
# print(string_split)

def double(double_string):
    # print("I am from double")
    for i in range(len(double_string)):
        # print(double_string)
        if double_string[i] == "double":
            # print("Found Double")
            double_string[i] = double_string[i + 1]   
            print(double_string[i])        
        double_string[i] = word_to_digit[double_string[i]]     
        
def triple(triple_string):
    # print("I am from triple")
    for i in range(len(triple_string) + 1):
        print(triple_string)
        if triple_string[i] == "triple":
            # print("Found Triple")
            triple_string[i : i + 1] = [triple_string[i + 1] , triple_string[i + 1]]
            print(triple_string)
        triple_string[i] = word_to_digit[triple_string[i]] 
          
def normal(normal_string):  
    # print("I am from normal")  
    for i in range(len(normal_string)):       
        if normal_string[i] in word_to_digit:
            # print("Found Normal")
            string_split[i] = word_to_digit[normal_string[i]]
                      
for i in range(len(string_split)):
    if string_split[i] == "double":           
        new_string_double = double(string_split)
        # print("Again Yes")
 
    # if string_split[i] == "triple":           
    #     new_string_triple = triple(string_split)
    #     # print("Again Again Yes")
        
    # if string_split[i] != "double" or string_split[i] != "triple":
    #     normal(string_split)
    #     # print("Yes")
   
result = int("".join(map(str, string_split)))

if len(str(result)) == 10:
    print(result)
    print("Number is Valid")

else:
    print("Number is Invalied")





