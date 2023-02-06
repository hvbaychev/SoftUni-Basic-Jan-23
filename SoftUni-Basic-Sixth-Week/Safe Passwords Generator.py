num1 = int(input())
num2 = int(input())
max_count = int(input())

start_num1 = 35
end_num1 = 55

start_num2 = 64
end_num2 = 96

counter = 0
flag = False
for a in range(start_num1, end_num1):
    for b in range(start_num2, end_num2):
        for x in range(1, num1 + 1):
            for y in range(1, num2 + 1):
                counter += 1

                if counter > max_count:
                    flag = True
                    break
                print(f'{chr(a)}{chr(b)}{x}{y}{chr(b)}{chr(a)}', end='|')
                if x == a and y == b:
                    flag = True
                    break
                a += 1
                if a > 55:
                    a = 35
                b += 1
                if b > 96:
                    b = 64

            if flag:
                break

        if flag:
            break

    if flag:
        break