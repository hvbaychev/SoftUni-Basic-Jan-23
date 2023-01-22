hour_for_exam = int(input())
min_for_exam = int(input())
hour_arrival = int(input())
min_arrival = int(input())

late = 'Late'
on_time = 'On time'
early = 'Early'

exam_time = (hour_for_exam * 60) + min_for_exam
arrival_time = (hour_arrival * 60) + min_arrival

total_time_diff = arrival_time - exam_time

student_arrival = late
if total_time_diff < -30:
    student_arrival = early
elif total_time_diff <= 0:
    student_arrival = on_time

result = ''
if total_time_diff != 0:
    hour_diff = abs(total_time_diff) // 60
    min_diff = abs(total_time_diff) % 60

    if hour_diff > 0:
        result = f'{hour_diff}:{min_diff:02} hours'
    else:
        result = f'{min_diff} minutes'

    if total_time_diff < 0:
        result += ' before the start'
    else:
        result += ' after the start'

print(student_arrival)
if result:
    print(result)