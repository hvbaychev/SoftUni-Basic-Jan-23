capacity_stadium = int(input())
number_of_fan = int(input())

A = 0
B = 0
V = 0
G = 0

average_fan = 0

for i in range(number_of_fan):
    sector = input()
    if sector == 'A':
        A += 1
    elif sector == 'B':
        B += 1
    elif sector == 'V':
        V += 1
    elif sector == 'G':
        G += 1

A = (A / number_of_fan) * 100
B = (B / number_of_fan) * 100
V = (V / number_of_fan) * 100
G = (G / number_of_fan) * 100
average_fan = (number_of_fan / capacity_stadium) * 100


print(f'{A:.2f}%')
print(f'{B:.2f}%')
print(f'{V:.2f}%')
print(f'{G:.2f}%')
print(f'{average_fan:.2f}%')
