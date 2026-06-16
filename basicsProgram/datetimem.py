"""
The date contains year, month, day, hour, minute, second, and microsecond.
"""
"""

import datetime
from datetime import datetime, timedelta
x=datetime.datetime.now()
y=datetime.datetime(2026, 3, 30)#  2026-03-30 00:00:00
print(x)# 2026-03-30 14:32:01.433618
print(x.year)# 2026
print(x.strftime("%A"))# Tuesday
print(y)# 2026-03-30 00:00:00
print(x.strftime("%B"))# March
print(x.strftime("%d"))# 30
print(x.strftime("%m"))# 03
print(x.strftime("%Y"))# 2026
print(x.strftime("%H"))# 14
print(x.strftime("%j"))# 090
print(x.strftime("%x"))# 03/30/26
now = datetime.now()
future_date = now + timedelta(weeks=1, days=2) # 1 week and 2 days in the future
past_date = now - timedelta(hours=5)           # 5 hours in the past

print(f"Current time: {now}")
print(f"Future date: {future_date}")
print(f"Past date: {past_date}")
"""
####################333
from datetime import datetime, timedelta
"""
# Get the current date and time
now=datetime.now()# 2026-03-30 15:02:44.589404
print(now)
# Add 2 years (approx. 730 days)
after_2_years=now+timedelta(days=500)
print(after_2_years)#2028-03-29 15:04:50.954617
# Add 2 days
after_2_days = now + timedelta(days=2)
print("After 2 Days:", after_2_days)
"""
###############3
"""
from datetime import datetime
z=datetime.now()
a=datetime(2026, 7, 30)
b=datetime(2024, 5, 20)
years=a.year-b.year
months=a.month-b.month
days=a.day-b.day
#print(z)
print(a)
print(b)
print(f"{years} Years, {months} Months, {days} Days")
## New time after 2 days
"""
# user input
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta
date_str = input("Enter a date (YYYY-MM-DD): ")
x = datetime.strptime(date_str, "%Y-%m-%d")
date_str1 = input("Enter another date (YYYY-MM-DD): ")
y = datetime.strptime(date_str1, "%Y-%m-%d")
diff = relativedelta(x, y)
"""
#date_diff=a.date-b.date
#month_diff=a.month-b.month
#year_diff=a.year-b.year
"""
print(f"Difference: {diff.years} years, {diff.months} months, {diff.days} days")
"""
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta
date_str = input("Enter a date (YYYY/MM/DD): ")
a = datetime.strptime(date_str, "%Y/%m/%d")
date_str1 = input("Enter another date (YYYY/MM/DD): ")

b = datetime.strptime(date_str1, "%Y/%m/%d")
diff = relativedelta(a, b)
diff1 = relativedelta(x, y)

#print(f"Difference: {diff.years} years, {diff.months} months, {diff.days} days")
#print(f"Difference (alternative): {diff1.years} years, {diff1.months} months, {diff1.days} days")
"""


from datetime import datetime
from dateutil.relativedelta import relativedelta
date_str1 = input("Enter first date (YYYY/MM/DD or YYYY-MM-DD or) ")
date_str2 = input("Enter second date (YYYY/MM/DD or YYYY-MM-DD)")
if "/" in date_str1:
    a=datetime.strptime(date_str1, "%Y/%m/%d")
elif "-" in date_str1:
    a=datetime.strptime(date_str1, "%Y-%m-%d")
elif len(date_str1.split()[1])==3:
    a=datetime.strptime(date_str1, "%Y %b %d")    
else:
    a=datetime.strptime(date_str1, "%Y %B %d" )

if "/" in date_str2:
    b=datetime.strptime(date_str2, "%Y/%m/%d")
elif "-" in date_str2:
    b=datetime.strptime(date_str2, "%Y-%m-%d")
elif len(date_str2.split()[1])==3:
    b=datetime.strptime(date_str2, "%Y %b %d")      
else:
   b=datetime.strptime(date_str2, "%Y %B %d")

diff = relativedelta(a,b)
print(f"Difference: {diff.years} years, {diff.months} months, {diff.days} days")


   
   
