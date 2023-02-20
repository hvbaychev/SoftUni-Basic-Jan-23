import sys
max_score = - sys.maxsize
current_name = ''
max_name = ''
hat_trick = False
name = input()

while name != 'END':
    goal = int(input())
    current_name = name
    if goal > max_score:
        max_score = goal
        max_name = name
    if goal >= 10:
        break
    name = input()
print(f'{max_name} is the best player!')
if max_score >= 3:
    print(f'He has scored {max_score} goals and made a hat-trick !!!')
elif max_score < 3:
    print(f'He has scored {max_score} goals.')


