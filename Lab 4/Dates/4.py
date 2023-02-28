import datetime

a = datetime.datetime(2023,2,23,12,31,27)
b = datetime.datetime(2023,2,23,12,31,59)

print((b-a).total_seconds())