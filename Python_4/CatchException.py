#Handling Multiple Exceptions

String = input("Enter something here : ")

try:
    num = int(input("Enter a number here : "))
    print(String + num)
except Exception as e:
    print(e)
  
print("Thank You")  