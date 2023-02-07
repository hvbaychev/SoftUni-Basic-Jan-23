days = int(input())
hour = int(input())
total_tax = 0
total_tax_day = 0


for den in range(1, days + 1):
    total_tax_day = 0
    for chas in range(1, hour+1):
        if den % 2 == 0 and chas % 2 != 0:
            total_tax += 2.50
            total_tax_day += 2.50
        elif den % 2 != 0 and chas % 2 == 0:
            total_tax += 1.25
            total_tax_day += 1.25
        else:
            total_tax += 1
            total_tax_day += 1

    print(f"Day: {den} - {total_tax_day:.2f} leva")
print(f"Total: {total_tax:.2f} leva")

