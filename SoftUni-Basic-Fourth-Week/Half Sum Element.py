import sys

n = int(input())

max_num = -sys.maxsize
sum_number = 0

for i in range(0, n):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_number += num

if max_num == sum_number - max_num:
    sum_others = sum_number - max_num
    print('Yes')
    print(f'Sum = {sum_others}')
else:
    sum_others = sum_number - max_num
    print('No')
    print(f'Diff = {abs(max_num - sum_others)}')
