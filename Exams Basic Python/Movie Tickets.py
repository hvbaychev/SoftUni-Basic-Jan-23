a1 = int(input())
a2 = int(input())
n = int(input())
sum_of_symbol = 0
new_n = int(n / 2 - 1)

for symbol1 in range(a1, a2):
    for symbol2 in range(1, n):
        for symbol3 in range(1, new_n+1):
            sum_of_symbol = symbol1 + symbol2 + symbol3
            if symbol1 % 2 != 0 and sum_of_symbol % 2 != 0:
                print(f'{chr(symbol1)}-{symbol2}{symbol3}{symbol1}')
