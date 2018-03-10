import datetime
from datetime import date
from pprint import pprint

def diff_dates(date1, date2):
    return abs(date2-date1).days

def main():
    input = '2005-02-28  17:35:22.90909'
    str = input.split('.')[0]
    d1 = datetime.datetime.strptime(str, '%Y-%m-%d %H:%M:%S').date()
    print d1
    d2 = datetime.date.today()

    result1 = diff_dates(d2, d1)
    print '{} days between {} and {}'.format(result1, d1, d2)
main()