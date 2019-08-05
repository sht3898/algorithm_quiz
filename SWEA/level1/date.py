date1 = '22220228'
date2 = '20150002'
date3 = '01010101'
date4 = '20140230'
date5 = '11111111'


def date(day):
    if int(day[4:6]) > 12 or int(day[4:6]) < 1:
        return (-1)
    elif day[4:6] =='02':
        if int(day[6:]) < 1 or int(day[6:]) > 28:
            return (-1)
        else:
            return (f'{day[:4]}/{day[4:6]}/{day[6:]}')
    elif day[4:6] in '01 03 05 07 08 10 11':
        if int(day[6:]) < 1 or int(day[6:]) > 31:
            return (-1)
        else:
            return (f'{day[:4]}/{day[4:6]}/{day[6:]}')
    elif day[4:6] in '04 06 09 11':
        if int(day[6:]) < 1 or int(day[6:]) > 30:
            return (-1)
        else:
            return (f'{day[:4]}/{day[4:6]}/{day[6:]}')
    else:
        return (-1)

print(f'#1 {date(date1)}')
print(f'#2 {date(date2)}')
print(f'#3 {date(date3)}')
print(f'#4 {date(date4)}')
print(f'#5 {date(date5)}')