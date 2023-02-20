n = input()
n1 = n[0]
n2 = n[1]
n3 = n[2]

for num1 in range(1, int(n3)+1):
    for num2 in range(1, int(n2)+1):
        for num3 in range(1, int(n1)+1):
            total_sum = num1 * num2 * num3
            print(f'{num1} * {num2} * {num3} = {total_sum};')
