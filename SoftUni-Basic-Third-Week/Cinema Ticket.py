day_from_week = input()

if day_from_week in 'Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday':
    if day_from_week in 'Monday, Tuesday, Friday':
        print('12')
    elif day_from_week in 'Wednesday, Thursday':
        print('14')
    elif day_from_week in 'Saturday, Sunday':
        print('16')