from datetime import datetime
from datetime import date

# 1
today = datetime.today()
day = today.day
month = today.month
year = today.year
hour = today.hour
minute = today.minute
timestamp = today.timestamp()
print(today, day, month, year, hour, minute, timestamp)

# 2
now = datetime.today()
formated_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formated_date)

# 3
time_string = '5 December, 2019'
time_parse = datetime.strptime(time_string, "%d %B, %Y")
print(time_parse)

# 4
new_year = datetime(2024,1,1,0,0,0)
diff = new_year - today
print('time to new year ', diff)

# 5
entry_date = datetime(1970, 1, 1)
newdiff = today - entry_date
print('diference between dates: ', newdiff)

#6
'''
to create an time register to a aplication interface
to register the time in a database
to create a conditional event based on time
'''