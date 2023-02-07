n1 = int(input())
n2 = int(input())

for num1 in range(1, n1 + 1):
    for num2 in range(1, n1 + 1):
        for num3 in range(97, n2 + 97):
            for num4 in range(97, n2 + 97):
                for num5 in range(1, n1+1):
                    if num5 > num1 and num5 > num2:
                        print(f'{num1}{num2}{chr(num3)}{chr(num4)}{num5}', end=" ")
