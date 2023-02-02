name = input()
my_list = []
count = 0

while len(my_list) < 12:
    grade = float(input())
    if 2 <= grade < 4:
        count += 1
    if 4 <= grade <= 6:
        my_list.append(grade)
    if count == 2:
        break

length_list = len(my_list)

if count == 2:
    print(f"{name} has been excluded at {length_list + 1} grade")
elif count == 0 or count == 1:
    average_grade = sum(my_list) / length_list
    print(f"{name} graduated. Average grade: {average_grade:.2f}")