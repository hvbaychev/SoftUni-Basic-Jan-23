num1 = int(input())
num2 = int(input())
num3 = int(input())

for one in range(1, num1+1):
    for two in range(1, num2+1):
        for tree in range(1, num3+1):
            if two == 2 or two == 3 or two == 5 or two == 7:
                if one % 2 == 0 and tree % 2 == 0:
                    print(f'{one} {two} {tree}')