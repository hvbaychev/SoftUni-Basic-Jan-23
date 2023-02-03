n = int(input())
total_sum = 0
average = 0

for i in range(n):
    new_number = int(input())
    total_sum += new_number
    average = total_sum / n

print(f'{average:.2f}')