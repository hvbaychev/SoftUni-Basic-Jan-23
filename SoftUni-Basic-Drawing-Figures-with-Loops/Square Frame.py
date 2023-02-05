n = int(input())

slashes = n - 2

print('+ ' + '- ' * slashes + '+')

for row in range(n - 2):
    print('| ' + '- ' * slashes + '|')

print('+ ' + '- ' * slashes + '+')
