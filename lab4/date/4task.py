from datetime import datetime, timedelta

def sec(d1, d2):
    diff = d2 - d1
    return diff.days * 24 * 3600 + diff.seconds

d1=datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
d2=datetime.now()

print(sec(d1 , d2))
