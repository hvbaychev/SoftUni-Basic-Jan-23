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
print(f'OddMin=' + f'{odd_min:.2f},' if odd_min != sys.maxsize else "OddMin=No,")
print(f'OddMax=' + f'{odd_max:.2f},' if odd_max != -sys.maxsize else "OddMax=No,")
print(f'EvenSum={even_sum:.2f},')
print(f'EvenMin=' + f'{even_min:.2f},' if even_min != sys.maxsize else "EvenMin=No,")
print(f'EvenMax=' + f'{even_max:.2f}' if even_max != -sys.maxsize else "EvenMax=No")
