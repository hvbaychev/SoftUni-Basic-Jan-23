a1 = int(input())
a2 = int(input())
n = int(input())
sum_of_symbol = 0
new_n = int(n / 2 - 1)

for symbol1 in chr(a1), chr(a2-1):
    for symbol2 in range(1, n):
        for symbol3 in range(1, new_n+1):
            for symbol4 in symbol1:
                sum_of_symbol = symbol2 + symbol3 + ord(symbol4)
                if ord(symbol1) % 2 == 1 and sum_of_symbol % 2 == 1:
                    print(f'{symbol1}-{symbol2}{symbol3}{ord(symbol4)}')
