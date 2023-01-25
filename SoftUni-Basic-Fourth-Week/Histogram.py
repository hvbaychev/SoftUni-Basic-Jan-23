num = int(input())

count_one = 0
count_two = 0
count_tree = 0
count_four = 0
count_five = 0

for i in range(0, num):
    current_number = int(input())
    if current_number < 200:
        count_one += 1
    elif current_number >= 200 and current_number <= 399:
        count_two += 1
    elif current_number >= 400 and current_number <=599:
        count_tree += 1
    elif current_number >= 600 and current_number <= 799:
        count_four += 1
    elif current_number >= 800:
        count_five += 1

p1 = (count_one / num) * 100
p2 = (count_two / num) * 100
p3 = (count_tree / num) * 100
p4 = (count_four / num) * 100
p5 = (count_five / num) * 100

print(f'{p1:.02f}%')
print(f'{p2:.02f}%')
print(f'{p3:.02f}%')
print(f'{p4:.02f}%')
print(f'{p5:.02f}%')