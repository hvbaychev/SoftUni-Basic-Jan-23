weatherTemperature = float(input())

if 26.00 <= weatherTemperature <= 35.00:
    print('Hot')
elif 20.1 <= weatherTemperature <= 25.90:
    print('Warm')
elif 15.00 <= weatherTemperature <= 20.00:
    print('Mild')
elif 12.00 <= weatherTemperature <= 14.90:
    print('Cool')
elif 5.00 <= weatherTemperature <= 11.90:
    print('Cold')
else:
    print('unknown')