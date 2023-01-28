colored_eggs = int(input())

red = 0
orange = 0
blue = 0
green = 0
max_from_color = 0
biggest = ''

for _ in range(colored_eggs):
    color = input()
    if color == 'red':
        red += 1
    elif color == 'orange':
        orange += 1
    elif color == 'blue':
        blue += 1
    elif color == 'green':
        green += 1

max_from_color = max(red, orange, blue, green)

if red > orange and red > blue and red > green:
    biggest = 'red'
elif orange > red and orange > blue and orange > green:
    biggest = 'orange'
elif blue > red and blue > orange and blue > green:
    biggest = 'blue'
else:
    biggest = 'green'

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f'Blue eggs: {blue}')
print(f"Green eggs: {green}")
print(f"Max eggs: {max_from_color} -> {biggest}")
