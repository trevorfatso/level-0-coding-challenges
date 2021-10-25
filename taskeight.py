#task8
def time(number):
    if number >= 60:
        hour = int(number/60)
        minute = number - int(number/60)*60
        string_hour = ''
        string_minute = ''
        if hour > 1 or hour == 0:  
            string_hour = f'{hour} hours'
        elif hour == 1:
            string_hour = f'{hour} hour'
        if minute > 1 or minute == 0:
            string_minute = f' {minute} minutes'
        elif minute == 1:
            string_minute = f' {minute} minute'
        return string_hour + ',' + string_minute
    else:
        return f'{number} minutes'