#Python Date

#Ex.1
from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days = 5)

print(current_date.strftime("%Y-%m-%d"))
print(new_date.strftime("%Y-%m-%d"))

#Ex.2
from datetime import datetime, timedelta

today = datetime.now()

yesterday = today - timedelta(days=1)

tomorrow = today + timedelta(days=1)

print(yesterday.strftime("%Y-%m-%d"))
print(today.strftime("%Y-%m-%d"))
print(tomorrow.strftime("%Y-%m-%d"))

#Ex.3
from datetime import datetime

current_datetime = datetime.now()
current_datetime_without_microseconds = current_datetime.replace(microsecond=0)

print(current_datetime_without_microseconds)

#Ex.4
from datetime import datetime

date_str1 = input()
date_str2 = input()

date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")

difference_seconds = abs((date2 - date1).total_seconds())

print(difference_seconds)