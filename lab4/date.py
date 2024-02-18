#exercise 1: Write a Python program to subtract five days from current date.

from datetime import datetime, timedelta

today = datetime.now()

five_days_ago = today - timedelta(days=5)

print(five_days_ago)


#exercise 2: Write a Python program to print yesterday, today, tomorrow.

from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(yesterday, today, tomorrow, sep = "\n")



#exercise 3: Write a Python program to drop microseconds from datetime.

from datetime import datetime

today = datetime.now()
today_micro = today.replace(microsecond=0)

print(today_micro)


#exercise 4: Write a Python program to calculate two date difference in seconds.

from datetime import datetime, timedelta

date1 = datetime.datetime(2024, 2, 13, 18, 56, 50)
date2 = datetime.datetime(2024, 2, 13, 18, 57, 0)

time_diff = date2 - date1
seconds = time_diff.total_seconds()

print(seconds)

