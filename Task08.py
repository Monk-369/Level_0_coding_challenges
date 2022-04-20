def convert_to_time(num):
    hours = num // 60
    minutes = num % 60
    time = (hours, minutes)
    if hours == 1 and minutes == 1:
        print(hours, 'hour', minutes, 'minute')
    elif hours == 1 and minutes > 1:
        print(hours, 'hour', minutes, 'minutes')
    elif hours > 1 and minutes == 1:
        print(hours, 'hours', minutes, 'minute')
    else:
        print(hours, 'hours', minutes, 'minutes')
    return time
convert_to_time(116)

                
