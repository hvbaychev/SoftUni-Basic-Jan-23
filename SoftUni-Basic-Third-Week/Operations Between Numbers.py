n1 = int(input())
n2 = int(input())
oper = input()

result = 0
number_is = ''


if oper == '+':
    result = n1 + n2
elif oper == '-':
    result = n1 - n2
elif oper == '*':
    result = n1 * n2
elif oper == '/' and n2 != 0:
    result = n1 / n2
elif oper == '%' and n2 != 0:
    result = n1 % n2


if result % 2 == 0:
    number_is = 'even'
else:
    number_is = 'odd'

if oper == '+':
    print(f'{n1} {oper} {n2} = {result} - {number_is}')
elif oper == '-':
    print(f'{n1} {oper} {n2} = {result} - {number_is}')
elif oper == '*':
    print(f'{n1} {oper} {n2} = {result} - {number_is}')
elif oper == '/' and n2 != 0:
    print(f'{n1} {oper} {n2} = {result:.2f}')
elif oper == '%' and n2 != 0:
    print(f'{n1} {oper} {n2} = {result}')
elif oper == '/' and n2 == 0:
    print(f'Cannot divide {n1} by zero')
elif oper == '%' and n2 == 0:
    print(f'Cannot divide {n1} by zero')
