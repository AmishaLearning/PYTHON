# Union()

# set_a = set("Hacker")
# print(set_a.union("Rank"))
# print(set_a.union(set(['R', 'a', 'n', 'k'])))
# # enumerate() keeps track of both index and corresponding value
# print(set_a.union(enumerate(['R', 'a', 'n', 'k'])))

# print(set_a.union({"Rank" : 1}))
# print(set_a | set("Rank"))

# stud_english_num = int(input("Enter the number of sutdents for English NP : "))
# rollno_eng = set(map(int, input("Enter the roll numbers for ENG NP : ").split()))

# stud_french_num = int(input("Enter the number of sutdents for French NP : "))
# rollno_french = set(map(int, input("Enter the roll numbers for French NP : ").split()))

# result = rollno_eng.union(rollno_french) 

# print(len(result))

# Intersection()

# set_b = set("Hacker")
# print(set_b.intersection("Rank"))
# print(set_b.intersection(set(['R', 'a', 'n', 'k'])))
# print(set_b.intersection(enumerate(['R', 'a', 'n', 'k'])))
# print(set_b.intersection({"Rank" : 1}))
# print(set_b & set("Rank"))

# stud_english_num = int(input("Enter the number of sutdents for English NP : "))
# rollno_eng = set(map(int, input("Enter the roll numbers for ENG NP : ").split()))

# stud_french_num = int(input("Enter the number of sutdents for French NP : "))
# rollno_french = set(map(int, input("Enter the roll numbers for French NP : ").split()))

# result = rollno_eng.intersection(rollno_french) 

# print(len(result))

# Difference()

# set_c = set("Hacker")
# print(set_c.difference("Rank"))
# print(set_c.difference(set(['R', 'a', 'n', 'k'])))
# print(set_c.difference(['R', 'a', 'n', 'k']))
# print(set_c.difference(enumerate(['R', 'a', 'n', 'k'])))
# print(set_c - set("Rank"))

# stud_english_num = int(input("Enter the number of sutdents for English NP : "))
# rollno_eng = set(map(int, input("Enter the roll numbers for ENG NP : ").split()))

# stud_french_num = int(input("Enter the number of sutdents for French NP : "))
# rollno_french = set(map(int, input("Enter the roll numbers for French NP : ").split()))

# result = rollno_eng.difference(rollno_french) 

# print(len(result))

# Symmetric_difference()

# set_d = set("Hacker")
# print(set_d.symmetric_difference("Rank"))
# print(set_d.symmetric_difference(set(['R', 'a', 'n', 'k'])))
# print(set_d.symmetric_difference(['R', 'a', 'n', 'k']))
# print(set_d.symmetric_difference(enumerate(['R', 'a', 'n', 'k'])))
# print(set_d.symmetric_difference({"Rank" : 1}))
# print(set_d ^ set("Rank"))

# stud_english_num = int(input("Enter the number of sutdents for English NP : "))
# rollno_eng = set(map(int, input("Enter the roll numbers for ENG NP : ").split()))

# stud_french_num = int(input("Enter the number of sutdents for French NP : "))
# rollno_french = set(map(int, input("Enter the roll numbers for French NP : ").split()))

# result = rollno_eng.symmetric_difference(rollno_french) 

# print(len(result))

# .update()

# set_e = set("Hacker")
# set_f = set("Rank")
# set_e.update(set_f)
# print(set_e)

# .intersection_update()

# set_g = set("hacker")
# set_h = set("Rank")
# set_g.intersection_update(set_h)

# print(set_g)

# .difference_update()

# set_i = set("Hacker")
# set_j = set("Rank")
# set_i.difference_update(set_j)
# print(set_i)

# .symmetric_difference_update()

# set_k = set("Hacker")
# set_l = set("Rank")
# set_k.symmetric_difference_update(set_l)
# print(set_k)


# num_set_A = int(input("Enter the number of elements in set A : "))
# elements_A = set(map(int, input("Enter the elements of set A : ").split()))

# other_set = int(input("Enter the number of other sets : "))

# for i in range(other_set):
#     command = input("Enter the operation to be performed : ").split()
#     set_B = set(map(int, input("Enter elements of set B : ").split()))
#     if command[0] == 'intersection_update':
#         elements_A.intersection_update(set_B)
#         print(elements_A)
#     if command[0] == 'update':
#         elements_A.update(set_B)
#         print(elements_A)
#     if command[0] == 'symmetric_difference_update':
#         elements_A.symmetric_difference_update(set_B)
#         print(elements_A)
#     if command[0] == 'difference_update':
#         elements_A.difference_update(set_B)
#         print(elements_A)
        
# print(sum(elements_A))

# while giving command in above example : update 2 means update is the command and 2 is the length of the another set 
