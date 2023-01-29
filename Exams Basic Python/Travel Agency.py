city_name = input()
pack_name = input()
vip_card = input()
rest_day = int(input())

equipment = 100
without_equipment = 80
food = 130
without_food = 100

total_sum = 0

if vip_card == 'yes':
    equipment *= 0.90
    without_equipment *= 0.95
    food *= 0.88
    without_food *= 0.93

if (city_name == 'Borovets' or city_name == 'Bansko') and pack_name == 'withEquipment':
    total_sum = rest_day * equipment
elif (city_name == 'Borovets' or city_name == 'Bansko') and pack_name == 'noEquipment':
    total_sum = rest_day * without_equipment

if (city_name == 'Burgas' or city_name == 'Varna') and pack_name == 'withBreakfast':
    total_sum = rest_day * food
elif (city_name == 'Burgas' or city_name == 'Varna') and pack_name == 'noBreakfast':
    total_sum = rest_day * without_food

if rest_day > 7:
    relax_sum = total_sum / rest_day
    total_sum = total_sum - relax_sum

if rest_day < 1:
    print('Days must be positive number!')
elif (city_name != 'Burgas' and city_name != 'Varna' and city_name != 'Bansko' and city_name != 'Borovets') or (pack_name != 'noBreakfast' and pack_name != 'withBreakfast' and pack_name != 'noEquipment' and pack_name != 'withEquipment'):
    print("Invalid input!")
else:
    print(f'The price is {total_sum:.2f}lv! Have a nice time!')



