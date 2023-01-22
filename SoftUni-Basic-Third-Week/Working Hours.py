hour = int(input())
day = input()

if (24 >= hour >= 0) and day in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'):
    if 10 <= hour <= 18:
        print('open')
    else:
        print('closed')

if day == 'Sunday':
    print('closed')