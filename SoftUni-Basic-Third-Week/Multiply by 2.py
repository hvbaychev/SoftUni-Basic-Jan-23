while True:
    x = float(input())
    if x < 0:
        print('Negative number!')
        break
    else:
        result = x * 2
        print(f'Result: {result:.2f}')