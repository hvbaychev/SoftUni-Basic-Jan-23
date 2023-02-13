days = int(input())
hours = int(input())
tax_parking = 0
total_sum = 0
for d in range(1, days+1):
    tax_parking = 0
    for h in range(1, hours+1):
        if d % 2 == 0 and h % 2 != 0:
            tax_parking += 2.50
        elif d % 2 != 0 and h % 2 == 0:
            tax_parking += 1.25
        else:
            tax_parking += 1
    total_sum += tax_parking

    print(f"Day: {d} - {tax_parking:.2f} leva")

print(f"Total: {total_sum:.2f} leva")