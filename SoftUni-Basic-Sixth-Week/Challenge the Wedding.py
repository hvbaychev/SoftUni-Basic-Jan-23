man = int(input())
women = int(input())
table = int(input())
count = 0
total_people = 0

for i in range(1, man+1):
    for x in range(1, women+1):
        if count == table:
            break
        print(f'({i} <-> {x})', end=' ')
        count += 1
