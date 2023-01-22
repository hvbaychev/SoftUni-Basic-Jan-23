fuel_type = input()
fuel_ltr = float(input())
club_member = input()
bill = 0

GASOLINE = 2.22
DIESEL = 2.33
GAS = 0.93

if club_member == "Yes":
    GASOLINE -= 0.18
    DIESEL -= 0.12
    GAS -= 0.08

if fuel_type == "Gasoline":
    bill = fuel_ltr * GASOLINE

if fuel_type == "Diesel":
    bill = fuel_ltr * DIESEL

if fuel_type == "Gas":
    bill = fuel_ltr * GAS

if 20 <= fuel_ltr <= 25:
    bill *= 0.92
elif fuel_ltr > 25:
    bill *= 0.90

print(f"{bill:.2f} lv.")