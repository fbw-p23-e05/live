
import datetime as dt

# Task 1

# current_date = dt.datetime.today()

# print('Current date and time:', current_date)

# print('Current year:', current_date.year)

# print('Month of year:', current_date.strftime('%B'))

# print('Week number of the year:', current_date.strftime('%W'))

# print('Weekday of the week:', current_date.strftime('%w'))
# print('Weekday of the week:', current_date.weekday())

# print('Day of year:', current_date.strftime('%j'))

# print('Day of the month :', current_date.day)
# print('Day of the month :', current_date.strftime('%d'))

# print('Day of week:', current_date.strftime('%A'))


# Task 2

# current_date = dt.date.today()

# days = dt.timedelta(days=1)

# yeasterday = current_date - days
# tomorrow = current_date + days

# print(f'Yesterday : {yeasterday}')
# print(f'Today : {current_date}')
# print(f'Tomorrow : {tomorrow}')


# Task 3

# current_datetime = dt.datetime.today()

# seconds = dt.timedelta(seconds=5)

# new_datetime = current_datetime + seconds


# print('Current time:', current_datetime.time())
# print('After adding 5 seconds:', new_datetime.time())


# Task 4

# current_datetime = dt.datetime.today()

# print('Today:', current_datetime)

# print('Next 5 days:')

# for i in range(5):
#     new_date = current_datetime + dt.timedelta(i+1)

#     print(new_date)

# for i in range(1,6):
#     new_date = current_datetime + dt.timedelta(i)

#     print(new_date)


# Task 5

# current_datetime = dt.datetime.today()

# print('Today:', current_datetime)

# print('Day of the year:', current_datetime.strftime('%j'))


# Task 6

# week = 37

# first_day = dt.date(2023, 1, 1)

# days = dt.timedelta((week - 1) * 7)

# new_date = first_day + days 

# print(new_date.weekday())

# # first_monday = new_date + dt.timedelta(1)

# first_monday = new_date + dt.timedelta(1)

# # print(first_monday.weekday())
# # print(first_monday.strftime('%W'))

# print('The first Monday of this week was:', first_monday)

# Another solution

# year = '2023'
# week = '37'
# first_monday = '1'

# date = dt.datetime.strptime(year + week + first_monday, '%Y%W%w')

# print(date.date())

# Task 7

year = int(input('Input a year: '))

date = dt.date(year, 1, 1)

print('Output:')

while year == date.year:
    if date.weekday() == 6:
        print(date)
    date += dt.timedelta(1)

# 365/366, 52/53


