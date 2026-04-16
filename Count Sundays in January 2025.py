import datetime
sundays = 0
for day in range(1, 32):
    if datetime.date(2025, 1, day).weekday() == 6:
        sundays += 1
print(sundays)
