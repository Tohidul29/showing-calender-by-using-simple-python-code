import calendar

year = int(input('Enter the year : '))
month = int(input('Enter the month : '))
day = int(input('Enter the date : '))

result = calendar.month(year, month, day)
print(result)