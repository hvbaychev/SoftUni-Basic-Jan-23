n = int(input())
is_n_even = n % 2 == 0
range_row = 0
stars = 1
dash = (n - stars) // 2

if is_n_even:
    range_row = n // 2
    stars = 2
else:
    range_row = n // 2 + 1

for row in range(0, range_row):
    print('-' * dash + '*' * stars + '-' * dash)
    stars += 2
    dash -= 1

new_line = n - range_row
for row in range(0, new_line):
    print('|' + '*' * (n - 2) + '|')
