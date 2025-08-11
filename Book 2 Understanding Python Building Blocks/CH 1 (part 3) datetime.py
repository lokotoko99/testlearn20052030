import datetime as dt

today = dt.date.today()

last_of_teens = dt.date(2019,12,31)

print(today, last_of_teens)

print(f"\n{today}\n{last_of_teens}")

print(last_of_teens.month)
print(last_of_teens.day)
print(last_of_teens.year)

print(f"{last_of_teens:%A,%B %d, %Y}")

print(f"{today:%m/%d/%Y}")

#Workign with times;;
#variable = datetime.time([hour[,minute[, second[, microsecond]]]])

midnight = dt.time()
print(midnight)
print(type(midnight))

almost_midnight = dt.time(23, 59, 59, 99999)
print(f"{almost_midnight:%I:%M %p}")

right_now =dt.datetime.now()
new_years_eve = dt.datetime(2025,12,31,23,59)
print(right_now)
print(new_years_eve)

new_years_day = dt.date(2024, 1, 1)
memorial_day = dt.date(2024, 5, 27)
days_between = memorial_day - new_years_day
print(days_between)
print(type(days_between))

duration = dt.timedelta(days = 147)
print(new_years_day+duration)

start_time = dt.datetime(2024, 3, 31, 8, 0, 0)
finish_time = dt.datetime(2024, 3, 31, 14, 34, 45)
time_between = finish_time - start_time
print(time_between)
print(type(time_between))

print(new_years_day + dt.timedelta(hours = 13))


now= dt.datetime.now()
birthdatetime = dt.datetime(1995, 3, 31, 8, 26)
age = now - birthdatetime
print(age)
print(type(age))


today = dt.date.today()
birthdate = dt.date(2000, 12, 31)
delta_age = (today - birthdate)

print(delta_age)

days_old = delta_age.days
print(days_old, type(days_old))

years_old = days_old // 365
months_old = days_old % 365 // 30
print(years_old)
print(months_old)






