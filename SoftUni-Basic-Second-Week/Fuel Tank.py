type_fuel = str(input())
liter_fuel_remain = float(input())

if type_fuel == 'Diesel':
    if liter_fuel_remain >= 25:
        print('You have enough diesel.')
    else:
        print('Fill your tank with diesel!')
elif type_fuel == 'Gasoline':
    if liter_fuel_remain >= 25:
        print('You have enough gasoline.')
    else:
        print('Fill your tank with gasoline!')
elif type_fuel == 'Gas':
    if liter_fuel_remain >= 25:
        print('You have enough gas.')
    else:
        print('Fill your tank with gas!')
else:
    print('Invalid fuel!')



