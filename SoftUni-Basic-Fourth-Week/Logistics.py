
number_of_pack = int(input())

bus_price = 200
truck_price = 175
train_price = 120
total_tonnage = 0
price_tonnage = 0
average = 0
total_tonnage_with_bus = 0
total_tonnage_with_truck = 0
total_tonnage_with_train = 0

for tonnage in range(number_of_pack):
    desire_tonnage = int(input())
    total_tonnage += desire_tonnage
    if desire_tonnage <= 3:
        price_tonnage += bus_price
        total_tonnage_with_bus += desire_tonnage
    elif 4 <= desire_tonnage <= 11:
        price_tonnage += truck_price
        total_tonnage_with_truck += desire_tonnage
    else:
        price_tonnage += train_price
        total_tonnage_with_train += desire_tonnage

average = (total_tonnage_with_bus * bus_price) + (total_tonnage_with_truck * truck_price) + (total_tonnage_with_train * train_price)
average = average / total_tonnage

t1 = (total_tonnage_with_bus / total_tonnage) * 100
t2 = (total_tonnage_with_truck / total_tonnage) * 100
t3 = (total_tonnage_with_train / total_tonnage) * 100

print(f'{average:.2f}')
print(f'{t1:.2f}%')
print(f'{t2:.2f}%')
print(f'{t3:.2f}%')
