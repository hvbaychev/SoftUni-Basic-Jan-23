n = int(input())  # 5 * 3 x 3  15 reda x 3 koloni

star = 2 * n
spaces = 5 * n - star * 2
slash = 2 * n - 2

is_n_even = n % 2 == 0

print('*' * star + ' ' * spaces + '*' * star)

for i in range(1, (n - 2) + 1):
    if i == n // 2 and not is_n_even:
        print('*' + '/' * slash + '*' + '|' * spaces + '*' + '/' * slash + '*')
    elif is_n_even and i == (n//2) - 1:
        print('*' + '/' * slash + '*' + '|' * spaces + '*' + '/' * slash + '*')
    else:
        print('*' + '/' * slash + '*' + ' ' * spaces + '*' + '/' * slash + '*')

print('*' * star + ' ' * spaces + '*' * star)
