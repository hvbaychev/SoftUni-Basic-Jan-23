import sys
max_goal = -sys.maxsize
max_score_for_name = -sys.maxsize
name_of_max_goal = str
the_name = str
name = input()

while name != 'END':
    goals = int(input())
    max_goal = max(goals, max_goal)
    if max_goal > max_score_for_name:
        the_name = name
        max_score_for_name = goals
    if max_goal >= 10:
        break
    name = input()
print(f'{the_name} is the best player!')

if max_goal >= 3:
    print(f"He has scored {max_goal} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goal} goals.")
