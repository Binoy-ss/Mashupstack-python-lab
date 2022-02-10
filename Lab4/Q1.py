import datetime

print("Current date and time are ", datetime.datetime.now())

print("The Current year is ", datetime.date.today().strftime("%Y"))

print("The Month of  year is ", datetime.date.today().strftime("%B"))

print("The Week of  year is ", datetime.date.today().strftime("%W"))

print("The Weekdays of  week is ", datetime.date.today().strftime("%w"))

print("Day of the year: ", datetime.date.today().strftime("%j"))

print("Day of the month : ", datetime.date.today().strftime("%d"))

print("Day of the week: ", datetime.date.today().strftime("%A"))