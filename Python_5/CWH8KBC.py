# KBC in python

def earnedMoney(choice):
    total_amount = 0
    
    pass    
    

def FirstQues():
    int(input("Enter Ur Choice as 1 to get the First Question on ur Computer Screen : "))
    print("The First Question is :" )
    print("What is the the value of 2 ** 4 ? ")
    input("The options are :\na)5     b)16\nc)12    d)20")
    choice = input("Enter the option you feel is Correct : ")
    if choice == "b":
        print("Yes!! Ur answer is correct")
        earnedMoney(choice)
        print("Lets go to the next question!!")
        SecondQues()
    else:
        print("Sorry!!U selected the wrong answer")
        
def SecondQues():
    int(input("Enter Ur Choice as 2 to get the First Question on ur Computer Screen : "))
    print("The Secong Question is :" )
    print("What is the the value of 51 // 5 ? ")
    input("The options are :\na)5     b)21\nc)2     d)1")
    choice = input("Enter the option you feel is Correct : ")
    if choice == "d":
        print("Yes!! Ur answer is correct")
        earnedMoney(choice)
    else:
        print("Sorry!!U selected the wrong answer")    
        

   
FirstQues()