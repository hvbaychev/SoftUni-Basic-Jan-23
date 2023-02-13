number_chemical = int(input())
number_marker = int(input())
litter_cleaner = int(input())
discount = int(input())

chemical = 5.80 * number_chemical
marker = 7.20 * number_marker
cleaner = 1.20 * litter_cleaner

total_sum = (chemical + marker + cleaner)
discount = total_sum * (discount / 100)

total_sums = total_sum - discount

print(total_sums)


