open_tab = int(input())
salary = int(input())


facebook = 150
instagram = 100
reddit = 50

penalty = 0

for i in range(0, open_tab):
    web = input()
    if web == 'Facebook':
        penalty += facebook
    elif web == 'Instagram':
        penalty += instagram
    elif web == 'Reddit':
        penalty += reddit
    if penalty >= salary:
        print('You have lost your salary.')
        break

if penalty < salary:
    diff = abs(salary - penalty)
    print(f'{diff}')



