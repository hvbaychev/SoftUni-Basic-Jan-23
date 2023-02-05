first_number = int(input())
second_number = int(input())
magic_number = int(input())

count = 0

for i in range(first_number, second_number + 1):
    for j in range(first_number, second_number + 1):
        count += 1

        if i + j == magic_number:
            print(f'Combination N:{count} ({i} + {j} = {magic_number})')
            exit()

print(f'{count} combinations - neither equals {magic_number}')
