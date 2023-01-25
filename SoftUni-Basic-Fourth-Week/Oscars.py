name_of_actor = input()
point_from_academy = float(input())
evaluative = int(input())

for i in range(evaluative):
    name_of_judge = input()
    point_from_judge = float(input())
    length_of_name = len(name_of_judge)

    current_score = (length_of_name * point_from_judge) / 2
    point_from_academy += current_score

    if point_from_academy >= 1250.5:
        break


if point_from_academy > 1250.5:
    print(f'Congratulations, {name_of_actor} got a nominee for leading role with {point_from_academy:.1f}!')
else:
    total_sum = abs(point_from_academy - 1250.5)
    print(f'Sorry, {name_of_actor} you need {total_sum:.1f} more!')
