type_fuel = str(input())
amount_fuel = int(input())
disc_car = str(input())

gasoline = 2.22
diesel = 2.33
gas = 0.93

disc_cart_gasoline = gasoline - 0.18
disc_cart_diesel = diesel - 0.12
disc_cart_gas = gas - 0.08

if type_fuel == 'Gas' and disc_car == 'Yes':
    final_price_gas = disc_cart_gas
    total_price_gas = amount_fuel * final_price_gas
    if 20 <= amount_fuel <= 25:
        total_price_gas = total_price_gas * 0.92
        print(f'{total_price_gas:.2f} lv.')
    elif amount_fuel > 25:
        total_price_gas = total_price_gas * 0.90
        print(f'{total_price_gas:.2f} lv.')

if type_fuel == 'Gas' and disc_car == 'No':
    price_gas_without_card = amount_fuel * gas
    if 20 <= amount_fuel <= 25:
        price_gas_without_card = price_gas_without_card * 0.92
        print(f'{price_gas_without_card:.2f} lv.')
    elif amount_fuel > 25:
        price_gas_without_card = price_gas_without_card * 0.90
        print(f'{price_gas_without_card:.2f} lv.')

if type_fuel == 'Gas' and disc_car == 'Yes' and amount_fuel < 20:
    price_gas_less = disc_cart_gas
    price_gas_less = amount_fuel * price_gas_less
    print(f'{price_gas_less:.2f} lv.')

if type_fuel == 'Gas' and disc_car == 'No' and amount_fuel < 20:
    price_gas_less_without_card = amount_fuel * gas
    print(f'{price_gas_less_without_card:.2f} lv')


if type_fuel == 'Diesel' and disc_car == 'Yes':
    final_price_diesel = disc_cart_diesel
    total_price_diesel = amount_fuel * final_price_diesel
    if 20 <= amount_fuel <= 25:
        total_price_diesel = total_price_diesel * 0.92
        print(f'{total_price_diesel:.2f} lv.')
    elif amount_fuel > 25:
        total_price_diesel = total_price_diesel * 0.90
        print(f'{total_price_diesel:.2f} lv.')

if type_fuel == 'Diesel' and disc_car == 'No':
    price_diesel_without_card = amount_fuel * diesel
    if 20 <= amount_fuel <= 25:
        price_diesel_without_card = price_diesel_without_card * 0.92
        print(f'{price_diesel_without_card:.2f} lv.')
    elif amount_fuel > 25:
        price_diesel_without_card = price_diesel_without_card * 0.90
        print(f'{price_diesel_without_card:.2f} lv.')

if type_fuel == 'Diesel' and disc_car == 'Yes' and amount_fuel < 20:
    price_diesel_less = disc_cart_diesel
    price_diesel_less = amount_fuel * price_diesel_less
    print(f'{price_diesel_less:.2f} lv.')

if type_fuel == 'Diesel' and disc_car == 'No' and amount_fuel < 20:
    price_diesel_less_without_card = amount_fuel * diesel
    print(f'{price_diesel_less_without_card:.2f} lv.')


if type_fuel == 'Gasoline' and disc_car == 'Yes':
    final_price_gasoline = disc_cart_gasoline
    total_price_gasoline = amount_fuel * final_price_gasoline
    if 20 <= amount_fuel <= 25:
        total_price_gas = total_price_gasoline * 0.92
        print(f'{total_price_gasoline:.2f} lv.')
    elif amount_fuel > 25:
        total_price_gas = total_price_gasoline * 0.90
        print(f'{total_price_gasoline:.2f} lv.')

if type_fuel == 'Gasoline' and disc_car == 'No':
    price_gasoline_without_card = amount_fuel * gasoline
    if 20 <= amount_fuel <= 25:
        price_gasoline_without_card = price_gasoline_without_card * 0.92
        print(f'{price_gasoline_without_card:.2f} lv.')
    elif amount_fuel > 25:
        price_gasoline_without_card = price_gasoline_without_card * 0.90
        print(f'{price_gasoline_without_card:.2f} lv.')

if type_fuel == 'Gasoline' and disc_car == 'Yes' and amount_fuel < 20:
    price_gasoline_less = disc_cart_gasoline
    price_gasoline_less = amount_fuel * price_gasoline_less
    print(f'{price_gasoline_less:.2f} lv.')

if type_fuel == 'Gasoline' and disc_car == 'No' and amount_fuel < 20:
    price_gasoline_less_without_card = amount_fuel * gasoline
    print(f'{price_gasoline_less_without_card:.2f} lv.')
