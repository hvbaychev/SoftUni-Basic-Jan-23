jury = int(input())

average = 0
total_average = 0
count_evaluation = 0
total_sum = 0

while True:
    presentation = input()
    average = 0
    if presentation == 'Finish':
        break
    for presentation_count in range(jury):
        evaluation_count = float(input())
        count_evaluation += 1
        total_sum += evaluation_count
        total_average = total_sum / count_evaluation
        average += evaluation_count / jury

    print(f'{presentation} - {average:.2f}.')

if presentation == 'Finish':
    print(f"Student's final assessment is {total_average:.2f}.")
