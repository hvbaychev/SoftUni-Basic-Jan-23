start_first = int(input())
start_second = int(input())

diff_first = int(input())
diff_second = int(input())

diff_one = start_first + diff_first
diff_two = start_second + diff_second

is_prime = False
is_secprime = False

for num1 in range(start_first, diff_one + 1):
    is_prime = True
    for i in range(2, num1):

        if num1 % i == 0:
            is_prime = False
    if not is_prime:
        continue
    else:
        pair1 = num1

    for num2 in range(start_second, diff_two + 1):
        is_secprime = True
        for a in range(2, num2):

            if num2 % a == 0:
                is_secprime = False
        if not is_secprime:
            continue
        else:
            pair2 = num2

            if is_prime and is_secprime:
                print(f'{pair1}{pair2}')

