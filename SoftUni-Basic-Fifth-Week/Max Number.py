import sys

max_number = -sys.maxsize

command = input()

while command != 'Stop':
    number = int(command)
    max_number = max(number, max_number)

    command = input()

print(max_number)
