num = int(input())

for num1 in range(1, 10):
    for num2 in range(1, 10):
        for num3 in range(1, 10):
            for num4 in range(1, 10):
                if num % num1 == 0 and num % num2 == 0 and num % num3 == 0 and num % num4 == 0:
                    print(f"{num1}{num2}{num3}{num4}", end=" ")
