one_lev = int(input())
two_lev = int(input())
five_lev = int(input())

sum_user = int(input())

for num1 in range(one_lev+1):
    for num2 in range(two_lev+1):
        for num3 in range(five_lev+1):
            if num1 * 1 + num2 * 2 + num3 * 5 == sum_user:
                print(f"{num1} * 1 lv. + {num2} * 2 lv. + {num3} * 5 lv. = {sum_user} lv.")
