name_student = input()
number_of_class = 0
average = 0
sum_of_evaluation = 0
count_fail = 0

while number_of_class < 12:
    evaluation = float(input())

    if 4 <= evaluation <= 6:
        sum_of_evaluation += evaluation
        number_of_class += 1
    elif 2 <= evaluation < 4.00:
        count_fail += 1

    if count_fail == 2:
        break


if count_fail == 2:
    print(f'{name_student} has been excluded at {number_of_class+1:.0f} grade')
else:
    average = sum_of_evaluation / number_of_class
    print(f'{name_student} graduated. Average grade: {average:.2f}')
