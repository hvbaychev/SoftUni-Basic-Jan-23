money = float(input())
destination = input()
season = input()
days = int(input())

total_sum = 0

if season == 'Winter':
    if destination == 'Dubai':
        dubai = 45000
        total_sum += dubai
    elif destination == 'Sofia':
        sofia = 17000
        total_sum += sofia
    elif destination == 'London':
        london = 24000
        total_sum += london

if season == 'Summer':
    if destination == 'Dubai':
        dubai = 40000
        total_sum += dubai
    elif destination == 'Sofia':
        sofia = 12500
        total_sum += sofia
    elif destination == 'London':
        london = 20250
        total_sum += london

if destination == 'Dubai':
    total_sum = total_sum * 0.70
elif destination == 'Sofia':
    total_sum = total_sum * 1.25

total_sum = total_sum * days

diff = abs(total_sum - money)
if total_sum <= money:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")
