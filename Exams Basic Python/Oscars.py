name_of_actor = input()
start_point_actor = float(input())
number_jury = int(input())
final_result = 1250.5
point = 0
total_points = 0

for _ in range(number_jury):
    name_of_jury = input()
    points_from_jury = float(input())

    len_of_the_name_jury = len(name_of_jury)
    point = (len_of_the_name_jury * points_from_jury) / 2
    total_points += point

    if total_points + start_point_actor > final_result:
        break

total_points += start_point_actor
if total_points > final_result:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    diff = abs(total_points - final_result)
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")