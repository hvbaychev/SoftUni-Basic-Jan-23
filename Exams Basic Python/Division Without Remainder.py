n = int(input())
count_2 = 0
count_3 = 0
count_4 = 0

for num in range(n):
    number = int(input())
    if number % 2 == 0:
        count_2 += 1
    if number % 3 == 0:
        count_3 += 1
    if number % 4 == 0:
        count_4 += 1

print(f'{(count_2 / n) * 100:.2f}%')
print(f'{(count_3 / n) * 100:.2f}%')
print(f'{(count_4 / n) * 100:.2f}%')
