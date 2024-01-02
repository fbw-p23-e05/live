import calendar

year = 2006
month = 8

# print a specific month
# print(calendar.month(year, month))

# # print full calendar
# print(calendar.calendar(2027))

# setfirstweekday() - set the first week day of our calendar
# print(calendar.setfirstweekday(2))
# print(calendar.calendar(2027))

# isleap() - tells whether a year is a leap year or not.add()
print("Is 2056 a leap year?", calendar.isleap(2056))

# monthrange() - returns the weekday of the first day of the month and the number of days in that month.
# parameters - month and year.

print(calendar.monthrange(2023, 10))

# weekday() - returns a day of the week for a particular date. 
print(calendar.weekday(2087, 12, 25))

# 1. Get today's date
# 2. Check the week number 
# 3. Check the day number for this week 

# import datetime

# today = datetime.datetime.now()
# year = today.year
# month = today.month
# day = today.day

# print(calendar.weekday(year, month, day))

from datetime import datetime, date, time
import datetime as dt # using dt as the class name
from datetime import timedelta as td

dt.datetime.now()

datetime.now() # Handles both date and time
date.today() # Handles the date explicitly
time.now() # Handles time specifically
