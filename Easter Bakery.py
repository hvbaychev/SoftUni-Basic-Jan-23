flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs = int(input())
yeast = int(input())


sugar_price = flour_price * 0.75
eggs_price = flour_price * 1.10
yeast_price = sugar_price * 0.20

sum_flour = flour_price * flour_kg
sum_sugar = sugar_price * sugar_kg
sum_eggs = eggs_price * eggs
sum_yeast = yeast_price * yeast

total_sum = sum_flour + sum_sugar + sum_eggs + sum_yeast

print(f'{total_sum:.2f}')
