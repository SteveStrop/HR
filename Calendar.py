import calendar
month, day, year = map(int,input().split())
print (calendar.day_name[calendar.weekday(year=year,day=day,month=month)].upper())

