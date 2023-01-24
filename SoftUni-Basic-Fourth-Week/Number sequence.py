import sys

n = int(input())

biggest_number = -sys.maxsize
min_number = sys.maxsize

for num in range(n):
    current_number = int(input())
    if current_number >= biggest_number:
        biggest_number = current_number
    if current_number <= min_number:
        min_number = current_number

print(f'Max number: {biggest_number}')
print(f'Min number: {min_number}')
