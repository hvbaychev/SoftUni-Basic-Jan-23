first_number = int(input())
last_number = int(input())


for num1 in range(first_number, last_number+1):
    for num2 in range(first_number, last_number+1):
        for num3 in range(first_number, last_number+1):
            for num4 in range(first_number, last_number+1):
                if (num1 % 2 == 0 and num4 % 2 != 0 or num1 % 2 != 0 and num4 % 2 == 0) and num1 > num4 and (num2 + num3) % 2 == 0:
                    print(f'{num1}{num2}{num3}{num4}', end=' ')


