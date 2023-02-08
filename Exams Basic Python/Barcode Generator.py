number1 = int(input())
number2 = int(input())

n = str(number1)
n1 = n[0]
n2 = n[1]
n3 = n[2]
n4 = n[3]

m = str(number2)
m1 = m[0]
m2 = m[1]
m3 = m[2]
m4 = m[3]


for num1 in range(int(n[0]), int(m[0])+1):
    for num2 in range(int(n[1]), int(m[1])+1):
        for num3 in range(int(n[2]), int(m[2])+1):
            for num4 in range(int(n[3]), int(m[3])+1):
                if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0 and num4 % 2 != 0:
                    print(f'{num1}{num2}{num3}{num4}', end=' ')
