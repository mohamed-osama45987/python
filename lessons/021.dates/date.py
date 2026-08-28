import datetime

date = datetime.date(2026, 1, 23)  # create specific date

today = datetime.date.today()


time = datetime.time(12, 20, 0)  # create specific date

current_time = datetime.datetime.now()

current_time_formatted = current_time.strftime("%H:%M:%S %d-%m-%Y")

print(date)  # 2026-01-23
print(today)  # 2026-08-28
print(time)  # 12:20:00
print(current_time)  # 2026-08-28 22:15:10.994644
print(current_time_formatted)  # 22:17:16 28-08-2026


# to see if target date time has passed
target_dateTime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_dateTime = datetime.datetime.now()

if target_dateTime < current_dateTime:
    print("Target Date has passed")
else:
    print("Target date has not passed")
