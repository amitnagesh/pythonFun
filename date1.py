from datetime import datetime 
from pprint import pprint

# date = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
# date = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

dt_str = '9/24/2010'
dt_obj = datetime.strptime(dt_str, '%m/%d/%Y').date()

print dt_obj

now = datetime.now()
dt_obj1 = now.strftime("%Y-%m-%d")
print dt_obj1

print '---------'

d1 = datetime.strptime(dt_obj1, "%Y-%m-%d")
d2 = datetime.strptime(dt_obj, "%Y-%m-%d")

result1 = abs((d2 - d1).days)

# result1 = days_between(dt_obj, dt_obj1)
# result1 = abs(dt_obj1-dt_obj).days
# print '{} days between {} and {}'.format(result1, dt_obj, dt_obj1)
print result1
print '---------'

# def days_between(d1, d2):
#     d1 = datetime.strptime(d1, "%Y-%m-%d")
#     d2 = datetime.strptime(d2, "%Y-%m-%d")
#     return abs((d2 - d1).days)