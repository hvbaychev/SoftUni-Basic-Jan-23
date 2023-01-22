animal = input()

rase_one = 'mammal'
rase_two = 'reptile'
rase_three = 'unknown'


if animal == 'dog':
    print(rase_one)
elif animal in ('crocodile', 'tortoise', 'snake'):
    print(rase_two)
else:
    print(rase_three)