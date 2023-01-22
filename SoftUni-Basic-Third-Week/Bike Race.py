juniors = int(input())
senior = int(input())
trace = input()

money_racers = 0
organisator_tax = 0.95

if trace == 'trail':
    juniors_tax = 5.50
    senior_tax = 7
elif trace == 'cross-country':
    juniors_tax = 8
    senior_tax = 9.50
elif trace == 'downhill':
    juniors_tax = 12.25
    senior_tax = 13.75
elif trace == 'road':
    juniors_tax = 20
    senior_tax = 21.50

if trace == 'cross-country':
    if juniors + senior >= 50:
        juniors_tax = 8 * 0.75
        senior_tax = 9.50 * 0.75

money_racers = (juniors_tax * juniors) + (senior_tax * senior)

money_racers = money_racers * organisator_tax

print(f'{money_racers:.2f}')