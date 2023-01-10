from datetime import datetime
# now = datetime.now()
# print(now)
# day = now.day
# month = now.month
# year = now.year
# hour = now.hour
# minute = now.minute
# second = now.second
# timestamp = now.timestamp()

# print(day, month, year, hour, minute)
# print('timestamp', timestamp)
# print(f'{day}/{month}/{year}, {hour}:{minute}')

# new_year = datetime(2020, 1, 1)
# print(new_year)
# day = new_year.day
# month = new_year.month
# year = new_year.year
# hour = new_year.hour
# minute = new_year.minute
# second = new_year.second
# print(day, month, year, hour, minute)
# print(f'{day}/{month}/{year}, {hour}:{minute}')

# now = datetime.now()
# t = now.strftime('%H:%M:%S')
# print('time: ', t)

# time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# print('time_one: ', time_one)

# time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# print('time_two', time_two)

# date_string = "5 December, 2019"
# print('date_string = ', date_string)

# date_object = datetime.strptime(date_string, '%d %B, %Y')
# print('date_object', date_object)
from datetime import date

# d = date(2020, 1, 1)
# print(d)
# print('current date: ', d.today())

# today = date.today()
# print('current year: ', today.year)
# print('current month: ', today.month)
# print('current day: ', today.day)

from datetime import time
# a = time()
# print('a = ', a)

# b = time(10, 30 ,50)
# print("b = ", b)

# c = time(hour=10, minute=30, second=50)
# print("c = ", c)

# d = time(10, 30, 50, 200555)
# print("d = ", d)

# today = date.today()
# new_year = date(2024, 1, 1)
# time_left_to_new_year = new_year - today
# print('time left to new year', time_left_to_new_year)

# t1 = datetime.today()
# t2 = datetime(2024,1,1,0,0,0)
# diff = t2 - t1
# print('timeleft to new year: ', diff)

from datetime import timedelta

# t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
# t2 = timedelta(days=7, hours=5, minutes=3, seconds=35)
# t3 = t1 - t2
# print('t3 = ', t3)