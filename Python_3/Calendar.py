import calendar

year = int(input("Enter the Year : "))
month = int(input("Enter the Month : "))

calendar = calendar.month(year, month)

print(calendar)
