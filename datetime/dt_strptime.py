"""
strptime() - creates a datetime object from a given string representing date and time.
takes 2 arguments:
- a string representing the date and time.
- format code equivalent to the first argument.
"""
import datetime as dt

world_cup_date = "8 September 2023"
print("Rugby World Cup start date:", world_cup_date)

# use strptime() to create a date object.

date = dt.datetime.strptime(world_cup_date, "%d %B %Y")
print("Date Object:", date)
