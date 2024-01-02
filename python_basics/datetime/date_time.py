import datetime as dt

x = dt.datetime.now()

# print(x)

# print(x.date())

# print(x.ctime())

# print(type(x))

# birthday = dt.datetime(2000, 12, 25, 11, 30, 44, 22)

# print(birthday)

# print(birthday.date())

# print(birthday.time())

# datetime.date()

# current_date = dt.date.today()
# print('Todays date is:', current_date)

# world_cup_date = dt.date(2023, 9, 8)
# print(world_cup_date)

# timestamp = dt.date.fromtimestamp(3498765445)
# print(timestamp)

# moon_landing = dt.date(1969, 7, 16)
# print('Moon landing year:', moon_landing.year)
# print('Moon landing month:', moon_landing.month)
# print('Moon landing day:', moon_landing.day)

# datetime.time()

# current_time = dt.time(hour = 18, minute = 39)
# print(current_time)
# print('current hour:', current_time.hour)
# print('current minute:', current_time.minute)
# print('current second:', current_time.second)
# print('current microsecond:', current_time.microsecond)

# datetime.timedelta

# calculate the date difference
# date_1 = dt.date(2023, 9, 12)
# date_2 = dt.date(2022, 7, 5)

# date_3 = date_1 - date_2
# print(date_3)

# date_4 = dt.datetime(2023, 9, 12, 9, 57, 47)
# date_5 = dt.datetime(2019, 8, 19, 17, 30, 23)

# date_6 = date_4 - date_5
# print(date_6)

# print('Type of date 3:', type(date_3))
# print('Type of date 6:', type(date_6))

# calculating difference between timedelta objects

# dif_one = date_3 - date_6
# print(dif_one)

# Get time duration in seconds

unix_date = dt.date(1970, 1, 1)
current_date = dt.date.today()

time_diff = current_date - unix_date
print(time_diff)

unix_timestamp = time_diff.total_seconds()
print(unix_timestamp)

new_date = dt.date.fromtimestamp(1694476800.0)
print(new_date)











