budjet = float(input())
season = input()

summerwint = 0
holiday = ''
rest = ''

if budjet <= 100:
    holiday = 'Bulgaria'
    if season == 'summer':
        summerwint = budjet * 0.30
        rest = 'Camp'
    elif season == 'winter':
        summerwint = budjet * 0.70
        rest = 'Hotel'

if 100 < budjet <= 1000:
    holiday = 'Balkans'
    if season == 'summer':
        summerwint = budjet * 0.40
        rest = 'Camp'
    elif season == 'winter':
        summerwint = budjet * 0.80
        rest = 'Hotel'

if budjet > 1000:
    rest = 'Hotel'
    holiday = 'Europe'
    summerwint = budjet * 0.90

print(f'Somewhere in {holiday}')
print(f'{rest} - {summerwint:.2f}')
