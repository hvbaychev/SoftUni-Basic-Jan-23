import sys

n = int(input())

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize

even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

for i in range(1, n + 1):
    new_number = float(input())
    if i % 2 != 0:
        odd_sum += new_number
        odd_max = max(odd_max, new_number)
        odd_min = min(odd_min, new_number)

    if i % 2 == 0:
        even_sum += new_number
        even_max = max(even_max, new_number)
        even_min = min(even_min, new_number)


print(f'OddSum={odd_sum:.2f},')

if odd_min == sys.maxsize:
    print('OddMin=No,')
else:
    print(f'OddMin={odd_min:.2f},')

if odd_max == -sys.maxsize:
    print('OddMax=No,')
else:
    print(f'OddMax={odd_max:.2f},')

print(f'EvenSum={even_sum:.2f},')

if even_min == sys.maxsize:
    print('EvenMin=No,')
else:
    print(f'EvenMin={even_min:.2f},')

if even_max == -sys.maxsize:
    print('EvenMax=No')
else:
    print(f'EvenMax={even_max:.2f}')