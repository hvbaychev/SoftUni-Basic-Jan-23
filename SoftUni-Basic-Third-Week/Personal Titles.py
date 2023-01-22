age = float(input())
gander = input()

if age >= 16:
    if gander == 'm':
        print('Mr.')
    else:
        print('Ms.')

if age < 16:
    if gander == 'm':
        print('Master')
    else:
        print('Miss')