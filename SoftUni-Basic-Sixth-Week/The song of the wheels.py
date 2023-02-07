number = int(input())
counter = 0
password = 'False'
a = 0
b = 0
c = 0
d = 0

for num1 in range(1, 10):
    for num2 in range(1, 10):
        for num3 in range(1, 10):
            for num4 in range(1, 10):
                if (num1 * num2) + (num3 * num4) == number and num1 < num2 and num3 > num4:
                    print(f'{num1}{num2}{num3}{num4}', end=' ')
                    counter += 1
                    if counter == 4:
                        a = num1
                        b = num2
                        c = num3
                        d = num4
                        password = 'True'

if password == 'True':
    print(f'\nPassword: {a}{b}{c}{d}')
else:
    print('\nNo!')