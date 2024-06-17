questions = [
    ["What is 2 ** 4? ", 12, 16, 21, 20, "None", 2],
    ["Which language is used to create fb?", "Python", "French", "Javascript", "Php", "None", 4],
    ["What is 4 * 2?", 12, 6, 8, 9, "None", 3],
    ["What is 9 * 2?", 18, 9, 23, 76, "None", 1],
    ["What is (10 + 10) * 0?", 10, 0, 20, 45, "None", 2 ]]


levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0

for i in range(len(questions)):
    question = questions[i]
    
    print(f"Question for Rs. {levels[i]} is : ")
    print(question[0])
    print(f"a. {question[1]}         b. {question[2]}")
    print(f"c. {question[3]}         d. {question[4]}")
    reply = int(input("Enter your answer (1-4) or 0 to quit : "))
    
    if reply == 0:
        money = levels[i - 1]
        break
    
    if reply == question[-1]:
        print(f"Correct answer!, U have won Rs. {levels[i]}!!! ")
        
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
    
    else:
        print("Wrong Answer!!")
        break
    
print(f"Your take home money is {money}")