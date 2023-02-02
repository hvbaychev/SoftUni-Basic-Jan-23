import sys

min_number = sys.maxsize
command = input()

while command != 'Stop':
    number = int(command)
    min_number = min(number, min_number)

    command = input()

print(min_number)
    