number = int(input())

total_sum = 0


while True:
    new_number = int(input())
    if total_sum + new_number >= number:
        total_sum += new_number
        break
    total_sum += new_number

print(f'{total_sum}')