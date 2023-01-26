number_of_students = int(input())

excellent_count = 0
very_good_count = 0
good_count = 0
bad_count = 0

average_result = 0

for result in range(number_of_students):
    result_of_exam = float(input())
    if 2.00 <= result_of_exam <= 2.99:
        bad_count += 1
        average_result += result_of_exam
    elif 3.00 <= result_of_exam <= 3.99:
        average_result += result_of_exam
        good_count += 1
    elif 4.00 <= result_of_exam <= 4.99:
        average_result += result_of_exam
        very_good_count += 1
    elif 5.00 <= result_of_exam <= 6.00:
        excellent_count += 1
        average_result += result_of_exam

average_result = average_result / number_of_students

s1 = (excellent_count / number_of_students) * 100
s2 = (very_good_count / number_of_students) * 100
s3 = (good_count / number_of_students) * 100
s4 = (bad_count / number_of_students) * 100

print(f'Top students: {s1:.2f}%')
print(f'Between 4.00 and 4.99: {s2:.2f}%')
print(f'Between 3.00 and 3.99: {s3:.2f}%')
print(f'Fail: {s4:.2f}%')
print(f'Average: {average_result:.2f}')