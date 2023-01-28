import math

ball_number = int(input())

points = 0
red = 5
orange = 10
yellow = 15
white = 20


red_count = 0
orange_count = 0
yellow_count = 0
white_count = 0
other_color = 0
black_count = 0

for _ in range(1, ball_number+1):
    color = input()
    if color == 'red':
        points += red
        red_count += 1
    elif color == 'orange':
        points += orange
        orange_count += 1
    elif color == 'yellow':
        points += yellow
        yellow_count += 1
    elif color == 'white':
        points += white
        white_count += 1
    elif color == 'black':
        points = math.floor(points / 2)
        black_count += 1
    elif color != ('red', 'orange', 'yellow', 'white', 'black'):
        other_color += 1
        continue

print(f'Total points: {points:.0f}')
print(f'Red balls: {red_count:.0f}')
print(f'Orange balls: {orange_count:.0f}')
print(f'Yellow balls: {yellow_count:.0f}')
print(f'White balls: {white_count:.0f}')
print(f'Other colors picked: {other_color:.0f}')
print(f'Divides from black balls: {black_count:.0f}')