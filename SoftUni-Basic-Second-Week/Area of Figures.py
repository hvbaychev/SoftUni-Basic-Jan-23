import math

figures = str(input('Enter the shape of figure: '))
area = 0.00

if figures == 'square':
    sideA = float(input('Enter the length of side: '))
    area = sideA * sideA
    print(f'{area:.3f}')
elif figures == 'rectangle':
    sideA = float(input('Enter the length of first side: '))
    sideB = float(input('Enter the length of second side: '))
    area = sideA * sideB
    print(f'{area:.3f}')
elif figures == 'circle':
    radius = float(input('Enter the radius of circle: '))
    area = math.pi * radius * radius
    print(f'{area:.3f}')
elif figures == 'triangle':
    sideA = float(input('Enter the height: '))
    sideB = float(input('Enter the length: '))
    area = (sideA * sideB) / 2
    print(f'{area:.3f}')

