
import datetime as dt

# import datetime

# from datetime import timedelta

# timedelta(15)

# Task 1

# current_datetime = '8/07/2021'

# new_date = dt.datetime.strptime(current_datetime, '%d/%m/%Y')

# days = dt.timedelta(days=15)

# past_date = new_date - days

# print(current_datetime)
# print(past_date.date())

# current_datetime = dt.datetime.now()

# days = dt.timedelta(days=15)

# past_date = current_datetime - days

# print(past_date.date())

# Task 2


# current_datetime = dt.datetime.today()

# days = dt.timedelta(days=7)

# future_date = current_datetime + days

# print(future_date.date())

# print(dir(dt))


# Task 3
# from datetime import datetime

current_date = dt.datetime(year=2020, month=1, day=1)

days = dt.timedelta(days=25)

rent_date = current_date + days

rent_text = rent_date.strftime('%d %B, %Y')

print(f'Hello Friedrich, your rent of 300 € is due on {rent_text}.')


