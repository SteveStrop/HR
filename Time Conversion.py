def timeConversion(s):
    hour = int(s[:2])

    if hour == 12:
        if 'AM' in s:
            hour = 0
        else:
            hour=12
    elif 'PM' in s:
        hour +=12

    hour='{:02}'.format(hour)

    return hour+s[2:-2]


print(timeConversion('01:05:45PM'))

