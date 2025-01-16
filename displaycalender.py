import calendar

# Input year and month from the user
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# Display the calendar
print(calendar.month(yy, mm))