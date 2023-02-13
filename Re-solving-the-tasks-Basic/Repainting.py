protector = int(input())
paint_litter = int(input())
mixer_litter = int(input())
hours = int(input())


protector_price = 1.50
paint_price = 14.50
mixer_price = 5.00

protector_price = (protector + 2) * protector_price
paint_price = (paint_litter * 1.10) * paint_price
mixer_price = mixer_litter * mixer_price
bags = 0.40
total_sum = protector_price + paint_price + mixer_price + bags

work_price = (total_sum * 0.30) * hours
total_sum = total_sum + work_price
print(total_sum)