"""
strftime() - creates a formatted string from given date, datetime or time object.
"""
import datetime as dt

# current date and time
curr_date = dt.datetime.now()
print(curr_date)

# Tuesday, 12 September 2023 - 10:54 AM
time_1 = curr_date.strftime("%A, %d %B %Y - %I:%M %p")
print(time_1)

# dd/mm/yyyy, H:M
time_2 = curr_date.strftime("%d/%m/%Y, %H:%M")
print(time_2)

# Local version of date and time
time_3 = curr_date.strftime("%c")
print(time_3)
